# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenuBar,
    QRadioButton,
    QStackedWidget,
    QStatusBar,
    QTextEdit,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 630)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0, 35, 875, 40))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.tb_metadata = QToolButton(self.frame)
        self.tb_metadata.setObjectName("tb_metadata")
        self.tb_metadata.setGeometry(QRect(350, 0, 175, 40))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.tb_metadata.setFont(font)
        self.tb_metadata.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tb_metadata.setStyleSheet("")
        self.tb_metadata.setCheckable(True)
        self.tb_metadata.setChecked(False)
        self.tb_metadata.setAutoExclusive(True)
        self.tb_datadisplay = QToolButton(self.frame)
        self.tb_datadisplay.setObjectName("tb_datadisplay")
        self.tb_datadisplay.setGeometry(QRect(175, 0, 175, 40))
        self.tb_datadisplay.setFont(font)
        self.tb_datadisplay.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tb_datadisplay.setStyleSheet("")
        self.tb_datadisplay.setCheckable(True)
        self.tb_datadisplay.setAutoExclusive(True)
        self.tb_startend = QToolButton(self.frame)
        self.tb_startend.setObjectName("tb_startend")
        self.tb_startend.setGeometry(QRect(0, 0, 175, 40))
        self.tb_startend.setFont(font)
        self.tb_startend.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tb_startend.setStyleSheet("")
        self.tb_startend.setCheckable(True)
        self.tb_startend.setChecked(True)
        self.tb_startend.setAutoExclusive(True)
        self.tb_engineer = QToolButton(self.frame)
        self.tb_engineer.setObjectName("tb_engineer")
        self.tb_engineer.setGeometry(QRect(700, 0, 175, 40))
        self.tb_engineer.setFont(font)
        self.tb_engineer.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tb_engineer.setStyleSheet("")
        self.tb_engineer.setCheckable(True)
        self.tb_engineer.setAutoExclusive(True)
        self.tb_sitereport = QToolButton(self.frame)
        self.tb_sitereport.setObjectName("tb_sitereport")
        self.tb_sitereport.setGeometry(QRect(525, 0, 175, 40))
        self.tb_sitereport.setFont(font)
        self.tb_sitereport.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tb_sitereport.setStyleSheet("")
        self.tb_sitereport.setCheckable(True)
        self.tb_sitereport.setAutoExclusive(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(0, 75, 950, 530))
        self.stackedWidget.setMaximumSize(QSize(950, 530))
        self.stackedWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.stackStartEndUI = QWidget()
        self.stackStartEndUI.setObjectName("stackStartEndUI")
        self.line_3 = QFrame(self.stackStartEndUI)
        self.line_3.setObjectName("line_3")
        self.line_3.setGeometry(QRect(475, 5, 3, 515))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_34 = QFrame(self.stackStartEndUI)
        self.frame_34.setObjectName("frame_34")
        self.frame_34.setEnabled(False)
        self.frame_34.setGeometry(QRect(485, 218, 451, 302))
        self.frame_34.setFrameShape(QFrame.Shape.Panel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.label_62 = QLabel(self.stackStartEndUI)
        self.label_62.setObjectName("label_62")
        self.label_62.setGeometry(QRect(0, 5, 475, 21))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_62.setFont(font1)
        self.label_62.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_63 = QLabel(self.stackStartEndUI)
        self.label_63.setObjectName("label_63")
        self.label_63.setGeometry(QRect(475, 5, 475, 21))
        self.label_63.setFont(font1)
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_35 = QFrame(self.stackStartEndUI)
        self.frame_35.setObjectName("frame_35")
        self.frame_35.setGeometry(QRect(10, 50, 455, 45))
        self.frame_35.setFrameShape(QFrame.Shape.Panel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.tb_shortcycle_2 = QToolButton(self.frame_35)
        self.tb_shortcycle_2.setObjectName("tb_shortcycle_2")
        self.tb_shortcycle_2.setGeometry(QRect(323, 5, 58, 35))
        font2 = QFont()
        font2.setPointSize(13)
        self.tb_shortcycle_2.setFont(font2)
        self.tb_shortcycle_2.setCheckable(False)
        self.tb_shortcycle_2.setAutoExclusive(True)
        self.tb_shortcycle_2.setAutoRaise(False)
        self.label_21 = QLabel(self.frame_35)
        self.label_21.setObjectName("label_21")
        self.label_21.setGeometry(QRect(5, 5, 313, 31))
        self.label_21.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_21.setWordWrap(True)
        self.label_short_cycle_led_2 = QLabel(self.frame_35)
        self.label_short_cycle_led_2.setObjectName("label_short_cycle_led_2")
        self.label_short_cycle_led_2.setGeometry(QRect(392, 8, 58, 29))
        self.label_short_cycle_led_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_36 = QFrame(self.stackStartEndUI)
        self.frame_36.setObjectName("frame_36")
        self.frame_36.setGeometry(QRect(10, 120, 455, 73))
        self.frame_36.setFrameShape(QFrame.Shape.Panel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.label_23 = QLabel(self.frame_36)
        self.label_23.setObjectName("label_23")
        self.label_23.setGeometry(QRect(5, 10, 313, 21))
        self.label_23.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_23.setWordWrap(True)
        self.label_mag_north_led = QLabel(self.frame_36)
        self.label_mag_north_led.setObjectName("label_mag_north_led")
        self.label_mag_north_led.setGeometry(QRect(392, 39, 58, 29))
        self.label_mag_north_led.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_mag_ready_led = QLabel(self.frame_36)
        self.label_mag_ready_led.setObjectName("label_mag_ready_led")
        self.label_mag_ready_led.setGeometry(QRect(392, 5, 58, 29))
        self.label_mag_ready_led.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.frame_36)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(325, 10, 59, 16))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_68 = QLabel(self.frame_36)
        self.label_68.setObjectName("label_68")
        self.label_68.setGeometry(QRect(325, 45, 59, 16))
        self.label_68.setFont(font3)
        self.label_24 = QLabel(self.frame_36)
        self.label_24.setObjectName("label_24")
        self.label_24.setGeometry(QRect(5, 45, 301, 21))
        self.label_24.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_24.setWordWrap(True)
        self.label_20 = QLabel(self.stackStartEndUI)
        self.label_20.setObjectName("label_20")
        self.label_20.setGeometry(QRect(10, 30, 141, 18))
        font4 = QFont()
        font4.setPointSize(16)
        self.label_20.setFont(font4)
        self.label_20.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_22 = QLabel(self.stackStartEndUI)
        self.label_22.setObjectName("label_22")
        self.label_22.setGeometry(QRect(10, 100, 168, 18))
        self.label_22.setFont(font4)
        self.label_22.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.frame_37 = QFrame(self.stackStartEndUI)
        self.frame_37.setObjectName("frame_37")
        self.frame_37.setGeometry(QRect(10, 218, 455, 73))
        self.frame_37.setFrameShape(QFrame.Shape.Panel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.label_25 = QLabel(self.frame_37)
        self.label_25.setObjectName("label_25")
        self.label_25.setGeometry(QRect(5, 5, 311, 61))
        self.label_25.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.label_25.setWordWrap(True)
        self.label_ex_spec_led = QLabel(self.frame_37)
        self.label_ex_spec_led.setObjectName("label_ex_spec_led")
        self.label_ex_spec_led.setGeometry(QRect(392, 5, 58, 29))
        self.label_ex_spec_led.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_ey_spec_led = QLabel(self.frame_37)
        self.label_ey_spec_led.setObjectName("label_ey_spec_led")
        self.label_ey_spec_led.setGeometry(QRect(392, 39, 58, 29))
        self.label_ey_spec_led.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_69 = QLabel(self.frame_37)
        self.label_69.setObjectName("label_69")
        self.label_69.setGeometry(QRect(325, 10, 71, 16))
        self.label_69.setFont(font3)
        self.label_70 = QLabel(self.frame_37)
        self.label_70.setObjectName("label_70")
        self.label_70.setGeometry(QRect(325, 45, 71, 16))
        self.label_70.setFont(font3)
        self.label_27 = QLabel(self.stackStartEndUI)
        self.label_27.setObjectName("label_27")
        self.label_27.setGeometry(QRect(10, 198, 221, 18))
        self.label_27.setFont(font4)
        self.label_27.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_28 = QLabel(self.stackStartEndUI)
        self.label_28.setObjectName("label_28")
        self.label_28.setGeometry(QRect(10, 296, 141, 18))
        self.label_28.setFont(font4)
        self.label_28.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.frame_38 = QFrame(self.stackStartEndUI)
        self.frame_38.setObjectName("frame_38")
        self.frame_38.setGeometry(QRect(10, 316, 455, 39))
        self.frame_38.setFrameShape(QFrame.Shape.Panel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.label_29 = QLabel(self.frame_38)
        self.label_29.setObjectName("label_29")
        self.label_29.setGeometry(QRect(5, 3, 313, 33))
        self.label_29.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_29.setWordWrap(True)
        self.label_metadata_led = QLabel(self.frame_38)
        self.label_metadata_led.setObjectName("label_metadata_led")
        self.label_metadata_led.setGeometry(QRect(392, 5, 58, 29))
        self.label_metadata_led.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_26 = QLabel(self.stackStartEndUI)
        self.label_26.setObjectName("label_26")
        self.label_26.setGeometry(QRect(485, 30, 141, 18))
        self.label_26.setFont(font4)
        self.label_26.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.frame_39 = QFrame(self.stackStartEndUI)
        self.frame_39.setObjectName("frame_39")
        self.frame_39.setGeometry(QRect(485, 50, 455, 45))
        self.frame_39.setFrameShape(QFrame.Shape.Panel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.tb_shortcycle_4 = QToolButton(self.frame_39)
        self.tb_shortcycle_4.setObjectName("tb_shortcycle_4")
        self.tb_shortcycle_4.setGeometry(QRect(323, 5, 58, 35))
        self.tb_shortcycle_4.setFont(font2)
        self.tb_shortcycle_4.setCheckable(False)
        self.tb_shortcycle_4.setAutoExclusive(True)
        self.tb_shortcycle_4.setAutoRaise(False)
        self.label_30 = QLabel(self.frame_39)
        self.label_30.setObjectName("label_30")
        self.label_30.setGeometry(QRect(5, 5, 313, 29))
        self.label_30.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_30.setWordWrap(True)
        self.label_short_cycle_led_4 = QLabel(self.frame_39)
        self.label_short_cycle_led_4.setObjectName("label_short_cycle_led_4")
        self.label_short_cycle_led_4.setGeometry(QRect(392, 8, 58, 29))
        self.label_short_cycle_led_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_40 = QFrame(self.stackStartEndUI)
        self.frame_40.setObjectName("frame_40")
        self.frame_40.setGeometry(QRect(485, 120, 455, 71))
        self.frame_40.setFrameShape(QFrame.Shape.Panel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.label_end_run_led = QLabel(self.frame_40)
        self.label_end_run_led.setObjectName("label_end_run_led")
        self.label_end_run_led.setGeometry(QRect(389, 5, 61, 61))
        self.label_end_run_led.setFrameShape(QFrame.Shape.NoFrame)
        self.tb_end_run = QToolButton(self.frame_40)
        self.tb_end_run.setObjectName("tb_end_run")
        self.tb_end_run.setGeometry(QRect(10, 10, 369, 51))
        self.tb_end_run.setFont(font2)
        self.tb_end_run.setCheckable(False)
        self.tb_end_run.setAutoExclusive(True)
        self.tb_end_run.setAutoRaise(False)
        self.label_65 = QLabel(self.stackStartEndUI)
        self.label_65.setObjectName("label_65")
        self.label_65.setGeometry(QRect(485, 100, 168, 18))
        self.label_65.setFont(font4)
        self.label_65.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_66 = QLabel(self.stackStartEndUI)
        self.label_66.setObjectName("label_66")
        self.label_66.setEnabled(False)
        self.label_66.setGeometry(QRect(485, 198, 168, 18))
        self.label_66.setFont(font4)
        self.label_66.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.frame_41 = QFrame(self.stackStartEndUI)
        self.frame_41.setObjectName("frame_41")
        self.frame_41.setGeometry(QRect(10, 380, 455, 71))
        self.frame_41.setFrameShape(QFrame.Shape.Panel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.label_start_run_led = QLabel(self.frame_41)
        self.label_start_run_led.setObjectName("label_start_run_led")
        self.label_start_run_led.setGeometry(QRect(389, 5, 61, 61))
        self.label_start_run_led.setFrameShape(QFrame.Shape.NoFrame)
        self.tb_start_run = QToolButton(self.frame_41)
        self.tb_start_run.setObjectName("tb_start_run")
        self.tb_start_run.setGeometry(QRect(10, 10, 369, 51))
        self.tb_start_run.setFont(font2)
        self.tb_start_run.setStyleSheet("")
        self.tb_start_run.setCheckable(False)
        self.tb_start_run.setAutoExclusive(True)
        self.tb_start_run.setAutoRaise(False)
        self.label_67 = QLabel(self.stackStartEndUI)
        self.label_67.setObjectName("label_67")
        self.label_67.setGeometry(QRect(10, 360, 168, 18))
        self.label_67.setFont(font4)
        self.label_67.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_31 = QLabel(self.stackStartEndUI)
        self.label_31.setObjectName("label_31")
        self.label_31.setGeometry(QRect(10, 456, 141, 18))
        self.label_31.setFont(font4)
        self.label_31.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.frame_42 = QFrame(self.stackStartEndUI)
        self.frame_42.setObjectName("frame_42")
        self.frame_42.setGeometry(QRect(10, 475, 455, 45))
        self.frame_42.setFrameShape(QFrame.Shape.Panel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.tb_shortcycle_3 = QToolButton(self.frame_42)
        self.tb_shortcycle_3.setObjectName("tb_shortcycle_3")
        self.tb_shortcycle_3.setGeometry(QRect(323, 5, 58, 35))
        self.tb_shortcycle_3.setFont(font2)
        self.tb_shortcycle_3.setCheckable(False)
        self.tb_shortcycle_3.setAutoExclusive(True)
        self.tb_shortcycle_3.setAutoRaise(False)
        self.label_64 = QLabel(self.frame_42)
        self.label_64.setObjectName("label_64")
        self.label_64.setGeometry(QRect(5, 5, 313, 29))
        self.label_64.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_64.setWordWrap(True)
        self.label_short_cycle_led_3 = QLabel(self.frame_42)
        self.label_short_cycle_led_3.setObjectName("label_short_cycle_led_3")
        self.label_short_cycle_led_3.setGeometry(QRect(392, 8, 58, 29))
        self.label_short_cycle_led_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.stackStartEndUI)
        self.stackDataUI = QWidget()
        self.stackDataUI.setObjectName("stackDataUI")
        self.frame_20 = QFrame(self.stackDataUI)
        self.frame_20.setObjectName("frame_20")
        self.frame_20.setGeometry(QRect(850, 10, 91, 510))
        self.frame_20.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName("frame_24")
        self.frame_24.setGeometry(QRect(0, 0, 91, 167))
        self.frame_24.setFrameShape(QFrame.Shape.Panel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget = QWidget(self.frame_24)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 91, 167))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        # ifndef Q_OS_MAC
        self.verticalLayout.setSpacing(-1)
        # endif
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(5, 29, 5, 29)
        self.label_93 = QLabel(self.verticalLayoutWidget)
        self.label_93.setObjectName("label_93")
        font5 = QFont()
        font5.setPointSize(17)
        self.label_93.setFont(font5)
        self.label_93.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.verticalLayout.addWidget(self.label_93)

        self.le_hx = QLineEdit(self.verticalLayoutWidget)
        self.le_hx.setObjectName("le_hx")
        self.le_hx.setFont(font2)
        self.le_hx.setStyleSheet(
            "QLineEdit#le_hx {color: black; background-color: rgb(255, 246, 131);}\n\n\n\n"
        )
        self.le_hx.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_hx)

        self.label_91 = QLabel(self.verticalLayoutWidget)
        self.label_91.setObjectName("label_91")
        self.label_91.setFont(font5)
        self.label_91.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.verticalLayout.addWidget(self.label_91)

        self.le_ey = QLineEdit(self.verticalLayoutWidget)
        self.le_ey.setObjectName("le_ey")
        self.le_ey.setEnabled(True)
        self.le_ey.setStyleSheet(
            "QLineEdit#le_ey {color: black; background-color: rgb(255, 246, 131);}\n\n\n\n"
        )
        self.le_ey.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_ey)

        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName("frame_25")
        self.frame_25.setGeometry(QRect(0, 172, 91, 167))
        self.frame_25.setFrameShape(QFrame.Shape.Panel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_25)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 91, 167))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        # ifndef Q_OS_MAC
        self.verticalLayout_2.setSpacing(-1)
        # endif
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 29, 5, 29)
        self.label_96 = QLabel(self.verticalLayoutWidget_2)
        self.label_96.setObjectName("label_96")
        self.label_96.setFont(font5)
        self.label_96.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.verticalLayout_2.addWidget(self.label_96)

        self.le_hy = QLineEdit(self.verticalLayoutWidget_2)
        self.le_hy.setObjectName("le_hy")
        self.le_hy.setFont(font2)
        self.le_hy.setStyleSheet(
            "QLineEdit#le_hy {color: black; background-color: rgb(255, 246, 131);}\n\n\n\n"
        )
        self.le_hy.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.le_hy)

        self.label_92 = QLabel(self.verticalLayoutWidget_2)
        self.label_92.setObjectName("label_92")
        self.label_92.setFont(font5)
        self.label_92.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.verticalLayout_2.addWidget(self.label_92)

        self.le_ex = QLineEdit(self.verticalLayoutWidget_2)
        self.le_ex.setObjectName("le_ex")
        self.le_ex.setEnabled(True)
        self.le_ex.setStyleSheet(
            "QLineEdit#le_ex {color: black; background-color: rgb(255, 246, 131);}\n\n\n\n"
        )
        self.le_ex.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.le_ex)

        self.frame_26 = QFrame(self.frame_20)
        self.frame_26.setObjectName("frame_26")
        self.frame_26.setGeometry(QRect(0, 344, 91, 166))
        self.frame_26.setFrameShape(QFrame.Shape.Panel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.frame_26)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 91, 167))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        # ifndef Q_OS_MAC
        self.verticalLayout_3.setSpacing(-1)
        # endif
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 58, 5, 60)
        self.label_97 = QLabel(self.verticalLayoutWidget_3)
        self.label_97.setObjectName("label_97")
        self.label_97.setFont(font5)
        self.label_97.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.verticalLayout_3.addWidget(self.label_97)

        self.le_hz = QLineEdit(self.verticalLayoutWidget_3)
        self.le_hz.setObjectName("le_hz")
        self.le_hz.setFont(font2)
        self.le_hz.setStyleSheet(
            "QLineEdit#le_hz {color: black; background-color: rgb(255, 246, 131);}\n\n\n\n"
        )
        self.le_hz.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.le_hz)

        self.frame_21 = QFrame(self.stackDataUI)
        self.frame_21.setObjectName("frame_21")
        self.frame_21.setGeometry(QRect(310, 10, 539, 510))
        self.frame_21.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_27 = QFrame(self.frame_21)
        self.frame_27.setObjectName("frame_27")
        self.frame_27.setGeometry(QRect(5, 0, 531, 167))
        self.frame_27.setFrameShape(QFrame.Shape.Panel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.f_hx = QFrame(self.frame_27)
        self.f_hx.setObjectName("f_hx")
        self.f_hx.setGeometry(QRect(5, 5, 20, 157))
        font6 = QFont()
        font6.setPointSize(13)
        font6.setBold(False)
        self.f_hx.setFont(font6)
        self.f_hx.setFrameShape(QFrame.Shape.NoFrame)
        self.f_hx.setFrameShadow(QFrame.Shadow.Raised)
        self.horlayout_hx_label = QHBoxLayout(self.f_hx)
        self.horlayout_hx_label.setObjectName("horlayout_hx_label")
        self.horlayout_hx_label.setContentsMargins(0, 0, 0, 0)
        self.f_ey = QFrame(self.frame_27)
        self.f_ey.setObjectName("f_ey")
        self.f_ey.setGeometry(QRect(506, 5, 20, 157))
        self.f_ey.setFrameShape(QFrame.Shape.NoFrame)
        self.f_ey.setFrameShadow(QFrame.Shadow.Raised)
        self.horlayout_ey_label = QHBoxLayout(self.f_ey)
        self.horlayout_ey_label.setObjectName("horlayout_ey_label")
        self.horlayout_ey_label.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_27)
        self.frame_43.setObjectName("frame_43")
        self.frame_43.setGeometry(QRect(30, 5, 471, 157))
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.f_hx_ey_graph = QFrame(self.frame_43)
        self.f_hx_ey_graph.setObjectName("f_hx_ey_graph")
        self.f_hx_ey_graph.setGeometry(QRect(-15, -15, 500, 225))
        self.f_hx_ey_graph.setFrameShape(QFrame.Shape.NoFrame)
        self.f_hx_ey_graph.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_hx_ey = QHBoxLayout(self.f_hx_ey_graph)
        self.layout_hx_ey.setObjectName("layout_hx_ey")
        self.layout_hx_ey.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_21)
        self.frame_28.setObjectName("frame_28")
        self.frame_28.setGeometry(QRect(5, 172, 531, 167))
        self.frame_28.setFrameShape(QFrame.Shape.Panel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.f_hy = QFrame(self.frame_28)
        self.f_hy.setObjectName("f_hy")
        self.f_hy.setGeometry(QRect(5, 5, 20, 157))
        self.f_hy.setToolTipDuration(-6)
        self.f_hy.setFrameShape(QFrame.Shape.NoFrame)
        self.f_hy.setFrameShadow(QFrame.Shadow.Raised)
        self.horlayout_hy_label = QHBoxLayout(self.f_hy)
        self.horlayout_hy_label.setObjectName("horlayout_hy_label")
        self.horlayout_hy_label.setContentsMargins(0, 0, 0, 0)
        self.f_ex = QFrame(self.frame_28)
        self.f_ex.setObjectName("f_ex")
        self.f_ex.setGeometry(QRect(506, 5, 20, 157))
        self.f_ex.setFrameShape(QFrame.Shape.NoFrame)
        self.f_ex.setFrameShadow(QFrame.Shadow.Raised)
        self.horlayout_ex_label = QHBoxLayout(self.f_ex)
        self.horlayout_ex_label.setObjectName("horlayout_ex_label")
        self.horlayout_ex_label.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_28)
        self.frame_44.setObjectName("frame_44")
        self.frame_44.setGeometry(QRect(30, 5, 471, 157))
        self.frame_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.f_hy_ex_graph = QFrame(self.frame_44)
        self.f_hy_ex_graph.setObjectName("f_hy_ex_graph")
        self.f_hy_ex_graph.setGeometry(QRect(-15, -15, 500, 225))
        self.f_hy_ex_graph.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_hy_ex_graph.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_hy_ex = QHBoxLayout(self.f_hy_ex_graph)
        self.layout_hy_ex.setObjectName("layout_hy_ex")
        self.layout_hy_ex.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_21)
        self.frame_29.setObjectName("frame_29")
        self.frame_29.setGeometry(QRect(5, 344, 531, 166))
        self.frame_29.setFrameShape(QFrame.Shape.Panel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.f_hz = QFrame(self.frame_29)
        self.f_hz.setObjectName("f_hz")
        self.f_hz.setGeometry(QRect(5, 5, 20, 157))
        self.f_hz.setFrameShape(QFrame.Shape.NoFrame)
        self.f_hz.setFrameShadow(QFrame.Shadow.Raised)
        self.horlayout_hz_label = QHBoxLayout(self.f_hz)
        self.horlayout_hz_label.setObjectName("horlayout_hz_label")
        self.horlayout_hz_label.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_29)
        self.frame_45.setObjectName("frame_45")
        self.frame_45.setGeometry(QRect(30, 5, 471, 157))
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.f_hz_graph = QFrame(self.frame_45)
        self.f_hz_graph.setObjectName("f_hz_graph")
        self.f_hz_graph.setGeometry(QRect(-15, -15, 500, 200))
        self.f_hz_graph.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_hz_graph.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_hz = QHBoxLayout(self.f_hz_graph)
        self.layout_hz.setObjectName("layout_hz")
        self.layout_hz.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.stackDataUI)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setGeometry(QRect(10, 10, 299, 510))
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_22 = QFrame(self.frame_5)
        self.frame_22.setObjectName("frame_22")
        self.frame_22.setGeometry(QRect(0, 0, 299, 339))
        self.frame_22.setFrameShape(QFrame.Shape.Panel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.label_95 = QLabel(self.frame_22)
        self.label_95.setObjectName("label_95")
        self.label_95.setGeometry(QRect(5, 5, 291, 170))
        self.label_95.setWordWrap(True)
        self.line = QFrame(self.frame_22)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(5, 180, 289, 3))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_gain_xlyl_led = QLabel(self.frame_22)
        self.label_gain_xlyl_led.setObjectName("label_gain_xlyl_led")
        self.label_gain_xlyl_led.setGeometry(QRect(84, 195, 61, 61))
        self.label_gain_xlyl_led.setFrameShape(QFrame.Shape.NoFrame)
        self.tb_gain_xlyl = QToolButton(self.frame_22)
        self.tb_gain_xlyl.setObjectName("tb_gain_xlyl")
        self.tb_gain_xlyl.setGeometry(QRect(5, 195, 74, 61))
        self.tb_gain_xlyl.setFont(font2)
        self.tb_gain_xlyl.setCheckable(False)
        self.tb_gain_xlyl.setAutoExclusive(True)
        self.tb_gain_xlyl.setAutoRaise(False)
        self.tb_gain_xhyl = QToolButton(self.frame_22)
        self.tb_gain_xhyl.setObjectName("tb_gain_xhyl")
        self.tb_gain_xhyl.setGeometry(QRect(5, 266, 74, 61))
        self.tb_gain_xhyl.setFont(font2)
        self.tb_gain_xhyl.setCheckable(False)
        self.tb_gain_xhyl.setAutoExclusive(True)
        self.tb_gain_xhyl.setAutoRaise(False)
        self.label_gain_xhyl_led = QLabel(self.frame_22)
        self.label_gain_xhyl_led.setObjectName("label_gain_xhyl_led")
        self.label_gain_xhyl_led.setGeometry(QRect(84, 266, 61, 61))
        self.label_gain_xhyl_led.setFrameShape(QFrame.Shape.NoFrame)
        self.tb_gain_xlyh = QToolButton(self.frame_22)
        self.tb_gain_xlyh.setObjectName("tb_gain_xlyh")
        self.tb_gain_xlyh.setGeometry(QRect(155, 195, 73, 61))
        self.tb_gain_xlyh.setFont(font2)
        self.tb_gain_xlyh.setCheckable(False)
        self.tb_gain_xlyh.setAutoExclusive(True)
        self.tb_gain_xlyh.setAutoRaise(False)
        self.label_gain_xlyh_led = QLabel(self.frame_22)
        self.label_gain_xlyh_led.setObjectName("label_gain_xlyh_led")
        self.label_gain_xlyh_led.setGeometry(QRect(233, 195, 61, 61))
        self.label_gain_xlyh_led.setFrameShape(QFrame.Shape.NoFrame)
        self.tb_gain_xhyh = QToolButton(self.frame_22)
        self.tb_gain_xhyh.setObjectName("tb_gain_xhyh")
        self.tb_gain_xhyh.setGeometry(QRect(155, 266, 73, 61))
        self.tb_gain_xhyh.setFont(font2)
        self.tb_gain_xhyh.setCheckable(False)
        self.tb_gain_xhyh.setAutoExclusive(True)
        self.tb_gain_xhyh.setAutoRaise(False)
        self.label_gain_xhyh_led = QLabel(self.frame_22)
        self.label_gain_xhyh_led.setObjectName("label_gain_xhyh_led")
        self.label_gain_xhyh_led.setGeometry(QRect(233, 266, 61, 61))
        self.label_gain_xhyh_led.setFrameShape(QFrame.Shape.NoFrame)
        self.line_2 = QFrame(self.frame_22)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(149, 195, 3, 132))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_23 = QFrame(self.frame_5)
        self.frame_23.setObjectName("frame_23")
        self.frame_23.setGeometry(QRect(0, 344, 299, 166))
        self.frame_23.setFrameShape(QFrame.Shape.Panel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.tb_mag_light = QToolButton(self.frame_23)
        self.tb_mag_light.setObjectName("tb_mag_light")
        self.tb_mag_light.setGeometry(QRect(10, 10, 279, 68))
        self.tb_mag_light.setFont(font2)
        self.tb_mag_light.setStyleSheet("")
        self.tb_mag_light.setCheckable(True)
        self.tb_mag_light.setAutoExclusive(False)
        self.tb_mag_light.setAutoRaise(False)
        self.tb_nims_leds = QToolButton(self.frame_23)
        self.tb_nims_leds.setObjectName("tb_nims_leds")
        self.tb_nims_leds.setGeometry(QRect(10, 88, 279, 68))
        self.tb_nims_leds.setFont(font2)
        self.tb_nims_leds.setCheckable(False)
        self.tb_nims_leds.setAutoExclusive(True)
        self.tb_nims_leds.setAutoRaise(False)
        self.stackedWidget.addWidget(self.stackDataUI)
        self.stackMetadataUI = QWidget()
        self.stackMetadataUI.setObjectName("stackMetadataUI")
        self.line_10 = QFrame(self.stackMetadataUI)
        self.line_10.setObjectName("line_10")
        self.line_10.setGeometry(QRect(5, 43, 940, 16))
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_56 = QLabel(self.stackMetadataUI)
        self.label_56.setObjectName("label_56")
        self.label_56.setGeometry(QRect(0, 0, 950, 25))
        self.label_56.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.label_56.setMargin(0)
        self.label_56.setIndent(-1)
        self.label_57 = QLabel(self.stackMetadataUI)
        self.label_57.setObjectName("label_57")
        self.label_57.setGeometry(QRect(0, 23, 950, 25))
        self.frame_2 = QFrame(self.stackMetadataUI)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setGeometry(QRect(5, 60, 240, 272))
        self.frame_2.setFrameShape(QFrame.Shape.Panel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(1)
        self.label_38 = QLabel(self.frame_2)
        self.label_38.setObjectName("label_38")
        self.label_38.setGeometry(QRect(52, 240, 50, 21))
        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName("label_40")
        self.label_40.setGeometry(QRect(36, 85, 66, 21))
        self.label_43 = QLabel(self.frame_2)
        self.label_43.setObjectName("label_43")
        self.label_43.setEnabled(True)
        self.label_43.setGeometry(QRect(49, 209, 53, 21))
        self.label_37 = QLabel(self.frame_2)
        self.label_37.setObjectName("label_37")
        self.label_37.setGeometry(QRect(10, 116, 100, 21))
        self.le_run_id = QLineEdit(self.frame_2)
        self.le_run_id.setObjectName("le_run_id")
        self.le_run_id.setGeometry(QRect(110, 54, 119, 21))
        self.le_run_id.setFont(font2)
        self.le_operator = QLineEdit(self.frame_2)
        self.le_operator.setObjectName("le_operator")
        self.le_operator.setGeometry(QRect(110, 178, 119, 21))
        self.label_42 = QLabel(self.frame_2)
        self.label_42.setObjectName("label_42")
        self.label_42.setGeometry(QRect(49, 147, 53, 21))
        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName("label_39")
        self.label_39.setGeometry(QRect(58, 54, 44, 21))
        self.le_site_name = QLineEdit(self.frame_2)
        self.le_site_name.setObjectName("le_site_name")
        self.le_site_name.setEnabled(True)
        self.le_site_name.setGeometry(QRect(110, 85, 119, 21))
        self.le_nims_id = QLineEdit(self.frame_2)
        self.le_nims_id.setObjectName("le_nims_id")
        self.le_nims_id.setGeometry(QRect(110, 209, 119, 21))
        self.label_41 = QLabel(self.frame_2)
        self.label_41.setObjectName("label_41")
        self.label_41.setGeometry(QRect(44, 178, 58, 21))
        self.le_country = QLineEdit(self.frame_2)
        self.le_country.setObjectName("le_country")
        self.le_country.setGeometry(QRect(110, 147, 119, 21))
        self.le_state_province = QLineEdit(self.frame_2)
        self.le_state_province.setObjectName("le_state_province")
        self.le_state_province.setGeometry(QRect(110, 116, 119, 21))
        self.le_mag_id = QLineEdit(self.frame_2)
        self.le_mag_id.setObjectName("le_mag_id")
        self.le_mag_id.setGeometry(QRect(110, 240, 119, 21))
        self.le_filename = QLineEdit(self.frame_2)
        self.le_filename.setObjectName("le_filename")
        self.le_filename.setEnabled(False)
        self.le_filename.setGeometry(QRect(110, 23, 119, 21))
        self.le_filename.setFont(font2)
        self.le_filename.setStyleSheet(
            "QLineEdit#le_filename {color: black; background-color: rgb(104, 104, 104);}\n"
        )
        self.label_58 = QLabel(self.frame_2)
        self.label_58.setObjectName("label_58")
        self.label_58.setEnabled(True)
        self.label_58.setGeometry(QRect(36, 23, 66, 21))
        self.label = QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 5, 240, 16))
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_6 = QFrame(self.stackMetadataUI)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setGeometry(QRect(252, 60, 450, 272))
        self.frame_6.setFrameShape(QFrame.Shape.Panel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_45 = QLabel(self.frame_6)
        self.label_45.setObjectName("label_45")
        self.label_45.setGeometry(QRect(0, 5, 450, 21))
        self.label_45.setFont(font1)
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName("frame_7")
        self.frame_7.setGeometry(QRect(5, 25, 217, 80))
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Plain)
        self.label_49 = QLabel(self.frame_7)
        self.label_49.setObjectName("label_49")
        self.label_49.setGeometry(QRect(0, 0, 217, 16))
        font7 = QFont()
        font7.setPointSize(14)
        font7.setUnderline(True)
        self.label_49.setFont(font7)
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayoutWidget_2 = QWidget(self.frame_7)
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 20, 201, 54))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.formLayoutWidget_2)
        self.label_52.setObjectName("label_52")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_52)

        self.le_ns_dipole_length = QLineEdit(self.formLayoutWidget_2)
        self.le_ns_dipole_length.setObjectName("le_ns_dipole_length")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_ns_dipole_length)

        self.label_53 = QLabel(self.formLayoutWidget_2)
        self.label_53.setObjectName("label_53")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_53)

        self.le_ns_dipole_heading = QLineEdit(self.formLayoutWidget_2)
        self.le_ns_dipole_heading.setObjectName("le_ns_dipole_heading")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_ns_dipole_heading)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName("frame_8")
        self.frame_8.setGeometry(QRect(5, 105, 191, 161))
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayoutWidget = QWidget(self.frame_8)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 171, 147))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.formLayoutWidget)
        self.label_55.setObjectName("label_55")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_55)

        self.le_n_electrode_id = QLineEdit(self.formLayoutWidget)
        self.le_n_electrode_id.setObjectName("le_n_electrode_id")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_n_electrode_id)

        self.label_50 = QLabel(self.formLayoutWidget)
        self.label_50.setObjectName("label_50")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_50)

        self.le_s_electrode_id = QLineEdit(self.formLayoutWidget)
        self.le_s_electrode_id.setObjectName("le_s_electrode_id")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_s_electrode_id)

        self.label_44 = QLabel(self.formLayoutWidget)
        self.label_44.setObjectName("label_44")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_44)

        self.le_e_electrode_id = QLineEdit(self.formLayoutWidget)
        self.le_e_electrode_id.setObjectName("le_e_electrode_id")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_e_electrode_id)

        self.label_54 = QLabel(self.formLayoutWidget)
        self.label_54.setObjectName("label_54")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_54)

        self.le_w_electrode_id = QLineEdit(self.formLayoutWidget)
        self.le_w_electrode_id.setObjectName("le_w_electrode_id")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_w_electrode_id)

        self.label_51 = QLabel(self.formLayoutWidget)
        self.label_51.setObjectName("label_51")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_51)

        self.le_gnd_electrode_id = QLineEdit(self.formLayoutWidget)
        self.le_gnd_electrode_id.setObjectName("le_gnd_electrode_id")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_gnd_electrode_id)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName("frame_9")
        self.frame_9.setGeometry(QRect(227, 25, 217, 80))
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_46 = QLabel(self.frame_9)
        self.label_46.setObjectName("label_46")
        self.label_46.setGeometry(QRect(0, 0, 217, 16))
        self.label_46.setFont(font7)
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayoutWidget_3 = QWidget(self.frame_9)
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(9, 19, 201, 54))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.formLayoutWidget_3)
        self.label_47.setObjectName("label_47")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_47)

        self.le_ew_dipole_length = QLineEdit(self.formLayoutWidget_3)
        self.le_ew_dipole_length.setObjectName("le_ew_dipole_length")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.le_ew_dipole_length)

        self.label_48 = QLabel(self.formLayoutWidget_3)
        self.label_48.setObjectName("label_48")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_48)

        self.le_ew_dipole_heading = QLineEdit(self.formLayoutWidget_3)
        self.le_ew_dipole_heading.setObjectName("le_ew_dipole_heading")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.le_ew_dipole_heading)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName("frame_10")
        self.frame_10.setEnabled(False)
        self.frame_10.setGeometry(QRect(201, 105, 244, 161))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.label_94 = QLabel(self.frame_10)
        self.label_94.setObjectName("label_94")
        self.label_94.setGeometry(QRect(0, 0, 244, 16))
        self.label_94.setFont(font7)
        self.label_94.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.frame_10)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 20, 231, 21))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.rb_x_layout = QRadioButton(self.horizontalLayoutWidget)
        self.rb_x_layout.setObjectName("rb_x_layout")
        self.rb_x_layout.setChecked(True)

        self.horizontalLayout.addWidget(self.rb_x_layout)

        self.rb_l_layout = QRadioButton(self.horizontalLayoutWidget)
        self.rb_l_layout.setObjectName("rb_l_layout")

        self.horizontalLayout.addWidget(self.rb_l_layout)

        self.rb_t_layout = QRadioButton(self.horizontalLayoutWidget)
        self.rb_t_layout.setObjectName("rb_t_layout")

        self.horizontalLayout.addWidget(self.rb_t_layout)

        self.label_north = QLabel(self.frame_10)
        self.label_north.setObjectName("label_north")
        self.label_north.setGeometry(QRect(9, 53, 46, 101))
        self.label_north.setFrameShape(QFrame.Shape.NoFrame)
        self.le_survey = QLabel(self.frame_10)
        self.le_survey.setObjectName("le_survey")
        self.le_survey.setEnabled(False)
        self.le_survey.setGeometry(QRect(60, 50, 179, 106))
        self.le_survey.setStyleSheet(
            "QLabel#le_survey {color: black; background-color: rgb(104, 104, 104);}\n\n\n"
        )
        self.le_survey.setFrameShape(QFrame.Shape.NoFrame)
        self.le_survey.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4 = QFrame(self.stackMetadataUI)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setGeometry(QRect(707, 337, 238, 186))
        self.frame_4.setFrameShape(QFrame.Shape.Panel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayoutWidget_4 = QWidget(self.frame_4)
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(9, 29, 221, 158))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.formLayout_4.setVerticalSpacing(-1)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.formLayoutWidget_4)
        self.label_34.setObjectName("label_34")
        font8 = QFont()
        font8.setBold(False)
        self.label_34.setFont(font8)
        self.label_34.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.label_34.setWordWrap(True)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_34)

        self.le_gps_time = QLineEdit(self.formLayoutWidget_4)
        self.le_gps_time.setObjectName("le_gps_time")
        self.le_gps_time.setFont(font2)
        self.le_gps_time.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_gps_time.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.le_gps_time.setStyleSheet(
            "QLineEdit#le_gps_time {color: black; background-color: rgb(255, 246, 131);}\n\n\n\n"
        )
        self.le_gps_time.setReadOnly(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.le_gps_time)

        self.label_33 = QLabel(self.formLayoutWidget_4)
        self.label_33.setObjectName("label_33")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_33)

        self.le_gps_date = QLineEdit(self.formLayoutWidget_4)
        self.le_gps_date.setObjectName("le_gps_date")
        self.le_gps_date.setMinimumSize(QSize(0, 0))
        self.le_gps_date.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_gps_date.setStyleSheet(
            "QLineEdit#le_gps_date {color: black; background-color: rgb(255, 246, 131);}"
        )
        self.le_gps_date.setDragEnabled(True)
        self.le_gps_date.setReadOnly(False)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.le_gps_date)

        self.label_35 = QLabel(self.formLayoutWidget_4)
        self.label_35.setObjectName("label_35")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_35)

        self.le_gps_lat = QLineEdit(self.formLayoutWidget_4)
        self.le_gps_lat.setObjectName("le_gps_lat")
        self.le_gps_lat.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_gps_lat.setStyleSheet(
            "QLineEdit#le_gps_lat {color: black; background-color: rgb(255, 246, 131);}\n"
        )

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.le_gps_lat)

        self.label_36 = QLabel(self.formLayoutWidget_4)
        self.label_36.setObjectName("label_36")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_36)

        self.le_gps_lon = QLineEdit(self.formLayoutWidget_4)
        self.le_gps_lon.setObjectName("le_gps_lon")
        self.le_gps_lon.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_gps_lon.setStyleSheet(
            "QLineEdit#le_gps_lon {color: black; background-color: rgb(255, 246, 131);}"
        )

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.le_gps_lon)

        self.label_32 = QLabel(self.formLayoutWidget_4)
        self.label_32.setObjectName("label_32")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_32)

        self.le_gps_alt = QLineEdit(self.formLayoutWidget_4)
        self.le_gps_alt.setObjectName("le_gps_alt")
        self.le_gps_alt.setEnabled(True)
        self.le_gps_alt.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_gps_alt.setStyleSheet(
            "\nQLineEdit#le_gps_alt {color: black; background-color: rgb(255, 246, 131);}"
        )
        self.le_gps_alt.setFrame(True)
        self.le_gps_alt.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.le_gps_alt)

        self.label_59 = QLabel(self.frame_4)
        self.label_59.setObjectName("label_59")
        self.label_59.setGeometry(QRect(0, 5, 238, 21))
        self.label_59.setFont(font1)
        self.label_59.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_11 = QFrame(self.stackMetadataUI)
        self.frame_11.setObjectName("frame_11")
        self.frame_11.setGeometry(QRect(5, 337, 240, 186))
        self.frame_11.setFrameShape(QFrame.Shape.Panel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.te_comments = QTextEdit(self.frame_11)
        self.te_comments.setObjectName("te_comments")
        self.te_comments.setGeometry(QRect(5, 25, 230, 156))
        self.l_comments_md = QLabel(self.frame_11)
        self.l_comments_md.setObjectName("l_comments_md")
        self.l_comments_md.setGeometry(QRect(0, 5, 240, 16))
        self.l_comments_md.setFont(font1)
        self.l_comments_md.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_12 = QFrame(self.stackMetadataUI)
        self.frame_12.setObjectName("frame_12")
        self.frame_12.setGeometry(QRect(707, 60, 238, 272))
        self.frame_12.setFrameShape(QFrame.Shape.Panel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.label_60 = QLabel(self.frame_12)
        self.label_60.setObjectName("label_60")
        self.label_60.setGeometry(QRect(0, 5, 238, 21))
        self.label_60.setFont(font1)
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.le_gps_status_byte_m = QLineEdit(self.frame_12)
        self.le_gps_status_byte_m.setObjectName("le_gps_status_byte_m")
        self.le_gps_status_byte_m.setGeometry(QRect(160, 240, 71, 21))
        self.le_gps_status_byte_m.setFont(font2)
        self.le_gps_status_byte_m.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_gps_status_byte_m.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.le_gps_status_byte_m.setStyleSheet(
            "QLineEdit#le_gps_status_byte_m {color: black; background-color: rgb(255, 246, 131);}\n"
            "\n"
            "\n"
            "\n"
            ""
        )
        self.le_gps_status_byte_m.setReadOnly(True)
        self.label_61 = QLabel(self.frame_12)
        self.label_61.setObjectName("label_61")
        self.label_61.setGeometry(QRect(40, 240, 111, 21))
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName("frame_14")
        self.frame_14.setGeometry(QRect(5, 40, 228, 61))
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.tb_shortcycle = QToolButton(self.frame_14)
        self.tb_shortcycle.setObjectName("tb_shortcycle")
        self.tb_shortcycle.setGeometry(QRect(0, 0, 141, 61))
        self.tb_shortcycle.setCheckable(False)
        self.tb_shortcycle.setAutoExclusive(True)
        self.tb_shortcycle.setAutoRaise(False)
        self.label_short_cycle_led = QLabel(self.frame_14)
        self.label_short_cycle_led.setObjectName("label_short_cycle_led")
        self.label_short_cycle_led.setGeometry(QRect(155, 0, 61, 61))
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName("frame_15")
        self.frame_15.setGeometry(QRect(5, 120, 228, 61))
        self.tb_almanac = QToolButton(self.frame_15)
        self.tb_almanac.setObjectName("tb_almanac")
        self.tb_almanac.setGeometry(QRect(0, 0, 141, 61))
        self.tb_almanac.setCheckable(False)
        self.tb_almanac.setAutoExclusive(True)
        self.tb_almanac.setAutoRaise(False)
        self.label_almanac_led = QLabel(self.frame_15)
        self.label_almanac_led.setObjectName("label_almanac_led")
        self.label_almanac_led.setGeometry(QRect(155, 0, 61, 61))
        self.frame_13 = QFrame(self.stackMetadataUI)
        self.frame_13.setObjectName("frame_13")
        self.frame_13.setGeometry(QRect(252, 337, 450, 186))
        self.frame_13.setFrameShape(QFrame.Shape.Panel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.te_gps_metadata_string = QTextEdit(self.frame_13)
        self.te_gps_metadata_string.setObjectName("te_gps_metadata_string")
        self.te_gps_metadata_string.setGeometry(QRect(5, 20, 440, 41))
        self.te_gps_metadata_string.setStyleSheet(
            "QTextEdit#te_gps_metadata_string {color: black; background-color: rgb(255, 246, 131);}\\n\\n\\n\\n"
        )
        self.te_gps_metadata_string.setReadOnly(True)
        self.te_gps_string_m = QTextEdit(self.frame_13)
        self.te_gps_string_m.setObjectName("te_gps_string_m")
        self.te_gps_string_m.setGeometry(QRect(5, 88, 440, 91))
        self.te_gps_string_m.setStyleSheet(
            "QTextEdit#te_gps_string_m {color: black; background-color: rgb(255, 246, 131);}\\n\\n\\n\\n"
        )
        self.te_gps_string_m.setReadOnly(True)
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(0, 5, 450, 16))
        font9 = QFont()
        font9.setPointSize(14)
        font9.setBold(False)
        self.label_8.setFont(font9)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(0, 70, 450, 16))
        self.label_9.setFont(font9)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.stackMetadataUI)
        self.stackSiteReportUI = QWidget()
        self.stackSiteReportUI.setObjectName("stackSiteReportUI")
        self.frame_47 = QFrame(self.stackSiteReportUI)
        self.frame_47.setObjectName("frame_47")
        self.frame_47.setGeometry(QRect(20, 40, 911, 61))
        self.frame_47.setFrameShape(QFrame.Shape.Panel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_47)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_14 = QFormLayout()
        self.formLayout_14.setObjectName("formLayout_14")
        self.label_123 = QLabel(self.frame_47)
        self.label_123.setObjectName("label_123")

        self.formLayout_14.setWidget(0, QFormLayout.LabelRole, self.label_123)

        self.le_run_id_sr = QLineEdit(self.frame_47)
        self.le_run_id_sr.setObjectName("le_run_id_sr")
        self.le_run_id_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_14.setWidget(0, QFormLayout.FieldRole, self.le_run_id_sr)

        self.horizontalLayout_3.addLayout(self.formLayout_14)

        self.formLayout_15 = QFormLayout()
        self.formLayout_15.setObjectName("formLayout_15")
        self.label_124 = QLabel(self.frame_47)
        self.label_124.setObjectName("label_124")

        self.formLayout_15.setWidget(0, QFormLayout.LabelRole, self.label_124)

        self.le_site_name_sr = QLineEdit(self.frame_47)
        self.le_site_name_sr.setObjectName("le_site_name_sr")
        self.le_site_name_sr.setMinimumSize(QSize(204, 21))

        self.formLayout_15.setWidget(0, QFormLayout.FieldRole, self.le_site_name_sr)

        self.horizontalLayout_3.addLayout(self.formLayout_15)

        self.formLayout_16 = QFormLayout()
        self.formLayout_16.setObjectName("formLayout_16")
        self.label_125 = QLabel(self.frame_47)
        self.label_125.setObjectName("label_125")

        self.formLayout_16.setWidget(0, QFormLayout.LabelRole, self.label_125)

        self.le_state_province_sr = QLineEdit(self.frame_47)
        self.le_state_province_sr.setObjectName("le_state_province_sr")
        self.le_state_province_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_16.setWidget(0, QFormLayout.FieldRole, self.le_state_province_sr)

        self.horizontalLayout_3.addLayout(self.formLayout_16)

        self.formLayout_20 = QFormLayout()
        self.formLayout_20.setObjectName("formLayout_20")
        self.label_127 = QLabel(self.frame_47)
        self.label_127.setObjectName("label_127")

        self.formLayout_20.setWidget(0, QFormLayout.LabelRole, self.label_127)

        self.le_country_sr = QLineEdit(self.frame_47)
        self.le_country_sr.setObjectName("le_country_sr")
        self.le_country_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_20.setWidget(0, QFormLayout.FieldRole, self.le_country_sr)

        self.horizontalLayout_3.addLayout(self.formLayout_20)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.formLayout_13 = QFormLayout()
        self.formLayout_13.setObjectName("formLayout_13")
        self.formLayout_13.setHorizontalSpacing(8)
        self.formLayout_13.setVerticalSpacing(-1)
        self.formLayout_13.setContentsMargins(0, -1, -1, -1)
        self.label_122 = QLabel(self.frame_47)
        self.label_122.setObjectName("label_122")
        self.label_122.setMinimumSize(QSize(41, 0))

        self.formLayout_13.setWidget(0, QFormLayout.LabelRole, self.label_122)

        self.le_crew = QLineEdit(self.frame_47)
        self.le_crew.setObjectName("le_crew")
        self.le_crew.setMinimumSize(QSize(836, 21))

        self.formLayout_13.setWidget(0, QFormLayout.FieldRole, self.le_crew)

        self.verticalLayout_5.addLayout(self.formLayout_13)

        self.label_6 = QLabel(self.stackSiteReportUI)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(20, 420, 84, 16))
        self.label_6.setMaximumSize(QSize(16777215, 16))
        self.label_6.setFont(font4)
        self.frame_31 = QFrame(self.stackSiteReportUI)
        self.frame_31.setObjectName("frame_31")
        self.frame_31.setGeometry(QRect(190, 110, 175, 131))
        self.frame_31.setFrameShape(QFrame.Shape.Panel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_31)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, -1, -1)
        self.label_118 = QLabel(self.frame_31)
        self.label_118.setObjectName("label_118")
        font10 = QFont()
        font10.setPointSize(16)
        font10.setBold(False)
        self.label_118.setFont(font10)

        self.verticalLayout_17.addWidget(self.label_118)

        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.formLayout_10.setVerticalSpacing(5)
        self.label_115 = QLabel(self.frame_31)
        self.label_115.setObjectName("label_115")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label_115)

        self.label_116 = QLabel(self.frame_31)
        self.label_116.setObjectName("label_116")

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.label_116)

        self.label_117 = QLabel(self.frame_31)
        self.label_117.setObjectName("label_117")

        self.formLayout_10.setWidget(3, QFormLayout.LabelRole, self.label_117)

        self.label_113 = QLabel(self.frame_31)
        self.label_113.setObjectName("label_113")
        self.label_113.setFont(font8)
        self.label_113.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.label_113.setWordWrap(True)

        self.formLayout_10.setWidget(4, QFormLayout.LabelRole, self.label_113)

        self.le_gps_lat_sr = QLineEdit(self.frame_31)
        self.le_gps_lat_sr.setObjectName("le_gps_lat_sr")
        self.le_gps_lat_sr.setMinimumSize(QSize(50, 21))
        self.le_gps_lat_sr.setMaximumSize(QSize(16777215, 21))

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.le_gps_lat_sr)

        self.le_gps_lon_sr = QLineEdit(self.frame_31)
        self.le_gps_lon_sr.setObjectName("le_gps_lon_sr")
        self.le_gps_lon_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.le_gps_lon_sr)

        self.le_gps_alt_sr = QLineEdit(self.frame_31)
        self.le_gps_alt_sr.setObjectName("le_gps_alt_sr")
        self.le_gps_alt_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_10.setWidget(3, QFormLayout.FieldRole, self.le_gps_alt_sr)

        self.le_gps_dec_sr = QLineEdit(self.frame_31)
        self.le_gps_dec_sr.setObjectName("le_gps_dec_sr")
        self.le_gps_dec_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_10.setWidget(4, QFormLayout.FieldRole, self.le_gps_dec_sr)

        self.verticalLayout_17.addLayout(self.formLayout_10)

        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.frame_32 = QFrame(self.stackSiteReportUI)
        self.frame_32.setObjectName("frame_32")
        self.frame_32.setGeometry(QRect(20, 110, 168, 191))
        self.frame_32.setFrameShape(QFrame.Shape.Panel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_32)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_85 = QLabel(self.frame_32)
        self.label_85.setObjectName("label_85")
        self.label_85.setFont(font10)

        self.verticalLayout_9.addWidget(self.label_85)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.formLayout_5.setVerticalSpacing(5)
        self.label_71 = QLabel(self.frame_32)
        self.label_71.setObjectName("label_71")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_71)

        self.le_nims_id_sr = QLineEdit(self.frame_32)
        self.le_nims_id_sr.setObjectName("le_nims_id_sr")
        self.le_nims_id_sr.setMinimumSize(QSize(50, 21))
        self.le_nims_id_sr.setMaximumSize(QSize(16777215, 21))

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.le_nims_id_sr)

        self.label_12 = QLabel(self.frame_32)
        self.label_12.setObjectName("label_12")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.le_mag_id_sr = QLineEdit(self.frame_32)
        self.le_mag_id_sr.setObjectName("le_mag_id_sr")
        self.le_mag_id_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.le_mag_id_sr)

        self.label_72 = QLabel(self.frame_32)
        self.label_72.setObjectName("label_72")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_72)

        self.le_n_electrode_id_sr = QLineEdit(self.frame_32)
        self.le_n_electrode_id_sr.setObjectName("le_n_electrode_id_sr")
        self.le_n_electrode_id_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.le_n_electrode_id_sr)

        self.label_73 = QLabel(self.frame_32)
        self.label_73.setObjectName("label_73")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_73)

        self.le_s_electrode_id_sr = QLineEdit(self.frame_32)
        self.le_s_electrode_id_sr.setObjectName("le_s_electrode_id_sr")
        self.le_s_electrode_id_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.le_s_electrode_id_sr)

        self.label_74 = QLabel(self.frame_32)
        self.label_74.setObjectName("label_74")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_74)

        self.le_e_electrode_id_sr = QLineEdit(self.frame_32)
        self.le_e_electrode_id_sr.setObjectName("le_e_electrode_id_sr")
        self.le_e_electrode_id_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.le_e_electrode_id_sr)

        self.label_75 = QLabel(self.frame_32)
        self.label_75.setObjectName("label_75")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_75)

        self.le_w_electrode_id_sr = QLineEdit(self.frame_32)
        self.le_w_electrode_id_sr.setObjectName("le_w_electrode_id_sr")
        self.le_w_electrode_id_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.le_w_electrode_id_sr)

        self.verticalLayout_9.addLayout(self.formLayout_5)

        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.layoutWidget = QWidget(self.stackSiteReportUI)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 899, 32))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.cb_status = QComboBox(self.layoutWidget)
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.setObjectName("cb_status")

        self.horizontalLayout_9.addWidget(self.cb_status)

        self.frame_30 = QFrame(self.layoutWidget)
        self.frame_30.setObjectName("frame_30")
        self.frame_30.setMinimumSize(QSize(719, 0))
        self.frame_30.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Shadow.Plain)

        self.horizontalLayout_9.addWidget(self.frame_30)

        self.te_comments_sr = QTextEdit(self.stackSiteReportUI)
        self.te_comments_sr.setObjectName("te_comments_sr")
        self.te_comments_sr.setGeometry(QRect(110, 420, 821, 41))
        self.te_comments_sr.setMinimumSize(QSize(330, 0))
        self.te_comments_sr.setMaximumSize(QSize(16777215, 16777215))
        self.frame_46 = QFrame(self.stackSiteReportUI)
        self.frame_46.setObjectName("frame_46")
        self.frame_46.setGeometry(QRect(508, 372, 84, 16))
        self.frame_46.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.tb_generate_report_sr = QToolButton(self.stackSiteReportUI)
        self.tb_generate_report_sr.setObjectName("tb_generate_report_sr")
        self.tb_generate_report_sr.setGeometry(QRect(599, 471, 271, 50))
        self.tb_generate_report_sr.setMinimumSize(QSize(220, 50))
        font11 = QFont()
        font11.setPointSize(24)
        font11.setBold(True)
        self.tb_generate_report_sr.setFont(font11)
        self.label_87 = QLabel(self.stackSiteReportUI)
        self.label_87.setObjectName("label_87")
        self.label_87.setGeometry(QRect(20, 471, 111, 19))
        self.label_87.setFont(font10)
        self.le_change_directory_sr = QLineEdit(self.stackSiteReportUI)
        self.le_change_directory_sr.setObjectName("le_change_directory_sr")
        self.le_change_directory_sr.setGeometry(QRect(142, 495, 449, 26))
        self.le_change_directory_sr.setMinimumSize(QSize(440, 21))
        self.le_change_directory_sr.setReadOnly(True)
        self.tb_change_directory_sr = QToolButton(self.stackSiteReportUI)
        self.tb_change_directory_sr.setObjectName("tb_change_directory_sr")
        self.tb_change_directory_sr.setGeometry(QRect(20, 495, 115, 26))
        self.tb_change_directory_sr.setMinimumSize(QSize(0, 20))
        font12 = QFont()
        font12.setPointSize(12)
        self.tb_change_directory_sr.setFont(font12)
        self.frame_33 = QFrame(self.stackSiteReportUI)
        self.frame_33.setObjectName("frame_33")
        self.frame_33.setGeometry(QRect(368, 110, 562, 301))
        self.frame_33.setFrameShape(QFrame.Shape.Panel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_33)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_86 = QLabel(self.frame_33)
        self.label_86.setObjectName("label_86")
        self.label_86.setFont(font10)

        self.verticalLayout_15.addWidget(self.label_86)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_84 = QLabel(self.frame_33)
        self.label_84.setObjectName("label_84")
        self.label_84.setMaximumSize(QSize(16777215, 17))
        self.label_84.setFont(font3)

        self.verticalLayout_7.addWidget(self.label_84)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_80 = QLabel(self.frame_33)
        self.label_80.setObjectName("label_80")
        font13 = QFont()
        font13.setUnderline(True)
        self.label_80.setFont(font13)

        self.verticalLayout_4.addWidget(self.label_80)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.formLayout_6.setContentsMargins(-1, -1, 4, -1)
        self.label_76 = QLabel(self.frame_33)
        self.label_76.setObjectName("label_76")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_76)

        self.le_pre_e_ns_r_sr = QLineEdit(self.frame_33)
        self.le_pre_e_ns_r_sr.setObjectName("le_pre_e_ns_r_sr")
        self.le_pre_e_ns_r_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.le_pre_e_ns_r_sr)

        self.label_77 = QLabel(self.frame_33)
        self.label_77.setObjectName("label_77")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_77)

        self.le_pre_e_sn_r_sr = QLineEdit(self.frame_33)
        self.le_pre_e_sn_r_sr.setObjectName("le_pre_e_sn_r_sr")
        self.le_pre_e_sn_r_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.le_pre_e_sn_r_sr)

        self.label_78 = QLabel(self.frame_33)
        self.label_78.setObjectName("label_78")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_78)

        self.le_pre_e_ew_r_sr = QLineEdit(self.frame_33)
        self.le_pre_e_ew_r_sr.setObjectName("le_pre_e_ew_r_sr")
        self.le_pre_e_ew_r_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.le_pre_e_ew_r_sr)

        self.label_79 = QLabel(self.frame_33)
        self.label_79.setObjectName("label_79")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_79)

        self.le_pre_e_we_r_sr = QLineEdit(self.frame_33)
        self.le_pre_e_we_r_sr.setObjectName("le_pre_e_we_r_sr")
        self.le_pre_e_we_r_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.le_pre_e_we_r_sr)

        self.verticalLayout_4.addLayout(self.formLayout_6)

        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.line_4 = QFrame(self.frame_33)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_81 = QLabel(self.frame_33)
        self.label_81.setObjectName("label_81")
        self.label_81.setMaximumSize(QSize(16777215, 16))
        self.label_81.setFont(font13)

        self.verticalLayout_6.addWidget(self.label_81)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.formLayout_7.setContentsMargins(-1, -1, 4, -1)
        self.label_82 = QLabel(self.frame_33)
        self.label_82.setObjectName("label_82")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_82)

        self.le_pre_e_ns_v_sr = QLineEdit(self.frame_33)
        self.le_pre_e_ns_v_sr.setObjectName("le_pre_e_ns_v_sr")
        self.le_pre_e_ns_v_sr.setMinimumSize(QSize(50, 21))

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.le_pre_e_ns_v_sr)

        self.label_83 = QLabel(self.frame_33)
        self.label_83.setObjectName("label_83")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_83)

        self.le_pre_e_ew_v_sr = QLineEdit(self.frame_33)
        self.le_pre_e_ew_v_sr.setObjectName("le_pre_e_ew_v_sr")
        self.le_pre_e_ew_v_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.le_pre_e_ew_v_sr)

        self.verticalLayout_6.addLayout(self.formLayout_7)

        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.horizontalLayout_6.addLayout(self.verticalLayout_7)

        self.line_5 = QFrame(self.frame_33)
        self.line_5.setObjectName("line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_5)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_104 = QLabel(self.frame_33)
        self.label_104.setObjectName("label_104")
        self.label_104.setFont(font3)

        self.verticalLayout_14.addWidget(self.label_104)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_89 = QLabel(self.frame_33)
        self.label_89.setObjectName("label_89")
        self.label_89.setFont(font13)

        self.verticalLayout_12.addWidget(self.label_89)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_88 = QLabel(self.frame_33)
        self.label_88.setObjectName("label_88")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_88)

        self.le_e_ns_r_sr = QLineEdit(self.frame_33)
        self.le_e_ns_r_sr.setObjectName("le_e_ns_r_sr")
        self.le_e_ns_r_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.le_e_ns_r_sr)

        self.label_103 = QLabel(self.frame_33)
        self.label_103.setObjectName("label_103")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_103)

        self.le_e_sn_r_sr = QLineEdit(self.frame_33)
        self.le_e_sn_r_sr.setObjectName("le_e_sn_r_sr")
        self.le_e_sn_r_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.le_e_sn_r_sr)

        self.label_102 = QLabel(self.frame_33)
        self.label_102.setObjectName("label_102")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_102)

        self.le_e_ew_r_sr = QLineEdit(self.frame_33)
        self.le_e_ew_r_sr.setObjectName("le_e_ew_r_sr")
        self.le_e_ew_r_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.le_e_ew_r_sr)

        self.label_101 = QLabel(self.frame_33)
        self.label_101.setObjectName("label_101")

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.label_101)

        self.le_e_we_r_sr = QLineEdit(self.frame_33)
        self.le_e_we_r_sr.setObjectName("le_e_we_r_sr")
        self.le_e_we_r_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.le_e_we_r_sr)

        self.label_100 = QLabel(self.frame_33)
        self.label_100.setObjectName("label_100")

        self.formLayout_8.setWidget(4, QFormLayout.LabelRole, self.label_100)

        self.le_e_ng_r_sr = QLineEdit(self.frame_33)
        self.le_e_ng_r_sr.setObjectName("le_e_ng_r_sr")
        self.le_e_ng_r_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_8.setWidget(4, QFormLayout.FieldRole, self.le_e_ng_r_sr)

        self.label_99 = QLabel(self.frame_33)
        self.label_99.setObjectName("label_99")

        self.formLayout_8.setWidget(5, QFormLayout.LabelRole, self.label_99)

        self.le_e_gn_r_sr = QLineEdit(self.frame_33)
        self.le_e_gn_r_sr.setObjectName("le_e_gn_r_sr")
        self.le_e_gn_r_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_8.setWidget(5, QFormLayout.FieldRole, self.le_e_gn_r_sr)

        self.label_98 = QLabel(self.frame_33)
        self.label_98.setObjectName("label_98")

        self.formLayout_8.setWidget(6, QFormLayout.LabelRole, self.label_98)

        self.le_ex_gps_sr = QLineEdit(self.frame_33)
        self.le_ex_gps_sr.setObjectName("le_ex_gps_sr")
        self.le_ex_gps_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_8.setWidget(6, QFormLayout.FieldRole, self.le_ex_gps_sr)

        self.label_90 = QLabel(self.frame_33)
        self.label_90.setObjectName("label_90")

        self.formLayout_8.setWidget(7, QFormLayout.LabelRole, self.label_90)

        self.le_ey_gps_sr = QLineEdit(self.frame_33)
        self.le_ey_gps_sr.setObjectName("le_ey_gps_sr")
        self.le_ey_gps_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_8.setWidget(7, QFormLayout.FieldRole, self.le_ey_gps_sr)

        self.verticalLayout_12.addLayout(self.formLayout_8)

        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_112 = QLabel(self.frame_33)
        self.label_112.setObjectName("label_112")
        self.label_112.setMaximumSize(QSize(16777215, 16))
        self.label_112.setFont(font13)

        self.verticalLayout_8.addWidget(self.label_112)

        self.formLayout_18 = QFormLayout()
        self.formLayout_18.setObjectName("formLayout_18")
        self.label_105 = QLabel(self.frame_33)
        self.label_105.setObjectName("label_105")

        self.formLayout_18.setWidget(0, QFormLayout.LabelRole, self.label_105)

        self.le_e_ns_vdc_sr = QLineEdit(self.frame_33)
        self.le_e_ns_vdc_sr.setObjectName("le_e_ns_vdc_sr")
        self.le_e_ns_vdc_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_18.setWidget(0, QFormLayout.FieldRole, self.le_e_ns_vdc_sr)

        self.label_106 = QLabel(self.frame_33)
        self.label_106.setObjectName("label_106")

        self.formLayout_18.setWidget(1, QFormLayout.LabelRole, self.label_106)

        self.le_e_ew_vdc_sr = QLineEdit(self.frame_33)
        self.le_e_ew_vdc_sr.setObjectName("le_e_ew_vdc_sr")
        self.le_e_ew_vdc_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_18.setWidget(1, QFormLayout.FieldRole, self.le_e_ew_vdc_sr)

        self.label_107 = QLabel(self.frame_33)
        self.label_107.setObjectName("label_107")

        self.formLayout_18.setWidget(2, QFormLayout.LabelRole, self.label_107)

        self.le_e_ng_vdc_sr = QLineEdit(self.frame_33)
        self.le_e_ng_vdc_sr.setObjectName("le_e_ng_vdc_sr")
        self.le_e_ng_vdc_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_18.setWidget(2, QFormLayout.FieldRole, self.le_e_ng_vdc_sr)

        self.verticalLayout_8.addLayout(self.formLayout_18)

        self.formLayout_19 = QFormLayout()
        self.formLayout_19.setObjectName("formLayout_19")
        self.label_108 = QLabel(self.frame_33)
        self.label_108.setObjectName("label_108")

        self.formLayout_19.setWidget(0, QFormLayout.LabelRole, self.label_108)

        self.le_e_ns_vac_sr = QLineEdit(self.frame_33)
        self.le_e_ns_vac_sr.setObjectName("le_e_ns_vac_sr")
        self.le_e_ns_vac_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_19.setWidget(0, QFormLayout.FieldRole, self.le_e_ns_vac_sr)

        self.label_109 = QLabel(self.frame_33)
        self.label_109.setObjectName("label_109")

        self.formLayout_19.setWidget(1, QFormLayout.LabelRole, self.label_109)

        self.le_e_ew_vac_sr = QLineEdit(self.frame_33)
        self.le_e_ew_vac_sr.setObjectName("le_e_ew_vac_sr")
        self.le_e_ew_vac_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_19.setWidget(1, QFormLayout.FieldRole, self.le_e_ew_vac_sr)

        self.label_110 = QLabel(self.frame_33)
        self.label_110.setObjectName("label_110")

        self.formLayout_19.setWidget(2, QFormLayout.LabelRole, self.label_110)

        self.le_e_ng_vac_sr = QLineEdit(self.frame_33)
        self.le_e_ng_vac_sr.setObjectName("le_e_ng_vac_sr")
        self.le_e_ng_vac_sr.setMinimumSize(QSize(0, 21))

        self.formLayout_19.setWidget(2, QFormLayout.FieldRole, self.le_e_ng_vac_sr)

        self.verticalLayout_8.addLayout(self.formLayout_19)

        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_14.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")

        self.horizontalLayout_6.addLayout(self.verticalLayout_13)

        self.verticalLayout_15.addLayout(self.horizontalLayout_6)

        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.frame_48 = QFrame(self.stackSiteReportUI)
        self.frame_48.setObjectName("frame_48")
        self.frame_48.setGeometry(QRect(20, 310, 341, 101))
        self.frame_48.setFrameShape(QFrame.Shape.Panel)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_48)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label_126 = QLabel(self.frame_48)
        self.label_126.setObjectName("label_126")
        self.label_126.setFont(font10)

        self.verticalLayout_11.addWidget(self.label_126)

        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName("formLayout_11")
        self.formLayout_11.setContentsMargins(0, -1, -1, -1)
        self.label_121 = QLabel(self.frame_48)
        self.label_121.setObjectName("label_121")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.label_121)

        self.le_last_time_stamp_sr = QLineEdit(self.frame_48)
        self.le_last_time_stamp_sr.setObjectName("le_last_time_stamp_sr")
        self.le_last_time_stamp_sr.setMinimumSize(QSize(153, 21))
        self.le_last_time_stamp_sr.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.le_last_time_stamp_sr)

        self.label_120 = QLabel(self.frame_48)
        self.label_120.setObjectName("label_120")

        self.formLayout_11.setWidget(1, QFormLayout.LabelRole, self.label_120)

        self.le_first_time_stamp_sr = QLineEdit(self.frame_48)
        self.le_first_time_stamp_sr.setObjectName("le_first_time_stamp_sr")
        self.le_first_time_stamp_sr.setMinimumSize(QSize(153, 21))

        self.formLayout_11.setWidget(1, QFormLayout.FieldRole, self.le_first_time_stamp_sr)

        self.verticalLayout_11.addLayout(self.formLayout_11)

        self.frame_49 = QFrame(self.stackSiteReportUI)
        self.frame_49.setObjectName("frame_49")
        self.frame_49.setGeometry(QRect(190, 245, 175, 54))
        self.frame_49.setMaximumSize(QSize(175, 16777215))
        self.frame_49.setFrameShape(QFrame.Shape.Panel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_49)
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 2, 5, 2)
        self.formLayout_17 = QFormLayout()
        self.formLayout_17.setObjectName("formLayout_17")
        self.label_114 = QLabel(self.frame_49)
        self.label_114.setObjectName("label_114")

        self.formLayout_17.setWidget(0, QFormLayout.LabelRole, self.label_114)

        self.le_battery_voltage_sr = QLineEdit(self.frame_49)
        self.le_battery_voltage_sr.setObjectName("le_battery_voltage_sr")
        self.le_battery_voltage_sr.setMinimumSize(QSize(21, 0))
        self.le_battery_voltage_sr.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_17.setWidget(0, QFormLayout.FieldRole, self.le_battery_voltage_sr)

        self.verticalLayout_19.addLayout(self.formLayout_17)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_119 = QLabel(self.frame_49)
        self.label_119.setObjectName("label_119")

        self.horizontalLayout_4.addWidget(self.label_119)

        self.le_ex_gain_sr = QLineEdit(self.frame_49)
        self.le_ex_gain_sr.setObjectName("le_ex_gain_sr")
        self.le_ex_gain_sr.setMinimumSize(QSize(21, 0))
        self.le_ex_gain_sr.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.le_ex_gain_sr)

        self.label_128 = QLabel(self.frame_49)
        self.label_128.setObjectName("label_128")

        self.horizontalLayout_4.addWidget(self.label_128)

        self.le_ey_gain_sr = QLineEdit(self.frame_49)
        self.le_ey_gain_sr.setObjectName("le_ey_gain_sr")
        self.le_ey_gain_sr.setMinimumSize(QSize(21, 0))
        self.le_ey_gain_sr.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.le_ey_gain_sr)

        self.verticalLayout_19.addLayout(self.horizontalLayout_4)

        self.label_check_sr = QLabel(self.stackSiteReportUI)
        self.label_check_sr.setObjectName("label_check_sr")
        self.label_check_sr.setGeometry(QRect(879, 471, 50, 50))
        self.label_check_sr.setAutoFillBackground(True)
        self.label_check_sr.setStyleSheet(
            "QLineEdit#label_icon {color: black; background-color: rgb(255, 246, 131);}"
        )
        self.label_check_sr.setFrameShape(QFrame.Shape.NoFrame)
        self.stackedWidget.addWidget(self.stackSiteReportUI)
        self.layoutWidget.raise_()
        self.te_comments_sr.raise_()
        self.frame_46.raise_()
        self.tb_generate_report_sr.raise_()
        self.label_87.raise_()
        self.le_change_directory_sr.raise_()
        self.tb_change_directory_sr.raise_()
        self.frame_33.raise_()
        self.frame_47.raise_()
        self.label_6.raise_()
        self.frame_31.raise_()
        self.frame_32.raise_()
        self.frame_48.raise_()
        self.frame_49.raise_()
        self.label_check_sr.raise_()
        self.stackEngineerUI = QWidget()
        self.stackEngineerUI.setObjectName("stackEngineerUI")
        self.te_filteredhexdata = QTextEdit(self.stackEngineerUI)
        self.te_filteredhexdata.setObjectName("te_filteredhexdata")
        self.te_filteredhexdata.setGeometry(QRect(50, 190, 850, 100))
        font14 = QFont()
        font14.setPointSize(15)
        self.te_filteredhexdata.setFont(font14)
        self.te_filteredhexdata.setStyleSheet(
            "QTextEdit#te_filteredhexdata {color: black; background-color: rgb(255, 246, 131);}\n"
            "\n"
            "\n"
            "\n"
            ""
        )
        self.te_filteredhexdata.setReadOnly(True)
        self.te_rawhex = QTextEdit(self.stackEngineerUI)
        self.te_rawhex.setObjectName("te_rawhex")
        self.te_rawhex.setGeometry(QRect(50, 325, 850, 100))
        font15 = QFont()
        font15.setPointSize(15)
        font15.setBold(False)
        self.te_rawhex.setFont(font15)
        self.te_rawhex.setStyleSheet(
            "QTextEdit#te_rawhex {color: black; background-color: rgb(255, 246, 131);}\n\n\n\n"
        )
        self.te_rawhex.setReadOnly(True)
        self.te_gps_string_e = QTextEdit(self.stackEngineerUI)
        self.te_gps_string_e.setObjectName("te_gps_string_e")
        self.te_gps_string_e.setGeometry(QRect(50, 460, 850, 55))
        self.te_gps_string_e.setStyleSheet(
            "QTextEdit#te_gps_string_e {color: black; background-color: rgb(255, 246, 131);}\n"
            "\n"
            "\n"
            "\n"
            ""
        )
        self.te_gps_string_e.setReadOnly(True)
        self.frame_19 = QFrame(self.stackEngineerUI)
        self.frame_19.setObjectName("frame_19")
        self.frame_19.setGeometry(QRect(50, 15, 850, 144))
        self.frame_19.setFrameShape(QFrame.Shape.Panel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.label_19 = QLabel(self.frame_19)
        self.label_19.setObjectName("label_19")
        self.label_19.setGeometry(QRect(10, 10, 830, 123))
        self.label_19.setFont(font2)
        self.label_19.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.label_19.setWordWrap(True)
        self.label_5 = QLabel(self.stackEngineerUI)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(50, 435, 850, 20))
        font16 = QFont()
        font16.setPointSize(23)
        font16.setBold(False)
        self.label_5.setFont(font16)
        self.label_13 = QLabel(self.stackEngineerUI)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QRect(50, 298, 181, 20))
        self.label_13.setFont(font16)
        self.label_15 = QLabel(self.stackEngineerUI)
        self.label_15.setObjectName("label_15")
        self.label_15.setGeometry(QRect(50, 165, 261, 20))
        self.label_15.setFont(font16)
        self.te_bytesread = QTextEdit(self.stackEngineerUI)
        self.te_bytesread.setObjectName("te_bytesread")
        self.te_bytesread.setGeometry(QRect(450, 295, 41, 25))
        self.te_bytesread.setFont(font15)
        self.te_bytesread.setStyleSheet(
            "QTextEdit#te_bytesread {color: black; background-color: rgb(255, 246, 131);}\n\n\n\n"
        )
        self.te_bytesread.setReadOnly(True)
        self.te_magstatus = QTextEdit(self.stackEngineerUI)
        self.te_magstatus.setObjectName("te_magstatus")
        self.te_magstatus.setGeometry(QRect(660, 295, 41, 25))
        self.te_magstatus.setFont(font14)
        self.te_magstatus.setStyleSheet(
            "QTextEdit#te_magstatus {color: black; background-color: rgb(255, 246, 131);}\n\n\n\n"
        )
        self.te_magstatus.setReadOnly(True)
        self.te_gps_status_byte_e = QTextEdit(self.stackEngineerUI)
        self.te_gps_status_byte_e.setObjectName("te_gps_status_byte_e")
        self.te_gps_status_byte_e.setGeometry(QRect(860, 295, 41, 25))
        self.te_gps_status_byte_e.setFont(font14)
        self.te_gps_status_byte_e.setStyleSheet(
            "QTextEdit#te_gps_status_byte_e {color: black; background-color: rgb(255, 246, 131);}\n"
            "\n"
            "\n"
            "\n"
            ""
        )
        self.te_gps_status_byte_e.setReadOnly(True)
        self.label_16 = QLabel(self.stackEngineerUI)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(QRect(312, 298, 135, 20))
        self.label_16.setFont(font16)
        self.label_17 = QLabel(self.stackEngineerUI)
        self.label_17.setObjectName("label_17")
        self.label_17.setGeometry(QRect(514, 298, 143, 20))
        self.label_17.setFont(font16)
        self.label_18 = QLabel(self.stackEngineerUI)
        self.label_18.setObjectName("label_18")
        self.label_18.setGeometry(QRect(722, 298, 135, 20))
        self.label_18.setFont(font16)
        self.stackedWidget.addWidget(self.stackEngineerUI)
        self.stackConnectionUI = QWidget()
        self.stackConnectionUI.setObjectName("stackConnectionUI")
        self.stackConnectionUI.setEnabled(False)
        self.label_14 = QLabel(self.stackConnectionUI)
        self.label_14.setObjectName("label_14")
        self.label_14.setGeometry(QRect(570, 100, 191, 16))
        self.stackedWidget.addWidget(self.stackConnectionUI)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 875, 35))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.cb_connection = QComboBox(self.frame_3)
        self.cb_connection.setObjectName("cb_connection")
        self.cb_connection.setGeometry(QRect(110, 0, 250, 35))
        self.cb_connection.setAutoFillBackground(False)
        self.cb_connection.setEditable(False)
        self.cb_connection.setMaxVisibleItems(20)
        self.cb_connection.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        self.cb_connection.setFrame(True)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(5, 0, 100, 35))
        self.label_7.setFont(font)
        self.horizontalLayoutWidget_2 = QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(370, 0, 501, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.horizontalLayoutWidget_2)
        self.frame_18.setObjectName("frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.label_connection_led = QLabel(self.frame_18)
        self.label_connection_led.setObjectName("label_connection_led")
        self.label_connection_led.setGeometry(QRect(0, 3, 58, 29))
        self.label_connection_led.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cb_speed = QComboBox(self.frame_18)
        self.cb_speed.setObjectName("cb_speed")
        self.cb_speed.setGeometry(QRect(70, 4, 91, 26))

        self.horizontalLayout_2.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.horizontalLayoutWidget_2)
        self.frame_17.setObjectName("frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.label_packets_led = QLabel(self.frame_17)
        self.label_packets_led.setObjectName("label_packets_led")
        self.label_packets_led.setGeometry(QRect(100, 3, 58, 29))
        self.label_packets_led.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QRect(10, 3, 71, 29))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.horizontalLayoutWidget_2)
        self.frame_16.setObjectName("frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.label_11 = QLabel(self.frame_16)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(20, 3, 68, 28))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_receiving_led = QLabel(self.frame_16)
        self.label_receiving_led.setObjectName("label_receiving_led")
        self.label_receiving_led.setGeometry(QRect(100, 3, 58, 29))
        self.label_receiving_led.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_16)

        self.frame_icon = QFrame(self.centralwidget)
        self.frame_icon.setObjectName("frame_icon")
        self.frame_icon.setGeometry(QRect(875, 0, 75, 75))
        self.frame_icon.setStyleSheet(
            "QFrameEdit#frame_icon {color: black; background-color: rgb(255, 246, 131);}"
        )
        self.frame_icon.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_icon.setFrameShadow(QFrame.Shadow.Raised)
        self.label_icon = QLabel(self.frame_icon)
        self.label_icon.setObjectName("label_icon")
        self.label_icon.setGeometry(QRect(1, 1, 70, 70))
        self.label_icon.setAutoFillBackground(True)
        self.label_icon.setStyleSheet(
            "QLineEdit#label_icon {color: black; background-color: rgb(255, 246, 131);}"
        )
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tb_shortcycle_2, self.le_filename)
        QWidget.setTabOrder(self.le_filename, self.le_run_id)
        QWidget.setTabOrder(self.le_run_id, self.le_site_name)
        QWidget.setTabOrder(self.le_site_name, self.le_state_province)
        QWidget.setTabOrder(self.le_state_province, self.le_country)
        QWidget.setTabOrder(self.le_country, self.le_operator)
        QWidget.setTabOrder(self.le_operator, self.le_nims_id)
        QWidget.setTabOrder(self.le_nims_id, self.le_mag_id)
        QWidget.setTabOrder(self.le_mag_id, self.le_ns_dipole_length)
        QWidget.setTabOrder(self.le_ns_dipole_length, self.le_ns_dipole_heading)
        QWidget.setTabOrder(self.le_ns_dipole_heading, self.le_ew_dipole_length)
        QWidget.setTabOrder(self.le_ew_dipole_length, self.le_ew_dipole_heading)
        QWidget.setTabOrder(self.le_ew_dipole_heading, self.le_n_electrode_id)
        QWidget.setTabOrder(self.le_n_electrode_id, self.le_s_electrode_id)
        QWidget.setTabOrder(self.le_s_electrode_id, self.le_e_electrode_id)
        QWidget.setTabOrder(self.le_e_electrode_id, self.le_w_electrode_id)
        QWidget.setTabOrder(self.le_w_electrode_id, self.le_gnd_electrode_id)
        QWidget.setTabOrder(self.le_gnd_electrode_id, self.rb_x_layout)
        QWidget.setTabOrder(self.rb_x_layout, self.rb_l_layout)
        QWidget.setTabOrder(self.rb_l_layout, self.rb_t_layout)
        QWidget.setTabOrder(self.rb_t_layout, self.te_comments)
        QWidget.setTabOrder(self.te_comments, self.cb_status)
        QWidget.setTabOrder(self.cb_status, self.le_run_id_sr)
        QWidget.setTabOrder(self.le_run_id_sr, self.le_site_name_sr)
        QWidget.setTabOrder(self.le_site_name_sr, self.le_state_province_sr)
        QWidget.setTabOrder(self.le_state_province_sr, self.le_country_sr)
        QWidget.setTabOrder(self.le_country_sr, self.le_crew)
        QWidget.setTabOrder(self.le_crew, self.le_nims_id_sr)
        QWidget.setTabOrder(self.le_nims_id_sr, self.le_mag_id_sr)
        QWidget.setTabOrder(self.le_mag_id_sr, self.le_n_electrode_id_sr)
        QWidget.setTabOrder(self.le_n_electrode_id_sr, self.le_s_electrode_id_sr)
        QWidget.setTabOrder(self.le_s_electrode_id_sr, self.le_e_electrode_id_sr)
        QWidget.setTabOrder(self.le_e_electrode_id_sr, self.le_w_electrode_id_sr)
        QWidget.setTabOrder(self.le_w_electrode_id_sr, self.le_gps_lat_sr)
        QWidget.setTabOrder(self.le_gps_lat_sr, self.le_gps_lon_sr)
        QWidget.setTabOrder(self.le_gps_lon_sr, self.le_gps_alt_sr)
        QWidget.setTabOrder(self.le_gps_alt_sr, self.le_gps_dec_sr)
        QWidget.setTabOrder(self.le_gps_dec_sr, self.le_battery_voltage_sr)
        QWidget.setTabOrder(self.le_battery_voltage_sr, self.le_ex_gain_sr)
        QWidget.setTabOrder(self.le_ex_gain_sr, self.le_ey_gain_sr)
        QWidget.setTabOrder(self.le_ey_gain_sr, self.le_last_time_stamp_sr)
        QWidget.setTabOrder(self.le_last_time_stamp_sr, self.le_first_time_stamp_sr)
        QWidget.setTabOrder(self.le_first_time_stamp_sr, self.le_pre_e_ns_r_sr)
        QWidget.setTabOrder(self.le_pre_e_ns_r_sr, self.le_pre_e_sn_r_sr)
        QWidget.setTabOrder(self.le_pre_e_sn_r_sr, self.le_pre_e_ew_r_sr)
        QWidget.setTabOrder(self.le_pre_e_ew_r_sr, self.le_pre_e_we_r_sr)
        QWidget.setTabOrder(self.le_pre_e_we_r_sr, self.le_pre_e_ns_v_sr)
        QWidget.setTabOrder(self.le_pre_e_ns_v_sr, self.le_pre_e_ew_v_sr)
        QWidget.setTabOrder(self.le_pre_e_ew_v_sr, self.le_e_ns_r_sr)
        QWidget.setTabOrder(self.le_e_ns_r_sr, self.le_e_sn_r_sr)
        QWidget.setTabOrder(self.le_e_sn_r_sr, self.le_e_ew_r_sr)
        QWidget.setTabOrder(self.le_e_ew_r_sr, self.le_e_we_r_sr)
        QWidget.setTabOrder(self.le_e_we_r_sr, self.le_e_ng_r_sr)
        QWidget.setTabOrder(self.le_e_ng_r_sr, self.le_e_gn_r_sr)
        QWidget.setTabOrder(self.le_e_gn_r_sr, self.le_ex_gps_sr)
        QWidget.setTabOrder(self.le_ex_gps_sr, self.le_ey_gps_sr)
        QWidget.setTabOrder(self.le_ey_gps_sr, self.le_e_ns_vdc_sr)
        QWidget.setTabOrder(self.le_e_ns_vdc_sr, self.le_e_ew_vdc_sr)
        QWidget.setTabOrder(self.le_e_ew_vdc_sr, self.le_e_ng_vdc_sr)
        QWidget.setTabOrder(self.le_e_ng_vdc_sr, self.le_e_ns_vac_sr)
        QWidget.setTabOrder(self.le_e_ns_vac_sr, self.le_e_ew_vac_sr)
        QWidget.setTabOrder(self.le_e_ew_vac_sr, self.le_e_ng_vac_sr)
        QWidget.setTabOrder(self.le_e_ng_vac_sr, self.te_comments_sr)
        QWidget.setTabOrder(self.te_comments_sr, self.tb_generate_report_sr)
        QWidget.setTabOrder(self.tb_generate_report_sr, self.le_hx)
        QWidget.setTabOrder(self.le_hx, self.le_hy)
        QWidget.setTabOrder(self.le_hy, self.tb_gain_xlyl)
        QWidget.setTabOrder(self.tb_gain_xlyl, self.tb_gain_xhyl)
        QWidget.setTabOrder(self.tb_gain_xhyl, self.tb_gain_xlyh)
        QWidget.setTabOrder(self.tb_gain_xlyh, self.tb_gain_xhyh)
        QWidget.setTabOrder(self.tb_gain_xhyh, self.le_change_directory_sr)
        QWidget.setTabOrder(self.le_change_directory_sr, self.tb_nims_leds)
        QWidget.setTabOrder(self.tb_nims_leds, self.tb_almanac)
        QWidget.setTabOrder(self.tb_almanac, self.tb_change_directory_sr)
        QWidget.setTabOrder(self.tb_change_directory_sr, self.tb_shortcycle)
        QWidget.setTabOrder(self.tb_shortcycle, self.tb_shortcycle_3)
        QWidget.setTabOrder(self.tb_shortcycle_3, self.le_ex)
        QWidget.setTabOrder(self.le_ex, self.tb_mag_light)
        QWidget.setTabOrder(self.tb_mag_light, self.te_gps_metadata_string)
        QWidget.setTabOrder(self.te_gps_metadata_string, self.le_hz)
        QWidget.setTabOrder(self.le_hz, self.le_ey)
        QWidget.setTabOrder(self.le_ey, self.tb_shortcycle_4)
        QWidget.setTabOrder(self.tb_shortcycle_4, self.te_filteredhexdata)
        QWidget.setTabOrder(self.te_filteredhexdata, self.te_rawhex)
        QWidget.setTabOrder(self.te_rawhex, self.te_gps_string_e)
        QWidget.setTabOrder(self.te_gps_string_e, self.te_bytesread)
        QWidget.setTabOrder(self.te_bytesread, self.te_magstatus)
        QWidget.setTabOrder(self.te_magstatus, self.cb_connection)
        QWidget.setTabOrder(self.cb_connection, self.te_gps_status_byte_e)
        QWidget.setTabOrder(self.te_gps_status_byte_e, self.cb_speed)
        QWidget.setTabOrder(self.cb_speed, self.te_gps_string_m)
        QWidget.setTabOrder(self.te_gps_string_m, self.tb_end_run)
        QWidget.setTabOrder(self.tb_end_run, self.tb_start_run)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.tb_metadata.setText(
            QCoreApplication.translate("MainWindow", "MetaData/\nGPS Control", None)
        )
        self.tb_datadisplay.setText(
            QCoreApplication.translate("MainWindow", "Data Display/\nGain Control", None)
        )
        self.tb_startend.setText(QCoreApplication.translate("MainWindow", "Start/End Run", None))
        self.tb_engineer.setText(QCoreApplication.translate("MainWindow", "Engineering Mode", None))
        self.tb_sitereport.setText(QCoreApplication.translate("MainWindow", "Site Report", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", "Start Run Procedure", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", "End Run Procedure", None))
        # if QT_CONFIG(tooltip)
        self.tb_shortcycle_2.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>GPS SHORT CYCLE occurs every 512 secs and completes in 3 min.  </p><p>To manually initiate a GPS SHORT CYCLE, press this button.  </p><p>During the GPS SHORT CYCLE the NIMS will not know its Gain.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tb_shortcycle_2.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_shortcycle_2.setText(QCoreApplication.translate("MainWindow", "Short\nCycle", None))
        self.label_21.setText(
            QCoreApplication.translate(
                "MainWindow", "Short Cycle the GPS. Completes in ~3 min from GPS Lock.", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.label_short_cycle_led_2.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Black = Idle\nRed = Obaining Lock\nYellow = Recieving\nGreen = Complete",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_short_cycle_led_2.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.label_23.setText(
            QCoreApplication.translate(
                "MainWindow", "Is magnetometer ready to record or still slewing?", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.label_mag_north_led.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Yellow = The East-West field (Hy) is greater than +-100nT\n"
                "Green = Ready to record",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_mag_north_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.label_mag_ready_led.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Red = Magnetometer is still slewing\nGreen = Magnetometer is read to record",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_mag_ready_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Ready?", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", "North?", None))
        self.label_24.setText(
            QCoreApplication.translate(
                "MainWindow", "Is magnetometer facing north (Hy < +/- 100 nT)?", None
            )
        )
        self.label_20.setText(QCoreApplication.translate("MainWindow", "Step 1: Short Cycle", None))
        self.label_22.setText(
            QCoreApplication.translate("MainWindow", "Step 2: Magnetometer", None)
        )
        self.label_25.setText(
            QCoreApplication.translate(
                "MainWindow",
                "If yellow, input is below +/- 16 mV and low gain.  Refer to 'Data Display' to check requirments if High Gain is an option. Gain Control located on the Data Display/Gain Control tab.",
                None,
            )
        )
        self.label_ex_spec_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.label_ey_spec_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.label_69.setText(QCoreApplication.translate("MainWindow", "Ex Spec?", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", "Ey Spec?", None))
        self.label_27.setText(
            QCoreApplication.translate("MainWindow", "Step 3: Electric Channel Gain", None)
        )
        self.label_28.setText(QCoreApplication.translate("MainWindow", "Step 4: Metadata", None))
        self.label_29.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Check MetaData tab information.  Missing information will be filled with default values.",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.label_metadata_led.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Black = No Information\n"
                "Yellow = Partial Information\n"
                "Green = Complete Information",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_metadata_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.label_26.setText(QCoreApplication.translate("MainWindow", "Step 1: Short Cycle", None))
        # if QT_CONFIG(tooltip)
        self.tb_shortcycle_4.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>GPS SHORT CYCLE occurs every 512 secs and completes in 3 min.  </p><p>To manually initiate a GPS SHORT CYCLE, press this button.  </p><p>During the GPS SHORT CYCLE the NIMS will not know its Gain.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tb_shortcycle_4.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_shortcycle_4.setText(QCoreApplication.translate("MainWindow", "Short\nCycle", None))
        self.label_30.setText(
            QCoreApplication.translate(
                "MainWindow", "Short Cycle the GPS. Completes in ~3 min from GPS Lock.", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.label_short_cycle_led_4.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Black = Idle\nRed = Obaining Lock\nYellow = Recieving\nGreen = Complete",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_short_cycle_led_4.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.label_end_run_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # if QT_CONFIG(statustip)
        self.tb_end_run.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_end_run.setText(QCoreApplication.translate("MainWindow", "End\nRun", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", "Step 2: End Run", None))
        self.label_66.setText(
            QCoreApplication.translate("MainWindow", "Step 3: Download Data", None)
        )
        # if QT_CONFIG(tooltip)
        self.label_start_run_led.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Black = Not Recording Data\nGreen = Recording Data", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_start_run_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.tb_start_run.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tb_start_run.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_start_run.setText(QCoreApplication.translate("MainWindow", "Start\nRun", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", "Step 5: Start Run", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", "Step 6: Short Cycle", None))
        # if QT_CONFIG(tooltip)
        self.tb_shortcycle_3.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>GPS SHORT CYCLE occurs every 512 secs and completes in 3 min.  </p><p>To manually initiate a GPS SHORT CYCLE, press this button.  </p><p>During the GPS SHORT CYCLE the NIMS will not know its Gain.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tb_shortcycle_3.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_shortcycle_3.setText(QCoreApplication.translate("MainWindow", "Short\nCycle", None))
        self.label_64.setText(
            QCoreApplication.translate(
                "MainWindow", "Short Cycle the GPS. Completes in ~3 min from GPS Lock.", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.label_short_cycle_led_3.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Black = Idle\nRed = Obaining Lock\nYellow = Recieving\nGreen = Complete",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_short_cycle_led_3.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.label_93.setText(QCoreApplication.translate("MainWindow", "Hx (nT):", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", "Ey (mV):", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", "Hy (nT):", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", "Ex (mV):", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", "Hz (nT):", None))
        self.label_95.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; font-weight:600;">Electric Dipole Gain Settings Guidelines</span></p><p>X:LOW Y:LOW...................is the default setting.</p><p>LOW GAIN...........................provides good data.</p><p>HIGH GAIN................provides higher resolution.</p><p>Use <span style=" color:#ff0000;">HIGH GAIN ONLY IF</span> an electric channel has <span style=" color:#ff0000;">less than +/-16 mVDC and &lt;2kOhm resistance</span>.</p></body></html>',
                None,
            )
        )
        self.label_gain_xlyl_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # if QT_CONFIG(statustip)
        self.tb_gain_xlyl.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_gain_xlyl.setText(
            QCoreApplication.translate("MainWindow", "Ex: LOW\nEy: LOW", None)
        )
        # if QT_CONFIG(statustip)
        self.tb_gain_xhyl.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_gain_xhyl.setText(
            QCoreApplication.translate("MainWindow", "Ex: HIGH\nEy: LOW", None)
        )
        self.label_gain_xhyl_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # if QT_CONFIG(statustip)
        self.tb_gain_xlyh.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_gain_xlyh.setText(
            QCoreApplication.translate("MainWindow", "Ex: LOW\nEy: HIGH", None)
        )
        self.label_gain_xlyh_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # if QT_CONFIG(statustip)
        self.tb_gain_xhyh.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_gain_xhyh.setText(
            QCoreApplication.translate("MainWindow", "Ex: HIGH\nEy: HIGH", None)
        )
        self.label_gain_xhyh_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # if QT_CONFIG(statustip)
        self.tb_mag_light.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_mag_light.setText(QCoreApplication.translate("MainWindow", "MAG\nLIGHT", None))
        # if QT_CONFIG(statustip)
        self.tb_nims_leds.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_nims_leds.setText(QCoreApplication.translate("MainWindow", "NIMS\nLEDS", None))
        self.label_56.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#ff0000;">All data runs require a header file containing metadata.</span></p></body></html>',
                None,
            )
        )
        self.label_57.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#ff0000;">There is no other way to identify a data file.</span></p></body></html>',
                None,
            )
        )
        self.label_38.setText(QCoreApplication.translate("MainWindow", "MAG ID", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", "Site Name", None))
        self.label_43.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p>NIMS ID</p></body></html>", None
            )
        )
        self.label_37.setText(QCoreApplication.translate("MainWindow", "State/Province", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", "Country", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", "Run ID", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", "Operator", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", "File Name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "General Information", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", "Electrode Metadata", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", "N-S Dipole (Ex)", None))
        # if QT_CONFIG(tooltip)
        self.label_52.setToolTip(
            QCoreApplication.translate("MainWindow", "Length of NS electrode line in meters", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("MainWindow", "Length (m)", None))
        # if QT_CONFIG(tooltip)
        self.le_ns_dipole_length.setToolTip(
            QCoreApplication.translate("MainWindow", "Length of NS electrode line in meters", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.label_53.setText(
            QCoreApplication.translate("MainWindow", "Heading (deg E mag N)", None)
        )
        self.label_55.setText(QCoreApplication.translate("MainWindow", "N Electrode ID", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", "S Electrode ID", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", "E Electrode ID", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", "W Electrode ID", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", "GND Electrode", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", "E-W Dipole (Ey)", None))
        # if QT_CONFIG(tooltip)
        self.label_47.setToolTip(
            QCoreApplication.translate("MainWindow", "Length of EW electrode line in meters", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.label_47.setText(QCoreApplication.translate("MainWindow", "Length (m)", None))
        # if QT_CONFIG(tooltip)
        self.le_ew_dipole_length.setToolTip(
            QCoreApplication.translate("MainWindow", "Length of EW electrode line in meters", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.label_48.setText(
            QCoreApplication.translate("MainWindow", "Heading (deg E mag N)", None)
        )
        self.label_94.setText(QCoreApplication.translate("MainWindow", "Survey Layout", None))
        self.rb_x_layout.setText(QCoreApplication.translate("MainWindow", "X", None))
        self.rb_l_layout.setText(QCoreApplication.translate("MainWindow", "L", None))
        self.rb_t_layout.setText(QCoreApplication.translate("MainWindow", "T", None))
        self.label_north.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.le_survey.setText("")
        self.label_34.setText(
            QCoreApplication.translate("MainWindow", "Most Recent  GPS\nTime Stamp (UTC)", None)
        )
        self.le_gps_time.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", "Date (dd/mm/yy)", None))
        self.le_gps_date.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", "Latitude (dd)", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", "Longitude (dd)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", "Altitude (m)", None))
        self.le_gps_alt.setText("")
        self.le_gps_alt.setPlaceholderText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", "GPS Metadata", None))
        # if QT_CONFIG(tooltip)
        self.te_comments.setToolTip(
            QCoreApplication.translate("MainWindow", "150 Characters Max", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_comments_md.setText(
            QCoreApplication.translate("MainWindow", "Field Crew Comments", None)
        )
        self.label_60.setText(QCoreApplication.translate("MainWindow", "GPS Control", None))
        # if QT_CONFIG(tooltip)
        self.le_gps_status_byte_m.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Codes: C7 = GPS Short Cycling, A3 = Receiving GPS Almanac", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.le_gps_status_byte_m.setText("")
        # if QT_CONFIG(tooltip)
        self.label_61.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Codes: C7 = GPS Short Cycling, A3 = Receiving GPS Almanac", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_61.setText(QCoreApplication.translate("MainWindow", "GPS Status Byte", None))
        # if QT_CONFIG(tooltip)
        self.tb_shortcycle.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>GPS SHORT CYCLE occurs every 512 secs and completes in 3 min.  </p><p>To manually initiate a GPS SHORT CYCLE, press this button.  </p><p>During the GPS SHORT CYCLE the NIMS will not know its Gain.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tb_shortcycle.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tb_shortcycle.setText(QCoreApplication.translate("MainWindow", "Short Cycle", None))
        self.label_short_cycle_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.tb_almanac.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>GPS ALMANAC will acquire the current set of active local satellites.</p><p>For use after distant travel or after <span style=" color:#ff0000;">30-45 minutes</span> to complete during which time the NIMS will not know its Gain.</p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.tb_almanac.setText(QCoreApplication.translate("MainWindow", "Almanac", None))
        self.label_almanac_led.setText("")
        self.te_gps_metadata_string.setDocumentTitle("")
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                "GPS data that will populate the header file if metadata is updated",
                None,
            )
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "MainWindow", "GPS Data (displayed during Acquisition)", None
            )
        )
        self.label_123.setText(QCoreApplication.translate("MainWindow", "Run ID:", None))
        self.le_run_id_sr.setText("")
        self.label_124.setText(QCoreApplication.translate("MainWindow", "Site Name:", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", "State/Province:", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", "Country:", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", "Crew:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "Comments:", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", "GPS:", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", "Lat:", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", "Long:", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", "Alt:", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", "Decl:", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", "Meta:", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", "NIMS ID:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", "Mag ID:", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", "N Elect. ID:", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", "S Elect. ID:", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", "E Elect. ID:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", "W Elect. ID:", None))
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt; font-weight:600;">Status:</span></p></body></html>',
                None,
            )
        )
        self.cb_status.setItemText(0, QCoreApplication.translate("MainWindow", "Install", None))
        self.cb_status.setItemText(1, QCoreApplication.translate("MainWindow", "Check", None))
        self.cb_status.setItemText(2, QCoreApplication.translate("MainWindow", "Extract", None))

        self.tb_generate_report_sr.setText(
            QCoreApplication.translate("MainWindow", "Generate Report", None)
        )
        self.label_87.setText(QCoreApplication.translate("MainWindow", "Save Directory:", None))
        self.tb_change_directory_sr.setText(
            QCoreApplication.translate("MainWindow", "Change Directory", None)
        )
        self.label_86.setText(
            QCoreApplication.translate("MainWindow", "Electrode Parameters:", None)
        )
        self.label_84.setText(
            QCoreApplication.translate("MainWindow", "Prior to Installation:", None)
        )
        self.label_80.setText(QCoreApplication.translate("MainWindow", "Resistance (ohms):", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", "S- to N+:", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", "N- to S+:", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", "W- to E+:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", "E- to W+:", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", "Voltage (mV):", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", "(S- to N+) DVC:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", "(W- to E+) DVC:", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", "At Installation:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", "Resistance (ohms):", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", "S- to N+:", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", "S- to S+:", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", "W- to E+:", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", "E- to W+:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", "G- to N+:", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", "N- to G+:", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", "Ex Gain- to GPS+", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", "Ey Gain- to GPS+", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", "Voltage (mV):", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", "(S- to N+) DVC:", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", "(W- to E+) DVC:", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", "(G- to N+) DVC:", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", "(S- to N+) AVC:", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", "(W- to E+) AVC:", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", "(G- to N+) AVC:", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", "Timing:", None))
        self.label_121.setText(
            QCoreApplication.translate("MainWindow", "Last Time Stamp for run x:", None)
        )
        self.label_120.setText(
            QCoreApplication.translate("MainWindow", "First Time Stamp for run x:", None)
        )
        self.label_114.setText(QCoreApplication.translate("MainWindow", "Battery (V):", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", "Ex Gain:", None))
        # if QT_CONFIG(tooltip)
        self.le_ex_gain_sr.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>Gain can either be H/h or L\\l.</p><p>No other values accepted.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_128.setText(QCoreApplication.translate("MainWindow", "Ey Gain:", None))
        # if QT_CONFIG(tooltip)
        self.le_ey_gain_sr.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Gain can either be H/h or Ll.\nNo other values accepted.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_check_sr.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.label_19.setText(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>EGINEERING MODE reveals the binary data packet streaming from the NIMS each second.</p><p>Each 25-byte data packet has the same order of bytes, numbered 0 through 24, beginning with a h01 and ending with a h04. ('h' means Hex display)</p><p>ENGINEERING MODE  enables the User to bypass the filters of the GUI and see the NIMS communication directly.  It can be helpful.</p><p>Frequently used bytes are displayed separately but can still be found in the original 25-byte packet.</p><p><br/></p></body></html>",
                None,
            )
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "GPS SHORT CYCLE DATA FEED", None)
        )
        self.label_13.setText(QCoreApplication.translate("MainWindow", "RAW PORT DATA", None))
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", "FILTERED HEX PACKETS", None)
        )
        # if QT_CONFIG(tooltip)
        self.te_gps_status_byte_e.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Codes: C7 = GPS Short Cycling, A3 = Receiving GPS Almanac", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", "BYTES READ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", "MAG STATUS", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", "GPS STATUS", None))
        self.label_14.setText(
            QCoreApplication.translate(
                "MainWindow", '<a href="http://www.onlinewebfonts.com">oNline Web Fonts</a>', None
            )
        )
        self.cb_connection.setCurrentText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Connection:", None))
        self.label_connection_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.cb_speed.setCurrentText("")
        self.label_packets_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.label_10.setText(QCoreApplication.translate("MainWindow", "Packets:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", "Receive:", None))
        self.label_receiving_led.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.label_icon.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )

    # retranslateUi
