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

from widgets.container import Container
from widgets.sliding_stacked_widget import SlidingStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1216, 785)
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
"	border: 1px solid transparent;\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
""
                        "	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QLineEdit#titleBarSearch\n"
"{\n"
"	border: 1px solid transparent;\n"
"	border-radius: 8px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(44, 64, 90, 255);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QLineEdit::hover\n"
"{\n"
"	border: 1px solid rgba(255, 255, 255, 200);\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QLineEdit::focus\n"
"{\n"
"	border: 1px solid #0190EA;\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QL"
                        "ineEdit#titleBarSearch::hover\n"
"{\n"
"	border: 1px solid transparent;\n"
"	border-radius: 8px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(44, 64, 90, 255);\n"
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
"QPushButton#apply_cancel\n"
"{\n"
"	background-color: transparent;\n"
"	border-radius: 9px;\n"
"	border-color: transparent;\n"
"	padding-left: 3px;\n"
"	padding-right: 3px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	color: white;\n"
""
                        "}\n"
"\n"
"QPushButton#apply_cancel:hover\n"
"{\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	border-radius: 9px;\n"
"	border-color: transparent;\n"
"	padding-left: 3px;\n"
"	padding-right: 3px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox \n"
"{\n"
"	border: 1px solid transparent;\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox::hover\n"
"{\n"
"	border: 1px solid rgba(255, 255, 255, 200);\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox::focus\n"
"{\n"
"	border: 1px solid #0190EA;\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(28, 41, 59, 128);\n"
""
                        "	color: white;\n"
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
"	image: url(:/images/images/arrow_drop_down-white-24dp.svg);\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	padding-right: 0px;\n"
"	padding-top: 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"	image: url(:/images/images/arrow_drop_up-white-24dp.svg);\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	padding-right: 0px;\n"
"	padding-top: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"	background: #212F41;\n"
"	color: white;\n"
"	border-top-style: inset;\n"
"	border-width: 0px;\n"
"	border-radius: 3px;\n"
"	border-color: #0190EA;\n"
"	selection-background-color: #0190EA;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"	outline: none;\n"
"	margin-top: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item\n"
"{\n"
"	min-height: 35px;\n"
"}\n"
"\n"
"QComboBox QScollBar:vertical\n"
"{\n"
"	border"
                        ": 0px;\n"
"	background: transparent;\n"
"	width: 10px;\n"
"	margin: 1px 1 1px 0;\n"
"}\n"
"\n"
"QComboBox QScollBar::handle:vertical\n"
"{\n"
"	background: #0190EA;\n"
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
"	image: url(:/images/images/receipt-20px-#72C1F2.png);\n"
"}\n"
"\n"
"QPushButton#settings \n"
"{\n"
"	background-color:  transparent;\n"
"	border-left: 1px solid #32465F;\n"
"	border-right: 1"
                        "px solid #32465F;\n"
"	padding: 6px 10px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#alerts \n"
"{\n"
"	background-color: transparent;\n"
"	border-left: 1px solid #32465F;\n"
"	padding: 6px 10px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#menu:hover, QPushButton#settings:hover, QPushButton#alerts:hover \n"
"{\n"
"	background-color:  rgba(255, 255, 255, 35);\n"
"	border-left: 1px solid #32465F;\n"
"	padding: 6px 10px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton[expanded=\"true\"]:hover \n"
"{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-radius: 6px;\n"
"	border-color: transparent;\n"
"	padding: 6px 6px;\n"
"	color: rgba(255, 255, 255, 128);\n"
"}\n"
"\n"
"QPushButton#settings:pressed, QPushButton#alerts:pressed \n"
"{\n"
"	background-color:  rgba(255, 255, 255, 80);\n"
"	border-left: 1px solid #32465F;\n"
"	padding: 6px 10px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton[expanded=\"true\"]:pressed \n"
"{\n"
"	background-color: rgba(255, 25"
                        "5, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: transparent;\n"
