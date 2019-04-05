# ************************************************************************
#  File Name: main.py
#
#  Created By: Brady Fry (frybr)
#
#  Purpose:
# ************************************************************************

# ***********************************************************************/
# imports
# ***********************************************************************/
# import sys
# from PyQt5 import QtGui
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.uic import loadUiType

import os
import sys
import nims
import time
import serial
import struct
import logging
import traceback
from re import search
from pathlib import Path
from datetime import datetime
from time import gmtime, strftime

from time import sleep

# import nimspy

from __init__ import __version__
from __init__ import __program__

from pyserial import list_ports

from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QFont
from PyQt5.uic import loadUi


# ***********************************************************************/
# global variables
# ***********************************************************************/
nimspystartui = "nimspy.ui"  # Enter file here.
# error file path
errflepth = ''

# tab windows
TABSTARTENDRUN = 0
TABDATADISPLAY = 1
TABMETADATA = 2
TABSITEREPORT = 3
TABENGINEERING = 4


class MainWindow(QMainWindow):
    """The Main class for for the nimspy application."""

    def __init__(self, *args):
        """Initialize the nimspy program."""
        super(MainWindow, self).__init__(*args)

        # serial port
        self.port = serial.Serial()

        # variable initialization
        self.packet = b''
        self.board = nims.MINERVA
        self.scstate = nims.INITIAL
        self.gpsstate = nims.GPSINITIAL
        self.gpsstring = ''

        self.portdata = b''
        # LED Instantiations
        # round leds
        self.ledblack = os.path.join('img', 'black_led_61_61.png')
        self.ledgreen = os.path.join('img', 'green_led_61_61.png')
        self.ledyellow = os.path.join('img', 'yellow_led_61_61.png')
        self.ledred = os.path.join('img', 'red_led_61_61.png')
        # oval leds
        self.ledovalblack = os.path.join('img', 'black_oval_58_29.png')
        self.ledovalgreen = os.path.join('img', 'green_oval_58_29.png')
        self.ledovalyellow = os.path.join('img', 'yellow_oval_58_29.png')
        self.ledovalred = os.path.join('img', 'red_oval_58_29.png')

        # round leds
        self.pxmprndblack = QPixmap(self.ledblack)
        self.pxmprndgreen = QPixmap(self.ledgreen)
        self.pxmprndyellow = QPixmap(self.ledyellow)
        self.pxmprndred = QPixmap(self.ledred)
        # oval leds
        self.pxmpovlblack = QPixmap(self.ledovalblack)
        self.pxmpovlgreen = QPixmap(self.ledovalgreen)
        self.pxmpovlyellow = QPixmap(self.ledovalyellow)
        self.pxmpovlred = QPixmap(self.ledovalred)

        # -------------------------General--------------------------------------
        # load in the ui
        loadUi(os.path.join(os.getcwd(), nimspystartui), self)

        # set the window name
        self.setWindowTitle(__program__ + " v" + __version__)

        # TODO: investigate this and see if needed
        # file -> close
        # quit = QAction("&Quit", self)
        # quit.setShortcut(Qt.Key_Escape) #Qt.CTRL + Qt.Key_Q)
        # quit.triggered.connect(self.close_program)
        # move backward tab
        backTab = QAction("&Move Back Tab", self)
        backTab.setShortcut(Qt.CTRL + Qt.SHIFT + Qt.Key_BraceLeft)
        backTab.setStatusTip('Move back 1 tab')
        backTab.triggered.connect(lambda: self.display('b'))
        # move forward tab
        forwardTab = QAction("&Move Forward Tab", self)
        forwardTab.setShortcut(Qt.CTRL + Qt.SHIFT + Qt.Key_BraceRight)
        forwardTab.setStatusTip('Move forward 1 tab')
        forwardTab.triggered.connect(lambda: self.display('f'))

        # populating the menu bar
        mainMenu = self.menuBar()

        # fileMenu = mainMenu.addMenu('&File')
        # fileMenu.addAction(quit)

        viewMenu = mainMenu.addMenu('&View')
        viewMenu.addAction(backTab)
        viewMenu.addAction(forwardTab)

        # -------------------------Tab Control----------------------------------
        self.displayindex = TABSTARTENDRUN

        # controls which "tab" is displayed
        self.tb_metadata.clicked.connect(lambda: self.display(TABMETADATA))
        self.tb_datadisplay.clicked.connect(lambda: self.display(TABDATADISPLAY))
        self.tb_startend.clicked.connect(lambda: self.display(TABSTARTENDRUN))
        self.tb_sitereport.clicked.connect(lambda: self.display(TABSITEREPORT))
        self.tb_engineer.clicked.connect(lambda: self.display(TABENGINEERING))

        # -------------------------Serial Connection----------------------------
        # set the ngf logo
        self.iconpth = os.path.join('img', 'NGF_logo_75_75.png')
        pixmap = QPixmap(self.iconpth)
        self.label_icon.setPixmap(pixmap)

        # initialize the connection/packets/receive leds
        self.label_connection_led.setPixmap(self.pxmpovlblack)
        self.label_packets_led.setPixmap(self.pxmpovlblack)
        self.label_receiving_led.setPixmap(self.pxmpovlblack)

        # initialize and start the serial drop down list of the available ports
        self.portmonitor = PortMonitor()
        self.portmonitor.pyports.connect(self.change_ports_list)
        self.portmonitor.start()

        # initialize the port read thread
        self.readport = PortRead(qport=self.port)
        self.readport.serdata.connect(self.parse_packet)

        # set up current port speed
        self.change_speed_list()
        self.cb_speed.currentIndexChanged.connect(self.connection_change)

        # initialize the port drop down list
        self.cb_connection.InsertAlphabetically
        self.cb_connection.currentIndexChanged.connect(self.connection_change)

        # initialize/open the port on startup
        self.change_ports_list(list_ports())

        # start the read port thread
        self.readport.start()

        # set the receiving led timer
        self.receiving_led_timer = QTimer()
        self.receiving_led_timer.timeout.connect(lambda: self.set_receiving_led(False))

        # -------------------------MetaData Tab---------------------------------
        self.metadata = Metadata()

        # connect the metadata fields
        self.le_site_name.textEdited.connect(self.update_site_name_md)
        self.le_state_province.textEdited.connect(self.update_state_province_md)
        self.le_country.textEdited.connect(self.update_country_md)
        self.le_run_id.textEdited.connect(self.update_run_id_md)
        self.le_operator.textEdited.connect(self.update_operator)
        self.le_nims_id.textEdited.connect(self.update_nims_id_md)
        self.le_mag_id.textEdited.connect(self.update_mag_id_md)
        self.le_ns_dipole_length.textEdited.connect(self.update_ns_length)
        self.le_ns_dipole_heading.textEdited.connect(self.update_ns_azimuth)
        self.le_ew_dipole_length.textEdited.connect(self.update_ew_length)
        self.le_ew_dipole_heading.textEdited.connect(self.update_ew_azimuth)
        self.le_n_electrode_id.textEdited.connect(self.update_n_id_md)
        self.le_s_electrode_id.textEdited.connect(self.update_s_id_md)
        self.le_e_electrode_id.textEdited.connect(self.update_e_id_md)
        self.le_w_electrode_id.textEdited.connect(self.update_w_id_md)
        self.le_gnd_electrode_id.textEdited.connect(self.update_gnd_id)
        self.rb_x_layout.layout = 'X'
        self.rb_x_layout.toggled.connect(self.update_survey_layout)
        self.rb_l_layout.layout = 'L'
        self.rb_l_layout.toggled.connect(self.update_survey_layout)
        self.rb_t_layout.layout = 'T'
        self.rb_t_layout.toggled.connect(self.update_survey_layout)
        self.te_comments.textChanged.connect(self.update_comments_md)

        self.iconnorth = os.path.join('img', 'north_icon_46_101.png')
        pixmapnorth = QPixmap(self.iconnorth)
        self.label_north.setPixmap(pixmapnorth)

        # intialize the gps short cycle button/led
        self.set_short_cycle_led_metadata(nims.GPSINITIAL)
        self.set_almanac_led(False)

        # intialize the gps almanac button/led
        self.tb_shortcycle.clicked.connect(self.send_short_cycle)
        self.tb_almanac.clicked.connect(self.send_almanac)

        # -------------------------Start/End Run--------------------------------
        # start run leds
        self.set_short_cycle_led_start_end(nims.GPSINITIAL)
        self.set_metadata_led(nims.METAEMPTY)
        self.set_mag_ready_led(nims.MAGERROR)
        self.set_mag_north_led(False)
        self.set_ex_spec_led(False)
        self.set_ey_spec_led(False)
        self.set_start_run_led(False)

        # end run leds
        self.set_end_run_led(False)

        # Attach the short cycle buttons
        self.tb_shortcycle_2.clicked.connect(self.send_short_cycle)
        self.tb_shortcycle_3.clicked.connect(self.send_short_cycle)
        self.tb_shortcycle_4.clicked.connect(self.send_short_cycle)

        # Attach the start and end run buttons
        self.tb_start_run.clicked.connect(self.start_run)
        self.tb_end_run.clicked.connect(self.end_run)

        # Check if currently recording
        self.check_if_recording()

        # -------------------------Data Display---------------------------------
        # Gain LEDs initialization.
        self.set_gain_leds(nims.EXUEYU)

        # Connect the gain buttons
        self.tb_gain_xlyl.clicked.connect(self.send_gain_xlyl)
        self.tb_gain_xhyl.clicked.connect(self.send_gain_xhyl)
        self.tb_gain_xlyh.clicked.connect(self.send_gain_xlyh)
        self.tb_gain_xhyh.clicked.connect(self.send_gain_xhyh)

        # Connection the misc buttons
        self.tb_mag_light.toggled.connect(self.send_mag_light)
        self.tb_nims_leds.clicked.connect(self.send_nims_leds)

        # Draw the vertical graph labels
        self.label_ey = VerticalText(text='Ey (mV)')
        self.label_ex = VerticalText(text='Ex (mV)')
        self.label_hx = VerticalText(text='Hx (nT)')
        self.label_hy = VerticalText(text='Hy (nT)')
        self.label_hz = VerticalText(text='Hz (nT)')
        # Add the text to the layouts
        self.horlayout_ex_label.addWidget(self.label_ex)
        self.horlayout_ey_label.addWidget(self.label_ey)
        self.horlayout_hx_label.addWidget(self.label_hx)
        self.horlayout_hy_label.addWidget(self.label_hy)
        self.horlayout_hz_label.addWidget(self.label_hz)

        # Data initialization
        self.graphdata = Data(ticks=20)
        self.graphdata.update_hx(0)
        self.graphdata.update_hy(0)
        self.graphdata.update_hz(0)
        self.graphdata.update_ex(0)
        self.graphdata.update_ey(0)
        # Graph initialization
        self.graph_hx_ey = Graph()
        self.graph_hy_ex = Graph()
        self.graph_hz = Graph()
        self.layout_hx_ey.addWidget(self.graph_hx_ey)
        self.layout_hy_ex.addWidget(self.graph_hy_ex)
        self.layout_hz.addWidget(self.graph_hz)
        # Add data to the graphs
        self.graph_hx_ey.add_data_h(self.graphdata.xdata, self.graphdata.hx,
                                    color=Qt.red, align=Qt.AlignLeft)
        self.graph_hx_ey.add_data_e(self.graphdata.xdata, self.graphdata.ey,
                                    color=Qt.blue, align=Qt.AlignRight)
        self.graph_hy_ex.add_data_h(self.graphdata.xdata, self.graphdata.hy,
                                    color=Qt.red, align=Qt.AlignLeft)
        self.graph_hy_ex.add_data_e(self.graphdata.xdata, self.graphdata.ex,
                                    color=Qt.blue, align=Qt.AlignRight)
        self.graph_hz.add_data_h(self.graphdata.xdata, self.graphdata.hz,
                                 color=Qt.red, align=Qt.AlignLeft)

        # -------------------------Site Report----------------------------------
        self.sr = SiteReport()

        # monitor status change: Install/Check/Extract
        self.status_change()
        self.cb_status.currentIndexChanged.connect(self.status_change)

        # update run information
        self.le_run_id_sr.textEdited.connect(self.update_run_id_sr)
        self.le_site_name_sr.textEdited.connect(self.update_site_name_sr)
        self.le_state_province_sr.textEdited.connect(self.update_state_province_sr)
        self.le_country_sr.textEdited.connect(self.update_country_sr)
        self.le_crew.textEdited.connect(self.update_crew_sr)

        # update Meta section
        self.le_nims_id_sr.textEdited.connect(self.update_nims_id_sr)
        self.le_mag_id_sr.textEdited.connect(self.update_mag_id_sr)
        self.le_n_electrode_id_sr.textEdited.connect(self.update_n_id_sr)
        self.le_s_electrode_id_sr.textEdited.connect(self.update_s_id_sr)
        self.le_e_electrode_id_sr.textEdited.connect(self.update_e_id_sr)
        self.le_w_electrode_id_sr.textEdited.connect(self.update_w_id_sr)

        # update the gps information
        self.le_gps_lat_sr.textEdited.connect(self.update_gps_lat_sr)
        self.le_gps_lon_sr.textEdited.connect(self.update_gps_lon_sr)
        self.le_gps_alt_sr.textEdited.connect(self.update_gps_alt_sr)
        self.le_gps_dec_sr.textEdited.connect(self.update_gps_dec_sr)

        # update the battery and gain
        self.le_battery_voltage_sr.textEdited.connect(self.update_batt_volt_sr)
        self.le_ex_gain_sr.textEdited.connect(self.update_gain_sr)
        self.le_ey_gain_sr.textEdited.connect(self.update_gain_sr)

        # update the timing section
        self.le_last_time_stamp_sr.textEdited.connect(self.update_last_time_stamp_sr)
        self.le_first_time_stamp_sr.textEdited.connect(self.update_first_time_stamp_sr)

        # update the preinstallation measurements
        self.le_pre_e_ns_r_sr.textEdited.connect(self.update_pre_e_ns_r_sr)
        self.le_pre_e_sn_r_sr.textEdited.connect(self.update_pre_e_sn_r_sr)
        self.le_pre_e_ew_r_sr.textEdited.connect(self.update_pre_e_ew_r_sr)
        self.le_pre_e_we_r_sr.textEdited.connect(self.update_pre_e_we_r_sr)
        self.le_pre_e_ns_v_sr.textEdited.connect(self.update_pre_e_ns_v_sr)
        self.le_pre_e_ew_v_sr.textEdited.connect(self.update_pre_e_ew_v_sr)

        # update the installation measurements
        self.le_e_ns_r_sr.textEdited.connect(self.update_e_ns_r_sr)
        self.le_e_sn_r_sr.textEdited.connect(self.update_e_sr_r_sr)
        self.le_e_ew_r_sr.textEdited.connect(self.update_e_ew_r_sr)
        self.le_e_we_r_sr.textEdited.connect(self.update_e_we_r_sr)
        self.le_e_ng_r_sr.textEdited.connect(self.update_e_ng_r_sr)
        self.le_e_gn_r_sr.textEdited.connect(self.update_e_gn_r_sr)
        self.le_ex_gps_sr.textEdited.connect(self.update_ex_gps_sr)
        self.le_ey_gps_sr.textEdited.connect(self.update_ey_gps_sr)
        self.le_e_ns_vdc_sr.textEdited.connect(self.update_e_ns_vdc_sr)
        self.le_e_ew_vdc_sr.textEdited.connect(self.update_e_ew_vdc_sr)
        self.le_e_ng_vdc_sr.textEdited.connect(self.update_e_ng_vdc_sr)
        self.le_e_ns_vac_sr.textEdited.connect(self.update_e_ns_vac_sr)
        self.le_e_ew_vac_sr.textEdited.connect(self.update_e_ew_vac_sr)
        self.le_e_ng_vac_sr.textEdited.connect(self.update_e_ng_vac_sr)

        # update on a change directory
        self.le_change_directory_sr.setText(self.sr.savepath)

        # update comments
        self.te_comments_sr.textChanged.connect(self.update_comments_sr)

        # update the save directory
        self.tb_change_directory_sr.clicked.connect(self.path_on_click)

        # set the check mark
        self.set_check_sr(False)
        # write to file
        self.tb_generate_report_sr.clicked.connect(self.write_report)

        # -------------------------Engineering----------------------------------
        self.tb_record_raw.clicked.connect(self.record_raw_data)

    # -------------------------General------------------------------------------
    def close_program(self):
        if self.port.is_open():
            self.port.close()
        """Close the Program."""
        self.close()

    def keyPressEvent(self, e):
        """Handle Key Press Event."""
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Close:
            self.close()

    def display(self, i):
        if i == TABMETADATA:
            self.stackedWidget.setCurrentIndex(TABMETADATA)
            self.displayindex = TABMETADATA
            self.tb_metadata.setChecked(True)
        elif i == TABDATADISPLAY:
            self.stackedWidget.setCurrentIndex(TABDATADISPLAY)
            self.displayindex = TABDATADISPLAY
            self.tb_datadisplay.setChecked(True)
        elif i == TABSTARTENDRUN:
            self.stackedWidget.setCurrentIndex(TABSTARTENDRUN)
            self.displayindex = TABSTARTENDRUN
            self.tb_startend.setChecked(True)
        elif i == TABSITEREPORT:
            self.stackedWidget.setCurrentIndex(TABSITEREPORT)
            self.displayindex = TABSITEREPORT
            self.tb_sitereport.setChecked(True)
        elif i == TABENGINEERING:
            self.stackedWidget.setCurrentIndex(TABENGINEERING)
            self.displayindex = TABENGINEERING
            self.tb_engineer.setChecked(True)
        elif i == 'b':
            if self.displayindex == TABSTARTENDRUN:
                self.displayindex = TABENGINEERING
            else:
                self.displayindex -= 1
            self.display(self.displayindex)
        elif i == 'f':
            if self.displayindex == TABENGINEERING:
                self.displayindex = TABSTARTENDRUN
            else:
                self.displayindex += 1
            self.display(self.displayindex)

    # -------------------------Connection---------------------------------------
    def connection_change(self, i):
        # close the thread
        self.readport.stop()
        # wait for thread to close
        while self.readport.isRunning():
            continue
        # if port open, close it
        if self.port.port is not None:
            self.port.close()
        # assign new port
        self.port.port = self.cb_connection.currentText()
        self.port.baudrate = int(self.cb_speed.currentText())
        self.port.timeout = 0.5
        self.port.stopbits = 2
        print(f'{self.port}')
        # open the port
        if not self.port.is_open:
            # Handle when can't open port
            try:
                self.port.open()
            except (OSError, serial.SerialException):
                print(f'Failed to open port: {self.port.port}')

        if self.port.is_open:
            # set the connection led to green
            self.set_connection_led(True)
            # set the packets led to red
            self.set_packets_led(False)
            # clear packet
            self.packet = b''
            # start the read port again
            self.readport.start()
        else:
            self.set_connection_led(False)
            self.set_packets_led(False)

        self.set_receiving_led(False)

        print(f'Port Open: \t{self.port.is_open}')

    def set_connection_led(self, state):
        if state is True:
            self.label_connection_led.setPixmap(self.pxmpovlgreen)
        else:
            self.label_connection_led.setPixmap(self.pxmpovlred)

    def set_packets_led(self, state):
        if state is True:
            self.label_packets_led.setPixmap(self.pxmpovlgreen)
        else:
            self.label_packets_led.setPixmap(self.pxmpovlred)

    def set_receiving_led(self, state):
        if state is True:
            self.label_receiving_led.setPixmap(self.pxmpovlgreen)
        else:
            self.label_receiving_led.setPixmap(self.pxmpovlblack)

    def change_ports_list(self, ports):
        dellst = []  # items to be removed from QComboBox
        # get the port names
        pnames = [p.port for p in ports]
        # get the port names in QComboBox
        seritems = [self.cb_connection.itemText(i) for i in
                    range(self.cb_connection.count())]

        # insert new ports into the list
        for p in ports:
            # check for port already in list
            if p.port not in seritems:
                self.cb_connection.addItem(p.port)

        # check for items to delete
        for i, s in enumerate(seritems, 0):
            if s not in pnames:
                dellst.append(i)

        # remove ports from QComboBox
        if dellst != []:
            dellst = list(reversed(dellst))
            # iterate through list and remove items
            for i in dellst:
                self.cb_connection.removeItem(i)

    def change_speed_list(self):
        speeds = ['115200', '19200']
        for s in speeds:
            self.cb_speed.addItem(s)

    # -------------------------MetaData-----------------------------------------
    def get_file_name(self) -> str:
        default = 'data.bin'

        fn = self.le_filename.text()

        if fn == '':
            fn = default

        return fn

    def update_site_name_md(self):
        # get text and update metadata field
        sitename = self.le_site_name.text()

        self.update_site_name(sitename)

    def update_site_name(self, sn):
        # get text and update metadata field
        self.metadata.sitename = sn
        # update metadata led
        self.check_metatdata()

        # update site report site name
        self.sr.sitename = sn

        # update the site id
        self.le_site_name.setText(sn)
        self.le_site_name_sr.setText(sn)

    def update_state_province_md(self):
        # get text
        sp = self.le_state_province.text()

        self.update_state_province(sp)

    def update_state_province(self, sp):
        # get text and update metadata field
        self.metadata.stateprov = sp
        # update metadata led
        self.check_metatdata()

        # update site report site state
        self.sr.sitestate = sp

        self.le_state_province.setText(sp)
        self.le_state_province_sr.setText(sp)

    def update_country_md(self):
        # get text
        cntry = self.le_country.text()

        self.update_country(cntry)

    def update_country(self, cntry):
        # get text and update metadata field
        self.metadata.country = cntry
        # update metadata led
        self.check_metatdata()

        # update site report country
        self.sr.country = cntry

        self.le_country.setText(cntry)
        self.le_country_sr.setText(cntry)

    def update_run_id_md(self):
        # get text and update metadata field
        # self.metadata.runid = self.le_run_id.text()
        txt = self.le_run_id.text()
        # update metadata led
        # self.check_metatdata()
        self.update_run_id(txt)

        # update the run id on site report
        # self.le_run_id_sr.setText(self.metadata.runid)

    def update_run_id(self, txt):
        # get text and update metadata field
        self.metadata.runid = txt
        # update metadata
        self.check_metatdata()

        # update the run id
        self.le_run_id_sr.setText(txt)
        self.le_run_id.setText(txt)

        self.sr.update_savename(txt)
        self.update_save_directory_sr()

    def update_operator(self):
        # get text and update metadata field
        self.metadata.operator = self.le_operator.text()
        # update metadata led
        self.check_metatdata()

    def update_nims_id_md(self):
        # get text and update metadata field
        nid = self.le_nims_id.text()

        self.update_nims_id(nid)

    def update_nims_id(self, nid):
        # get text and update metadata field
        self.metadata.nimsid = nid
        # update metadata led
        self.check_metatdata()

        # update the site report
        self.sr.nimsid = nid

        # update the nims id
        self.le_nims_id.setText(nid)
        self.le_nims_id_sr.setText(nid)

    def update_mag_id_md(self):
        # get text and update metadata field
        mid = self.le_mag_id.text()

        self.update_mag_id(mid)

    def update_mag_id(self, mid):
        # get text and update metadata field
        self.metadata.magid = mid
        # update metadata led
        self.check_metatdata()

        # update the site report
        self.sr.magid = mid

        # update the mag id
        self.le_mag_id.setText(mid)
        self.le_mag_id_sr.setText(mid)

    def update_ns_length(self):
        # get text and update metadata field
        try:
            self.metadata.nsdipolelen = int(self.le_ns_dipole_length.text())
        except ValueError:
            self.le_ns_dipole_length.setText('')
        # update metadata led
        self.check_metatdata()

    def update_ns_azimuth(self):
        # get text and update metadata field
        try:
            self.metadata.nsdipoleazi = int(self.le_ns_dipole_heading.text())
        except ValueError:
            self.le_ns_dipole_heading.setText('')
        # update metadata led
        self.check_metatdata()

    def update_ew_length(self):
        # get text and update metadata field
        try:
            self.metadata.ewdipolelen = int(self.le_ew_dipole_length.text())
        except ValueError:
            self.le_ew_dipole_length.setText('')
        # update metadata led
        self.check_metatdata()

    def update_ew_azimuth(self):
        # get text and update metadata field
        try:
            self.metadata.ewdipoleazi = int(self.le_ew_dipole_heading.text())
        except ValueError:
            self.le_ew_dipole_heading.setText('')
        # update metadata led
        self.check_metatdata()

    def update_n_id_md(self):
        eid = self.le_n_electrode_id.text()

        self.update_n_id(eid)

    def update_n_id(self, eid):
        self.metadata.ndipoleid = eid
        # update metadata led
        self.check_metatdata()

        # update the site report
        self.sr.enid = eid

        # update the electrode id
        self.le_n_electrode_id.setText(eid)
        self.le_n_electrode_id_sr.setText(eid)

    def update_s_id_md(self):
        eid = self.le_s_electrode_id.text()

        self.update_s_id(eid)

    def update_s_id(self, eid):
        self.metadata.sdipoleid = eid
        # update metadata led
        self.check_metatdata()

        # update the site report
        self.sr.esid = eid

        # update the electrode id
        self.le_s_electrode_id.setText(eid)
        self.le_s_electrode_id_sr.setText(eid)

    def update_e_id_md(self):
        eid = self.le_e_electrode_id.text()

        self.update_e_id(eid)

    def update_e_id(self, eid):
        self.metadata.edipoleid = eid
        # update metadata led
        self.check_metatdata()

        # update the site report
        self.sr.eeid = eid

        # update the electrode id
        self.le_e_electrode_id.setText(eid)
        self.le_e_electrode_id_sr.setText(eid)

    def update_w_id_md(self):
        eid = self.le_w_electrode_id.text()

        self.update_w_id(eid)

    def update_w_id(self, eid):
        self.metadata.wdipoleid = eid
        # update metadata led
        self.check_metatdata()

        # update the site report
        self.sr.ewid = eid

        # update the electrode id
        self.le_w_electrode_id.setText(eid)
        self.le_w_electrode_id_sr.setText(eid)

    def update_gnd_id(self):
        # get text and update metadata field
        self.metadata.gndelectrode = self.le_gnd_electrode_id.text()
        # update metadata led
        self.check_metatdata()

    def update_survey_layout(self):
        sender = self.sender()
        if sender.isChecked():
            # get checked value
            self.metadata.surveylayout = sender.layout
            # update metadata led
            self.check_metatdata()

    def update_comments_md(self):
        # get text and update metadata field
        comments = self.te_comments.toPlainText()

        # check the comments length
        self.check_comments_length(comments)

        # set comments
        self.set_comments_sr(comments)

    def set_comments_md(self, comments):
        # check the comments length
        self.check_comments_length(comments)

        # disconnect the signals
        self.te_comments.textChanged.disconnect()
        # update the comments
        self.te_comments.setText(comments)
        # reconnect the signals
        self.te_comments.textChanged.connect(self.update_comments_md)

    def check_comments_length(self, comments):
        """Check for the length of the comment section.

        Checks the length of the metadata comments for overrun.

        Args:
            comments (String): The present comments in the md section.

        Returns:

        """
        max = 150

        if len(comments) >= max:
            # get text and update metadata field
            self.metadata.comments = comments[0:max - 1]
            self.set_comments_label(True)
        else:
            # get text and update metadata field
            self.metadata.comments = comments
            self.set_comments_label(False)

        # update metadata led
        self.check_metatdata()

    def set_comments_label(self, flag):
        """Set the comment label.

        The set_comments_label function sets the comments label on the MetaData
        tab, depending on the length of the metadata comments.

        Args:
            flag (bool): True, comment overrun, False, < 150 chars

        Returns:

        """
        label = 'Field Crew Comments'
        warning = 'TOO MANY CHARACTERS!'

        if flag:
            self.l_comments_md.setText(warning)
            self.l_comments_md.setStyleSheet('color: red')
        else:
            self.l_comments_md.setText(label)
            self.l_comments_md.setStyleSheet('color: black')

    def set_short_cycle_led_metadata(self, state):
        if state == nims.GPSINITIAL:
            self.label_short_cycle_led.setPixmap(self.pxmprndblack)
        elif state == nims.GPSAQLOCK:
            self.label_short_cycle_led.setPixmap(self.pxmprndyellow)
        elif state == nims.GPSRECEIVING:
            self.label_short_cycle_led.setPixmap(self.pxmprndyellow)
        elif state == nims.GPSRECEIVED:
            self.label_short_cycle_led.setPixmap(self.pxmprndgreen)
        elif state == nims.GPSALMANAC:
            self.label_short_cycle_led.setPixmap(self.pxmprndblack)

    def update_gps_value_m(self, value):
        # assign the value in the metadata panel
        self.le_gps_status_byte_m.setText(value)

    def set_almanac_led(self, state):
        if state is True:
            self.label_almanac_led.setPixmap(self.pxmprndgreen)
        else:
            self.label_almanac_led.setPixmap(self.pxmprndblack)

    def clear_gps_string_m(self):
        self.te_gps_string_m.setText('')

    def update_gps_string_m(self):
        self.te_gps_string_m.setText(self.gpsstring)

    def update_gps_metadata_string(self, gprmc, gpgga):
        # parse the needed data from the sentences
        date = gprmc[nims.GPSDATE]
        time = gpgga[nims.GPSTIME].split('.')[0]
        decl = gprmc[nims.GPSDECL]
        decd = gprmc[nims.GPSDECD]
        print(date)
        print(time)
        print(decl)
        print(decd)

        if decl != '' and decd != '':
            self.update_gps_dec(decl, decd)

        lat = "%s %s" % (self.dm_to_dd(gpgga[nims.GPSLATI]), gpgga[nims.GPSLATD])
        lon = "%s %s" % (self.dm_to_dd(gpgga[nims.GPSLONG]), gpgga[nims.GPSLOND])
        alt = gpgga[nims.GPSALTI]

        # format the data and time
        date = '/'.join([date[i:i + 2] for i in range(0, len(date), 2)])
        time = ':'.join([time[i:i + 2] for i in range(0, len(time), 2)])

        # update the metadata string
        self.metadata.gpstimestamp = "%s %s %s %s %s" % (date, time, lat, lon, alt)

        # update GUI GPS string
        self.te_gps_metadata_string.setText(self.metadata.gpstimestamp)

        # update site report timestamp
        self.update_timestamp_sr(date, time)

    def dm_to_dd(self, ll_dms: str) -> str:
        """Convert from degree minute to decimal degree.

        The dms_to_dd function takes a degree minute gps lat/long and
        convert it to decimal degrees.
        Decimal Degrees = degrees + (minutes/60)

        Parameters
        ----------
        ll_dms : string
            GPS lat/long in 'DD{D}MM.M{M:}' format.

        Returns
        -------
        string
            GPS lat/long in 'D{D:}.dddddd'

        """
        try:
            i = ll_dms.index('.')
            deg = int(ll_dms[:i - 2])
            min = float(ll_dms[i - 2:]) / 60
        except (IndexError, ValueError) as error:
            deg = 0
            min = 0

        return "{:.6f}".format(deg + min)

    def update_gps_time(self):
        # initialize empty time
        time = ''
        # parse the string into a list
        gpslist = self.metadata.gpstimestamp.split(' ')

        # extract the time, check for array error
        try:
            time = gpslist[nims.GPSSTRINGTIME]
        except IndexError:
            pass

        # update the gps field
        self.le_gps_time.setText(time)

    def update_gps_date(self):
        # initialize empty date
        date = ''
        # parse the string into a list
        gpslist = self.metadata.gpstimestamp.split(' ')

        # extract the date, check for array error
        try:
            date = gpslist[nims.GPSSTRINGDATE]
        except IndexError:
            pass

        # update the gps field
        self.le_gps_date.setText(date)

    def update_gps_lat(self):
        # initialize empty latitude
        lat = ''
        # parse the string into a list
        gpslist = self.metadata.gpstimestamp.split(' ')

        # extract the lat, check for array error
        try:
            lat = "{} {}".format(gpslist[nims.GPSSTRINGLATI], gpslist[nims.GPSSTRINGLATD])
        except IndexError:
            pass

        # update the gps field
        self.le_gps_lat.setText(lat)
        # update the site report tab
        self.le_gps_lat_sr.setText(lat)
        # update the site report
        self.sr.lat = lat

    def update_gps_lon(self):
        # initialize empty longitude
        lon = ''
        # parse the string into a list
        gpslist = self.metadata.gpstimestamp.split(' ')

        # extract the longitude, check for array error
        try:
            lon = "%s %s" % (gpslist[nims.GPSSTRINGLONG], gpslist[nims.GPSSTRINGLOND])
        except IndexError:
            pass

        # update the gps field
        self.le_gps_lon.setText(lon)
        # update the site report tab
        self.le_gps_lon_sr.setText(lon)
        # update the site report
        self.sr.lon = lon

    def update_gps_alt(self):
        # initialize empty altitude
        alt = ''
        # parse the string into a list
        gpslist = self.metadata.gpstimestamp.split(' ')

        # extract the alt, check for array error
        try:
            alt = gpslist[nims.GPSSTRINGALTI]
        except IndexError:
            pass

        # update the gps field
        self.le_gps_alt.setText(alt)
        self.le_gps_alt_sr.setText(alt)
        # update the site report
        self.sr.alt = alt

    def send_short_cycle(self):
        if self.board == nims.MINERVA:
            print(f'Send Command: \t{bytes.fromhex(nims.SHORTCYCLE)}')
            self.send_byte(bytes.fromhex(nims.SHORTCYCLE))
        else:
            self.send_byte(bytes.fromhex(nims.SENDNIMS))
            self.send_byte(bytes.fromhex(nims.SHORTCYCLE))

    def send_almanac(self):
        if self.board == nims.MINERVA:
            print(f'Send Command: \t{bytes.fromhex(nims.ALMANAC)}')
            self.send_byte(bytes.fromhex(nims.ALMANAC))
        else:
            self.send_byte(bytes.fromhex(nims.SENDNIMS))
            self.send_byte(bytes.fromhex(nims.ALMANAC))

    # -------------------------Data Display-------------------------------------
    def set_gain_leds(self, state):
        # set all leds to black
        self.label_gain_xlyl_led.setPixmap(self.pxmpovlblack)
        self.label_gain_xhyl_led.setPixmap(self.pxmpovlblack)
        self.label_gain_xlyh_led.setPixmap(self.pxmpovlblack)
        self.label_gain_xhyh_led.setPixmap(self.pxmpovlblack)

        # Only turn the correct LED green
        if state == nims.EXLEYL:
            self.label_gain_xlyl_led.setPixmap(self.pxmpovlgreen)
        elif state == nims.EXHEYL:
            self.label_gain_xhyl_led.setPixmap(self.pxmpovlgreen)
        elif state == nims.EXLEYH:
            self.label_gain_xlyh_led.setPixmap(self.pxmpovlgreen)
        elif state == nims.EXHEYH:
            self.label_gain_xhyh_led.setPixmap(self.pxmpovlgreen)

    def send_gain_xlyl(self):
        if self.board == nims.MINERVA:
            print(f'Send Command: \t{bytes.fromhex(nims.GAINXLYL)}')
            self.send_byte(bytes.fromhex(nims.GAINXLYL))
        else:
            self.send_byte(bytes.fromhex(nims.SENDNIMS))
            self.send_byte(bytes.fromhex(nims.GAINXLYL))

    def send_gain_xhyl(self):
        # send low gain command first
        self.send_gain_xlyl()
        # wait for gain to change
        sleep(0.15)
        if self.board == nims.MINERVA:
            # send gain command
            print(f'Send Command: \t{bytes.fromhex(nims.GAINXHYL)}')
            self.send_byte(bytes.fromhex(nims.GAINXHYL))
        else:
            # send the command to forward to NIMS
            self.send_byte(bytes.fromhex(nims.SENDNIMS))
            # send gain command
            self.send_byte(bytes.fromhex(nims.GAINXHYL))

    def send_gain_xlyh(self):
        # send low gain command first
        self.send_gain_xlyl()
        # wait for gain to change
        sleep(0.15)
        if self.board == nims.MINERVA:
            # send gain command
            print(f'Send Command: \t{bytes.fromhex(nims.GAINXLYH)}')
            self.send_byte(bytes.fromhex(nims.GAINXLYH))
        else:
            # send the command to forward to NIMS
            self.send_byte(bytes.fromhex(nims.SENDNIMS))
            # send gain command
            self.send_byte(bytes.fromhex(nims.GAINXLYH))

    def send_gain_xhyh(self):
        # send low gain command first
        self.send_gain_xlyl()
        # wait for gain to change
        sleep(0.15)
        if self.board == nims.MINERVA:
            # send gain command
            print(f'Send Command: \t{bytes.fromhex(nims.GAINXHYH)}')
            self.send_byte(bytes.fromhex(nims.GAINXHYH))
        else:
            # send the command to forward to NIMS
            self.send_byte(bytes.fromhex(nims.SENDNIMS))
            # send gain command
            self.send_byte(bytes.fromhex(nims.GAINXHYH))

    def send_mag_light(self, checked):
        if self.board == nims.MINERVA:
            if checked:
                print(f'Toggle Mag Light: \t{False}')
                self.port.setRTS(False)
            else:
                print(f'Toggle Mag Light: \t{True}')
                self.port.setRTS(True)
        else:
            if checked:
                # send mag light turn on command
                self.send_byte(bytes.fromhex(nims.MAGLIGHTON))
            else:
                # send mag light turn off command
                self.send_byte(bytes.fromhex(nims.MAGLIGHTOFF))

    def send_nims_leds(self):
        # send the nims command
        if self.board == nims.MINERVA:
            print(f'Send Command: \t{bytes.fromhex(nims.NIMSLEDS)}')
            self.send_byte(bytes.fromhex(nims.NIMSLEDS))
        else:
            self.send_byte(bytes.fromhex(nims.SENDNIMS))
            self.send_byte(bytes.fromhex(nims.NIMSLEDS))

    def update_graphs(self):
        # update graphs
        self.graph_hx_ey.add_point_h(self.graphdata.hx)
        self.graph_hx_ey.add_point_e(self.graphdata.ey)
        self.graph_hy_ex.add_point_h(self.graphdata.hy)
        self.graph_hy_ex.add_point_e(self.graphdata.ex)
        self.graph_hz.add_point_h(self.graphdata.hz)

    def update_sensor_values(self):
        self.set_hx_label(self.graphdata.hx[-1])
        self.set_hy_label(self.graphdata.hy[-1])
        self.set_hz_label(self.graphdata.hz[-1])
        self.set_ex_label(self.graphdata.ex[-1])
        self.set_ey_label(self.graphdata.ey[-1])

    def set_hx_label(self, value):
        self.le_hx.setText('%.3f' % (value))

    def set_hy_label(self, value):
        self.le_hy.setText('%.3f' % (value))

    def set_hz_label(self, value):
        self.le_hz.setText('%.3f' % (value))

    def set_ex_label(self, value):
        self.le_ex.setText('%.3f' % (value))

    def set_ey_label(self, value):
        self.le_ey.setText('%.3f' % (value))

    # -------------------------Start/End Run------------------------------------
    def check_if_recording(self):
        if self.board == nims.OWL:
            pass
            # TODO: send recording command

    def set_short_cycle_led_start_end(self, state):
        if state == nims.GPSINITIAL:
            self.label_short_cycle_led_2.setPixmap(self.pxmpovlblack)
            self.label_short_cycle_led_3.setPixmap(self.pxmpovlblack)
            self.label_short_cycle_led_4.setPixmap(self.pxmpovlblack)
        elif state == nims.GPSAQLOCK:
            self.label_short_cycle_led_2.setPixmap(self.pxmpovlyellow)
            self.label_short_cycle_led_3.setPixmap(self.pxmpovlyellow)
            self.label_short_cycle_led_4.setPixmap(self.pxmpovlyellow)
        elif state == nims.GPSRECEIVING:
            self.label_short_cycle_led_2.setPixmap(self.pxmpovlyellow)
            self.label_short_cycle_led_3.setPixmap(self.pxmpovlyellow)
            self.label_short_cycle_led_4.setPixmap(self.pxmpovlyellow)
        elif state == nims.GPSRECEIVED:
            self.label_short_cycle_led_2.setPixmap(self.pxmpovlgreen)
            self.label_short_cycle_led_3.setPixmap(self.pxmpovlgreen)
            self.label_short_cycle_led_4.setPixmap(self.pxmpovlgreen)
        elif state == nims.GPSALMANAC:
            self.label_short_cycle_led_2.setPixmap(self.pxmpovlblack)
            self.label_short_cycle_led_3.setPixmap(self.pxmpovlblack)
            self.label_short_cycle_led_4.setPixmap(self.pxmpovlblack)

    def set_mag_ready_led(self, state):
        if state == nims.MAGREADY:
            self.label_mag_ready_led.setPixmap(self.pxmpovlgreen)
        elif state == nims.MAGSLEWING:
            self.label_mag_ready_led.setPixmap(self.pxmpovlyellow)
        elif state == nims.MAGERROR:
            self.label_mag_ready_led.setPixmap(self.pxmpovlred)
        else:
            self.label_mag_ready_led.setPixmap(self.pxmpovlblack)

    def set_mag_north_led(self, state):
        if state is True:
            self.label_mag_north_led.setPixmap(self.pxmpovlgreen)
        else:
            self.label_mag_north_led.setPixmap(self.pxmpovlyellow)

    def set_ex_spec_led(self, state):
        if state is True:
            self.label_ex_spec_led.setPixmap(self.pxmpovlgreen)
        else:
            self.label_ex_spec_led.setPixmap(self.pxmpovlyellow)

    def set_ey_spec_led(self, state):
        if state is True:
            self.label_ey_spec_led.setPixmap(self.pxmpovlgreen)
        else:
            self.label_ey_spec_led.setPixmap(self.pxmpovlyellow)

    def set_metadata_led(self, state):
        if state is nims.METACOMPLETE:
            self.label_metadata_led.setPixmap(self.pxmpovlgreen)
        elif state == nims.METAPARTIAL:
            self.label_metadata_led.setPixmap(self.pxmpovlyellow)
        else:
            self.label_metadata_led.setPixmap(self.pxmpovlred)

    def set_start_run_led(self, state):
        if state is True:
            self.label_start_run_led.setPixmap(self.pxmprndgreen)
            self.label_end_run_led.setPixmap(self.pxmprndblack)
        else:
            self.label_start_run_led.setPixmap(self.pxmprndblack)

    def set_end_run_led(self, state):
        if state is True:
            self.label_end_run_led.setPixmap(self.pxmprndred)
            self.label_start_run_led.setPixmap(self.pxmprndblack)
        else:
            self.label_end_run_led.setPixmap(self.pxmprndblack)

    def update_ready_led(self):
        status = self.packet[nims.STATUSSRT:nims.STATUSSTP].hex()
        if status == nims.MAGREADY:
            self.set_mag_ready_led(nims.MAGREADY)
        elif status == nims.MAGSLEWING:
            self.set_mag_ready_led(nims.MAGSLEWING)
        elif status == nims.MAGERROR:
            self.set_mag_ready_led(nims.MAGERROR)
        else:
            self.set_mag_ready_led(status)

    def update_north_led(self):
        value = self.graphdata.hy[-1]
        # Check if mag is in range of north.
        if value < nims.MAGHIGHRANGE and value > nims.MAGLOWRANGE:
            self.set_mag_north_led(True)
        else:
            self.set_mag_north_led(False)

    def update_e_spec_leds(self):
        mvoltcutoff = 16
        gain = self.packet[nims.STATUSSRT:nims.STATUSSTP]

        if self.graphdata.ex[-1] >= mvoltcutoff:
            self.set_ex_spec_led(True)
        elif gain == bytes.fromhex(nims.EXHEYL) or gain == bytes.fromhex(nims.EXHEYH):
            self.set_ex_spec_led(True)
        else:
            self.set_ex_spec_led(False)

        if self.graphdata.ey[-1] >= mvoltcutoff:
            self.set_ey_spec_led(True)
        elif gain == bytes.fromhex(nims.EXLEYH) or gain == bytes.fromhex(nims.EXHEYH):
            self.set_ey_spec_led(True)
        else:
            self.set_ey_spec_led(False)

    def check_metatdata(self):
        empty = False
        allempty = False

        # check all meta boxes
        if self.le_site_name.text() == '' or self.le_state_province.text() == '' or\
                self.le_country.text() == '' or self.le_run_id.text() == '' or\
                self.le_operator.text() == '' or self.le_nims_id.text() == '' or\
                self.le_mag_id.text() == '' or self.le_ns_dipole_length.text == '' or\
                self.le_ns_dipole_heading.text() == '' or self.le_ew_dipole_length.text == '' or\
                self.le_ew_dipole_heading.text() == '' or self.le_n_electrode_id.text() == '' or\
                self.le_s_electrode_id.text() == '' or self.le_e_electrode_id.text() == '' or\
                self.le_w_electrode_id.text() == '' or self.le_gnd_electrode_id.text() == '' or\
                self.te_comments.toPlainText() == '':
            empty = True

        if self.le_site_name.text() == '' and self.le_state_province.text() == '' and\
                self.le_country.text() == '' and self.le_run_id.text() == ''and\
                self.le_operator.text() == '' and self.le_nims_id.text() == '' and\
                self.le_mag_id.text() == '' and self.le_ns_dipole_length.text == '' and\
                self.le_ns_dipole_heading.text() == '' and self.le_ew_dipole_length.text == '' and\
                self.le_ew_dipole_heading.text() == '' and self.le_n_electrode_id.text() == '' and\
                self.le_s_electrode_id.text() == '' and self.le_e_electrode_id.text() == '' and\
                self.le_w_electrode_id.text() == '' and self.le_gnd_electrode_id.text() == '' and\
                self.te_comments.toPlainText() == '':
            allempty = True

        # set the metadata led
        if allempty is True:
            self.set_metadata_led(nims.METAEMPTY)
        elif empty is True:
            self.set_metadata_led(nims.METAPARTIAL)
        else:
            self.set_metadata_led(nims.METACOMPLETE)

    def start_run(self):
        # turn on the start run led
        self.set_start_run_led(True)
        # pull the current time from the computer
        self.metadata.set_head_comp_time()
        # compile the metadata
        self.metadata.make_header()
        # stop recieving packets
        self.readport.stop()

        # start the run
        if self.board == nims.MINERVA:
            print(f'Send Command: \t{bytes.fromhex(nims.HEADER)}')
            self.send_byte(bytes.fromhex(nims.HEADER))
            sleep(0.30)
            print(f'Send Command: \t{bytes.fromhex(nims.RECORD)}')
            self.send_byte(bytes.fromhex(nims.RECORD))
            sleep(0.50)
            self.send_header_blocks()
            sleep(0.50)
            print(f'Send Command: \t{bytes.fromhex(nims.HEADER)}')
            self.send_byte(bytes.fromhex(nims.HEADER))
        else:
            self.send_file_name()
            sleep(0.15)
            self.send_file_header()
            sleep(0.15)
            self.send_byte(bytes.fromhex(nims.RECORD))

        # Clear the packet and start reading from the port
        self.packet = b''
        self.readport.start()

    def send_file_name(self):
        self.send_byte(bytes.fromhex(nims.FLENAME))
        self.send_byte(self.get_file_name().encode('utf-8'))
        self.send_byte(bytes.fromhex(nims.FLENAME))

    def send_header_blocks(self):
        blocksize = 64
        i = 0
        j = blocksize
        while(j <= len(self.metadata.fileheader)):
            print(f'Send Header: \n{self.metadata.fileheader[i:j].encode("utf-8")}')
            self.send_byte(self.metadata.fileheader[i:j].encode('utf-8'))
            i += blocksize
            j += blocksize
            sleep(0.15)

    def send_file_header(self):
        self.send_byte(bytes.fromhex(nims.HEADER))
        self.send_byte(self.metadata.fileheader.encode('utf-8'))
        self.send_byte(bytes.fromhex(nims.HEADER))

    def end_run(self):
        # toggle start run/end run leds
        self.set_end_run_led(True)
        # send end run command
        print(f'Send Command: \t{bytes.fromhex(nims.ENDREC)}')
        self.send_byte(bytes.fromhex(nims.ENDREC))

    # -------------------------Site Report--------------------------------------
    def status_change(self):
        self.sr.status = self.cb_status.currentText()
        if self.sr.status == 'Install':
            self.svr_enable_install()
        elif self.sr.status == 'Check':
            self.svr_enable_check()
        elif self.sr.status == 'Extract':
            self.svr_enable_extract()

    def svr_enable_install(self):
        self.svr_preinstall_electrodes(True)
        self.svr_timing('Install')

    def svr_enable_check(self):
        self.svr_preinstall_electrodes(False)
        self.svr_timing('Check')

    def svr_enable_extract(self):
        self.svr_preinstall_electrodes(False)
        self.svr_timing('Extract')

    def svr_timing(self, state):
        if state == 'Install':
            self.le_last_time_stamp_sr.setText('')
            self.sr.last_ts = ''
            self.label_104.setText("At Installation:")
            self.le_last_time_stamp_sr.setEnabled(False)
            self.le_last_time_stamp_sr.setStyleSheet("background-color: rgb(104, 104, 104)")
            self.le_first_time_stamp_sr.setEnabled(True)
            self.le_first_time_stamp_sr.setStyleSheet("background-color: rgb(255, 255, 255)")
        elif state == 'Check':
            self.label_104.setText("At Check:")
            self.le_last_time_stamp_sr.setEnabled(True)
            self.le_last_time_stamp_sr.setStyleSheet("background-color: rgb(255, 255, 255)")
            self.le_first_time_stamp_sr.setEnabled(True)
            self.le_first_time_stamp_sr.setStyleSheet("background-color: rgb(255, 255, 255)")
        elif state == 'Extract':
            self.label_104.setText("At Extraction:")
            self.le_last_time_stamp_sr.setEnabled(True)
            self.le_last_time_stamp_sr.setStyleSheet("background-color: rgb(255, 255, 255)")
            self.le_first_time_stamp_sr.setText('')
            self.sr.first_ts = ''
            self.le_first_time_stamp_sr.setEnabled(False)
            self.le_first_time_stamp_sr.setStyleSheet("background-color: rgb(104, 104, 104)")

    def svr_preinstall_electrodes(self, state):
        if state is True:
            back_color = "background-color: rgb(255, 255, 255)"
        else:
            back_color = "background-color: rgb(104, 104, 104)"

        # clear values if disabled
        if state is False:
            self.clear_pre_e_sr()

        # set enabled/disabled
        self.le_pre_e_ns_r_sr.setEnabled(state)
        self.le_pre_e_sn_r_sr.setEnabled(state)
        self.le_pre_e_ew_r_sr.setEnabled(state)
        self.le_pre_e_we_r_sr.setEnabled(state)
        self.le_pre_e_ns_v_sr.setEnabled(state)
        self.le_pre_e_ew_v_sr.setEnabled(state)

        # set the background colors
        self.le_pre_e_ns_r_sr.setStyleSheet(back_color)
        self.le_pre_e_sn_r_sr.setStyleSheet(back_color)
        self.le_pre_e_ew_r_sr.setStyleSheet(back_color)
        self.le_pre_e_we_r_sr.setStyleSheet(back_color)
        self.le_pre_e_ns_v_sr.setStyleSheet(back_color)
        self.le_pre_e_ew_v_sr.setStyleSheet(back_color)

    def set_check_sr(self, state):
        if state is True:
            checkpath = os.path.join('img', 'check_green_50_50.png')
        else:
            checkpath = os.path.join('img', 'x_red_50_50.png')

        checkpixmap = QPixmap(checkpath)
        self.label_check_sr.setPixmap(checkpixmap)

    def path_on_click(self):
        self.hide()
        savedir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.sr.update_savepath(savedir)

        print(f'Site Report save directory: \t{savedir}')
        self.show()

        self.update_save_directory_sr()

    def update_save_directory_sr(self):
        self.le_change_directory_sr.setText(os.path.join(self.sr.savepath, self.sr.savename))

    def update_site_name_sr(self):
        # get text and update metadata field
        sitename = self.le_site_name_sr.text()

        self.update_site_name(sitename)

    def update_state_province_sr(self):
        # get text and update metadata field
        sp = self.le_state_province_sr.text()

        self.update_state_province(sp)

    def update_country_sr(self):
        # get text and update metadata field
        cntry = self.le_country_sr.text()

        self.update_country(cntry)

    def update_crew_sr(self):
        self.sr.crew = self.le_crew.text()

    def update_run_id_sr(self):
        txt = self.le_run_id_sr.text()

        self.update_run_id(txt)

    def update_nims_id_sr(self):
        txt = self.le_nims_id_sr.text()

        self.update_nims_id(txt)

    def update_mag_id_sr(self):
        txt = self.le_mag_id_sr.text()

        self.update_mag_id(txt)

    def update_n_id_sr(self):
        txt = self.le_n_electrode_id_sr.text()

        self.update_n_id(txt)

    def update_s_id_sr(self):
        txt = self.le_s_electrode_id_sr.text()

        self.update_s_id(txt)

    def update_e_id_sr(self):
        txt = self.le_e_electrode_id_sr.text()

        self.update_e_id(txt)

    def update_w_id_sr(self):
        txt = self.le_w_electrode_id_sr.text()

        self.update_w_id(txt)

    def update_gps_lat_sr(self):
        self.sr.lat = self.le_gps_lat_sr.text()

    def update_gps_lon_sr(self):
        self.sr.lon = self.le_gps_lon_sr.text()

    def update_gps_alt_sr(self):
        self.sr.alt = self.le_gps_alt_sr.text()

    def update_gps_dec(self, decl, decd):
        d = {'N': '+', 'S': '-', 'E': '+', 'W': '-'}
        try:
            dec = '{}{}'.format(d[decd[0]], decl)
            self.le_gps_dec_sr.setText("{0:.2f}".format(float(dec)))

        except SyntaxError:
            self.le_gps_dec_sr.setText(str(0))

        self.update_gps_dec_sr()

    def update_gps_dec_sr(self):
        self.sr.dec = self.le_gps_dec_sr.text()

    def update_batt_volt_sr(self):
        self.sr.battery = self.le_battery_voltage_sr.text()

    def update_gain_sr(self):
        exgain = self.verify_gain_value(self.le_ex_gain_sr.text())
        eygain = self.verify_gain_value(self.le_ey_gain_sr.text())

        # set values
        self.le_ex_gain_sr.setText(exgain)
        self.le_ey_gain_sr.setText(eygain)

        # clear the gain
        self.sr.gain = ''
        # set the new gain
        if exgain == 'L' and eygain == 'L':
            self.sr.gain = 'L'
        elif exgain == 'H' and eygain == 'L':
            self.sr.gain = 'X'
        elif exgain == 'L' and eygain == 'H':
            self.sr.gain = 'Y'
        elif exgain == 'H' and eygain == 'H':
            self.sr.gain = 'H'

    def verify_gain_value(self, val: str) -> str:
        # verify text is empty, h, l
        gain = ''

        if val == 'L' or val == 'l':
            gain = 'L'
        elif val == 'H' or val == 'h':
            gain = 'H'

        return gain

    def update_last_time_stamp_sr(self):
        self.sr.last_ts = self.le_last_time_stamp_sr.text()

    def update_first_time_stamp_sr(self):
        self.sr.first_ts = self.le_first_time_stamp_sr.text()

    def update_timestamp_sr(self, date, time):
        d = date.split('/')
        try:
            dt = "20{}-{}-{} {}".format(d[2], d[0], d[1], time)
        except IndexError:
            dt = "{} {}".format(date, time)

        if self.sr.status == 'Extract':
            self.le_last_time_stamp_sr.setText(dt)
            self.sr.last_ts = dt
        else:
            self.le_first_time_stamp_sr.setText(dt)
            self.sr.first_ts = dt

    def clear_pre_e_sr(self):
        self.sr.pre_e_ns_r = ''
        self.le_pre_e_ns_r_sr.setText('')
        self.sr.pre_e_sn_r = ''
        self.le_pre_e_sn_r_sr.setText('')
        self.sr.pre_e_ew_r = ''
        self.le_pre_e_ew_r_sr.setText('')
        self.sr.pre_e_we_r = ''
        self.le_pre_e_we_r_sr.setText('')
        self.sr.pre_e_ns_v = ''
        self.le_pre_e_ns_v_sr.setText('')
        self.sr.pre_e_ew_v = ''
        self.le_pre_e_ew_v_sr.setText('')

    def update_pre_e_ns_r_sr(self):
        self.sr.pre_e_ns_r = self.le_pre_e_ns_r_sr.text()

    def update_pre_e_sn_r_sr(self):
        self.sr.pre_e_sn_r = self.le_pre_e_sn_r_sr.text()

    def update_pre_e_ew_r_sr(self):
        self.sr.pre_e_ew_r = self.le_pre_e_ew_r_sr.text()

    def update_pre_e_we_r_sr(self):
        self.sr.pre_e_we_r = self.le_pre_e_we_r_sr.text()

    def update_pre_e_ns_v_sr(self):
        self.sr.pre_e_ns_v = self.le_pre_e_ns_v_sr.text()

    def update_pre_e_ew_v_sr(self):
        self.sr.pre_e_ew_v = self.le_pre_e_ew_v_sr.text()

    def update_e_ns_r_sr(self):
        self.sr.e_ns_r = self.le_e_ns_r_sr.text()

    def update_e_sr_r_sr(self):
        self.sr.e_sn_r = self.le_e_sn_r_sr.text()

    def update_e_ew_r_sr(self):
        self.sr.e_ew_r = self.le_e_ew_r_sr.text()

    def update_e_we_r_sr(self):
        self.sr.e_we_r = self.le_e_we_r_sr.text()

    def update_e_ng_r_sr(self):
        self.sr.e_ng_r = self.le_e_ng_r_sr.text()

    def update_e_gn_r_sr(self):
        self.sr.e_gn_r = self.le_e_gn_r_sr.text()

    def update_ex_gps_sr(self):
        self.sr.ex_gps = self.le_ex_gps_sr.text()

    def update_ey_gps_sr(self):
        self.sr.ey_gps = self.le_ey_gps_sr.text()

    def update_e_ns_vdc_sr(self):
        self.sr.e_ns_vdc = self.le_e_ns_vdc_sr.text()

    def update_e_ew_vdc_sr(self):
        self.sr.e_ew_vdc = self.le_e_ew_vdc_sr.text()

    def update_e_ng_vdc_sr(self):
        self.sr.e_ng_vdc = self.le_e_ng_vdc_sr.text()

    def update_e_ns_vac_sr(self):
        self.sr.e_ns_vac = self.le_e_ns_vac_sr.text()

    def update_e_ew_vac_sr(self):
        self.sr.e_ew_vac = self.le_e_ew_vac_sr.text()

    def update_e_ng_vac_sr(self):
        self.sr.e_ng_vac = self.le_e_ng_vac_sr.text()

    def update_comments_sr(self):
        # get text and update metadata field
        comments = self.te_comments_sr.toPlainText()

        # set the comments on metadata
        self.set_comments_md(comments)

    def set_comments_sr(self, comments):
        # update comments in site report
        self.sr.comments = comments

        # disconnect the signals
        self.te_comments_sr.textChanged.disconnect()
        # update the comments
        self.te_comments_sr.setText(comments)
        # reconnect the signals
        self.te_comments_sr.textChanged.connect(self.update_comments_sr)

    def write_report(self):
        try:
            self.sr.write_file()
            self.set_check_sr(True)
        except (PermissionError, FileNotFoundError, TypeError) as error:
            self.set_check_sr(False)

    # -------------------------Engineering--------------------------------------

    def update_hex_data(self, packet):
        text = self.te_rawhex.toPlainText()
        # print(len(text))
        if len(text) >= 100:
            text = f'{text[-98:]} '
        self.te_rawhex.setText(f'{text}\t{packet}')

    def record_raw_data(self):
        """Record the port data since opening.

        The record_raw_data will record the data that has been read on the port
        since opening of the port.  Each toggle of the button writes a new file
        with the saved information.

        Args:

        Returns:

        """
        # get date and time
        dtetme = strftime("%Y%m%d_%H%M%S", gmtime())
        # set filename
        flenme = f'port_data_{dtetme}.txt'
        # the save location
        home = str(Path.home())
        flepth = os.path.join(
            home, f'Dropbox/Air2-Air3-DropBox/surveys/Earthscope/nimspy_logs/{flenme}')
        # write filename
        fleptr = open(flepth, 'wb')
        fleptr.write(self.portdata)
        fleptr.close()

    def update_filtered_data(self, packet):
        self.te_filteredhexdata.setText(packet)

    def update_bytes_read(self):
        self.te_bytesread.setText(str(len(self.packet)))

    def update_mag_status(self):
        value = self.packet[nims.STATUSSRT:nims.STATUSSTP].hex().upper()
        # update the mag status byte
        self.te_magstatus.setText(value)

    def update_variant(self):
        if self.packet[nims.LENGTHSRT:nims.LENGTHSTP] == bytes.fromhex(nims.LEN1HZ):
            self.label_variant.setText('1 Hz')
        else:
            self.label_variant.setText('8 Hz')

    def update_gps_value_e(self, value):
        # assign the value in the engineering panel
        self.te_gps_status_byte_e.setText(value)

    def clear_gps_string_e(self):
        self.te_gps_string_e.setText('')

    def update_gps_string_e(self):
        self.te_gps_string_e.setText(self.gpsstring)

    # -------------------------Processing---------------------------------------

    def parse_packet(self, data):
        self.set_receiving_led(True)
        self.receiving_led_timer.stop()
        self.receiving_led_timer.start(250)
        # save data to variable
        self.portdata += data
        # TODO: raw
        self.update_hex_data(data.hex().upper())
        # if len(self.packet) > 4:
        #     print(len(self.packet))
        #     print(2*(int(self.packet[2:4], 16)-1))
        # print(data)

        # print(self.packet)
        if len(self.packet) == 0 and data == bytes.fromhex(nims.SOH):
            try:
                self.packet = b''.join([self.packet, data])
            except TypeError:
                self.set_packets_led(False)
                pass
        elif len(self.packet) != 0:
            try:
                self.packet = b''.join([self.packet, data])
            except TypeError:
                pass
            # self.packet += data
            if (len(self.packet) == int(self.packet[1:2].hex(), 16)) and data == bytes.fromhex(nims.EOH):
                # change packets led to valid
                self.set_packets_led(True)
                # set the variant label
                # self.update_variant()
                # process the data packet
                self.process_packet()
            elif len(self.packet) > int(self.packet[1:2].hex(), 16):
                # change packets led to valid
                self.set_packets_led(False)
                self.packet = b''

        else:
            self.set_packets_led(False)
            # handle command
            pass

    def process_packet(self):
        # convert from bytes to upper case hex
        packet = self.packet.hex().upper()
        # reformat packet bytes
        packet = '\t'.join([packet[i:i + 2] for i in range(0, len(packet), 2)])

        # update data values
        self.update_data()

        # update gui
        # self.update_hex_data(packet)
        self.update_filtered_data(packet)
        self.update_graphs()
        self.update_sensor_values()
        self.update_bytes_read()
        self.update_h()
        self.update_e()
        self.update_gps()
        # clear packets
        self.packet = b''

    def update_data(self):
        hx = self.packet[nims.HXSTART:nims.HXSTOP]
        hy = self.packet[nims.HYSTART:nims.HYSTOP]
        hz = self.packet[nims.HZSTART:nims.HZSTOP]
        ex = self.packet[nims.EXSTART:nims.EXSTOP]
        ey = self.packet[nims.EYSTART:nims.EYSTOP]

        self.graphdata.update_hx(byte_to_int(hx) * nims.HCONVERSION)
        self.graphdata.update_hy(byte_to_int(hy) * nims.HCONVERSION)
        self.graphdata.update_hz(byte_to_int(hz) * nims.HCONVERSION)
        self.graphdata.update_ex(byte_to_int(ex) * nims.ECONVERSION)
        self.graphdata.update_ey(byte_to_int(ey) * nims.ECONVERSION)

    def update_gps(self):
        # get the binary value
        binvalue = self.packet[nims.GPSSRT:nims.GPSSTP]
        # get the gps value and cast as uppercase hex
        value = self.packet[nims.GPSSRT:nims.GPSSTP].hex().upper()
        # update the GPS value in metadata
        self.update_gps_value_m(value)
        # update the GPS value in engineering
        self.update_gps_value_e(value)
        # check the gps receive state
        if value == nims.GPSINITIAL and self.gpsstate == nims.INITIAL:
            # set the leds in 'metadata'
            self.set_short_cycle_led_metadata(value)
            self.set_almanac_led(False)
            # set the leds in 'Start/End Run'
            self.set_short_cycle_led_start_end(value)
        elif value == nims.GPSALMANAC:
            # set the gps state
            self.gpsstate = nims.GPSALMANAC
            # set the leds in 'metadata'
            self.set_short_cycle_led_metadata(value)
            self.set_almanac_led(True)
            # set the leds in 'Start/End Run'
            self.set_short_cycle_led_start_end(value)
        elif value == nims.GPSAQLOCK:
            # set the gps state
            self.gpsstate = nims.GPSAQLOCK
            # set the leds in 'metadata'
            self.set_short_cycle_led_metadata(value)
            self.set_almanac_led(False)
            # set the leds in 'Start/End Run'
            self.set_short_cycle_led_start_end(value)
        elif value == '24' and self.gpsstate == nims.GPSAQLOCK:
            # set the gps state
            self.gpsstate = nims.GPSRECEIVING
            # convert the first character from binary to unicode, add to gpsstring
            # self.gpsstring = binvalue.decode('utf-8')
            self.gpsstring = ''
            # update the gps boxes
            self.clear_gps_string_m()
            self.update_gps_string_e()
            self.clear_gps_string_e()
            self.update_gps_string_e()

        # enter while receiving gps sentences
        if self.gpsstate == nims.GPSRECEIVING:
            # read 139 bytes
            self.gpsstring += binvalue.decode('utf-8', 'ignore')

            # update the gps bytes
            self.update_gps_string_m()
            self.update_gps_string_e()

            # if read 139 bytes, exit
            if len(self.gpsstring) >= 139:
                # set the gps state
                self.gpsstate = nims.GPSRECEIVED
                # set the leds in 'metadata'
                self.set_short_cycle_led_metadata(nims.GPSRECEIVED)
                self.set_almanac_led(False)
                # set the leds in 'Start/End Run'
                self.set_short_cycle_led_start_end(nims.GPSRECEIVED)
                # parse the data
                self.parse_gps_packet()
            # # update gps string until get to a unicode error
            # try:
            #     # update gps string convert from binary to unicode value
            #     # TODO: add ignore here
            #     self.gpsstring += binvalue.decode('utf-8')
            #     print(self.gpsstring)
            #     # update status byte labels
            #     self.update_gps_string_m()
            #     self.update_gps_string_e()
            # except UnicodeDecodeError:
            #     # set the gps state
            #     self.gpsstate = nims.GPSRECEIVED
            #     # set the leds in 'metadata'
            #     self.set_short_cycle_led_metadata(nims.GPSRECEIVED)
            #     self.set_almanac_led(False)
            #     # set the leds in 'Start/End Run'
            #     self.set_short_cycle_led_start_end(nims.GPSRECEIVED)
            #     # parse the string into gps sentences
            #     gpssentences = self.gpsstring.split("\n")
            #     # split the sentences in lists
            #     gprmc = gpssentences[0].split(',')
            #     gpgga = gpssentences[1].split(',')
            #     # format the lists into readable gps string
            #     self.update_gps_metadata_string(gprmc, gpgga)
            #     # update gps fields on 'Metadata' tab
            #     self.update_gps_time()
            #     self.update_gps_date()
            #     self.update_gps_lat()
            #     self.update_gps_lon()
            #     self.update_gps_alt()
            #     self.clear_gps_string_e()
            #     self.clear_gps_string_m()

    def parse_gps_packet(self):
        print("Finished recieving GPS Data")
        print(self.gpsstring)
        # parse the string into gps sentences
        gpssentences = self.gpsstring.split('\r\n')

        # find the rmc and gga NMEA sentences
        for s in gpssentences:
            if search('RMC', s) is not None:
                gprmc = s.split(',')
            if search('GGA', s) is not None:
                gpgga = s.split(',')
        # format the lists into readable gps string
        self.update_gps_metadata_string(gprmc, gpgga)
        # update gps fields on 'Metadata' tab
        self.update_gps_time()
        self.update_gps_date()
        self.update_gps_lat()
        self.update_gps_lon()
        self.update_gps_alt()
        # clear the gps text boxes
        self.clear_gps_string_e()
        self.clear_gps_string_m()

    def update_e(self):
        # parse the gain byte
        gain = self.packet[nims.GAINSRT:nims.GAINSTP].hex().upper()
        # Update gain lights on Data display
        self.set_gain_leds(gain)
        # Update E gain spec leds on Start/End Run
        self.update_e_spec_leds()

    def update_h(self):
        # Update 'Data Display' components
        # Update 'Start/End Run' components
        self.update_ready_led()
        self.update_north_led()
        # Update 'Endineering' components
        self.update_mag_status()

    def send_byte(self, cmd):
        if self.port.is_open:
            self.port.write(cmd)


