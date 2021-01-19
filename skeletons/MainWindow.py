# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from widgets.drawer import Drawer
from widgets.slidingStackedWidget import SlidingStackedWidget
from widgets.container import Container

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1176, 723)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/images/bold-36px-#2ABFB0.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#MainWindow \n"
"{\n"
"	background: #212F41;\n"
"}\n"
"\n"
"#menuBar \n"
"{\n"
"	background: #2C405A;\n"
"	border-bottom: 1px solid #47566B;\n"
"}\n"
"\n"
"QGroupBox \n"
"{\n"
"	background-color: #26374C;\n"
"	border-radius: 4px;\n"
"	border-color: #344457;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	margin-top: 6ex;\n"
"	margin-left: 1ex;\n"
"	margin-right: 1ex;\n"
"	padding-top: 30px;\n"
"}\n"
"\n"
"QGroupBox#accounts \n"
"{\n"
"	background-color: transparent;\n"
"	border-color: transparent;\n"
"	margin-top: 0ex;\n"
"	margin-left: 0ex;\n"
"	margin-right: 0ex;\n"
"	padding-top: 0px;\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"	background-color: transparent;\n"
"	color: rgba(255, 255, 255, 230);\n"
"	padding: 0px 15px;\n"
"	margin-bottom: -55px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"}\n"
"\n"
"QLineEdit \n"
"{\n"
"	border: 1px solid #21405D;\n"
"	border-radius: 0px;\n"
"	padding-top: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	"
                        "background: transparent;\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QLineEdit::hover\n"
"{\n"
"	border: 1px solid #0190EA;\n"
"	border-radius: 0px;\n"
"	padding-top: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QLineEdit::disabled\n"
"{\n"
"	border: 1px solid grey;\n"
"	border-radius: 0px;\n"
"	padding-top: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	selection-background-color: grey;\n"
"}\n"
"\n"
"QPushButton \n"
"{\n"
"	background-color: #309db5;\n"
"	border-radius: 5px;\n"
"	border-color: transparent;\n"
"	padding-left: 7px;\n"
"	padding-right: 7px;\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox \n"
"{\n"
"	background-color: transparent;\n"
"	border-bottom-style: outset;\n"
"	border-bottom-width: 1px;\n"
"	border-radius: 0px;\n"
"	border-color: transp"
                        "arent;\n"
"	color: white;\n"
"	padding-left: 0px;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 9pt;\n"
"}\n"
"\n"
"QComboBox ::hover\n"
"{\n"
"	background-color: transparent;\n"
"	border-bottom-style: outset;\n"
"	border-bottom-width: 1px;\n"
"	border-radius: 0px;\n"
"	border-color: transparent;\n"
"	color: white;\n"
"	padding-left: 0px;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 9pt;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	border: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: none;\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	padding-right: 0px;\n"
"	padding-top: 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"	image: none;\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	padding-right: 0px;\n"
"	padding-top: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"	background: #26374C;\n"
"	color: white;\n"
"	border-top-style: inset;\n"
"	border-width: 1px;\n"
"	border-radius: 0px;\n"
"	border-color: #309db5;\n"
"	selection-bckground-color: #309db5;"
                        "\n"
"	padding-left: 0px;\n"
"	padding-bottom: 3px;\n"
"	spacing: 10px;\n"
"	outline: none;\n"
"}\n"
"\n"
"QComboBox QScollBar:vertical\n"
"{\n"
"	border: 0px;\n"
"	background: transparent;\n"
"	width: 10px;\n"
"	margin: 1px 1 1px 0;\n"
"}\n"
"\n"
"QComboBox QScollBar::handle:vertical\n"
"{\n"
"	background: #309db5;\n"
"	min-height: 20px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QGroupBox#distribution::indicator\n"
"{\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	margin-bottom: -15px;\n"
"	margin-left: 8px;\n"
"	margin-right: 0px; \n"
"	image: url(:/images/images/chart-pie-20px-#72C1F2.png);\n"
"}\n"
"\n"
"QGroupBox#accounts::indicator\n"
"{\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	margin-bottom: -15px;\n"
"	margin-left: 8px;\n"
"	margin-right: 0px; \n"
"	image: url(:/images/images/wallet-20px-#72C1F2.png);\n"
"}\n"
"\n"
"QGroupBox#transactions::indicator\n"
"{\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	margin-bottom: -15px;\n"
"	margin-left: 8px;\n"
"	margin-right: 0px; \n"
"	image: url(:/images/images/receipt-20px"
                        "-#72C1F2.png);\n"