"	padding: 3px  3px;\n"
"	color: rgba(36, 42, 117, 255);\n"
"}\n"
"\n"
"QFrame[frameShape=\"5\"] \n"
"{\n"
"	color: #32465F;\n"
"}\n"
"\n"
"QScrollArea \n"
"{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QScrollArea > QWidget > QWidget \n"
"{ \n"
"	background: transparent; \n"
"}\n"
"\n"
"QScrollArea > QWidget > QScrollBar \n"
"{ \n"
"	background: palette(base); \n"
"}\n"
"\n"
"QLabel#menuLabel \n"
"{\n"
"	color: white;\n"
"}\n"
"\n"
"QChartView \n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QTableView \n"
"{\n"
"	background-color: #141C26;\n"
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
"QLabel#categoryExpense \n"
"{\n"
"	color: #a2a3ae;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 12pt;\n"
"	margin-bottom: 15px;\n"
"}\n"
"\n"
"QLabel#amountExpense \n"
"{\n"
""
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
"QPushButton#menuDashboard, QPushButton#menu,\n"
"QPushButton#menuGraph, QPushButton#menuInsights \n"
"{\n"
"    background-color: transparent;\n"
"	border-radius: 0px;\n"
"    border-style: none;\n"
"    padding: 8px 6px 8px 6px;\n"
"}\n"
"\n"
"QPushButton#menuDashboard:checked, QPushButton#menuGraph:checked,\n"
"QPushButton#menuInsights:checked \n"
"{\n"
"    b"
                        "ackground-color: #19344D;\n"
"	border-radius: 0px;\n"
"    border-left: 3px solid #0093EE;\n"
"    padding: 8px 6px 8px 3px;\n"
"}\n"
"\n"
"QPushButton#menuDashboard:hover:!checked, QPushButton#menuGraph:hover:!checked,\n"
"QPushButton#menuInsights:hover:!checked \n"
"{\n"
"    background-color: #19344D;\n"
"	border-radius: 0px;\n"
"    border-style: none;\n"
"    padding: 8px 6px 8px 6px;\n"
"}\n"
"\n"
"QPushButton#menu:hover \n"
"{\n"
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
"QDockWidget > QWidget \n"
"{\n"
"	color: white;\n"
"	background-color: #26374C;\n"
"	border: 1px solid #344457;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QMainWindow::separator \n"
"{\n"
"	width: 10px;\n"
"	height: 0px;\n"
"	margin: -10px;\n"
"	padding: 0p"
                        "x;\n"
"}\n"
"\n"
"QLabel#titleBarTitle \n"
"{\n"
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
"QWidget#titleBarEmptyWidget \n"
"{\n"
"	background-color: #26374C;\n"
"	border-top: 1px solid #344457;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"}\n"
"\n"
"QWidget#leftAddWidget \n"
"{\n"
"	background-color: #26374C;\n"
"	border-top: 1px solid #344457;\n"
"	border-right: 1px solid #344457;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 4px;\n"
"	b"
                        "order-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"}\n"
"\n"
"QPushButton#titleBarAdd \n"
"{\n"
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
"QStatusBar \n"
"{\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border-top: 1px solid #344457;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QStatusBar::item \n"
"{\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#statusBarSettings \n"
"{\n"
"	background-color: #26374C;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: "
                        "0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"}\n"
"\n"
"QPushButton[activated=\"true\"] \n"
"{\n"
"	background-color: #26374C;\n"
"	color: white;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 11pt;\n"
"	margin-left: 10px;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"	padding-bottom: 4px;\n"
"	padding-top: 4px;\n"
"	border: 1px solid #165C8D;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton[activated=\"false\"] \n"
"{\n"
"	background-color: #26374C;\n"
"	color: rgba(255, 255, 255, 100);\n"
"	font-family: \"Roboto\";\n"
"	font-size: 11pt;\n"
"	margin-left: 10px;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"	padding-bottom: 4px;\n"
"	padding-top: 4px;\n"
"	border: 1px solid transparent;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QListView \n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QListView::item\n"
"{\n"
"	background: #212F41;\n"
"	color: white;\n"
"	outline: none;\n"
"}\n"
"\n"
""
                        "QListView::item:hover\n"