class PortRead(QThread):
    serdata = pyqtSignal(bytes)

    def __init__(self, qport=None):
        QThread.__init__(self)
        self.qport = qport

        self.running = False

        # TODO: for testing
        # -------------------
        # self.path = '../test/NEL26a_data.nim'
        # self.path = '../test/NEW_GPS_data.BIN'
        # self.flepnt = open(self.path, 'rb')
        # -------------------

    def __del__(self):
        self.wait()

    def stop(self):
        # TODO: for testing
        # -------------------
        # self.flepnt.close()
        # -------------------
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            data = b''
            # TODO: for testing
            # -------------------
            # sleep(0.25)
            # for i in range(0, 25):
            #     data = self.flepnt.read(1)
            #     if data is not b'':
            #         self.serdata.emit(data)
            # -------------------

            # read port
            if self.qport.is_open:
                try:
                    data = self.qport.read()
                except serial.SerialException:
                    data = b''

            # emit the data
            if data is not b'':
                self.serdata.emit(data)


class PortMonitor(QThread):
    pyports = pyqtSignal(list)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while(1):
            sleep(3)
            ports = list_ports()
            self.pyports.emit(ports)


class VerticalText(QWidget):

    def __init__(self, text='default'):
        QWidget.__init__(self)
        self.text = text
        self.rotateh = -90
        self.rotatee = 90

    def paintEvent(self, event):
        self.myFont = QFont()
        self.myFont.setPointSize(16)
        self.myFont.setBold(True)
        painter = QPainter(self)
        if self.text.startswith('E'):
            painter.translate(5, self.height() - 100)
            painter.rotate(self.rotatee)
            painter.setPen(Qt.blue)
        else:
            painter.translate(15, self.height() - 50)
            painter.rotate(self.rotateh)
            painter.setPen(Qt.red)
        painter.setFont(self.myFont)
        painter.drawText(0, 0, self.text)
        painter.end()


