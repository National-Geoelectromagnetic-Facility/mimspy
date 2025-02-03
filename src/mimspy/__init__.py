"""Mimspy Main Application."""

import contextlib
import os
import struct
from pathlib import Path
from re import search
from time import gmtime, sleep, strftime

import serial
from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtGui import QAction, QCloseEvent, QKeyEvent, QPixmap
from PySide6.QtWidgets import QComboBox, QFileDialog, QMainWindow, QWidget

from . import nims
from .configs import APP_NAME, APP_VERSION
from .metadata import Metadata
from .port import PortMonitor, PortRead, SerialNode, list_ports
from .site_report import SiteReport
from .ui.main import Ui_MainWindow
from .widgets import GraphWidget, VerticalTextLabel


class Mimspy(QMainWindow, Ui_MainWindow):
    """The main application window."""

    TAB_START_END_RUN = 0
    TAB_DATA_DISPLAY = 1
    TAB_METADATA = 2
    TAB_SITE_REPORT = 3
    TAB_ENGINEERING = 4

    def __init__(self, icon_path: Path, parent: QWidget | None = None):
        super().__init__(parent=parent)
        self.setupUi(self)  # type: ignore  # noqa: PGH003

        self.port: serial.Serial = serial.Serial()
        self.receiving_led_timer = QTimer()
        self.read_port = PortRead(com_port=self.port)
        self.port_monitor = PortMonitor()
        self.metadata = Metadata()

        self.icon_path: Path = icon_path
        self.display_index: int = 0
        self.graph_hx_ey = GraphWidget()
        self.graph_hy_ex = GraphWidget()
        self.graph_hz = GraphWidget()
        self.graph_data = GraphData(ticks=20)

        self.packet: bytes = b""
        self.gps_state: str = nims.GPSINITIAL
        self.gps_string: str = ""

        self.port_data: bytes = b""

        # round leds
        self.led_black_round = QPixmap(Path(icon_path, "black_led_61_61.png"))
        self.led_green_round = QPixmap(Path(icon_path, "green_led_61_61.png"))
        self.led_yellow_round = QPixmap(Path(icon_path, "yellow_led_61_61.png"))
        self.led_red_round = QPixmap(Path(icon_path, "red_led_61_61.png"))
        # oval leds
        self.led_black_oval = QPixmap(Path(icon_path, "black_oval_58_29.png"))
        self.led_green_oval = QPixmap(Path(icon_path, "green_oval_58_29.png"))
        self.led_yellow_oval = QPixmap(Path(icon_path, "yellow_oval_58_29.png"))
        self.led_red_oval = QPixmap(Path(icon_path, "red_oval_58_29.png"))

        self.sr = SiteReport()
        self.init_ui(icon_path)

    def init_ui(self, icon_path: Path):
        """Initialize the UI."""
        # set the window name
        self.setWindowTitle(APP_NAME + " v" + APP_VERSION)
        self.setMinimumSize(QSize(950, 630))
        self.setMaximumSize(QSize(950, 630))
        self.init_menu_bar_keyboard_shortcuts()
        self.init_serial_connection(icon_path)
        self.init_start_end_run()
        self.init_metadata()
        self.init_data_display()
        self.init_site_report()
        self.init_engineering()

    def init_menu_bar_keyboard_shortcuts(self):
        """Initialize the menu bar and keyboard shortcuts."""
        # move backward tab
        back_tab = QAction("&Move Back Tab", self)
        back_tab.setShortcut(
            Qt.Modifier.CTRL | Qt.Modifier.SHIFT | Qt.Key_BraceLeft  # type: ignore[attr-defined]
        )
        back_tab.setStatusTip("Move back 1 tab")
        back_tab.triggered.connect(lambda: self.display("b"))
        # move forward tab
        forward_tab = QAction("&Move Forward Tab", self)
        forward_tab.setShortcut(
            Qt.Modifier.CTRL | Qt.Modifier.SHIFT | Qt.Key_BraceRight  # type: ignore[attr-defined]
        )
        forward_tab.setStatusTip("Move forward 1 tab")
        forward_tab.triggered.connect(lambda: self.display("f"))

        # populating the menu bar
        main_menu = self.menuBar()

        view_menu = main_menu.addMenu("&View")
        view_menu.addAction(back_tab)
        view_menu.addAction(forward_tab)

        # -------------------------Tab Control----------------------------------
        self.display_index = self.TAB_START_END_RUN

        # controls which "tab" is displayed
        self.tb_metadata.clicked.connect(lambda: self.display(self.TAB_METADATA))
        self.tb_datadisplay.clicked.connect(lambda: self.display(self.TAB_DATA_DISPLAY))
        self.tb_startend.clicked.connect(lambda: self.display(self.TAB_START_END_RUN))
        self.tb_sitereport.clicked.connect(lambda: self.display(self.TAB_SITE_REPORT))
        self.tb_engineer.clicked.connect(lambda: self.display(self.TAB_ENGINEERING))

    def init_serial_connection(self, icon_path: Path):
        """Initialize the serial connection."""
        # set the ngf logo
        pixmap = QPixmap(Path(icon_path, "NGF_logo_75_75.png"))
        self.label_icon.setPixmap(pixmap)

        # initialize the connection/packets/receive leds
        self.label_connection_led.setPixmap(self.led_black_oval)
        self.label_packets_led.setPixmap(self.led_black_oval)
        self.label_receiving_led.setPixmap(self.led_black_oval)

        # initialize and start the serial drop down list of the available ports
        self.port_monitor.pyports.connect(self.change_ports_list)
        self.port_monitor.start()

        # initialize the port read thread
        self.read_port.SERIAL_DATA.connect(self.parse_packet)

        # set up current port speed
        self.change_baud_rate_list()
        self.cb_speed.currentIndexChanged.connect(self.connection_change)  # type: ignore  # noqa: PGH003

        # initialize the port drop down list
        self.cb_connection.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        self.cb_connection.currentIndexChanged.connect(self.connection_change)  # type: ignore  # noqa: PGH003

        # initialize/open the port on startup
        self.change_ports_list(list_ports())

        # start the read port thread
        self.read_port.start()

        # set the receiving led timer
        self.receiving_led_timer.timeout.connect(lambda: self.set_receiving_led(False))

        # -------------------------MetaData Tab---------------------------------

    def init_metadata(self):
        """Initialize the metadata tab."""
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
        # self.rb_x_layout.layout = "X"
        # self.rb_x_layout.toggled.connect(self.update_survey_layout)
        # self.rb_l_layout.layout = "L"
        # self.rb_l_layout.toggled.connect(self.update_survey_layout)
        # self.rb_t_layout.layout = "T"
        # self.rb_t_layout.toggled.connect(self.update_survey_layout)
        self.te_comments.textChanged.connect(self.update_comments_md)

        pixmap_north = QPixmap(Path(self.icon_path, "north_icon_46_101.png"))
        self.label_north.setPixmap(pixmap_north)

        # initialize the gps short cycle button/led
        self.set_short_cycle_led_metadata(nims.GPSINITIAL)
        self.set_almanac_led(False)

        # initialize the gps almanac button/led
        self.tb_shortcycle.clicked.connect(self.send_short_cycle)
        self.tb_almanac.clicked.connect(self.send_almanac)

    def init_start_end_run(self):
        """Initialize the start/end run tab."""
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

    def init_data_display(self):
        """Initialize the data display tab."""
        # Gain LEDs initialization.
        self.set_gain_leds(nims.EXUEYU)

        # Connect the gain buttons
        self.tb_gain_xlyl.clicked.connect(self.send_gain_x_low_y_low)
        self.tb_gain_xhyl.clicked.connect(self.send_gain_x_high_y_low)
        self.tb_gain_xlyh.clicked.connect(self.send_gain_x_low_y_high)
        self.tb_gain_xhyh.clicked.connect(self.send_gain_x_high_y_high)

        # Connection the misc buttons
        self.tb_mag_light.toggled.connect(self.send_mag_light)
        self.tb_nims_leds.clicked.connect(self.send_nims_leds)

        # Draw the vertical graph labels
        label_ey = VerticalTextLabel(text="Ey (mV)")
        label_ex = VerticalTextLabel(text="Ex (mV)")
        label_hx = VerticalTextLabel(text="Hx (nT)")
        label_hy = VerticalTextLabel(text="Hy (nT)")
        label_hz = VerticalTextLabel(text="Hz (nT)")

        # Add the text to the layouts
        self.horlayout_ex_label.addWidget(label_ex)
        self.horlayout_ey_label.addWidget(label_ey)
        self.horlayout_hx_label.addWidget(label_hx)
        self.horlayout_hy_label.addWidget(label_hy)
        self.horlayout_hz_label.addWidget(label_hz)

        # Data initialization
        self.graph_data.update_hx(0.0)
        self.graph_data.update_hy(0.0)
        self.graph_data.update_hz(0.0)
        self.graph_data.update_ex(0.0)
        self.graph_data.update_ey(0.0)
        # Graph initialization
        self.layout_hx_ey.addWidget(self.graph_hx_ey)
        self.layout_hy_ex.addWidget(self.graph_hy_ex)
        self.layout_hz.addWidget(self.graph_hz)
        # Add data to the graphs
        self.graph_hx_ey.add_data_h(
            self.graph_data.xdata,
            self.graph_data.hx,
            color=Qt.GlobalColor.red,
            align=Qt.AlignmentFlag.AlignLeft,
        )
        self.graph_hx_ey.add_data_e(
            self.graph_data.xdata,
            self.graph_data.ey,
            color=Qt.GlobalColor.blue,
            align=Qt.AlignmentFlag.AlignRight,
        )
        self.graph_hy_ex.add_data_h(
            self.graph_data.xdata,
            self.graph_data.hy,
            color=Qt.GlobalColor.red,
            align=Qt.AlignmentFlag.AlignLeft,
        )
        self.graph_hy_ex.add_data_e(
            self.graph_data.xdata,
            self.graph_data.ex,
            color=Qt.GlobalColor.blue,
            align=Qt.AlignmentFlag.AlignRight,
        )
        self.graph_hz.add_data_h(
            self.graph_data.xdata,
            self.graph_data.hz,
            color=Qt.GlobalColor.red,
            align=Qt.AlignmentFlag.AlignLeft,
        )

    def init_site_report(self):
        """Initialize the site report tab."""
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
        self.le_change_directory_sr.setText(str(self.sr.save_path))

        # update comments
        self.te_comments_sr.textChanged.connect(self.update_comments_sr)

        # update the save directory
        self.tb_change_directory_sr.clicked.connect(self.path_on_click)

        # set the check mark
        self.set_check_sr(False)
        # write to file
        self.tb_generate_report_sr.clicked.connect(self.write_report)

    def init_engineering(self):
        """Initialize the engineering tab."""
        self.tb_record_raw.clicked.connect(self.record_raw_data)

    # -------------------------General------------------------------------------
    def closeEvent(self, event: QCloseEvent):
        """Handle the close event."""
        # self.close()
        self.port_monitor.stop()
        self.read_port.stop()
        if not self.port:
            self.port.close()
        super().closeEvent(event)

    def keyPressEvent(self, e: QKeyEvent):
        """Handle Key Press Event."""
        if e.key() == Qt.Key.Key_Escape or e.key() == Qt.Key.Key_Close:
            self.close()

    def display(self, i: int | str):
        """Change the display tab."""
        if i == self.TAB_METADATA:
            self.stackedWidget.setCurrentIndex(self.TAB_METADATA)
            self.display_index = self.TAB_METADATA
            self.tb_metadata.setChecked(True)
        elif i == self.TAB_DATA_DISPLAY:
            self.stackedWidget.setCurrentIndex(self.TAB_DATA_DISPLAY)
            self.display_index = self.TAB_DATA_DISPLAY
            self.tb_datadisplay.setChecked(True)
        elif i == self.TAB_START_END_RUN:
            self.stackedWidget.setCurrentIndex(self.TAB_START_END_RUN)
            self.display_index = self.TAB_START_END_RUN
            self.tb_startend.setChecked(True)
        elif i == self.TAB_SITE_REPORT:
            self.stackedWidget.setCurrentIndex(self.TAB_SITE_REPORT)
            self.display_index = self.TAB_SITE_REPORT
            self.tb_sitereport.setChecked(True)
        elif i == self.TAB_ENGINEERING:
            self.stackedWidget.setCurrentIndex(self.TAB_ENGINEERING)
            self.display_index = self.TAB_ENGINEERING
            self.tb_engineer.setChecked(True)
        elif i == "b":
            if self.display_index == self.TAB_START_END_RUN:
                self.display_index = self.TAB_ENGINEERING
            else:
                self.display_index -= 1
            self.display(self.display_index)
        elif i == "f":
            if self.display_index == self.TAB_ENGINEERING:
                self.display_index = self.TAB_START_END_RUN
            else:
                self.display_index += 1
            self.display(self.display_index)

    # -------------------------Connection---------------------------------------
    def connection_change(self, _):
        """Handle a port change selection."""
        # close the thread
        self.read_port.stop()
        # wait for thread to close
        while self.read_port.isRunning():
            continue
        # if port open, close it
        if self.port.port is not None:
            self.port.close()
        # assign new port
        self.port.port = self.cb_connection.currentText()
        self.port.baudrate = int(self.cb_speed.currentText())
        self.port.timeout = 0.5
        self.port.stopbits = 2
        print(f"{self.port}")
        # open the port
        if not self.port.is_open:
            # Handle when can't open port
            try:
                self.port.open()
            except (OSError, serial.SerialException):
                print(f"Failed to open port: {self.port.port}")

        if self.port.is_open:
            # set the connection led to green
            self.set_connection_led(True)
            # set the packets led to red
            self.set_packets_led(False)
            # clear packet
            self.packet = b""
            # start the read port again
            self.read_port.start()
        else:
            self.set_connection_led(False)
            self.set_packets_led(False)

        self.set_receiving_led(False)

        print(f"Port Open: \t{self.port.is_open}")

    def set_connection_led(self, state: bool):
        """Set the connection led."""
        if state is True:
            self.label_connection_led.setPixmap(self.led_green_oval)
        else:
            self.label_connection_led.setPixmap(self.led_red_oval)

    def set_packets_led(self, state: bool):
        """Set the packets led."""
        if state is True:
            self.label_packets_led.setPixmap(self.led_green_oval)
        else:
            self.label_packets_led.setPixmap(self.led_red_oval)

    def set_receiving_led(self, state: bool):
        """Set the receiving led."""
        if state is True:
            self.label_receiving_led.setPixmap(self.led_green_oval)
        else:
            self.label_receiving_led.setPixmap(self.led_black_oval)

    def change_ports_list(self, ports: list[SerialNode]):
        """Change the ports list."""
        serial_items = [self.cb_connection.itemText(i) for i in range(self.cb_connection.count())]

        # insert new ports into the list
        for p in ports:
            # check for port already in list
            if p.port not in serial_items:
                self.cb_connection.addItem(p.port)

    def change_baud_rate_list(self):
        """List of available baud rates."""
        speeds = ["19200"]
        for s in speeds:
            self.cb_speed.addItem(s)

    # -------------------------MetaData-----------------------------------------
    def get_file_name(self) -> str:
        """Get the file name."""
        default = "data.bin"

        fn = self.le_filename.text()

        if fn == "":
            fn = default

        return fn

    def update_site_name_md(self):
        """Update the site name in metadata."""
        # get text and update metadata field
        site_name = self.le_site_name.text()

        self.update_site_name(site_name)

    def update_site_name(self, sn: str):
        """Update the site name."""
        # get text and update metadata field
        self.metadata.site_name = sn
        # update metadata led
        self.check_metadata()

        # update site report site name
        self.sr.site_name = sn

        # update the site id
        self.le_site_name.setText(sn)
        self.le_site_name_sr.setText(sn)

    def update_state_province_md(self):
        """Update the state/province in metadata."""
        # get text
        sp = self.le_state_province.text()

        self.update_state_province(sp)

    def update_state_province(self, sp: str):
        """Update the state/province."""
        # get text and update metadata field
        self.metadata.state_province = sp
        # update metadata led
        self.check_metadata()

        # update site report site state
        self.sr.site_state = sp

        self.le_state_province.setText(sp)
        self.le_state_province_sr.setText(sp)

    def update_country_md(self):
        """Update the country in metadata."""
        # get text
        cntry = self.le_country.text()

        self.update_country(cntry)

    def update_country(self, cntry: str):
        """Update the country."""
        # get text and update metadata field
        self.metadata.country = cntry
        # update metadata led
        self.check_metadata()

        # update site report country
        self.sr.country = cntry

        self.le_country.setText(cntry)
        self.le_country_sr.setText(cntry)

    def update_run_id_md(self):
        """Update the run id in metadata."""
        # get text and update metadata field
        # self.metadata.run_id = self.le_run_id.text()
        txt = self.le_run_id.text()
        # update metadata led
        # self.check_metadata()
        self.update_run_id(txt)

        # update the run id on site report
        # self.le_run_id_sr.setText(self.metadata.run_id)

    def update_run_id(self, txt: str):
        """Update the run id."""
        # get text and update metadata field
        self.metadata.run_id = txt
        # update metadata
        self.check_metadata()

        # update the run id
        self.le_run_id_sr.setText(txt)
        self.le_run_id.setText(txt)

        self.sr.update_save_name(txt)
        self.update_save_directory_sr()

    def update_operator(self):
        """Update the operator in metadata."""
        # get text and update metadata field
        self.metadata.operator = self.le_operator.text()
        # update metadata led
        self.check_metadata()

    def update_nims_id_md(self):
        """Update the nims id in metadata."""
        # get text and update metadata field
        nid = self.le_nims_id.text()

        self.update_nims_id(nid)

    def update_nims_id(self, nid: str):
        """Update the nims id."""
        # get text and update metadata field
        self.metadata.nims_id = nid
        # update metadata led
        self.check_metadata()

        # update the site report
        self.sr.nims_id = nid

        # update the nims id
        self.le_nims_id.setText(nid)
        self.le_nims_id_sr.setText(nid)

    def update_mag_id_md(self):
        """Update the mag id in metadata."""
        # get text and update metadata field
        mid = self.le_mag_id.text()

        self.update_mag_id(mid)

    def update_mag_id(self, mid: str):
        """Update the mag id."""
        # get text and update metadata field
        self.metadata.mag_id = mid
        # update metadata led
        self.check_metadata()

        # update the site report
        self.sr.mag_id = mid

        # update the mag id
        self.le_mag_id.setText(mid)
        self.le_mag_id_sr.setText(mid)

    def update_ns_length(self):
        """Update the north-south dipole length in metadata."""
        # get text and update metadata field
        try:
            self.metadata.ns_length = int(self.le_ns_dipole_length.text())
        except ValueError:
            self.le_ns_dipole_length.setText("")
        # update metadata led
        self.check_metadata()

    def update_ns_azimuth(self):
        """Update the north-south dipole azimuth in metadata."""
        # get text and update metadata field
        try:
            self.metadata.ns_azimuth = int(self.le_ns_dipole_heading.text())
        except ValueError:
            self.le_ns_dipole_heading.setText("")
        # update metadata led
        self.check_metadata()

    def update_ew_length(self):
        """Update the east-west dipole length in metadata."""
        # get text and update metadata field
        try:
            self.metadata.ew_length = int(self.le_ew_dipole_length.text())
        except ValueError:
            self.le_ew_dipole_length.setText("")
        # update metadata led
        self.check_metadata()

    def update_ew_azimuth(self):
        """Update the east-west dipole azimuth in metadata."""
        # get text and update metadata field
        try:
            self.metadata.ew_azimuth = int(self.le_ew_dipole_heading.text())
        except ValueError:
            self.le_ew_dipole_heading.setText("")
        # update metadata led
        self.check_metadata()

    def update_n_id_md(self):
        """Update the north electrode id in metadata."""
        eid = self.le_n_electrode_id.text()

        self.update_n_id(eid)

    def update_n_id(self, eid: str):
        """Update the north electrode id."""
        self.metadata.electrode_north_id = eid
        # update metadata led
        self.check_metadata()

        # update the site report
        self.sr.electrode_north_id = eid

        # update the electrode id
        self.le_n_electrode_id.setText(eid)
        self.le_n_electrode_id_sr.setText(eid)

    def update_s_id_md(self):
        """Update the south electrode id in metadata."""
        eid = self.le_s_electrode_id.text()

        self.update_s_id(eid)

    def update_s_id(self, eid: str):
        """Update the south electrode id."""
        self.metadata.electrode_south_id = eid
        # update metadata led
        self.check_metadata()

        # update the site report
        self.sr.electrode_south_id = eid

        # update the electrode id
        self.le_s_electrode_id.setText(eid)
        self.le_s_electrode_id_sr.setText(eid)

    def update_e_id_md(self):
        """Update the east electrode id in metadata."""
        eid = self.le_e_electrode_id.text()

        self.update_e_id(eid)

    def update_e_id(self, eid: str):
        """Update the east electrode id."""
        self.metadata.electrode_east_id = eid
        # update metadata led
        self.check_metadata()

        # update the site report
        self.sr.electrode_east_id = eid

        # update the electrode id
        self.le_e_electrode_id.setText(eid)
        self.le_e_electrode_id_sr.setText(eid)

    def update_w_id_md(self):
        """Update the east electrode id."""
        eid = self.le_w_electrode_id.text()

        self.update_w_id(eid)

    def update_w_id(self, eid: str):
        """Update the west electrode id."""
        self.metadata.electrode_west_id = eid
        # update metadata led
        self.check_metadata()

        # update the site report
        self.sr.electrode_west_id = eid

        # update the electrode id
        self.le_w_electrode_id.setText(eid)
        self.le_w_electrode_id_sr.setText(eid)

    def update_gnd_id(self):
        """Update the west electrode id."""
        # get text and update metadata field
        self.metadata.ground = self.le_gnd_electrode_id.text()
        # update metadata led
        self.check_metadata()

    # def update_survey_layout(self):
    #     """Update the survey layout."""
    #     sender = self.sender()
    #     if sender.isChecked():
    #         # get checked value
    #         self.metadata.survey_layout = sender.layout
    #         # update metadata led
    #         self.check_metadata()

    def update_comments_md(self):
        """Update the Comments in metadata."""
        # get text and update metadata field
        comments = self.te_comments.toPlainText()

        # check the comments length
        self.check_comments_length(comments)

        # set comments
        self.set_comments_sr(comments)

    def set_comments_md(self, comments: str):
        """Set the comments in metadata."""
        # check the comments length
        self.check_comments_length(comments)

        # disconnect the signals
        self.te_comments.textChanged.disconnect()
        # update the comments
        self.te_comments.setText(comments)
        # reconnect the signals
        self.te_comments.textChanged.connect(self.update_comments_md)

    def check_comments_length(self, comments: str):
        """Check for the length of the comment section for overrun.

        Parameters
        ----------
        comments : str
            The present comments in the md section.
        """
        max_comment_length = 150

        if len(comments) >= max_comment_length:
            # get text and update metadata field
            self.metadata.comments = comments[0 : max_comment_length - 1]
            self.set_comments_label(True)
        else:
            # get text and update metadata field
            self.metadata.comments = comments
            self.set_comments_label(False)

        # update metadata led
        self.check_metadata()

    def set_comments_label(self, flag: bool):
        """Set the comment label.

        The set_comments_label function sets the comments label on the MetaData
        tab, depending on the length of the metadata comments.

        Args:
            flag (bool): True, comment overrun, False, < 150 chars
        -------

        """
        label = "Field Crew Comments"
        warning = "TOO MANY CHARACTERS!"

        if flag:
            self.l_comments_md.setText(warning)
            self.l_comments_md.setStyleSheet("color: red")
        else:
            self.l_comments_md.setText(label)
            self.l_comments_md.setStyleSheet("color: black")

    def set_short_cycle_led_metadata(self, code: str):
        """Set the short cycle led in metadata tab."""
        match code:
            case nims.GPSAQLOCK | nims.GPSRECEIVING:
                pix_icon = self.led_yellow_round
            case nims.GPSRECEIVED:
                pix_icon = self.led_green_round
            case _:
                pix_icon = self.led_black_round
        self.label_short_cycle_led.setPixmap(pix_icon)

    def update_gps_value_m(self, value: str):
        """Update the GPS value in the metadata panel."""
        # assign the value in the metadata panel
        self.le_gps_status_byte_m.setText(value)

    def set_almanac_led(self, state: bool):
        """Set the almanac led in metadata tab."""
        self.label_almanac_led.setPixmap(self.led_green_round if state else self.led_black_round)

    def clear_gps_string_m(self):
        """Clear the GPS string in the metadata panel."""
        self.te_gps_string_m.setText("")

    def update_gps_string_m(self):
        """Update the GPS string in the metadata panel."""
        self.te_gps_string_m.setText(self.gps_string)

    def update_gps_metadata_string(self, gprmc: list[str], gpgga: list[str]):
        """Update the GPS metadata string."""
        # parse the needed data from the sentences
        date = gprmc[nims.GPSDATE]
        time = gpgga[nims.GPSTIME].split(".")[0]
        declination = gprmc[nims.GPSDECL]
        declination_direction = gprmc[nims.GPSDECD]

        if declination != "" and declination_direction != "":
            self.update_gps_dec(declination, declination_direction)

        lat = "%s %s" % (self.dm_to_dd(gpgga[nims.GPSLATI]), gpgga[nims.GPSLATD])
        lon = "%s %s" % (self.dm_to_dd(gpgga[nims.GPSLONG]), gpgga[nims.GPSLOND])
        alt = gpgga[nims.GPSALTI]

        # format the data and time
        date = "/".join([date[i : i + 2] for i in range(0, len(date), 2)])
        time = ":".join([time[i : i + 2] for i in range(0, len(time), 2)])

        # update the metadata string
        self.metadata.gps_timestamp = "%s %s %s %s %s" % (date, time, lat, lon, alt)

        # update GUI GPS string
        self.te_gps_metadata_string.setText(self.metadata.gps_timestamp)

        # update site report timestamp
        self.update_timestamp_sr(date, time)

    @staticmethod
    def dm_to_dd(ll_dms: str) -> str:
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
            GPS lat/long in "D{D:}.dddddd"

        """
        try:
            i = ll_dms.index(".")
            degree = int(ll_dms[: i - 2])
            minute = float(ll_dms[i - 2 :]) / 60
        except (IndexError, ValueError):
            degree = 0
            minute = 0

        return "{:.6f}".format(degree + minute)

    def update_gps_time(self):
        """Update the GPS time in metadata."""
        # parse the string into a list
        gps_list = self.metadata.gps_timestamp.split(" ")

        # extract the time, check for array error
        try:
            time = gps_list[nims.GPSSTRINGTIME]
        except IndexError:
            time = "00:00:00"

        # update the gps field
        self.le_gps_time.setText(time)

    def update_gps_date(self):
        """Update the GPS date in metadata."""
        # parse the string into a list
        gps_list = self.metadata.gps_timestamp.split(" ")

        # extract the date, check for array error
        try:
            date = gps_list[nims.GPSSTRINGDATE]
        except IndexError:
            date: str = "00/00/00"

        # update the gps field
        self.le_gps_date.setText(date)

    def update_gps_lat(self):
        """Update the GPS latitude in metadata."""
        # parse the string into a list
        gps_list = self.metadata.gps_timestamp.split(" ")

        # extract the lat, check for array error
        try:
            lat = f"{gps_list[nims.GPSSTRINGALTI]} {gps_list[nims.GPSSTRINGLATD]}"
        except IndexError:
            lat = "0.0"

        # update the gps field
        self.le_gps_lat.setText(lat)
        # update the site report tab
        self.le_gps_lat_sr.setText(lat)
        # update the site report
        self.sr.lat = lat

    def update_gps_lon(self):
        """Update the GPS longitude in metadata."""
        # parse the string into a list
        gps_list = self.metadata.gps_timestamp.split(" ")

        # extract the longitude, check for array error
        try:
            lon = f"{gps_list[nims.GPSSTRINGLONG]} {gps_list[nims.GPSSTRINGLOND]}"
        except IndexError:
            lon = "0.0"

        # update the gps field
        self.le_gps_lon.setText(lon)
        # update the site report tab
        self.le_gps_lon_sr.setText(lon)
        # update the site report
        self.sr.lon = lon

    def update_gps_alt(self):
        """Update the GPS longitude in metadata."""
        # initialize empty altitude
        # parse the string into a list
        gps_list = self.metadata.gps_timestamp.split(" ")

        # extract the alt, check for array error
        try:
            alt = gps_list[nims.GPSSTRINGALTI]
        except IndexError:
            alt = "0.0"

        # update the gps field
        self.le_gps_alt.setText(alt)
        self.le_gps_alt_sr.setText(alt)
        # update the site report
        self.sr.alt = alt

    def send_short_cycle(self):
        """Send the short cycle command."""
        print(f"Send Command: \t{bytes.fromhex(nims.SHORTCYCLE)}")
        self.send_byte(bytes.fromhex(nims.SHORTCYCLE))

    def send_almanac(self):
        """Send the almanac command."""
        print(f"Send Command: \t{bytes.fromhex(nims.ALMANAC)}")
        self.send_byte(bytes.fromhex(nims.ALMANAC))

    # -------------------------Data Display-------------------------------------
    def set_gain_leds(self, code: str):
        """Set the gain LEDs."""
        # set all leds to black
        self.label_gain_xlyl_led.setPixmap(self.led_black_oval)
        self.label_gain_xhyl_led.setPixmap(self.led_black_oval)
        self.label_gain_xlyh_led.setPixmap(self.led_black_oval)
        self.label_gain_xhyh_led.setPixmap(self.led_black_oval)

        # Only turn the correct LED green
        match code:
            case nims.EXLEYL:
                self.label_gain_xlyl_led.setPixmap(self.led_green_oval)
            case nims.EXHEYL:
                self.label_gain_xhyl_led.setPixmap(self.led_green_oval)
            case nims.EXLEYH:
                self.label_gain_xlyh_led.setPixmap(self.led_green_oval)
            case nims.EXHEYH:
                self.label_gain_xhyh_led.setPixmap(self.led_green_oval)
            case _:
                pass

    def send_gain_x_low_y_low(self):
        """Send the gain command."""
        print(f"Send Command: \t{bytes.fromhex(nims.GAINXLYL)}")
        self.send_byte(bytes.fromhex(nims.GAINXLYL))

    def send_gain_x_high_y_low(self):
        """Send the gain command."""
        # send low gain command first
        self.send_gain_x_low_y_low()
        # wait for gain to change
        sleep(0.15)
        # send gain command
        print(f"Send Command: \t{bytes.fromhex(nims.GAINXHYL)}")
        self.send_byte(bytes.fromhex(nims.GAINXHYL))

    def send_gain_x_low_y_high(self):
        """Send the gain command."""
        # send low gain command first
        self.send_gain_x_low_y_low()
        # wait for gain to change
        sleep(0.15)
        # send gain command
        print(f"Send Command: \t{bytes.fromhex(nims.GAINXLYH)}")
        self.send_byte(bytes.fromhex(nims.GAINXLYH))

    def send_gain_x_high_y_high(self):
        """Send the gain command."""
        # send low gain command first
        self.send_gain_x_low_y_low()
        # wait for gain to change
        sleep(0.15)
        # send gain command
        print(f"Send Command: \t{bytes.fromhex(nims.GAINXHYH)}")
        self.send_byte(bytes.fromhex(nims.GAINXHYH))

    def send_mag_light(self, checked: bool):
        """Turn on the mag light."""
        if checked:
            print(f"Toggle Mag Light: \t{False}")
            self.port.setRTS(False)  # type: ignore  # noqa: PGH003
        else:
            print(f"Toggle Mag Light: \t{True}")
            self.port.setRTS(True)  # type: ignore  # noqa: PGH003

    def send_nims_leds(self):
        """Pulse the Minerva LEDs."""
        # send the nims command
        print(f"Send Command: \t{bytes.fromhex(nims.NIMSLEDS)}")
        self.send_byte(bytes.fromhex(nims.NIMSLEDS))

    def update_graphs(self):
        """Update the graphs."""
        # update graphs
        self.graph_hx_ey.add_point_h(self.graph_data.hx)
        self.graph_hx_ey.add_point_e(self.graph_data.ey)
        self.graph_hy_ex.add_point_h(self.graph_data.hy)
        self.graph_hy_ex.add_point_e(self.graph_data.ex)
        self.graph_hz.add_point_h(self.graph_data.hz)

    def update_sensor_values(self):
        """Update the sensor values."""
        self.set_hx_label(self.graph_data.hx[-1])
        self.set_hy_label(self.graph_data.hy[-1])
        self.set_hz_label(self.graph_data.hz[-1])
        self.set_ex_label(self.graph_data.ex[-1])
        self.set_ey_label(self.graph_data.ey[-1])

    def set_hx_label(self, value: float):
        """Set the Hx value."""
        self.le_hx.setText("%.3f" % value)

    def set_hy_label(self, value: float):
        """Set the Hy value."""
        self.le_hy.setText("%.3f" % value)

    def set_hz_label(self, value: float):
        """Set the Hz value."""
        self.le_hz.setText("%.3f" % value)

    def set_ex_label(self, value: float):
        """Set the Ex value."""
        self.le_ex.setText("%.3f" % value)

    def set_ey_label(self, value: float):
        """Set the Ey value."""
        self.le_ey.setText("%.3f" % value)

    # -------------------------Start/End Run------------------------------------
    def set_short_cycle_led_start_end(self, code: str):
        """Set the short cycle led in start/end run tab."""
        match code:
            case nims.GPSAQLOCK | nims.GPSRECEIVING:
                pix_icon = self.led_yellow_oval
            case nims.GPSRECEIVED:
                pix_icon = self.led_green_oval
            case _:
                pix_icon = self.led_black_oval
        self.label_short_cycle_led_2.setPixmap(pix_icon)
        self.label_short_cycle_led_3.setPixmap(pix_icon)
        self.label_short_cycle_led_4.setPixmap(pix_icon)

    def set_mag_ready_led(self, code: str):
        """Set the mag ready led in start/end run tab."""
        match code:
            case nims.MAGREADY:
                self.label_mag_ready_led.setPixmap(self.led_green_oval)
            case nims.MAGSLEWING:
                self.label_mag_ready_led.setPixmap(self.led_yellow_oval)
            case nims.MAGERROR:
                self.label_mag_ready_led.setPixmap(self.led_red_oval)
            case _:
                self.label_mag_ready_led.setPixmap(self.led_black_oval)

    def set_mag_north_led(self, state: bool):
        """Set the mag north led in start/end run tab."""
        self.label_mag_north_led.setPixmap(self.led_green_oval if state else self.led_yellow_oval)

    def set_ex_spec_led(self, state: bool):
        """Set the Ex spec led in start/end run tab."""
        self.label_ex_spec_led.setPixmap(self.led_green_oval if state else self.led_yellow_oval)

    def set_ey_spec_led(self, state: bool):
        """Set the Ey spec led in start/end run tab."""
        self.label_ey_spec_led.setPixmap(self.led_green_oval if state else self.led_yellow_oval)

    def set_metadata_led(self, code: int):
        """Set the metadata led in start/end run tab."""
        match code:
            case nims.METACOMPLETE:
                pix_icon = self.led_green_oval
            case nims.METAPARTIAL:
                pix_icon = self.led_yellow_oval
            case _:
                pix_icon = self.led_red_oval
        self.label_metadata_led.setPixmap(pix_icon)

    def set_start_run_led(self, state: bool):
        """Set the start run led in start/end run tab."""
        if state is True:
            self.label_start_run_led.setPixmap(self.led_green_round)
            self.label_end_run_led.setPixmap(self.led_black_round)
        else:
            self.label_start_run_led.setPixmap(self.led_black_round)

    def set_end_run_led(self, state: bool):
        """Set the end run led in start/end run tab."""
        if state is True:
            self.label_end_run_led.setPixmap(self.led_red_round)
            self.label_start_run_led.setPixmap(self.led_black_round)
        else:
            self.label_end_run_led.setPixmap(self.led_black_round)

    def update_ready_led(self):
        """Update the ready led."""
        status = self.packet[nims.STATUSSRT : nims.STATUSSTP].hex()
        if status == nims.MAGREADY:
            self.set_mag_ready_led(nims.MAGREADY)
        elif status == nims.MAGSLEWING:
            self.set_mag_ready_led(nims.MAGSLEWING)
        elif status == nims.MAGERROR:
            self.set_mag_ready_led(nims.MAGERROR)
        else:
            self.set_mag_ready_led(status)

    def update_north_led(self):
        """Update the north led."""
        value = self.graph_data.hy[-1]
        # Check if mag is in range of north.
        if nims.MAGHIGHRANGE > value > nims.MAGLOWRANGE:
            self.set_mag_north_led(True)
        else:
            self.set_mag_north_led(False)

    def update_e_spec_leds(self):
        """Update the Ex spec led."""
        cutoff_voltage_mv = 16
        gain = self.packet[nims.STATUSSRT : nims.STATUSSTP]

        if (
            self.graph_data.ex[-1] >= cutoff_voltage_mv
            or gain == bytes.fromhex(nims.EXHEYL)
            or gain == bytes.fromhex(nims.EXHEYH)
        ):
            self.set_ex_spec_led(True)
        else:
            self.set_ex_spec_led(False)

        if (
            self.graph_data.ey[-1] >= cutoff_voltage_mv
            or gain == bytes.fromhex(nims.EXLEYH)
            or gain == bytes.fromhex(nims.EXHEYH)
        ):
            self.set_ey_spec_led(True)
        else:
            self.set_ey_spec_led(False)

    def check_metadata(self):
        """Check the metadata."""
        empty = False
        all_empty = False

        # check all meta boxes
        if (
            self.le_site_name.text() == ""
            or self.le_state_province.text() == ""
            or self.le_country.text() == ""
            or self.le_run_id.text() == ""
            or self.le_operator.text() == ""
            or self.le_nims_id.text() == ""
            or self.le_mag_id.text() == ""
            or self.le_ns_dipole_length.text() == ""
            or self.le_ns_dipole_heading.text() == ""
            or self.le_ew_dipole_length.text() == ""
            or self.le_ew_dipole_heading.text() == ""
            or self.le_n_electrode_id.text() == ""
            or self.le_s_electrode_id.text() == ""
            or self.le_e_electrode_id.text() == ""
            or self.le_w_electrode_id.text() == ""
            or self.le_gnd_electrode_id.text() == ""
            or self.te_comments.toPlainText() == ""
        ):
            empty = True

        if (
            self.le_site_name.text() == ""
            and self.le_state_province.text() == ""
            and self.le_country.text() == ""
            and self.le_run_id.text() == ""
            and self.le_operator.text() == ""
            and self.le_nims_id.text() == ""
            and self.le_mag_id.text() == ""
            and self.le_ns_dipole_length.text() == ""
            and self.le_ns_dipole_heading.text() == ""
            and self.le_ew_dipole_length.text() == ""
            and self.le_ew_dipole_heading.text() == ""
            and self.le_n_electrode_id.text() == ""
            and self.le_s_electrode_id.text() == ""
            and self.le_e_electrode_id.text() == ""
            and self.le_w_electrode_id.text() == ""
            and self.le_gnd_electrode_id.text() == ""
            and self.te_comments.toPlainText() == ""
        ):
            all_empty = True

        # set the metadata led
        if all_empty is True:
            self.set_metadata_led(nims.METAEMPTY)
        elif empty is True:
            self.set_metadata_led(nims.METAPARTIAL)
        else:
            self.set_metadata_led(nims.METACOMPLETE)

    def start_run(self):
        """Start the run."""
        # turn on the start run led
        self.set_start_run_led(True)
        # pull the current time from the computer
        self.metadata.set_head_comp_time()
        # compile the metadata
        self.metadata.make_header()
        # stop receiving packets
        self.read_port.stop()

        # start the run
        print(f"Send Command: \t{bytes.fromhex(nims.HEADER)}")
        self.send_byte(bytes.fromhex(nims.HEADER))
        sleep(0.30)
        print(f"Send Command: \t{bytes.fromhex(nims.RECORD)}")
        self.send_byte(bytes.fromhex(nims.RECORD))
        sleep(0.50)
        self.send_header_blocks()
        sleep(0.50)
        print(f"Send Command: \t{bytes.fromhex(nims.HEADER)}")
        self.send_byte(bytes.fromhex(nims.HEADER))

        # Clear the packet and start reading from the port
        self.packet = b""
        self.read_port.start()

    def send_file_name(self):
        """Send the file name."""
        self.send_byte(bytes.fromhex(nims.FLENAME))
        self.send_byte(self.get_file_name().encode("utf-8"))
        self.send_byte(bytes.fromhex(nims.FLENAME))

    def send_header_blocks(self):
        """Send the header blocks."""
        block_size = 64
        i = 0
        j = block_size
        while j <= len(self.metadata.file_header):
            print(f"Send Header: \n{self.metadata.file_header[i:j].encode('utf-8')}")
            self.send_byte(self.metadata.file_header[i:j].encode("utf-8"))
            i += block_size
            j += block_size
            sleep(0.15)

    def send_file_header(self):
        """Send the file header."""
        self.send_byte(bytes.fromhex(nims.HEADER))
        self.send_byte(self.metadata.file_header.encode("utf-8"))
        self.send_byte(bytes.fromhex(nims.HEADER))

    def end_run(self):
        """End the run."""
        # toggle start run/end run leds
        self.set_end_run_led(True)
        # send end run command
        print(f"Send Command: \t{bytes.fromhex(nims.ENDREC)}")
        self.send_byte(bytes.fromhex(nims.ENDREC))

    # -------------------------Site Report--------------------------------------
    def status_change(self):
        """Change the status of the site report."""
        self.sr.status = self.cb_status.currentText()
        if self.sr.status == "Install":
            self.svr_enable_install()
        elif self.sr.status == "Check":
            self.svr_enable_check()
        elif self.sr.status == "Extract":
            self.svr_enable_extract()

    def svr_enable_install(self):
        """Enable the site report for installation."""
        self.svr_preinstall_electrodes(True)
        self.svr_timing("Install")

    def svr_enable_check(self):
        """Enable the site report for check."""
        self.svr_preinstall_electrodes(False)
        self.svr_timing("Check")

    def svr_enable_extract(self):
        """Enable the site report for extraction."""
        self.svr_preinstall_electrodes(False)
        self.svr_timing("Extract")

    def svr_timing(self, code: str):
        """Set the timing for the site report."""
        match code:
            case "Install":
                self.le_last_time_stamp_sr.setText("")
                self.sr.last_ts = ""
                self.label_104.setText("At Installation:")
                self.le_last_time_stamp_sr.setEnabled(False)
                self.le_last_time_stamp_sr.setStyleSheet("background-color: rgb(104, 104, 104)")
                self.le_first_time_stamp_sr.setEnabled(True)
                self.le_first_time_stamp_sr.setStyleSheet("background-color: rgb(255, 255, 255)")
            case "Check":
                self.label_104.setText("At Check:")
                self.le_last_time_stamp_sr.setEnabled(True)
                self.le_last_time_stamp_sr.setStyleSheet("background-color: rgb(255, 255, 255)")
                self.le_first_time_stamp_sr.setEnabled(True)
                self.le_first_time_stamp_sr.setStyleSheet("background-color: rgb(255, 255, 255)")
            case "Extract":
                self.label_104.setText("At Extraction:")
                self.le_last_time_stamp_sr.setEnabled(True)
                self.le_last_time_stamp_sr.setStyleSheet("background-color: rgb(255, 255, 255)")
                self.le_first_time_stamp_sr.setText("")
                self.sr.first_ts = ""
                self.le_first_time_stamp_sr.setEnabled(False)
                self.le_first_time_stamp_sr.setStyleSheet("background-color: rgb(104, 104, 104)")
            case _:
                pass

    def svr_preinstall_electrodes(self, state: bool):
        """Enable the site visit report pre-installation electrodes fields."""
        back_color = (
            "background-color: rgb(255, 255, 255)"
            if state
            else "background-color: rgb(104, 104, 104)"
        )

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

    def set_check_sr(self, state: bool):
        """Set the check led in the site report."""
        check_icon_path = Path(
            self.icon_path, "check_green_50_50.png" if state else "x_red_50_50.png"
        )
        self.label_check_sr.setPixmap(QPixmap(check_icon_path))

    def path_on_click(self):
        """Open the file dialog to select the save directory."""
        self.hide()
        save_dir = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.show()

        if not save_dir:
            return
        self.sr.update_save_path(Path(save_dir))
        self.update_save_directory_sr()

        print(f"Site Report save directory: \t{save_dir}")

    def update_save_directory_sr(self):
        """Update the save directory in the site report."""
        self.le_change_directory_sr.setText(os.path.join(self.sr.save_path, self.sr.save_name))

    def update_site_name_sr(self):
        """Update the site name in the site report."""
        # get text and update metadata field
        site_name = self.le_site_name_sr.text()

        self.update_site_name(site_name)

    def update_state_province_sr(self):
        """Update the state/province in the site report."""
        # get text and update metadata field
        sp = self.le_state_province_sr.text()

        self.update_state_province(sp)

    def update_country_sr(self):
        """Update the country in the site report."""
        # get text and update metadata field
        cntry = self.le_country_sr.text()

        self.update_country(cntry)

    def update_crew_sr(self):
        """Update the crew in the site report."""
        self.sr.crew = self.le_crew.text()

    def update_run_id_sr(self):
        """Update the run id in the site report."""
        txt = self.le_run_id_sr.text()

        self.update_run_id(txt)

    def update_nims_id_sr(self):
        """Update the NIMS id in the site report."""
        txt = self.le_nims_id_sr.text()

        self.update_nims_id(txt)

    def update_mag_id_sr(self):
        """Update the mag id in the site report."""
        txt = self.le_mag_id_sr.text()

        self.update_mag_id(txt)

    def update_n_id_sr(self):
        """Update the north electrode id in the site report."""
        txt = self.le_n_electrode_id_sr.text()

        self.update_n_id(txt)

    def update_s_id_sr(self):
        """Update the south electrode id in the site report."""
        txt = self.le_s_electrode_id_sr.text()

        self.update_s_id(txt)

    def update_e_id_sr(self):
        """Update the east electrode id in the site report."""
        txt = self.le_e_electrode_id_sr.text()

        self.update_e_id(txt)

    def update_w_id_sr(self):
        """Update the west electrode id in the site report."""
        txt = self.le_w_electrode_id_sr.text()

        self.update_w_id(txt)

    def update_gps_lat_sr(self):
        """Update the GPS latitude in the site report."""
        self.sr.lat = self.le_gps_lat_sr.text()

    def update_gps_lon_sr(self):
        """Update the GPS longitude in the site report."""
        self.sr.lon = self.le_gps_lon_sr.text()

    def update_gps_alt_sr(self):
        """Update the GPS altitude in the site report."""
        self.sr.alt = self.le_gps_alt_sr.text()

    def update_gps_dec(self, declination: str, declination_direction: str):
        """Update the GPS declination in the site report."""
        d = {"N": "+", "S": "-", "E": "+", "W": "-"}
        try:
            dec = f"{d[declination_direction[0]]}{declination}"
            self.le_gps_dec_sr.setText("{0:.2f}".format(float(dec)))

        except SyntaxError:
            self.le_gps_dec_sr.setText(str(0))

        self.update_gps_dec_sr()

    def update_gps_dec_sr(self):
        """Update the GPS declination in the site report."""
        self.sr.dec = self.le_gps_dec_sr.text()

    def update_batt_volt_sr(self):
        """Update the battery voltage in the site report."""
        self.sr.battery = self.le_battery_voltage_sr.text()

    def update_gain_sr(self):
        """Update the gain in the site report."""
        ex_gain = self.verify_gain_value(self.le_ex_gain_sr.text())
        ey_gain = self.verify_gain_value(self.le_ey_gain_sr.text())

        # set values
        self.le_ex_gain_sr.setText(ex_gain)
        self.le_ey_gain_sr.setText(ey_gain)

        # Set the gain code
        match ex_gain + ey_gain:
            case "LL":
                gain = "L"
            case "HL":
                gain = "X"
            case "LH":
                gain = "Y"
            case "HH":
                gain = "H"
            case _:
                gain = "U"
        self.sr.gain = gain

    @staticmethod
    def verify_gain_value(val: str) -> str:
        """Verify the gain value."""
        # verify text is empty, h, l
        gain = ""

        if val == "L" or val == "l":
            gain = "L"
        elif val == "H" or val == "h":
            gain = "H"

        return gain

    def update_last_time_stamp_sr(self):
        """Update the last time stamp in the site report."""
        self.sr.last_ts = self.le_last_time_stamp_sr.text()

    def update_first_time_stamp_sr(self):
        """Update the first time stamp in the site report."""
        self.sr.first_ts = self.le_first_time_stamp_sr.text()

    def update_timestamp_sr(self, date: str, time: str):
        """Update the timestamp in the site report."""
        d = date.split("/")
        try:
            dt = "20{}-{}-{} {}".format(d[2], d[0], d[1], time)
        except IndexError:
            dt = "{} {}".format(date, time)

        if self.sr.status == "Extract":
            self.le_last_time_stamp_sr.setText(dt)
            self.sr.last_ts = dt
        else:
            self.le_first_time_stamp_sr.setText(dt)
            self.sr.first_ts = dt

    def clear_pre_e_sr(self):
        """Clear the pre-installation electrodes."""
        self.sr.pre_e_ns_r = ""
        self.le_pre_e_ns_r_sr.setText("")
        self.sr.pre_e_sn_r = ""
        self.le_pre_e_sn_r_sr.setText("")
        self.sr.pre_e_ew_r = ""
        self.le_pre_e_ew_r_sr.setText("")
        self.sr.pre_e_we_r = ""
        self.le_pre_e_we_r_sr.setText("")
        self.sr.pre_e_ns_v = ""
        self.le_pre_e_ns_v_sr.setText("")
        self.sr.pre_e_ew_v = ""
        self.le_pre_e_ew_v_sr.setText("")

    def update_pre_e_ns_r_sr(self):
        """Update the pre-installation NS resistance in the site report."""
        self.sr.pre_e_ns_r = self.le_pre_e_ns_r_sr.text()

    def update_pre_e_sn_r_sr(self):
        """Update the pre-installation SN resistance in the site report."""
        self.sr.pre_e_sn_r = self.le_pre_e_sn_r_sr.text()

    def update_pre_e_ew_r_sr(self):
        """Update the pre-installation EW resistance in the site report."""
        self.sr.pre_e_ew_r = self.le_pre_e_ew_r_sr.text()

    def update_pre_e_we_r_sr(self):
        """Update the pre-installation WE resistence in the site report."""
        self.sr.pre_e_we_r = self.le_pre_e_we_r_sr.text()

    def update_pre_e_ns_v_sr(self):
        """Update the pre-installation NS voltage in the site report."""
        self.sr.pre_e_ns_v = self.le_pre_e_ns_v_sr.text()

    def update_pre_e_ew_v_sr(self):
        """Update the pre-installation EW voltage in the site report."""
        self.sr.pre_e_ew_v = self.le_pre_e_ew_v_sr.text()

    def update_e_ns_r_sr(self):
        """Update the NS resistance in the site report."""
        self.sr.e_ns_r = self.le_e_ns_r_sr.text()

    def update_e_sr_r_sr(self):
        """Update the SR resistance in the site report."""
        self.sr.e_sn_r = self.le_e_sn_r_sr.text()

    def update_e_ew_r_sr(self):
        """Update the EW resistance in the site report."""
        self.sr.e_ew_r = self.le_e_ew_r_sr.text()

    def update_e_we_r_sr(self):
        """Update the WE resistence in the site report."""
        self.sr.e_we_r = self.le_e_we_r_sr.text()

    def update_e_ng_r_sr(self):
        """Update the NG resistance in the site report."""
        self.sr.e_ng_r = self.le_e_ng_r_sr.text()

    def update_e_gn_r_sr(self):
        """Update the GN resistance in the site report."""
        self.sr.e_gn_r = self.le_e_gn_r_sr.text()

    def update_ex_gps_sr(self):
        """Update the EX GPS in the site report."""
        self.sr.ex_gps = self.le_ex_gps_sr.text()

    def update_ey_gps_sr(self):
        """Update the EY GPS in the site report."""
        self.sr.ey_gps = self.le_ey_gps_sr.text()

    def update_e_ns_vdc_sr(self):
        """Update the NS voltage in the site report."""
        self.sr.e_ns_vdc = self.le_e_ns_vdc_sr.text()

    def update_e_ew_vdc_sr(self):
        """Update the EW voltage in the site report."""
        self.sr.e_ew_vdc = self.le_e_ew_vdc_sr.text()

    def update_e_ng_vdc_sr(self):
        """Update the NG voltage in the site report."""
        self.sr.e_ng_vdc = self.le_e_ng_vdc_sr.text()

    def update_e_ns_vac_sr(self):
        """Update the NS voltage in the site report."""
        self.sr.e_ns_vac = self.le_e_ns_vac_sr.text()

    def update_e_ew_vac_sr(self):
        """Update the EW voltage in the site report."""
        self.sr.e_ew_vac = self.le_e_ew_vac_sr.text()

    def update_e_ng_vac_sr(self):
        """Update the NG voltage in the site report."""
        self.sr.e_ng_vac = self.le_e_ng_vac_sr.text()

    def update_comments_sr(self):
        """Update the comments in the site report."""
        # get text and update metadata field
        comments = self.te_comments_sr.toPlainText()

        # set the comments on metadata
        self.set_comments_md(comments)

    def set_comments_sr(self, comments: str):
        """Set the comments in the site report."""
        # update comments in site report
        self.sr.comments = comments

        # disconnect the signals
        self.te_comments_sr.textChanged.disconnect()
        # update the comments
        self.te_comments_sr.setText(comments)
        # reconnect the signals
        self.te_comments_sr.textChanged.connect(self.update_comments_sr)

    def write_report(self):
        """Write the site report."""
        try:
            self.sr.write_file()
            self.set_check_sr(True)
        except (PermissionError, FileNotFoundError, TypeError):
            self.set_check_sr(False)

    # -------------------------Engineering--------------------------------------

    def update_hex_data(self, packet: str):
        """Update the hex data in the engineering tab."""
        text = self.te_rawhex.toPlainText()
        # print(len(text))
        if len(text) >= 100:
            text = f"{text[-98:]} "
        self.te_rawhex.setText(f"{text}\t{packet}")

    def record_raw_data(self):
        """Record the port data since opening.

        The record_raw_data will record the data that has been read on the port
        since opening of the port.  Each toggle of the button writes a new file
        with the saved information.
        """
        # get date and time
        date_time = strftime("%Y%m%d_%H%M%S", gmtime())
        # set filename
        fle_nme = f"port_data_{date_time}.txt"
        # the save location
        fle_pth = Path(Path.home(), "Documents", fle_nme)

        # write filename
        with open(fle_pth, "wb") as fle_ptr:
            fle_ptr.write(self.port_data)

    def update_filtered_data(self, packet: str):
        """Update the filtered data in the engineering tab."""
        self.te_filteredhexdata.setText(packet)

    def update_bytes_read(self):
        """Update the bytes read in the engineering tab."""
        self.te_bytesread.setText(str(len(self.packet)))

    def update_mag_status(self):
        """Update the mag status in the engineering tab."""
        value = self.packet[nims.STATUSSRT : nims.STATUSSTP].hex().upper()
        # update the mag status byte
        self.te_magstatus.setText(value)

    def update_gps_value_e(self, value: str):
        """Update the GPS value in the engineering tab."""
        # assign the value in the engineering panel
        self.te_gps_status_byte_e.setText(value)

    def clear_gps_string_e(self):
        """Clear the GPS string in the engineering tab."""
        self.te_gps_string_e.setText("")

    def update_gps_string_e(self):
        """Update the GPS string in the engineering tab."""
        self.te_gps_string_e.setText(self.gps_string)

    # -------------------------Processing---------------------------------------

    def parse_packet(self, data: bytes):
        """Parse the packet and update the GUI."""
        self.set_receiving_led(True)
        self.receiving_led_timer.stop()
        self.receiving_led_timer.start(250)
        # save data to variable
        self.port_data += data
        # TODO: raw
        self.update_hex_data(data.hex().upper())
        # if len(self.packet) > 4:
        #     print(len(self.packet))
        #     print(2*(int(self.packet[2:4], 16)-1))
        # print(data)

        # print(self.packet)
        if len(self.packet) == 0 and data == bytes.fromhex(nims.SOH):
            try:
                self.packet = b"".join([self.packet, data])
            except TypeError:
                self.set_packets_led(False)
                pass
        elif len(self.packet) != 0:
            with contextlib.suppress(TypeError):
                self.packet = b"".join([self.packet, data])
            # self.packet += data
            if (len(self.packet) == int(self.packet[1:2].hex(), 16)) and data == bytes.fromhex(
                nims.EOH
            ):
                # change packets led to valid
                self.set_packets_led(True)
                # set the variant label
                # self.update_variant()
                # process the data packet
                self.process_packet()
            elif len(self.packet) > int(self.packet[1:2].hex(), 16):
                # change packets led to valid
                self.set_packets_led(False)
                self.packet = b""

        else:
            self.set_packets_led(False)
            # handle command
            pass

    def process_packet(self):
        """Parse the packet and update the GUI."""
        # convert from bytes to upper case hex
        packet: str = self.packet.hex().upper()
        # reformat packet bytes
        packet: str = "\t".join([packet[i : i + 2] for i in range(0, len(packet), 2)])

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
        self.packet = b""

    def update_data(self):
        """Update the data values in the engineering tab."""
        hx = self.packet[nims.HXSTART : nims.HXSTOP]
        hy = self.packet[nims.HYSTART : nims.HYSTOP]
        hz = self.packet[nims.HZSTART : nims.HZSTOP]
        ex = self.packet[nims.EXSTART : nims.EXSTOP]
        ey = self.packet[nims.EYSTART : nims.EYSTOP]

        self.graph_data.update_hx(byte_to_int(hx) * nims.HCONVERSION)
        self.graph_data.update_hy(byte_to_int(hy) * nims.HCONVERSION)
        self.graph_data.update_hz(byte_to_int(hz) * nims.HCONVERSION)
        self.graph_data.update_ex(byte_to_int(ex) * nims.ECONVERSION)
        self.graph_data.update_ey(byte_to_int(ey) * nims.ECONVERSION)

    def update_gps(self):
        """Update the GPS values in the engineering tab."""
        # get the binary value
        bin_value: bytes = self.packet[nims.GPSSRT : nims.GPSSTP]
        # get the gps value and cast as uppercase hex
        value: str = self.packet[nims.GPSSRT : nims.GPSSTP].hex().upper()
        # update the GPS value in metadata
        self.update_gps_value_m(value)
        # update the GPS value in engineering
        self.update_gps_value_e(value)
        # check the gps receive state
        if value == nims.GPSINITIAL and self.gps_state == nims.GPSINITIAL:
            # set the leds in 'metadata'
            self.set_short_cycle_led_metadata(value)
            self.set_almanac_led(False)
            # set the leds in 'Start/End Run'
            self.set_short_cycle_led_start_end(value)
        elif value == nims.GPSALMANAC:
            # set the gps state
            self.gps_state = nims.GPSALMANAC
            # set the leds in 'metadata'
            self.set_short_cycle_led_metadata(value)
            self.set_almanac_led(True)
            # set the leds in 'Start/End Run'
            self.set_short_cycle_led_start_end(value)
        elif value == nims.GPSAQLOCK:
            # set the gps state
            self.gps_state = nims.GPSAQLOCK
            # set the leds in 'metadata'
            self.set_short_cycle_led_metadata(value)
            self.set_almanac_led(False)
            # set the leds in 'Start/End Run'
            self.set_short_cycle_led_start_end(value)
        elif value == "24" and self.gps_state == nims.GPSAQLOCK:
            # set the gps state
            self.gps_state = nims.GPSRECEIVING
            # convert the first character from binary to Unicode, add to gps_string
            self.gps_string = ""
            # update the gps boxes
            self.clear_gps_string_m()
            self.update_gps_string_e()
            self.clear_gps_string_e()
            self.update_gps_string_e()

        # enter while receiving gps sentences
        if self.gps_state == nims.GPSRECEIVING:
            # read 139 bytes
            self.gps_string += bin_value.decode("utf-8", "ignore")

            # update the gps bytes
            self.update_gps_string_m()
            self.update_gps_string_e()

            # if read 139 bytes, exit
            if len(self.gps_string) >= 139:
                # set the gps state
                self.gps_state = nims.GPSRECEIVED
                # set the leds in 'metadata'
                self.set_short_cycle_led_metadata(nims.GPSRECEIVED)
                self.set_almanac_led(False)
                # set the leds in 'Start/End Run'
                self.set_short_cycle_led_start_end(nims.GPSRECEIVED)
                # parse the data
                self.parse_gps_packet()

    def parse_gps_packet(self):
        """Parse the GPS packet."""
        gps_rmc = []
        gps_gga = []
        print("Finished receiving GPS Data")
        print(self.gps_string)
        # parse the string into gps sentences
        gps_sentences: list[str] = self.gps_string.split("\r\n")

        # find the rmc and gga NMEA sentences
        for s in gps_sentences:
            if search("RMC", s) is not None:
                gps_rmc: list[str] = s.split(",")
            if search("GGA", s) is not None:
                gps_gga: list[str] = s.split(",")
        # format the lists into readable gps string
        self.update_gps_metadata_string(gps_rmc, gps_gga)
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
        """Update the 'Data Display' and 'Start/End Run' components."""
        # parse the gain byte
        gain = self.packet[nims.GAINSRT : nims.GAINSTP].hex().upper()
        # Update gain lights on Data display
        self.set_gain_leds(gain)
        # Update E gain spec leds on Start/End Run
        self.update_e_spec_leds()

    def update_h(self):
        """Update the 'Data Display' and 'Start/End Run' components."""
        # Update 'Data Display' components
        # Update 'Start/End Run' components
        self.update_ready_led()
        self.update_north_led()
        # Update 'Engineering' components
        self.update_mag_status()

    def send_byte(self, cmd: bytes):
        """Send a byte to the port."""
        if self.port.is_open:
            self.port.write(cmd)


def byte_to_int(_bytes: bytes) -> int:
    """Convert a byte4 into a signed int.

    The byte_to_int takes a byte (data type), length of 4 bytes, and converts,
    unpacks, it into a signed integer.

    Args:
        _bytes (bytes): A 4 byte(length) byte(type).

    Returns
    -------
        value (int): Description of returned object.

    """
    std_length = 4

    if len(_bytes) < std_length:
        _bytes = to_byte4(_bytes)

    value = struct.unpack(">i", _bytes)[0]

    return value


def to_byte4(_bytes: bytes) -> bytes:
    """Convert n length byte string to a 4 byte string.

    The to_byte4 function takes an n byte (less than 4 bytes), two's
    compliment, string and returns a 4 byte, two's compliment, version
    of the same number.

    Parameters
    ----------
    _bytes : bytes
        N byte string, twos compliment.

    Returns
    -------
    bytes : 4 byte string, twos compliment.
    """
    standard_length: int = 4  # Desired string length, in bytes.
    neg_byte = b"\xff"  # Leading byte for negative number.
    pos_byte = b"\x00"  # Leading byte for positive number.

    # check if leading bit is 1 or 0: b:1000 0000 = 128
    if _bytes[0] > 127:
        # add leading bytes until 4 bytes in length
        while len(_bytes) < standard_length:
            _bytes = b"".join([neg_byte, _bytes])
    else:
        # add leading bytes until 4 bytes in length
        while len(_bytes) < standard_length:
            _bytes = b"".join([pos_byte, _bytes])

    return _bytes


class GraphData:
    """GraphData class."""

    def __init__(
        self,
        ticks: int = 60,
        hx: list[float] | None = None,
        hy: list[float] | None = None,
        hz: list[float] | None = None,
        ex: list[float] | None = None,
        ey: list[float] | None = None,
    ):
        if ey is None:
            ey = []
        if ex is None:
            ex = []
        if hz is None:
            hz = []
        if hy is None:
            hy = []
        if hx is None:
            hx = []
        self.ticks: int = ticks
        self.xdata: list[int] = list(range(0, ticks))
        self.hx: list[float] = hx
        self.hy: list[float] = hy
        self.hz: list[float] = hz
        self.ex: list[float] = ex
        self.ey: list[float] = ey

    def update_hx(self, value: float):
        """Update the hx value.

        Parameters
        ----------
        value : float
            The new value to be added to the list.
        """
        if not self.hx:
            for _ in range(0, self.ticks):
                self.hx.append(value)

        self.hx.pop(0)
        self.hx.append(value)

    def update_hy(self, value: float):
        """Update the hy value.

        Parameters
        ----------
        value : float
            The new value to be added to the list.
        """
        if not self.hy:
            for _ in range(0, self.ticks):
                self.hy.append(value)

        self.hy.pop(0)
        self.hy.append(value)

    def update_hz(self, value: float):
        """Update the hz value.

        Parameters
        ----------
        value : float
            The new value to be added to the list.
        """
        if not self.hz:
            for _ in range(0, self.ticks):
                self.hz.append(value)

        self.hz.pop(0)
        self.hz.append(value)

    def update_ex(self, value: float):
        """Update the ex value.

        Parameters
        ----------
        value : str
            The new value to be added to the list.
        """
        if not self.ex:
            for _ in range(0, self.ticks):
                self.ex.append(value)

        self.ex.pop(0)
        self.ex.append(value)

    def update_ey(self, value: float):
        """Update the ey value.

        Parameters
        ----------
        value : str
            The new value to be added to the list.
        """
        if not self.ey:
            for _ in range(0, self.ticks):
                self.ey.append(value)

        self.ey.pop(0)
        self.ey.append(value)