"{\n"
"	background: #0190EA;\n"
"	color: white;\n"
"	outline: none;\n"
"}\n"
"\n"
"QMenu \n"
"{\n"
"    background-color: #385170;\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QMenu::item \n"
"{\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	padding-left: 8px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px\n"
"}\n"
"\n"
"QMenu::item:selected \n"
"{\n"
"    background-color: #0190EA;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QMenu::icon \n"
"{\n"
"	padding-left: 10px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox \n"
"{\n"
"	border: 1px solid transparent;\n"
"	border-radius: 2px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 2px;\n"
"	padding-right: 5px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	border: 1px solid rgba(255, 255, 255, 200);\n"
"	border-radius: 2px;\n"
"	padding-top: 3px;\n"
"	padd"
                        "ing-bottom: 3px;\n"
"	padding-left: 2px;\n"
"	padding-right: 5px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QDoubleSpinBox:focus {\n"
"	border: 1px solid #0190EA;\n"
"	border-radius: 2px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 2px;\n"
"	padding-right: 5px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 16px;\n"
"	height: 16px;\n"
"    border-image: url(:/images/images/expand_less-white-18dp.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover \n"
"{\n"
"    border-image: url(:/images/images/expand_less-hovered-18dp.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed \n"
"{\n"
"    border-image: url(:/images/images/expand_less-hovered-18dp.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button \n"
"{\n"
"    subcontrol-origin: bo"
                        "rder;\n"
"    subcontrol-position: bottom right;\n"
"    width: 16px;\n"
"	height: 16px;\n"
"    border-image: url(:/images/images/expand_more-white-18dp.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover \n"
"{\n"
"    border-image: url(:/images/images/expand_more-hovered-18dp.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed\n"
"{\n"
"    border-image: url(:/images/images/expand_more-hovered-18dp.svg);\n"
"}\n"
"\n"
"QDateEdit\n"
"{\n"
"	border: 1px solid transparent;\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QDateEdit:hover\n"
"{\n"
"	border: 1px solid rgba(255, 255, 255, 200);\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}"
                        "\n"
"\n"
"QDateEdit:focus\n"
"{\n"
"	border: 1px solid #0190EA;\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QDateEdit::drop-down \n"
"{\n"
"    image: url(:/images/images/today-white-24dp.svg);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"	padding-right: 2px;\n"
"    subcontrol-position: right center;\n"
"    subcontrol-origin: padding;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton \n"
"{\n"
"  	color: white;\n"
"  	icon-size: 18px, 18px;\n"
"	font: 10pt \"Roboto Bold\";\n"
"  	background-color: #0190EA;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover \n"
"{\n"
"  	color: white;\n"
"	border: none;\n"
"  	icon-size: 18px, 18px;\n"
"	font: 10pt \"Roboto Bold\";\n"
"  	background-color: #0190EA;\n"
"}\n"
"\n"
"QCalendarWidget QMenu \n"
"{\n"
"  	color: white;\n"
""
                        "	font: 10pt \"Roboto\";\n"
"  	background-color: #0190EA;\n"
"}\n"
"\n"
"QCalendarWidget QMenu::right-arrow\n"
"{ \n"
"	image: none; \n"
"} \n"
"\n"
"QCalendarWidget QSpinBox\n"
"{ \n"
"	font: 10pt \"Roboto\";\n"
"  	color: white; \n"
"  	background-color: #0190EA; \n"
"  	selection-background-color: #212F41;\n"
"  	selection-color: white;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button \n"
"{ \n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 18px;\n"
"	height: 18px;\n"
"    border-image: url(:/images/images/expand_less-white-18dp.svg);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::down-button \n"
"{\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 18px;\n"
"	height: 18px;\n"
"    border-image: url(:/images/images/expand_more-white-18dp.svg);	\n"
"}\n"
"\n"
"QCalendarWidget QWidget \n"
"{ \n"
"	alternate-background-color: #212F41;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled \n"
"{\n"
"	font: 9pt \"Roboto\"; \n"
"  	"
                        "color: white;  \n"