class Graph(QMainWindow):

    def __init__(self, parent=None):
        super(Graph, self).__init__(parent=parent)
        self.n_h = 0        # x value increments
        self.n_e = 0        # x value increments
        self.chart = QChart()
        self.chart.legend().hide()
        self.view = QChartView(self.chart)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(self.view)
        self.chart.layout().setContentsMargins(0, 0, 0, 0)

    def set_title(self, title):
        self.chart.setTitle(title)

    def add_data_e(self, xdata, ydata, ticks=20, color=Qt.blue, align=Qt.AlignRight):
        # define the x axis
        axisX = QValueAxis()
        axisX.setTickCount(ticks)
        self.chart.addAxis(axisX, Qt.AlignBottom)

        # define the y axis
        self.axisY_e = QValueAxis()
        if color is not None:
            self.axisY_e.setLinePenColor(color)
        self.chart.addAxis(self.axisY_e, align)
        # set the range of the Y axis
        self.axisY_h.setMax(max(ydata) + 1)
        self.axisY_h.setMin(min(ydata) - 1)

        # define the dataset
        self.series_e = QLineSeries()
        # create the graph color
        pen = self.series_e.pen()
        # set the color of the graph
        if color is not None:
            pen.setColor(color)
        self.series_e.setPen(pen)
        # get the data series_e
        for x, y in zip(xdata, ydata):
            self.n_e += 1
            self.series_e.append(x, y)
        # add the data to the chart
        self.chart.addSeries(self.series_e)

        # add the axis to the series
        self.series_e.attachAxis(self.axisY_e)
        # series.attachAxis(axisX)

    def add_data_h(self, xdata, ydata, ticks=20, color=Qt.red, align=Qt.AlignLeft):
        # define the x axis
        axisX = QValueAxis()
        axisX.setTickCount(ticks)
        self.chart.addAxis(axisX, Qt.AlignBottom)

        # define the y axis
        self.axisY_h = QValueAxis()
        if color is not None:
            self.axisY_h.setLinePenColor(color)
        self.chart.addAxis(self.axisY_h, align)
        # set the axis limits
        self.axisY_h.setMax(max(ydata) + 1)
        self.axisY_h.setMin(min(ydata) - 1)

        # define the dataset
        self.series_h = QLineSeries()
        # create the graph color
        pen = self.series_h.pen()
        # set the color of the graph
        if color is not None:
            pen.setColor(color)
        self.series_h.setPen(pen)
        # get the data series
        for x, y in zip(xdata, ydata):
            self.n_h += 1
            self.series_h.append(x, y)
        # add the data to the chart
        self.chart.addSeries(self.series_h)

        # add the axis to the series
        self.series_h.attachAxis(self.axisY_h)
        # series.attachAxis(axisX)

    def add_point_e(self, ydata):
        # remove the series so that is can be updated
        self.chart.removeSeries(self.series_e)
        # remove the first value, far left
        self.series_e.remove(0)
        self.n_e += 1
        # add value to end, far right
        self.series_e.append(self.n_e, ydata[-1])
        self.chart.addSeries(self.series_e)

        # set the axis limits
        self.axisY_e.setMax(max(ydata) + 1)
        self.axisY_e.setMin(min(ydata) - 1)

    def add_point_h(self, ydata):
        # remove the series so that is can be updated
        self.chart.removeSeries(self.series_h)
        # remove the first value, far left
        self.series_h.remove(0)
        self.n_h += 1
        # add value to end, far right
        self.series_h.append(self.n_h, ydata[-1])
        self.chart.addSeries(self.series_h)

        # set the axis limits
        self.axisY_h.setMax(max(ydata) + 1)
        self.axisY_h.setMin(min(ydata) - 1)