"}\n"
"\n"
"QPushButton#settings {\n"
"	background-color:  transparent;\n"
"	border-left: 1px solid #32465F;\n"
"	border-right: 1px solid #32465F;\n"
"	padding: 6px 10px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#alerts {\n"
"	background-color: transparent;\n"
"	border-left: 1px solid #32465F;\n"
"	padding: 6px 10px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#menu:hover, QPushButton#settings:hover, QPushButton#alerts:hover {\n"
"	background-color:  rgba(255, 255, 255, 35);\n"
"	border-left: 1px solid #32465F;\n"
"	padding: 6px 10px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton[expanded=\"true\"]:hover {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-radius: 6px;\n"
"	border-color: transparent;\n"
"	padding: 6px 6px;\n"
"	color: rgba(255, 255, 255, 128);\n"
"}\n"
"\n"
"QPushButton#settings:pressed, QPushButton#alerts:pressed {\n"
"	background-color:  rgba(255, 255, 255, 80);\n"
"	border-left: 1px solid #32465F;\n"
"	padding: 6px "
                        "10px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton[expanded=\"true\"]:pressed {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: transparent;\n"
"	padding: 3px  3px;\n"
"	color: rgba(36, 42, 117, 255);\n"
"}\n"
"\n"
"QFrame#navigation {\n"
"	background-color: #1C293B;\n"
"	margin-bottom: 0px;\n"
"	margin-top: 0px;\n"
"	border-style: none;\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}\n"
"\n"
"QFrame[frameShape=\"5\"] {\n"
"	color: #32465F;\n"
"}\n"
"\n"
"QScrollArea {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QScrollArea > QWidget > QWidget { \n"
"	background: transparent; \n"
"}\n"
"\n"
"QScrollArea > QWidget > QScrollBar { \n"
"	background: palette(base); \n"
"}\n"
"\n"
"Card \n"
"{\n"
"	border-radius: 5px;\n"
"	border-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"	margin-top: 6ex;\n"
"	margin-left: 1ex;\n"
"	margin-right: 1ex;\n"
"	padding-top: 30px;\n"
"}\n"
"\n"
"Card"
                        "::title\n"
"{\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	padding: 0 14px;\n"
"	margin-bottom: -55px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"}\n"
"\n"
"Card > QLabel#amount {\n"
"	color: white;\n"
"	text-align: right;\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 0px 0px;\n"
"	font-family: \"Roboto\";\n"
"	margin-left: 55px;\n"
"	margin-top: 15px;\n"
"	font-size: 24pt;\n"
"}\n"
"\n"
"Card > QPushButton#monthTrend[positive=\"false\"] {\n"
"	color: #F20505;\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 0px 0px;\n"
"	margin-bottom: 10px;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 17pt;\n"
"}\n"
"\n"
"Card > QPushButton#monthTrend[positive=\"true\"] {\n"
"	color: #12A61C;\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 0px 0px;\n"
"	margin-bottom: 10px;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 17pt;\n"
"}\n"
"\n"
"Card > QPushBut"
                        "ton#monthTrend[positive=\"none\"] {\n"
"	color: white;\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 0px 0px;\n"
"	margin-bottom: 10px;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 17pt;\n"
"}\n"
"\n"
"Card > QLabel#currency {\n"
"	color: rgba(255, 255, 255, 180);\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 0px 0px;\n"
"	margin-right: 25px;\n"
"	margin-top: 18px;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 18pt;\n"
"}\n"
"\n"
"QLabel#menuLabel {\n"
"	color: white;\n"
"}\n"
"\n"
"QChartView {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QTableView {\n"
"	background-color: #141C26;\n"
"}\n"
"\n"
"Thumbnail\n"
"{\n"
"	background-color: transparent;\n"
"	border-radius: 30px;\n"
"	border-color: #2d4057;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"Thumbnail::title\n"
"{\n"
"	background-color: transparent;\n"
"	color: rgba(255, 255, 255, 230);\n"
"	padding: 0px 0px;\n"
"	margin-botto"
                        "m: 0px;\n"