"  	background-color: #212F41;  \n"
"  	selection-background-color: #0190EA; \n"
"	selection-border-radius: 4px; \n"
"  	selection-color: white; \n"
"	outline: none;\n"
"}\n"
" \n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"	background-color: #0190EA; \n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth\n"
"{\n"
"	qproperty-icon: url(:/images/images/chevron_left-white-18dp.svg);\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_nextmonth\n"
"{\n"
"	qproperty-icon: url(:/images/images/chevron_right-white-18dp.svg);\n"
"}\n"
"\n"
"ExpensesOrIncome > QWidget\n"
"{\n"
"	background-color: transparent;\n"
"	border: 1px solid #21405D;\n"
"}\n"
"\n"
"ExpensesOrIncome:hover\n"
"{\n"
"	background-color: transparent;\n"
"    border: 1px solid #0190EA;\n"
"}\n"
"\n"
"QToolBar\n"
"{\n"
"	background-color: #1C293B;\n"
"	border: none;\n"
"	spacing: 18px;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"	width: 50px;\n"
"	height: 30px;\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"	pad"
                        "ding-bottom: 2px;\n"
"	padding-right: 2px; \n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	width: 50px;\n"
"	height: 30px;\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-right: 2px; \n"
"	background: #19344D;\n"
"	border: none;\n"
"}\n"
"\n"
"QToolButton:checked\n"
"{\n"
"	width: 50px;\n"
"	height: 30px;\n"
"	padding-left: -1px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-right: 2px; \n"
"    background-color: #19344D;\n"
"	border-radius: 0px;\n"
"    border-left: 3px solid #0093EE;\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.actionDashboard = QAction(MainWindow)
        self.actionDashboard.setObjectName(u"actionDashboard")
        self.actionDashboard.setCheckable(True)
        self.actionDashboard.setChecked(True)
        icon = QIcon()
        icon.addFile(u":/images/images/dashboard-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDashboard.setIcon(icon)
        self.actionMenu = QAction(MainWindow)
        self.actionMenu.setObjectName(u"actionMenu")
        self.actionMenu.setCheckable(True)
        self.actionMenu.setChecked(False)
        icon1 = QIcon()
        icon1.addFile(u":/images/images/menu-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMenu.setIcon(icon1)
        self.actionGraph = QAction(MainWindow)
        self.actionGraph.setObjectName(u"actionGraph")
        self.actionGraph.setCheckable(True)
        icon2 = QIcon()
        icon2.addFile(u":/images/images/assessment-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGraph.setIcon(icon2)
        self.actionInsights = QAction(MainWindow)
        self.actionInsights.setObjectName(u"actionInsights")
        self.actionInsights.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u":/images/images/insights-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInsights.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.menuBar = QWidget(self.centralwidget)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.menuBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 0, -1, 0)
        self.menuLabel = QLabel(self.menuBar)
        self.menuLabel.setObjectName(u"menuLabel")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(14)
        self.menuLabel.setFont(font)

        self.horizontalLayout.addWidget(self.menuLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.alerts = QPushButton(self.menuBar)
        self.alerts.setObjectName(u"alerts")
        self.alerts.setMinimumSize(QSize(45, 39))
        self.alerts.setMaximumSize(QSize(45, 39))
        self.alerts.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/notifications-white-24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.alerts.setIcon(icon4)
        self.alerts.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.alerts)

        self.settings = QPushButton(self.menuBar)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(45, 39))
        self.settings.setMaximumSize(QSize(45, 39))
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/settings-white-24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon5)
        self.settings.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.settings)


        self.gridLayout.addWidget(self.menuBar, 0, 0, 1, 1)

        self.stackedWidget = SlidingStackedWidget(self.centralwidget)
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
        self.transactions.setMaximumSize(QSize(524287, 524287))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(13)
        self.transactions.setFont(font1)
        self.transactions.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.transactions.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.gridLayout_4 = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.transactions.setWidget(self.dockWidgetContents_2)

        self.gridLayout_2.addWidget(self.transactions, 1, 0, 2, 2)

        self.accounts = Container(self.dashboard)
        self.accounts.setObjectName(u"accounts")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accounts.sizePolicy().hasHeightForWidth())
        self.accounts.setSizePolicy(sizePolicy)
        self.accounts.setMinimumSize(QSize(40, 46))
        self.accounts.setMaximumSize(QSize(650, 300))
        self.accounts.setFont(font1)
        self.accounts.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.accounts.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.gridLayout_5 = QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.accounts.setWidget(self.dockWidgetContents_3)

        self.gridLayout_2.addWidget(self.accounts, 0, 0, 1, 1)

        self.spending = Container(self.dashboard)
        self.spending.setObjectName(u"spending")
        sizePolicy.setHeightForWidth(self.spending.sizePolicy().hasHeightForWidth())
        self.spending.setSizePolicy(sizePolicy)
        self.spending.setMinimumSize(QSize(40, 46))
        self.spending.setMaximumSize(QSize(524287, 300))
        self.spending.setFont(font1)
        self.spending.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.spending.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_8 = QWidget()
        self.dockWidgetContents_8.setObjectName(u"dockWidgetContents_8")
        self.gridLayout_91 = QGridLayout(self.dockWidgetContents_8)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.spending.setWidget(self.dockWidgetContents_8)

        self.gridLayout_2.addWidget(self.spending, 0, 1, 1, 1)

        self.shortcuts = Container(self.dashboard)
        self.shortcuts.setObjectName(u"shortcuts")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.shortcuts.sizePolicy().hasHeightForWidth())
        self.shortcuts.setSizePolicy(sizePolicy1)
        self.shortcuts.setMinimumSize(QSize(94, 59))
        self.shortcuts.setMaximumSize(QSize(500, 524287))
        self.shortcuts.setFont(font1)
        self.shortcuts.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.shortcuts.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents1 = QWidget()
        self.dockWidgetContents1.setObjectName(u"dockWidgetContents1")
        self.gridLayout_92 = QGridLayout(self.dockWidgetContents1)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.gridLayout_92.setContentsMargins(0, 0, 0, -1)
        self.shortcuts.setWidget(self.dockWidgetContents1)

        self.gridLayout_2.addWidget(self.shortcuts, 2, 4, 1, 1)

        self.monthlyExpenses = Container(self.dashboard)
        self.monthlyExpenses.setObjectName(u"monthlyExpenses")
        sizePolicy1.setHeightForWidth(self.monthlyExpenses.sizePolicy().hasHeightForWidth())
        self.monthlyExpenses.setSizePolicy(sizePolicy1)
        self.monthlyExpenses.setMinimumSize(QSize(40, 500))
        self.monthlyExpenses.setMaximumSize(QSize(500, 500))
        self.monthlyExpenses.setFont(font1)
        self.monthlyExpenses.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.monthlyExpenses.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_9 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, -1)
        self.monthlyExpenses.setWidget(self.dockWidgetContents)

        self.gridLayout_2.addWidget(self.monthlyExpenses, 0, 4, 2, 1)

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

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(Qt.NoToolBarArea)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionMenu)
        self.toolBar.addAction(self.actionDashboard)
        self.toolBar.addAction(self.actionGraph)
        self.toolBar.addAction(self.actionInsights)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#if QT_CONFIG(tooltip)
        self.actionDashboard.setToolTip(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.actionMenu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
#if QT_CONFIG(tooltip)
        self.actionMenu.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.actionGraph.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
#if QT_CONFIG(tooltip)
        self.actionGraph.setToolTip(QCoreApplication.translate("MainWindow", u"Graphs", None))
#endif // QT_CONFIG(tooltip)
        self.actionInsights.setText(QCoreApplication.translate("MainWindow", u"Insights", None))
#if QT_CONFIG(tooltip)
        self.actionInsights.setToolTip(QCoreApplication.translate("MainWindow", u"Insights", None))
#endif // QT_CONFIG(tooltip)
        self.menuLabel.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#if QT_CONFIG(tooltip)
        self.alerts.setToolTip(QCoreApplication.translate("MainWindow", u"Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.alerts.setText("")
#if QT_CONFIG(tooltip)
        self.settings.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings.setText("")
        self.transactions.setWindowTitle(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.accounts.setWindowTitle(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.spending.setWindowTitle(QCoreApplication.translate("MainWindow", u"Spending", None))
        self.shortcuts.setWindowTitle(QCoreApplication.translate("MainWindow", u"Shortcuts", None))
        self.monthlyExpenses.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expenses Distribution", None))
        self.total.setTitle(QCoreApplication.translate("MainWindow", u"Total", None))
        self.savings.setTitle(QCoreApplication.translate("MainWindow", u"Savings", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