def byte_to_int(bytex: bytes) -> int:
    """Convert a byte4 into a signed int.

    The byte_to_int takes a byte (data type), length of 4 bytes, and converts,
    unpacks, it into a sighned integer.

    Args:
        bytex (bytes): A 4 byte(length) byte(type).

    Returns:
        value (int): Description of returned object.

    """
    stdlen = 4

    if len(bytex) < stdlen:
        bytex = to_byte4(bytex)

    value = struct.unpack('>i', bytex)[0]

    return value


def to_byte4(bytex: bytes) -> bytes:
    """Convert a n lenth byte string to a 4 byte string.

    The to_byte4 function takes an n byte (less than 4 bytes), two's
    compliment, string and returns a 4 byte, two's compliment, version
    of the same number.

    Args:
        bytex (bytes): N byte string, twos compliment.

    Returns:
        bytex (bytes): 4 byte string, twos compliment.

    """
    stdlen = 4          # Desired string length, in bytes.
    negB = b'\xff'      # Leading byte for negative number.
    posB = b'\x00'      # Leading byte for positive number.

    # check if leading bit is 1 or 0: b'1000 0000 = d'128
    if bytex[0] > 127:
        # add leading bytes until 4 bytes in length
        while(len(bytex) < stdlen):
            bytex = b''.join([negB, bytex])
    else:
        # add leading bytes until 4 bytes in length
        while(len(bytex) < stdlen):
            bytex = b''.join([posB, bytex])

    return bytex