"}\n"
"\n"
"QPushButton#logoExpense\n"
"{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border-color: transparent;\n"
"	color: white;\n"
"}\n"
"\n"
"QLabel#categoryExpense {\n"
"	color: #a2a3ae;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 12pt;\n"
"	margin-bottom: 15px;\n"
"}\n"
"\n"
"QLabel#amountExpense {\n"
"	color: white;\n"
"	font-family: \"Roboto Black\";\n"
"	font-size: 12pt;\n"
"\n"
"}\n"
"\n"
"QLabel#monthExpense {\n"
"	color: #a2a3ae;\n"
"	font-family: \"Roboto Light\";\n"
"	font-size: 12pt;\n"
"}\n"
"\n"
"QGroupBox#page1MonthlyExpenses, QGroupBox#page2MonthlyExpenses \n"
"{\n"
"	background-color: transparent;\n"
"	border-color: transparent;\n"
"	margin-top: 0ex;\n"
"	margin-left: 0ex;\n"
"	margin-right: 0ex;\n"
"	padding-top: 0px;\n"
"}\n"
"\n"
"QPushButton#rightPageMonthlyExpenses, QPushButton#leftPageMonthlyExpenses\n"
"{\n"
"	background-color: transparent;\n"
"	border-radius: 0px;\n"
"	border-color: transparent;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#menuDa"
                        "shboard, QPushButton#menu,\n"
"QPushButton#menuGraph, QPushButton#menuInsights {\n"
"    background-color: transparent;\n"
"	border-radius: 0px;\n"
"    border-style: none;\n"
"    padding: 8px 6px 8px 6px;\n"
"}\n"
"\n"
"QPushButton#menuDashboard:checked, QPushButton#menuGraph:checked,\n"
"QPushButton#menuInsights:checked {\n"
"    background-color: #19344D;\n"
"	border-radius: 0px;\n"
"    border-left: 3px solid #0093EE;\n"
"    padding: 8px 6px 8px 3px;\n"
"}\n"
"\n"
"QPushButton#menuDashboard:hover:!checked, QPushButton#menuGraph:hover:!checked,\n"
"QPushButton#menuInsights:hover:!checked {\n"
"    background-color: #19344D;\n"
"	border-radius: 0px;\n"
"    border-style: none;\n"
"    padding: 8px 6px 8px 6px;\n"
"}\n"
"\n"
"QPushButton#menu:hover {\n"
"    background-color: transparent;\n"
"	border-radius: 0px;\n"
"    border-style: none;\n"
"    padding: 8px 6px 8px 6px;\n"
"}\n"
"\n"
"QDockWidget {\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QDockWidget > QWidget {\n"
"	color: white;\n"
""
                        "	background-color: #26374C;\n"
"	border: 1px solid #344457;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QMainWindow::separator {\n"
"	width: 10px;\n"
"	height: 0px;\n"
"	margin: -10px;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QLabel#titleBarTitle {\n"
"	background-color: #26374C;\n"
"	border-top: 1px solid #344457;\n"
"	border-left: 1px solid #344457;  \n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"	padding-bottom: 10px;\n"
"	padding-left: 12px;\n"
"	padding-top: 10px;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 13pt;\n"
"	color: white;\n"
"}\n"
"\n"
"QWidget#titleBarEmptyWidget {\n"
"	background-color: #26374C;\n"
"	border-top: 1px solid #344457;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
""
                        "	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"}\n"
"\n"
"QWidget#leftAddWidget {\n"
"	background-color: #26374C;\n"
"	border-top: 1px solid #344457;\n"
"	border-right: 1px solid #344457;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"}\n"
"\n"
"QPushButton#titleBarAdd {\n"
"	background-color: #26374C;\n"
"	border-top: 0px solid #344457;\n"
"	border-right: 0px solid #344457;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"	padding-bottom: 0px;\n"
"	padding-left: 0px;\n"
"	padding-top: 0px;\n"
"}\n"
"\n"
"QStatusBar {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border-top: 1px solid #344457;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	bord"
                        "er-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#statusBarSettings {\n"