class Data:
    """Short summary.

    Longsummary.

    Args:
        void (type): Description of parameter `void`.

    Returns:
        var (type): Description of returned object.

    """

    def __init__(self, ticks=60, xdata=[], hx=[], hy=[], hz=[], ex=[], ey=[]):
        """Short summary.

        Longsummary.

        Args:
            ticks (type): Description of parameter `ticks`. Defaults to 20.
            xdata (type): Description of parameter `xdata`. Defaults to [].
            hx (type): Description of parameter `hx`. Defaults to [].
            hy (type): Description of parameter `hy`. Defaults to [].
            hz (type): Description of parameter `hz`. Defaults to [].
            ex (type): Description of parameter `ex`. Defaults to [].
            ey (type): Description of parameter `ey`. Defaults to [].

        Returns:
            var (type): Description of returned object.

        """
        self.ticks = ticks
        self.xdata = [i for i in range(0, ticks)]
        self.hx = hx
        self.hy = hy
        self.hz = hz
        self.ex = ex
        self.ey = ey

    def update_hx(self, value):
        """Short summary.

        Longsummary.

        Args:
            value (type): Description of parameter `value`.

        Returns:
            var (type): Description of returned object.

        """
        if self.hx == []:
            for i in range(0, self.ticks):
                self.hx.append(value)

        self.hx = self.hx[1:]
        self.hx.append(value)

    def update_hy(self, value):
        """Short summary.

        Longsummary.

        Args:
            value (type): Description of parameter `value`.

        Returns:
            var (type): Description of returned object.

        """
        if self.hy == []:
            for i in range(0, self.ticks):
                self.hy.append(value)

        self.hy = self.hy[1:]
        self.hy.append(value)

    def update_hz(self, value):
        """Short summary.

        Longsummary.

        Args:
            value (type): Description of parameter `value`.

        Returns:
            var (type): Description of returned object.

        """
        if self.hz == []:
            for i in range(0, self.ticks):
                self.hz.append(value)

        self.hz = self.hz[1:]
        self.hz.append(value)

    def update_ex(self, value: str):
        """Short summary.

        Longsummary.

        Args:
            value (type): Description of parameter `value`.

        Returns:
            var (type): Description of returned object.

        """
        if self.ex == []:
            for i in range(0, self.ticks):
                self.ex.append(value)

        self.ex = self.ex[1:]
        self.ex.append(value)

    def update_ey(self, value: str):
        """Short summary.

        Longsummary.

        Args:
            value (type): Description of parameter `value`.

        Returns:
            var (type): Description of returned object.

        """
        if self.ey == []:
            for i in range(0, self.ticks):
                self.ey.append(value)

        self.ey = self.ey[1:]
        self.ey.append(value)


class SiteReport:

    def __init__(self):
        self.status = 'Install'
        self.settings = QSettings('NGF', 'nismpy')
        self.savepath = self.settings.value('savepath')
        if self.savepath is None:
            self.savepath = os.getcwd()
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.savename = "{}_.txt".format(self.date)
        self.sw = '{} v{}'.format(__program__, __version__)
        self.crew = ''
        self.siteid = ''
        self.sitename = ''
        self.sitestate = ''
        self.country = ''
        self.nimsid = ''
        self.magid = ''
        self.enid = ''
        self.esid = ''
        self.eeid = ''
        self.ewid = ''
        self.lat = ''
        self.lon = ''
        self.alt = ''
        self.dec = ''
        self.battery = ''
        self.gain = ''
        self.ex_gps = ''
        self.ey_gps = ''
        self.last_ts = ''
        self.first_ts = ''
        self.pre_e_ns_r = ''
        self.pre_e_sn_r = ''
        self.pre_e_ew_r = ''
        self.pre_e_we_r = ''
        self.pre_e_ns_v = ''
        self.pre_e_ew_v = ''
        self.e_ns_r = ''
        self.e_sn_r = ''
        self.e_ew_r = ''
        self.e_we_r = ''
        self.e_gn_r = ''
        self.e_ng_r = ''
        self.e_ns_vdc = ''
        self.e_ew_vdc = ''
        self.e_ng_vdc = ''
        self.e_ns_vac = ''
        self.e_ew_vac = ''
        self.e_ng_vac = ''
        self.comments = ''

    def update_savename(self, runid: str):
        self.siteid = runid
        self.savename = "{}_{}.txt".format(self.date, runid)
        # print(self.savename)

    def update_savepath(self, dir: str):
        self.settings.setValue('savepath', dir)
        self.savepath = self.settings.value('savepath')
        # print(self.savepath)

    def write_file(self):
        divider = '--------------------------------------------------------------------'

        fleptr = open(os.path.join(self.savepath, self.savename), 'w', encoding='utf-8')

        fleptr.write("Date: \t\t\t{}\n\n".format(self.date))
        fleptr.write("Software: \t\t{}\n\n".format(self.sw))
        fleptr.write("Crew: \t\t\t{}\n\n".format(self.crew))
        fleptr.write("Run ID: \t\t{}\n".format(self.siteid))
        fleptr.write("Site Name: \t\t{}, {}, {}\n\n".format(
            self.sitename, self.sitestate, self.country))
        fleptr.write("Status: \t\t{}\n".format(self.status))

        fleptr.write("{}\n".format(divider))
        fleptr.write("NIMS ID: \t\t{}\n".format(self.nimsid))
        fleptr.write("Mag ID: \t\t{}\n".format(self.magid))
        fleptr.write("Electrodes ID:\tN\t{}\n".format(self.enid))
        fleptr.write("\t\tS\t{}\n".format(self.esid))
        fleptr.write("\t\tE\t{}\n".format(self.eeid))
        fleptr.write("\t\tW\t{}\n".format(self.ewid))

        fleptr.write("{}\n".format(divider))
        fleptr.write("Electrode Parameters, prior to installation:\n\n")
        fleptr.write("Resistance (ohms):\n")
        fleptr.write("(S- to N+) = \t\t{}\n".format(self.pre_e_ns_r))
        fleptr.write("(N- to S+) = \t\t{}\n".format(self.pre_e_sn_r))
        fleptr.write("(W- to E+) = \t\t{}\n".format(self.pre_e_ew_r))
        fleptr.write("(E- to W+) = \t\t{}\n\n".format(self.pre_e_we_r))
        fleptr.write("Voltage (mV):\n")
        fleptr.write("(S- to N+) DVC = \t{}\n".format(self.pre_e_ns_v))
        fleptr.write("(W- to E+) DVC = \t{}\n".format(self.pre_e_ew_v))

        fleptr.write("{}\n".format(divider))
        fleptr.write("Electrode Parameters, at {}:\n\n".format(self.status))
        fleptr.write("Resistance (ohms):\n")
        fleptr.write("(S- to N+) = \t\t{}\n".format(self.e_ns_r))
        fleptr.write("(N- to S+) = \t\t{}\n".format(self.e_sn_r))
        fleptr.write("(W- to E+) = \t\t{}\n".format(self.e_ew_r))
        fleptr.write("(E- to W+) = \t\t{}\n".format(self.e_we_r))
        fleptr.write("(G- to N+) = \t\t{}\n".format(self.e_ng_r))
        fleptr.write("(N- to G+) = \t\t{}\n\n".format(self.e_gn_r))
        fleptr.write("Voltage (mV):\n")
        fleptr.write("(S- to N+) DVC = \t{}\n".format(self.e_ns_vdc))
        fleptr.write("(W- to E+) DVC = \t{}\n".format(self.e_ew_vdc))
        fleptr.write("(G- to N+) DVC = \t{}\n\n".format(self.e_ng_vdc))
        fleptr.write("(S- to N+) AVC = \t{}\n".format(self.e_ns_vac))
        fleptr.write("(W- to E+) AVC = \t{}\n".format(self.e_ew_vac))
        fleptr.write("(G- to N+) AVC = \t{}\n".format(self.e_ng_vac))

        fleptr.write("{}\n".format(divider))
        fleptr.write("Gain = \t\t\t{}\n".format(self.gain))
        fleptr.write("(Ex Gain- to GPS+) = \t{}\n".format(self.ex_gps))
        fleptr.write("(Ey Gain- to GPS+) = \t{}\n".format(self.ey_gps))

        fleptr.write("{}\n".format(divider))
        fleptr.write("Last time stamp for previous run = \t{}\n".format(self.last_ts))
        fleptr.write("First time stamp for run = \t\t{}\n\n".format(self.first_ts))
        fleptr.write("Lat = \t\t\t{}\n".format(self.lat))
        fleptr.write("Long = \t\t\t{}\n".format(self.lon))
        fleptr.write("Altitude = \t\t{}\n".format(self.alt))
        fleptr.write("Declination = \t\t{}\n".format(self.dec))

        fleptr.write("{}\n".format(divider))
        fleptr.write("Battery (V) = \t\t{}\n".format(self.battery))

        fleptr.write("{}\n".format(divider))
        fleptr.write("Comments:\n\n{}".format(self.comments))

        fleptr.close()