"	background-color: #26374C;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"}\n"
"\n"
"QPushButton[activated=\"true\"] {\n"
"	background-color: #26374C;\n"
"	color: white;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 10pt;\n"
"	margin-left: 10px;\n"
"}\n"
"\n"
"QPushButton[activated=\"false\"] {\n"
"	background-color: #26374C;\n"
"	color: rgba(255, 255, 255, 100);\n"
"	font-family: \"Roboto\";\n"
"	font-size: 10pt;\n"
"	margin-left: 10px;\n"
"}\n"
"\n"
"QListView {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #385170;\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: "
                        "transparent;\n"
"    color: white;\n"
"	padding-left: 8px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #0190EA;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"	padding-left: 10px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox {\n"
"    padding-right: 5px;\n"
"	background-color: transparent;\n"
"	border: 1px solid #21405D;\n"
"	border-radius: 0px;\n"
"	padding-left: 3px;\n"
"	padding-top: 1px;\n"
"	padding-bottom: 1px;\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"    padding-right: 5px;\n"
"	background-color: transparent;\n"
"	border: 1px solid #0190EA;\n"
"	border-radius: 0px;\n"
"	padding-left: 3px;\n"
"	padding-top: 1px;\n"
"	padding-bottom: 1px;\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 18px"
                        ";\n"
"	height: 18px;\n"
"    border-image: url(:/images/images/expand_less-white-18dp.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover {\n"
"    border-image: url(:/images/images/expand_less-hovered-18dp.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"    border-image: url(:/images/images/expand_less-hovered-18dp.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 18px;\n"
"	height: 18px;\n"
"    border-image: url(:/images/images/expand_more-white-18dp.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover {\n"
"    border-image: url(:/images/images/expand_more-hovered-18dp.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"    border-image: url(:/images/images/expand_more-hovered-18dp.svg);\n"
"}\n"
"\n"
"QDateEdit\n"
"{\n"
"    background-color: transparent;\n"
"    border: 1px solid #21405D;\n"
"	color: white;\n"
"	padding-top: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-left: 2px;\n"
"	p"
                        "adding-right: 2px;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"\n"
"QDateEdit::drop-down \n"
"{\n"
"    image: url(:/images/images/today-white-24dp.svg);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    subcontrol-position: right center;\n"
"    subcontrol-origin: margin;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = SlidingStackedWidget(MainWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.gridLayout_2 = QGridLayout(self.dashboard)
        self.gridLayout_2.setSpacing(15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.transactions = Container(self.dashboard)
        self.transactions.setObjectName(u"transactions")
        self.transactions.setMinimumSize(QSize(40, 46))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(13)
        self.transactions.setFont(font)
        self.transactions.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.transactions.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.gridLayout_4 = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.transactions.setWidget(self.dockWidgetContents_2)

        self.gridLayout_2.addWidget(self.transactions, 0, 3, 1, 1)

        self.monthlyExpenses = Container(self.dashboard)
        self.monthlyExpenses.setObjectName(u"monthlyExpenses")
        sizePolicy.setHeightForWidth(self.monthlyExpenses.sizePolicy().hasHeightForWidth())
        self.monthlyExpenses.setSizePolicy(sizePolicy)
        self.monthlyExpenses.setMinimumSize(QSize(40, 44))
        self.monthlyExpenses.setMaximumSize(QSize(500, 524287))
        self.monthlyExpenses.setFont(font)
        self.monthlyExpenses.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.monthlyExpenses.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_9 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, -1)
        self.monthlyExpenses.setWidget(self.dockWidgetContents)

        self.gridLayout_2.addWidget(self.monthlyExpenses, 0, 4, 1, 1)

        self.stackedWidget.addWidget(self.dashboard)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.total = QGroupBox(self.page_2)
        self.total.setObjectName(u"total")

        self.gridLayout_3.addWidget(self.total, 0, 0, 1, 1)

        self.savings = QGroupBox(self.page_2)
        self.savings.setObjectName(u"savings")

        self.gridLayout_3.addWidget(self.savings, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 3)

        self.menuBar = QWidget(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.menuBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 0, -1, 0)
        self.menuLabel = QLabel(self.menuBar)
        self.menuLabel.setObjectName(u"menuLabel")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.menuLabel.setFont(font1)

        self.horizontalLayout.addWidget(self.menuLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.alerts = QPushButton(self.menuBar)
        self.alerts.setObjectName(u"alerts")
        self.alerts.setMinimumSize(QSize(45, 39))
        self.alerts.setMaximumSize(QSize(45, 39))
        self.alerts.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/notifications-white-24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.alerts.setIcon(icon1)
        self.alerts.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.alerts)

        self.settings = QPushButton(self.menuBar)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(45, 39))
        self.settings.setMaximumSize(QSize(45, 39))
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/settings-white-24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon2)
        self.settings.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.settings)


        self.gridLayout.addWidget(self.menuBar, 0, 1, 1, 3)

        self.drawer = Drawer(MainWindow)
        self.drawer.setObjectName(u"drawer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.drawer.sizePolicy().hasHeightForWidth())
        self.drawer.setSizePolicy(sizePolicy1)
        self.drawer.setMinimumSize(QSize(50, 0))
        self.drawer.setMaximumSize(QSize(50, 16777215))
        self.gridLayout_7 = QGridLayout(self.drawer)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.navigation = QFrame(self.drawer)
        self.navigation.setObjectName(u"navigation")
        self.navigation.setFrameShape(QFrame.StyledPanel)
        self.navigation.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.navigation)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 7)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.menu = QPushButton(self.navigation)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(50, 40))
        self.menu.setMaximumSize(QSize(50, 40))
        self.menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/menu-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon3)
        self.menu.setIconSize(QSize(24, 24))
        self.menu.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.menu)


        self.gridLayout_8.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.menuDashboard = QPushButton(self.navigation)
        self.menuDashboard.setObjectName(u"menuDashboard")
        self.menuDashboard.setMinimumSize(QSize(50, 40))
        self.menuDashboard.setMaximumSize(QSize(50, 40))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(12)
        self.menuDashboard.setFont(font2)
        self.menuDashboard.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/dashboard-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuDashboard.setIcon(icon4)
        self.menuDashboard.setIconSize(QSize(24, 24))
        self.menuDashboard.setCheckable(True)
        self.menuDashboard.setChecked(True)

        self.verticalLayout_2.addWidget(self.menuDashboard)

        self.menuGraph = QPushButton(self.navigation)
        self.menuGraph.setObjectName(u"menuGraph")
        self.menuGraph.setMinimumSize(QSize(50, 40))
        self.menuGraph.setMaximumSize(QSize(50, 40))
        self.menuGraph.setFont(font2)
        self.menuGraph.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/assessment-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuGraph.setIcon(icon5)
        self.menuGraph.setIconSize(QSize(24, 24))
        self.menuGraph.setCheckable(True)

        self.verticalLayout_2.addWidget(self.menuGraph)

        self.menuInsights = QPushButton(self.navigation)
        self.menuInsights.setObjectName(u"menuInsights")
        self.menuInsights.setMinimumSize(QSize(50, 40))
        self.menuInsights.setMaximumSize(QSize(50, 40))
        self.menuInsights.setFont(font2)
        self.menuInsights.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/images/images/insights-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuInsights.setIcon(icon6)
        self.menuInsights.setIconSize(QSize(24, 24))
        self.menuInsights.setCheckable(True)

        self.verticalLayout_2.addWidget(self.menuInsights)


        self.gridLayout_8.addLayout(self.verticalLayout_2, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 6, 0, 1, 2)


        self.gridLayout_7.addWidget(self.navigation, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.drawer, 0, 0, 2, 1)


        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Budgetter", None))
        self.transactions.setWindowTitle(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.monthlyExpenses.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expenses Distribution", None))
        self.total.setTitle(QCoreApplication.translate("MainWindow", u"Total", None))
        self.savings.setTitle(QCoreApplication.translate("MainWindow", u"Savings", None))
        self.menuLabel.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#if QT_CONFIG(tooltip)
        self.alerts.setToolTip(QCoreApplication.translate("MainWindow", u"Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.alerts.setText("")
#if QT_CONFIG(tooltip)
        self.settings.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings.setText("")
        self.menu.setText("")
#if QT_CONFIG(tooltip)
        self.menuDashboard.setToolTip(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.menuDashboard.setText("")
#if QT_CONFIG(tooltip)
        self.menuGraph.setToolTip(QCoreApplication.translate("MainWindow", u"Graph", None))
#endif // QT_CONFIG(tooltip)
        self.menuGraph.setText("")
#if QT_CONFIG(tooltip)
        self.menuInsights.setToolTip(QCoreApplication.translate("MainWindow", u"Insights", None))
#endif // QT_CONFIG(tooltip)
        self.menuInsights.setText("")
    # retranslateUi