class Metadata:

    def __init__(self, sitename='NGFLAB', stateprov='Oregon', country='USA',
                 runid='lab001', operator='Nikola Tesla', nimsid='2612-01',
                 magid='2612-01', nsdipolelen=100, nsdipoleazi=0, ewdipolelen=100,
                 ewdipoleazi=90, ndipoleid='1', sdipoleid='2', edipoleid='3',
                 wdipoleid='4', gndelectrode='Cpr', surveylayout='X', gpstimestamp='',
                 comptimestamp='', comments='Default comments, needs updating.'):
        self.sitename = sitename
        self.stateprov = stateprov
        self.country = country
        self.runid = runid
        self.operator = operator
        self.nimsid = nimsid
        self.magid = magid
        self.nsdipolelen = nsdipolelen
        self.nsdipoleazi = nsdipoleazi
        self.ewdipolelen = ewdipolelen
        self.ewdipoleazi = ewdipoleazi
        self.surveylayout = surveylayout
        self.ndipoleid = ndipoleid
        self.sdipoleid = sdipoleid
        self.edipoleid = edipoleid
        self.wdipoleid = wdipoleid
        self.gndelectrode = gndelectrode
        self.gpstimestamp = gpstimestamp
        self.comptimestamp = comptimestamp
        self.comments = comments
        self.fileheader = ''

    def set_head_comp_time(self):
        # get the current computer time
        curtime = time.localtime()
        # parse the time zone of the computer time
        tzone = time.tzname[curtime[8]]
        # format the computer time of 'Start Run' clicked and time zone
        self.comptimestamp = time.strftime('%Y/%m/%d %H:%M:%S') + ' ' + tzone

    def make_header(self):
        """Short summary.

        Longsummary.

        Returns:
            var (type): Description of returned object.

        """
        headerlen = 1024
        header = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n'
        header += '>>>user field>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n'
        header += 'SITE NAME: %s\n' % (self.sitename)
        header += 'STATE/PROVINCE: %s\n' % (self.stateprov)
        header += 'COUNTRY: %s\n' % (self.country)
        header += '>>> The following code in double quotes is REQUIRED to start the NIMS <<\n'
        header += '>>> The next 3 lines contain values required for processing <<<<<<<<<<<<\n'
        header += '>>> The lines after that are optional <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'
        header += '\"%s\"\t<-- 2 CHAR EXPERIMENT CODE + 3 CHAR SITE CODE + RUN LETTER\n' \
            % (self.runid)
        header += '%s; %s\t<-- SYSTEM BOX I.D.; MAG HEAD ID (if different)\n' \
            % (self.nimsid, self.magid)
        header += '%i  %i\t<-- N-S Ex WIRE LENGTH (m); HEADING (deg E mag N)\n' \
            % (self.nsdipolelen, self.nsdipoleazi)
        header += '%i  %i\t<-- E-W Ex WIRE LENGTH (m); HEADING (deg E mag N)\n' \
            % (self.ewdipolelen, self.ewdipoleazi)
        header += '{}\t<-- Survey Layout\n'.format(self.surveylayout)
        header += '%s\t<-- N ELECTRODE ID\n' % (self.ndipoleid)
        header += '%s\t<-- E ELECTRODE ID\n' % (self.edipoleid)
        header += '%s\t<-- S ELECTRODE ID\n' % (self.sdipoleid)
        header += '%s\t<-- W ELECTRODE ID\n' % (self.wdipoleid)
        header += '%s\t<-- Ground ELECTRODE INFO\n' % (self.gndelectrode)
        header += 'GPS INFO: %s\n' % (self.gpstimestamp)
        header += 'COMPUTER TIME STAMP: %s\n' % (self.comptimestamp)
        header += 'OPERATOR: %s\n' % (self.operator)
        header += 'SOFTWARE: {} v{}\n'.format(__program__, __version__)
        header += 'COMMENTS: %s' % (self.comments)

        self.fileheader = header

        while(len(self.fileheader) < headerlen - 1):
            self.fileheader += ' '
        self.fileheader += '\n'

        print(f'{self.fileheader}')


def log_except_hook(*exc_info):
    global errflepth

    text = "".join(traceback.format_exception(*exc_info))
    logging.basicConfig(filename=errflepth, level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging.error("{} v{} Unhandled exception: \n{}".format(__program__, __version__, text))


def main(argv):
    # redirect the errors to write them to a file
    global errflepth
    home = str(Path.home())
    errflepth = os.path.join(
        home, 'Dropbox/Air2-Air3-DropBox/surveys/Earthscope/nimspy_logs/NIMSpy.log')
    sys.excepthook = log_except_hook
    # start the app
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())


# ***********************************************************************/
#                            __name__
# Needed to define main function in python program
# ***********************************************************************/
if __name__ == "__main__":
    main(sys.argv[1:])
