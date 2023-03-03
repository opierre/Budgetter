# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QAction, QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QAbstractSpinBox, QCheckBox, QComboBox,
                               QDateEdit, QDateTimeEdit, QDockWidget, QFrame,
                               QGridLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QToolBar,
                               QToolButton, QVBoxLayout, QWidget)

from budgetter.view.widgets.animated_button import AnimatedButton
from budgetter.view.widgets.container import Container
from budgetter.view.widgets.sliding_stacked_widget import SlidingStackedWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1216, 979)
        MainWindow.setStyleSheet("#MainWindow \n"
                                 "{\n"
                                 "	background: #212F41;\n"
                                 "}\n"
                                 "\n"
                                 "#menuBar \n"
                                 "{\n"
                                 "	background: #2C405A;\n"
                                 "	border-bottom: 1px solid #47566B;\n"
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit \n"
                                 "{\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-radius: 2px;\n"
                                 "	padding-top: 2"
                                 "px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 5px;\n"
                                 "	padding-right: 3px;\n"
                                 "	background: rgba(28, 41, 59, 128);\n"
                                 "	color: white;\n"
                                 "	selection-background-color: #0190EA;\n"
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit::hover\n"
                                 "{\n"
                                 "	border: 1px solid rgba(255, 255, 255, 200);\n"
                                 "	border-radius: 2px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 5px;\n"
                                 "	padding-right: 3px;\n"
                                 "	background: rgba(28, 41, 59, 128);\n"
                                 "	color: white;\n"
                                 "	selection-background-color: #0190EA;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit::focus\n"
                                 "{\n"
                                 "	border: 1px solid #0190EA;\n"
                                 "	border-radius: 2px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 5px;\n"
                                 ""
                                 "	padding-right: 3px;\n"
                                 "	background: rgba(28, 41, 59, 128);\n"
                                 "	color: white;\n"
                                 "	selection-background-color: #0190EA;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit#titleBarSearch::hover\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit::disabled\n"
                                 "{\n"
                                 "	border: 1px solid grey;\n"
                                 "	border-radius: 0px;\n"
                                 "	padding-top: 1px;\n"
                                 "	padding-bottom: 1px;\n"
                                 "	padding-left: 5px;\n"
                                 "	padding-right: 3px;\n"
                                 "	background: transparent;\n"
                                 "	color: white;\n"
                                 "	selection-background-color: grey;\n"
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#apply\n"
                                 "{"
                                 "\n"
                                 "	background-color: rgba(109, 210, 48, 180);\n"
                                 "	border-radius: 12px;\n"
                                 "	border-color: transparent;\n"
                                 "	padding-left: 3px;\n"
                                 "	padding-right: 3px;\n"
                                 "	padding-top: 3px;\n"
                                 "	padding-bottom: 3px;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#apply:hover\n"
                                 "{\n"
                                 "	background-color: rgba(109, 210, 48, 210);\n"
                                 "	border-radius: 12px;\n"
                                 "	border-color: transparent;\n"
                                 "	padding-left: 3px;\n"
                                 "	padding-right: 3px;\n"
                                 "	padding-top: 3px;\n"
                                 "	padding-bottom: 3px;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#cancel\n"
                                 "{\n"
                                 "	background-color: rgba(226, 74, 141, 180);\n"
                                 "	border-radius: 12px;\n"
                                 "	border-color: transparent;\n"
                                 "	padding-left: 3px;\n"
                                 "	padding-right: 3px;\n"
                                 "	padding-top: 3px;\n"
                                 "	padding-bottom: 3px;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#cancel:hover\n"
                                 "{\n"
                                 "	background-color: rgba(226, 74, 141, 210);\n"
                                 "	border-radius: 12px;\n"
                                 "	border-color: transparent;\n"
                                 "	padding-left: 3px;\n"
                                 "	padding-right: 3px;\n"
                                 "	padd"
                                 "ing-top: 3px;\n"
                                 "	padding-bottom: 3px;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox \n"
                                 "{\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-radius: 2px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 5px;\n"
                                 "	padding-right: 2px;\n"
                                 "	background: rgba(28, 41, 59, 128);\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::hover\n"
                                 "{\n"
                                 "	border: 1px solid rgba(255, 255, 255, 200);\n"
                                 "	border-radius: 2px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 5px;\n"
                                 "	padding-right: 2px;\n"
                                 "	background: rgba(28, 41, 59, 128);\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::focus\n"
                                 "{\n"
                                 "	border: 1px solid #0190EA;\n"
                                 "	border-radius: 2px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 5px;\n"
                                 "	padding-right: 2px;\n"
                                 "	background: rgba(28, 41, 59, 128);\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down\n"
                                 "{\n"
                                 "	border: 0px;\n"
                                 "	background-color: transparent;\n"
                                 "	outline: none;"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::down-arrow\n"
                                 "{\n"
                                 "	image: url(:/images/images/expand_more-white-18dp.svg);\n"
                                 "	width: 18px;\n"
                                 "	height: 18px;\n"
                                 "	padding-right: 0px;\n"
                                 "	padding-top: 0px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QComboBox::down-arrow:on\n"
                                 "{\n"
                                 "	image: url(:/images/images/expand_less-white-18dp.svg);\n"
                                 "	width: 18px;\n"
                                 "	height: 18px;\n"
                                 "	padding-right: 0px;\n"
                                 "	padding-top: 0px;\n"
                                 "	outline: none;\n"
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
                                 "	padding-left: 2px;\n"
                                 "	padding-right: 2px;\n"
                                 "	outline: none;\n"
                                 "	margin-top: 5px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QAbstractItemView::item\n"
                                 "{\n"
                                 "	min-height: 35px;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QScollBar:vertical\n"
                                 "{\n"
                                 "	border: 0px;\n"
                                 "	background: transparent;\n"
                                 "	width: 10px;\n"
                                 ""
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
                                 "	border-right: 1px solid #32465F;\n"
                                 "	padding: 6px 10px;\n"
                                 "	border-radiu"
                                 "s: 0px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#alerts \n"
                                 "{\n"
                                 "	background-color: transparent;\n"
                                 "	border-left: 1px solid #32465F;\n"
                                 "	padding: 6px 10px;\n"
                                 "	border-radius: 0px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#menu:hover, QPushButton#settings:hover, QPushButton#alerts:hover \n"
                                 "{\n"
                                 "	background-color:  rgba(255, 255, 255, 35);\n"
                                 "	border-left: 1px solid #32465F;\n"
                                 "	padding: 6px 10px;\n"
                                 "	border-radius: 0px;\n"
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#settings:pressed, QPushButton#alerts:pressed \n"
                                 "{\n"
                                 "	background-color:  rgba(255, 255, 255, 80);\n"
                                 "	border-left: 1px solid #32465F;\n"
                                 "	padding: 6px 10px;\n"
                                 "	border-radius: 0px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton[expanded=\"true\"]:pressed \n"
                                 ""
                                 "{\n"
                                 "	background-color: rgba(255, 255, 255, 0);\n"
                                 "	border-style: outset;\n"
                                 "	border-width: 1px;\n"
                                 "	border-radius: 6px;\n"
                                 "	border-color: transparent;\n"
                                 "	padding: 3px  3px;\n"
                                 "	color: rgba(36, 42, 117, 255);\n"
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#logoExpense\n"
                                 "{\n"
                                 "	background-color: transparent;\n"
                                 "	border-radius: 5px;\n"
                                 "	border-color: transparent;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel#categoryExpense \n"
                                 "{\n"
                                 "	color: #a2a3ae;\n"
                                 "	font-family: \"Robo"
                                 "to\";\n"
                                 "	font-size: 12pt;\n"
                                 "	margin-bottom: 15px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel#amountExpense \n"
                                 "{\n"
                                 "	color: white;\n"
                                 "	font-family: \"Roboto Black\";\n"
                                 "	font-size: 12pt;\n"
                                 "	outline: none;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QLabel#monthExpense {\n"
                                 "	color: #a2a3ae;\n"
                                 "	font-family: \"Roboto Light\";\n"
                                 "	font-size: 12pt;\n"
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#rightPageMonthlyExpenses, QPushButton#leftPageMonthlyExpenses\n"
                                 "{\n"
                                 "	background-color: transparent;\n"
                                 "	border-radius: 0px;\n"
                                 "	border-color: transparent;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#menuDashboard, QPushButton#menu,\n"
                                 "QPushButton#menuGraph, QPushButton#menuInsights \n"
                                 "{\n"
                                 "    background-color: transparent;\n"
                                 "	border-radius: "
                                 "0px;\n"
                                 "    border-style: none;\n"
                                 "    padding: 8px 6px 8px 6px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#menuDashboard:checked, QPushButton#menuGraph:checked,\n"
                                 "QPushButton#menuInsights:checked \n"
                                 "{\n"
                                 "    background-color: #19344D;\n"
                                 "	border-radius: 0px;\n"
                                 "    border-left: 3px solid #0093EE;\n"
                                 "    padding: 8px 6px 8px 3px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#menuDashboard:hover:!checked, QPushButton#menuGraph:hover:!checked,\n"
                                 "QPushButton#menuInsights:hover:!checked \n"
                                 "{\n"
                                 "    background-color: #19344D;\n"
                                 "	border-radius: 0px;\n"
                                 "    border-style: none;\n"
                                 "    padding: 8px 6px 8px 6px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#menu:hover \n"
                                 "{\n"
                                 "    background-color: transparent;\n"
                                 "	border-radius: 0px;\n"
                                 "    border-style: none;\n"
                                 "    padding: 8px 6px 8px 6px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget {\n"
                                 "	color: white;\n"
                                 "	border-radius: 5px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget > QWidget \n"
                                 "{\n"
                                 "	color: white;\n"
                                 "	background-color: #"
                                 "26374C;\n"
                                 "	border: 1px solid #344457;\n"
                                 "	border-top-left-radius: 0px;\n"
                                 "	border-top-right-radius: 0px;\n"
                                 "	border-bottom-left-radius: 4px;\n"
                                 "	border-bottom-right-radius: 4px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator \n"
                                 "{\n"
                                 "	width: 10px;\n"
                                 "	height: 0px;\n"
                                 "	margin: -10px;\n"
                                 "	padding: 0px;\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget#titleBarEmptyWidget \n"
                                 "{\n"
                                 "	background-color: #26374C;\n"
                                 "	border-top: 1px solid #344457;\n"
                                 "	border-top-left-radius: 0px;\n"
                                 "	border-top-right-radius: 0px;\n"
                                 "	b"
                                 "order-bottom-left-radius: 0px;\n"
                                 "	border-bottom-right-radius: 0px;\n"
                                 "	margin-left: 0px;\n"
                                 "	margin-right: 0px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget#leftAddWidget \n"
                                 "{\n"
                                 "	background-color: #26374C;\n"
                                 "	border-top: 1px solid #344457;\n"
                                 "	border-right: 1px solid #344457;\n"
                                 "	border-top-left-radius: 0px;\n"
                                 "	border-top-right-radius: 4px;\n"
                                 "	border-bottom-left-radius: 0px;\n"
                                 "	border-bottom-right-radius: 0px;\n"
                                 "	margin-left: 0px;\n"
                                 "	margin-right: 0px;\n"
                                 "	outline: none;\n"
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QStatusBar \n"
                                 "{\n"
                                 "	background-color: transparent;\n"
                                 ""
                                 "	color: white;\n"
                                 "	border-top: 1px solid #344457;\n"
                                 "	border-top-left-radius: 0px;\n"
                                 "	border-top-right-radius: 0px;\n"
                                 "	border-bottom-left-radius: 0px;\n"
                                 "	border-bottom-right-radius: 0px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QStatusBar::item \n"
                                 "{\n"
                                 "	border: none;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#statusBarSettings, QPushButton#statusBarPrevious, QPushButton#statusBarNext  \n"
                                 "{\n"
                                 "	background-color: #26374C;\n"
                                 "	border-top-left-radius: 0px;\n"
                                 "	border-top-right-radius: 0px;\n"
                                 "	border-bottom-left-radius: 0px;\n"
                                 "	border-bottom-right-radius: 0px;\n"
                                 "	margin-left: 0px;\n"
                                 "	margin-right: 0px;\n"
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
                                 ""
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
                                 "	outline: none;\n"
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
                                 "    background-color: #01"
                                 "90EA;\n"
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
                                 "	padding-bottom: 3px;\n"
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
                                 "	selection-background-"
                                 "color: #0190EA;\n"
                                 "}\n"
                                 "\n"
                                 "QDoubleSpinBox::up-button {\n"
                                 "    subcontrol-origin: border;\n"
                                 "    subcontrol-position: top right;\n"
                                 "    width: 16px;\n"
                                 "	height: 16px;\n"
                                 "	padding-right: 0px;\n"
                                 "    image: url(:/images/images/arrow_drop_up_white_18dp.svg);\n"
                                 "}\n"
                                 "\n"
                                 "QDoubleSpinBox::up-button:hover \n"
                                 "{\n"
                                 "    image: url(:/images/images/arrow_drop_up_white_18dp_hover.svg);\n"
                                 "}\n"
                                 "\n"
                                 "QDoubleSpinBox::up-button:pressed \n"
                                 "{\n"
                                 "    image: url(:/images/images/arrow_drop_up_white_18dp_hover.svg);\n"
                                 "}\n"
                                 "\n"
                                 "QDoubleSpinBox::down-button \n"
                                 "{\n"
                                 "    subcontrol-origin: border;\n"
                                 "    subcontrol-position: bottom right;\n"
                                 "    width: 16px;\n"
                                 "	height: 16px;\n"
                                 "	padding-top: 0px;\n"
                                 "    image: url(:/images/images/arrow_drop_down_white_18dp.svg);\n"
                                 "}\n"
                                 "\n"
                                 "QDoubleSpinBox::down-button:hover \n"
                                 "{\n"
                                 "    image: url(:/images/images/arrow_drop_down_white_18dp_hover.svg);\n"
                                 "}\n"
                                 "\n"
                                 "QDoubleSpinBox::down-button:pressed\n"
                                 "{\n"
                                 "    image: url(:/images/images/arrow_drop_down_white_18d"
                                 "p_hover.svg);\n"
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
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
                                 "}\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QDateEdit::drop-down \n"
                                 "{\n"
                                 "    image:"
                                 " url(:/images/images/today-white-24dp.svg);\n"
                                 "    width: 18px;\n"
                                 "    height: 18px;\n"
                                 "	padding-right: 2px;\n"
                                 "    subcontrol-position: right center;\n"
                                 "    subcontrol-origin: padding;\n"
                                 "    background-color: transparent;\n"
                                 "    border: none;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QCalendarWidget QToolButton \n"
                                 "{\n"
                                 "  	color: white;\n"
                                 "  	icon-size: 18px, 18px;\n"
                                 "	font: 10pt \"Roboto Bold\";\n"
                                 "  	background-color: #0190EA;\n"
                                 "	outline: none;\n"
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
                                 "  	selection-background-color: #"
                                 "212F41;\n"
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
                                 "  	color: white;  \n"
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
                                 ""
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton\n"
                                 "{\n"
                                 "	width: 50px;\n"
                                 "	height: 30px;\n"
                                 "	padding-left: 2px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-right: 2px; \n"
                                 "	background: transparent;\n"
                                 "	border: none;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton:hover\n"
                                 "{\n"
                                 "	width: 50px;\n"
                                 "	height: 30px;\n"
                                 "	padding-left: 2px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-right: 2px;"
                                 " \n"
                                 "	background: #19344D;\n"
                                 "	border: none;\n"
                                 "	outline: none;\n"
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
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox#income_choice, QComboBox#expenses_choice  \n"
                                 "{\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-bottom: 1px solid rgba(255, 255, 255, 200);\n"
                                 "	border-radius: 4px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 7px;\n"
                                 "	padding-right: 2px;\n"
                                 "	background: #1C293B;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox#income_choice::hover, QComboBox#expenses_choice::hover\n"
                                 "{\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-bottom: 1px solid rgba(1, 144, 234, 200);\n"
                                 "	border-radius: 4px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 7px;\n"
                                 "	padding-right: 2px;\n"
                                 "	ba"
                                 "ckground: #1C293B;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox#income_choice::focus, QComboBox#expenses_choice::focus\n"
                                 "{\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-bottom: 1px solid rgba(1, 144, 234, 200);\n"
                                 "	border-radius: 4px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 7px;\n"
                                 "	padding-right: 2px;\n"
                                 "	background: #1C293B;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox#income_choice::down-arrow, QComboBox#expenses_choice::down-arrow\n"
                                 "{\n"
                                 "	image: url(:/images/images/expand_more_white_18dp.svg);\n"
                                 "	width: 18px;\n"
                                 "	height:18px;\n"
                                 "	padding-right: 7px;\n"
                                 "	padding-top: 0px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox#income_choice::down-arrow:on, QComboBox#expenses_choice::down-arrow:on\n"
                                 "{\n"
                                 "	image: url(:/images/images/expand_less_white_18dp.svg);\n"
                                 "	width: 18px;\n"
                                 "	height:18px;\n"
                                 "	padding-right: 7px;\n"
                                 "	padding-top: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QDateEdit#dateEdit_income_from, QDateEdit#dateEdit_income_to, QDateEdit#dateEdit"
                                 "_expenses_from, QDateEdit#dateEdit_expenses_to \n"
                                 "{\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-bottom: 1px solid rgba(255, 255, 255, 200);\n"
                                 "	border-radius: 4px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 7px;\n"
                                 "	padding-right: 7px;\n"
                                 "	background: rgba(47, 67, 93, 150);\n"
                                 "	color: white;\n"
                                 "	selection-background-color: #0190EA;\n"
                                 "}\n"
                                 "\n"
                                 "QDateEdit#dateEdit_income_from:hover, QDateEdit#dateEdit_income_to:hover, QDateEdit#dateEdit_expenses_from:hover, QDateEdit#dateEdit_expenses_to:hover\n"
                                 "{\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-bottom: 1px solid rgba(1, 144, 234, 200);\n"
                                 "	border-radius: 4px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 7px;\n"
                                 "	padding-right: 7px;\n"
                                 "	background: rgba(47, 67, 93, 150);\n"
                                 "	color: white;\n"
                                 "	selection-background-color: #0190EA;\n"
                                 "}\n"
                                 "\n"
                                 "QDateEdit#dateEdit_income_from:focus, QDateEdit#dateEdit_income_to:focus, QDateEdit#dateEdit_expenses_from:focus, QDateEdit#dateEdit_expenses_to:focus\n"
                                 ""
                                 "{\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-bottom: 1px solid rgba(1, 144, 234, 200);\n"
                                 "	border-radius: 4px;\n"
                                 "	padding-top: 2px;\n"
                                 "	padding-bottom: 2px;\n"
                                 "	padding-left: 7px;\n"
                                 "	padding-right: 7px;\n"
                                 "	background: rgba(47, 67, 93, 150);\n"
                                 "	color: white;\n"
                                 "	selection-background-color: #0190EA;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget#widget_income, QWidget#widget_expenses\n"
                                 "{\n"
                                 "	background-color: #1C293B;\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton#refresh_income, QPushButton#refresh_expenses\n"
                                 "{\n"
                                 "	background-color: rgba(47, 67, 93, 0);\n"
                                 "	border: 1px solid;\n"
                                 "	border-radius: 28px;\n"
                                 "	border-color: transparent;\n"
                                 "	padding-left: 0px;\n"
                                 "	padding-right: 0px;\n"
                                 "	padding-top: 0px;\n"
                                 "	padding-bottom: 0px;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton#refresh_income:hover, QPushButton#refresh_expenses:hover\n"
                                 "{\n"
                                 "	background-color: rgba(1, 144, 234, 0);\n"
                                 "	border: 1px solid;\n"
                                 "	border-radius: 28px;\n"
                                 ""
                                 "	border-color: transparent;\n"
                                 "	padding-left: 0px;\n"
                                 "	padding-right: 0px;\n"
                                 "	padding-top: 0px;\n"
                                 "	padding-bottom: 0px;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton#refresh_income:pressed, QPushButton#refresh_expenses:pressed\n"
                                 "{\n"
                                 "	background-color: rgba(2, 113, 184, 0);\n"
                                 "	border: 1px solid;\n"
                                 "	border-radius: 28px;\n"
                                 "	border-color: transparent;\n"
                                 "	padding-left: 0px;\n"
                                 "	padding-right: 0px;\n"
                                 "	padding-top: 0px;\n"
                                 "	padding-bottom: 0px;\n"
                                 "	color: white;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#this_year_income, QPushButton#last_12_months_income, QPushButton#previous_year_income, QPushButton#this_year_expenses, QPushButton#last_12_months_expenses, QPushButton#previous_year_expenses\n"
                                 "{\n"
                                 "	background-color: transparent;\n"
                                 "	border: 1px solid rgba(66, 96, 135, 250); \n"
                                 "	border-radius: 12px;\n"
                                 "	color: rgba(66, 96, 135, 250);\n"
                                 "	outline: none;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#this_year_income::checked, QPushButton#last_12_months_income::che"
                                 "cked, QPushButton#previous_year_income::checked, QPushButton#this_year_expenses::checked, QPushButton#last_12_months_expenses::checked, QPushButton#previous_year_expenses::checked\n"
                                 "{\n"
                                 "	background-color: rgba(66, 96, 135, 250);\n"
                                 "	border: 1px solid rgba(66, 96, 135, 250); \n"
                                 "	border-radius: 12px;\n"
                                 "	color: rgba(255, 255, 255, 200);\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QFrame#frame_expenses, QFrame#frame_income\n"
                                 "{\n"
                                 "	background-color: rgba(66, 96, 135, 120);\n"
                                 "	border-bottom-left-radius: 28px;\n"
                                 "	border-bottom-right-radius: 28px;\n"
                                 "	border-top-right-radius: 4px;\n"
                                 "	border-top-left-radius: 4px;\n"
                                 "	border-top: 1px inset rgba(66, 96, 135, 140);\n"
                                 "	border-left: 1px inset rgba(66, 96, 135, 140);\n"
                                 "	border-right: 1px outset rgba(66, 96, 135, 140);\n"
                                 "	border-bottom: none;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox:checked\n"
                                 "{\n"
                                 "	color: rgba(255, 255, 255, 200);\n"
                                 "	outline: none;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox:checked:hover\n"
                                 "{\n"
                                 "	color: rgba(255, 255, 255, 150);\n"
                                 "	outline: none;\n"
                                 ""
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:checked\n"
                                 "{\n"
                                 "	image: url(:/images/images/check_box_white_24dp.svg);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:checked:hover\n"
                                 "{\n"
                                 "	image: url(:/images/images/check_box_white_24dp_hover.svg);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox:unchecked\n"
                                 "{\n"
                                 "	color: rgba(66, 96, 135, 250);\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox:unchecked:hover\n"
                                 "{\n"
                                 "	color: rgba(66, 96, 135, 200);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:unchecked\n"
                                 "{\n"
                                 "	image: url(:/images/images/check_box_outline_blank_white_24dp.svg);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:unchecked:hover\n"
                                 "{\n"
                                 "	image: url(:/images/images/check_box_outline_blank_white_24dp_hover.svg);\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:vertical \n"
                                 "{\n"
                                 "    border: none;\n"
                                 "    background-color: rgba(33, 47, 65, 180);\n"
                                 "    width: 10px;\n"
                                 "    margin: 20px 0px 20 0px;\n"
                                 "	border-radius: 5px;\n"
                                 "	outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical \n"
                                 "{\n"
                                 "    background: #0190ea;\n"
                                 "	border-radius: 5px;\n"
                                 "    min-height: 20px;\n"
                                 "}\n"
                                 "\n"
                                 ""
                                 "QScrollBar::add-line:vertical\n"
                                 "{\n"
                                 "    border: none;\n"
                                 "    background-color: transparent;\n"
                                 "    height: 0px;\n"
                                 "    subcontrol-position: bottom;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:vertical \n"
                                 "{\n"
                                 "    border: none;\n"
                                 "    background-color: transparent;\n"
                                 "    height: 0px;\n"
                                 "    subcontrol-position: top;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical \n"
                                 "{\n"
                                 "     background: none;\n"
                                 " }")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.actionDashboard = QAction(MainWindow)
        self.actionDashboard.setObjectName("actionDashboard")
        self.actionDashboard.setCheckable(True)
        self.actionDashboard.setChecked(True)
        icon = QIcon()
        icon.addFile(":/images/images/dashboard-white-36dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionDashboard.setIcon(icon)
        self.actionMenu = QAction(MainWindow)
        self.actionMenu.setObjectName("actionMenu")
        self.actionMenu.setCheckable(True)
        self.actionMenu.setChecked(False)
        icon1 = QIcon()
        icon1.addFile(":/images/images/menu-white-36dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionMenu.setIcon(icon1)
        self.actionGraph = QAction(MainWindow)
        self.actionGraph.setObjectName("actionGraph")
        self.actionGraph.setCheckable(True)
        icon2 = QIcon()
        icon2.addFile(":/images/images/assessment-white-36dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionGraph.setIcon(icon2)
        self.actionInsights = QAction(MainWindow)
        self.actionInsights.setObjectName("actionInsights")
        self.actionInsights.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(":/images/images/insights-white-36dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionInsights.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.menuBar = QWidget(self.centralwidget)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.menuBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 0, -1, 0)
        self.menuLabel = QLabel(self.menuBar)
        self.menuLabel.setObjectName("menuLabel")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(14)
        self.menuLabel.setFont(font)

        self.horizontalLayout.addWidget(self.menuLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.alerts = QPushButton(self.menuBar)
        self.alerts.setObjectName("alerts")
        self.alerts.setMinimumSize(QSize(45, 39))
        self.alerts.setMaximumSize(QSize(45, 39))
        self.alerts.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(":/images/images/notifications-white-24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.alerts.setIcon(icon4)
        self.alerts.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.alerts)

        self.settings = QPushButton(self.menuBar)
        self.settings.setObjectName("settings")
        self.settings.setMinimumSize(QSize(45, 39))
        self.settings.setMaximumSize(QSize(45, 39))
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(":/images/images/settings-white-24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings.setIcon(icon5)
        self.settings.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.settings)

        self.gridLayout.addWidget(self.menuBar, 0, 0, 1, 1)

        self.stackedWidget = SlidingStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashboard = QWidget()
        self.dashboard.setObjectName("dashboard")
        self.gridLayout_2 = QGridLayout(self.dashboard)
        self.gridLayout_2.setSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.transactions = Container(self.dashboard)
        self.transactions.setObjectName("transactions")
        self.transactions.setMinimumSize(QSize(40, 46))
        self.transactions.setMaximumSize(QSize(524287, 524287))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(13)
        self.transactions.setFont(font1)
        self.transactions.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.transactions.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_4 = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.transactions.setWidget(self.dockWidgetContents_2)

        self.gridLayout_2.addWidget(self.transactions, 1, 0, 2, 2)

        self.accounts = Container(self.dashboard)
        self.accounts.setObjectName("accounts")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accounts.sizePolicy().hasHeightForWidth())
        self.accounts.setSizePolicy(sizePolicy)
        self.accounts.setMinimumSize(QSize(64, 105))
        self.accounts.setMaximumSize(QSize(650, 300))
        self.accounts.setFont(font1)
        self.accounts.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.accounts.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_5 = QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.accounts.setWidget(self.dockWidgetContents_3)

        self.gridLayout_2.addWidget(self.accounts, 0, 0, 1, 1)

        self.spending = Container(self.dashboard)
        self.spending.setObjectName("spending")
        sizePolicy.setHeightForWidth(self.spending.sizePolicy().hasHeightForWidth())
        self.spending.setSizePolicy(sizePolicy)
        self.spending.setMinimumSize(QSize(40, 46))
        self.spending.setMaximumSize(QSize(524287, 300))
        self.spending.setFont(font1)
        self.spending.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.spending.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_8 = QWidget()
        self.dockWidgetContents_8.setObjectName("dockWidgetContents_8")
        self.gridLayout_91 = QGridLayout(self.dockWidgetContents_8)
        self.gridLayout_91.setObjectName("gridLayout_91")
        self.spending.setWidget(self.dockWidgetContents_8)

        self.gridLayout_2.addWidget(self.spending, 0, 1, 1, 1)

        self.savings = Container(self.dashboard)
        self.savings.setObjectName("savings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.savings.sizePolicy().hasHeightForWidth())
        self.savings.setSizePolicy(sizePolicy1)
        self.savings.setMinimumSize(QSize(94, 59))
        self.savings.setMaximumSize(QSize(500, 524287))
        self.savings.setFont(font1)
        self.savings.setStyleSheet("")
        self.savings.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.savings.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents1 = QWidget()
        self.dockWidgetContents1.setObjectName("dockWidgetContents1")
        self.gridLayout_92 = QGridLayout(self.dockWidgetContents1)
        self.gridLayout_92.setSpacing(0)
        self.gridLayout_92.setObjectName("gridLayout_92")
        self.gridLayout_92.setContentsMargins(0, 0, 0, 0)
        self.savings.setWidget(self.dockWidgetContents1)

        self.gridLayout_2.addWidget(self.savings, 2, 4, 1, 1)

        self.monthlyExpenses = Container(self.dashboard)
        self.monthlyExpenses.setObjectName("monthlyExpenses")
        sizePolicy1.setHeightForWidth(self.monthlyExpenses.sizePolicy().hasHeightForWidth())
        self.monthlyExpenses.setSizePolicy(sizePolicy1)
        self.monthlyExpenses.setMinimumSize(QSize(40, 500))
        self.monthlyExpenses.setMaximumSize(QSize(500, 500))
        self.monthlyExpenses.setFont(font1)
        self.monthlyExpenses.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.monthlyExpenses.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_9 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, -1)
        self.monthlyExpenses.setWidget(self.dockWidgetContents)

        self.gridLayout_2.addWidget(self.monthlyExpenses, 0, 4, 2, 1)

        self.stackedWidget.addWidget(self.dashboard)
        self.graphs = QWidget()
        self.graphs.setObjectName("graphs")
        self.gridLayout_3 = QGridLayout(self.graphs)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setContentsMargins(15, 15, 15, 15)
        self.expenses = Container(self.graphs)
        self.expenses.setObjectName("expenses")
        self.expenses.setFont(font1)
        self.expenses.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.expenses.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_23 = QWidget()
        self.dockWidgetContents_23.setObjectName("dockWidgetContents_23")
        self.gridLayout_43 = QGridLayout(self.dockWidgetContents_23)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.gridLayout_43.setContentsMargins(12, 12, 12, 12)
        self.widget_expenses_graph = QWidget(self.dockWidgetContents_23)
        self.widget_expenses_graph.setObjectName("widget_expenses_graph")

        self.gridLayout_43.addWidget(self.widget_expenses_graph, 0, 1, 1, 1)

        self.widget_expenses = QWidget(self.dockWidgetContents_23)
        self.widget_expenses.setObjectName("widget_expenses")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_expenses.sizePolicy().hasHeightForWidth())
        self.widget_expenses.setSizePolicy(sizePolicy2)
        self.widget_expenses.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_expenses)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_expenses = QFrame(self.widget_expenses)
        self.frame_expenses.setObjectName("frame_expenses")
        self.frame_expenses.setFrameShape(QFrame.StyledPanel)
        self.frame_expenses.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_expenses)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 20, 9, 20)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.toolButton_icon_category_2 = QToolButton(self.frame_expenses)
        self.toolButton_icon_category_2.setObjectName("toolButton_icon_category_2")
        self.toolButton_icon_category_2.setEnabled(False)
        self.toolButton_icon_category_2.setMinimumSize(QSize(36, 36))
        self.toolButton_icon_category_2.setMaximumSize(QSize(36, 36))
        icon6 = QIcon()
        icon6.addFile(":/images/images/payments_black_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(":/images/images/payments_black_24dp.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.toolButton_icon_category_2.setIcon(icon6)
        self.toolButton_icon_category_2.setIconSize(QSize(36, 36))

        self.horizontalLayout_2.addWidget(self.toolButton_icon_category_2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.expenses_choice = QComboBox(self.frame_expenses)
        self.expenses_choice.addItem("")
        self.expenses_choice.addItem("")
        self.expenses_choice.addItem("")
        self.expenses_choice.setObjectName("expenses_choice")
        self.expenses_choice.setMinimumSize(QSize(200, 0))
        self.expenses_choice.setMaximumSize(QSize(200, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        self.expenses_choice.setFont(font2)

        self.horizontalLayout_2.addWidget(self.expenses_choice)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3.addWidget(self.frame_expenses)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(20)
        self.gridLayout_10.setVerticalSpacing(15)
        self.gridLayout_10.setContentsMargins(16, 8, 19, -1)
        self.dateEdit_expenses_from = QDateEdit(self.widget_expenses)
        self.dateEdit_expenses_from.setObjectName("dateEdit_expenses_from")
        self.dateEdit_expenses_from.setMaximumSize(QSize(130, 16777215))
        self.dateEdit_expenses_from.setFont(font2)
        self.dateEdit_expenses_from.setFrame(True)
        self.dateEdit_expenses_from.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEdit_expenses_from.setCalendarPopup(False)

        self.gridLayout_10.addWidget(self.dateEdit_expenses_from, 0, 1, 1, 1)

        self.label_from_income_2 = QLabel(self.widget_expenses)
        self.label_from_income_2.setObjectName("label_from_income_2")
        self.label_from_income_2.setFont(font2)
        self.label_from_income_2.setStyleSheet("color: white;")

        self.gridLayout_10.addWidget(self.label_from_income_2, 0, 0, 1, 1)

        self.dateEdit_expenses_to = QDateEdit(self.widget_expenses)
        self.dateEdit_expenses_to.setObjectName("dateEdit_expenses_to")
        self.dateEdit_expenses_to.setMaximumSize(QSize(130, 16777215))
        self.dateEdit_expenses_to.setFont(font2)
        self.dateEdit_expenses_to.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEdit_expenses_to.setCurrentSection(QDateTimeEdit.MonthSection)
        self.dateEdit_expenses_to.setCalendarPopup(False)

        self.gridLayout_10.addWidget(self.dateEdit_expenses_to, 1, 1, 1, 1)

        self.refresh_expenses = AnimatedButton(self.widget_expenses)
        self.refresh_expenses.setObjectName("refresh_expenses")
        self.refresh_expenses.setMinimumSize(QSize(54, 54))
        self.refresh_expenses.setMaximumSize(QSize(54, 54))
        self.refresh_expenses.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.refresh_expenses, 0, 2, 2, 1)

        self.label_3 = QLabel(self.widget_expenses)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet("color: white;")

        self.gridLayout_10.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 0, 3, 2, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_10)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(6)
        self.gridLayout_7.setVerticalSpacing(15)
        self.gridLayout_7.setContentsMargins(9, 18, 9, -1)
        self.this_year_expenses = QPushButton(self.widget_expenses)
        self.this_year_expenses.setObjectName("this_year_expenses")
        self.this_year_expenses.setMinimumSize(QSize(110, 28))
        self.this_year_expenses.setMaximumSize(QSize(110, 28))
        self.this_year_expenses.setFont(font2)
        self.this_year_expenses.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(":/images/images/date_range_black_18dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(":/images/images/date_range_black_18dp_checked.svg", QSize(), QIcon.Active, QIcon.State.On)
        self.this_year_expenses.setIcon(icon7)
        self.this_year_expenses.setIconSize(QSize(18, 18))
        self.this_year_expenses.setCheckable(True)
        self.this_year_expenses.setChecked(False)
        self.this_year_expenses.setAutoExclusive(True)

        self.gridLayout_7.addWidget(self.this_year_expenses, 0, 1, 1, 1)

        self.last_12_months_expenses = QPushButton(self.widget_expenses)
        self.last_12_months_expenses.setObjectName("last_12_months_expenses")
        self.last_12_months_expenses.setMinimumSize(QSize(150, 28))
        self.last_12_months_expenses.setMaximumSize(QSize(150, 28))
        self.last_12_months_expenses.setFont(font2)
        self.last_12_months_expenses.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(":/images/images/history_black_18dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(":/images/images/history_black_18dp_checked.svg", QSize(), QIcon.Active, QIcon.State.On)
        self.last_12_months_expenses.setIcon(icon8)
        self.last_12_months_expenses.setIconSize(QSize(18, 18))
        self.last_12_months_expenses.setCheckable(True)
        self.last_12_months_expenses.setChecked(True)
        self.last_12_months_expenses.setAutoExclusive(True)

        self.gridLayout_7.addWidget(self.last_12_months_expenses, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.previous_year_expenses = QPushButton(self.widget_expenses)
        self.previous_year_expenses.setObjectName("previous_year_expenses")
        self.previous_year_expenses.setMinimumSize(QSize(140, 28))
        self.previous_year_expenses.setMaximumSize(QSize(140, 28))
        self.previous_year_expenses.setFont(font2)
        self.previous_year_expenses.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(":/images/images/calendar_today_black_18dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(":/images/images/calendar_today_black_18dp_checked.svg", QSize(), QIcon.Active, QIcon.State.On)
        self.previous_year_expenses.setIcon(icon9)
        self.previous_year_expenses.setIconSize(QSize(18, 18))
        self.previous_year_expenses.setCheckable(True)
        self.previous_year_expenses.setAutoRepeat(True)
        self.previous_year_expenses.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.previous_year_expenses)

        self.gridLayout_7.addLayout(self.horizontalLayout_11, 1, 0, 1, 2)

        self.verticalLayout_3.addLayout(self.gridLayout_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(19, 18, 19, 15)
        self.check_labels_expenses = QCheckBox(self.widget_expenses)
        self.check_labels_expenses.setObjectName("check_labels_expenses")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(10)
        self.check_labels_expenses.setFont(font3)
        self.check_labels_expenses.setChecked(True)

        self.verticalLayout_4.addWidget(self.check_labels_expenses)

        self.check_average_expenses = QCheckBox(self.widget_expenses)
        self.check_average_expenses.setObjectName("check_average_expenses")
        self.check_average_expenses.setFont(font3)
        self.check_average_expenses.setChecked(False)

        self.verticalLayout_4.addWidget(self.check_average_expenses)

        self.check_total_expenses = QCheckBox(self.widget_expenses)
        self.check_total_expenses.setObjectName("check_total_expenses")
        self.check_total_expenses.setFont(font3)
        self.check_total_expenses.setChecked(True)

        self.verticalLayout_4.addWidget(self.check_total_expenses)

        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.gridLayout_43.addWidget(self.widget_expenses, 0, 2, 1, 1)

        self.expenses.setWidget(self.dockWidgetContents_23)

        self.gridLayout_3.addWidget(self.expenses, 1, 0, 1, 1)

        self.income = Container(self.graphs)
        self.income.setObjectName("income")
        self.income.setFont(font1)
        self.income.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.income.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_231 = QWidget()
        self.dockWidgetContents_231.setObjectName("dockWidgetContents_231")
        self.gridLayout_431 = QGridLayout(self.dockWidgetContents_231)
        self.gridLayout_431.setObjectName("gridLayout_431")
        self.gridLayout_431.setContentsMargins(12, 12, 12, 12)
        self.widget_income_graph = QWidget(self.dockWidgetContents_231)
        self.widget_income_graph.setObjectName("widget_income_graph")

        self.gridLayout_431.addWidget(self.widget_income_graph, 0, 1, 4, 1)

        self.widget_income = QWidget(self.dockWidgetContents_231)
        self.widget_income.setObjectName("widget_income")
        sizePolicy2.setHeightForWidth(self.widget_income.sizePolicy().hasHeightForWidth())
        self.widget_income.setSizePolicy(sizePolicy2)
        self.widget_income.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_income)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_income = QFrame(self.widget_income)
        self.frame_income.setObjectName("frame_income")
        self.frame_income.setFrameShape(QFrame.StyledPanel)
        self.frame_income.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_income)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, 20)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.toolButton_icon_category = QToolButton(self.frame_income)
        self.toolButton_icon_category.setObjectName("toolButton_icon_category")
        self.toolButton_icon_category.setEnabled(False)
        self.toolButton_icon_category.setMinimumSize(QSize(36, 36))
        self.toolButton_icon_category.setMaximumSize(QSize(36, 36))
        icon10 = QIcon()
        icon10.addFile(":/images/images/savings_black_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(":/images/images/savings_black_24dp.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.toolButton_icon_category.setIcon(icon10)
        self.toolButton_icon_category.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.toolButton_icon_category)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.income_choice = QComboBox(self.frame_income)
        self.income_choice.addItem("")
        self.income_choice.addItem("")
        self.income_choice.addItem("")
        self.income_choice.setObjectName("income_choice")
        self.income_choice.setMinimumSize(QSize(200, 0))
        self.income_choice.setMaximumSize(QSize(200, 16777215))
        self.income_choice.setFont(font2)

        self.horizontalLayout_3.addWidget(self.income_choice)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.verticalLayout_2.addWidget(self.frame_income)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(20)
        self.gridLayout_8.setVerticalSpacing(15)
        self.gridLayout_8.setContentsMargins(16, 8, 19, -1)
        self.label_from_income = QLabel(self.widget_income)
        self.label_from_income.setObjectName("label_from_income")
        self.label_from_income.setFont(font2)
        self.label_from_income.setStyleSheet("color: white;")

        self.gridLayout_8.addWidget(self.label_from_income, 0, 0, 1, 1)

        self.dateEdit_income_from = QDateEdit(self.widget_income)
        self.dateEdit_income_from.setObjectName("dateEdit_income_from")
        self.dateEdit_income_from.setMaximumSize(QSize(130, 16777215))
        self.dateEdit_income_from.setFont(font2)
        self.dateEdit_income_from.setFrame(True)
        self.dateEdit_income_from.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEdit_income_from.setCalendarPopup(False)

        self.gridLayout_8.addWidget(self.dateEdit_income_from, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget_income)
        self.label_2.setObjectName("label_2")
        self.label_2.setMinimumSize(QSize(39, 0))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet("color: white;")

        self.gridLayout_8.addWidget(self.label_2, 1, 0, 2, 1)

        self.dateEdit_income_to = QDateEdit(self.widget_income)
        self.dateEdit_income_to.setObjectName("dateEdit_income_to")
        self.dateEdit_income_to.setMaximumSize(QSize(130, 16777215))
        self.dateEdit_income_to.setFont(font2)
        self.dateEdit_income_to.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEdit_income_to.setCurrentSection(QDateTimeEdit.MonthSection)
        self.dateEdit_income_to.setCalendarPopup(False)

        self.gridLayout_8.addWidget(self.dateEdit_income_to, 1, 1, 2, 1)

        self.refresh_income = AnimatedButton(self.widget_income)
        self.refresh_income.setObjectName("refresh_income")
        self.refresh_income.setMinimumSize(QSize(54, 54))
        self.refresh_income.setMaximumSize(QSize(54, 54))
        self.refresh_income.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_5 = QVBoxLayout(self.refresh_income)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)

        self.gridLayout_8.addWidget(self.refresh_income, 0, 2, 3, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 0, 3, 3, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_8)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setVerticalSpacing(15)
        self.gridLayout_6.setContentsMargins(9, 18, 9, -1)
        self.this_year_income = QPushButton(self.widget_income)
        self.this_year_income.setObjectName("this_year_income")
        self.this_year_income.setMinimumSize(QSize(110, 28))
        self.this_year_income.setMaximumSize(QSize(110, 28))
        self.this_year_income.setFont(font2)
        self.this_year_income.setCursor(QCursor(Qt.PointingHandCursor))
        self.this_year_income.setIcon(icon7)
        self.this_year_income.setIconSize(QSize(18, 18))
        self.this_year_income.setCheckable(True)
        self.this_year_income.setChecked(False)
        self.this_year_income.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.this_year_income, 0, 1, 1, 1)

        self.last_12_months_income = QPushButton(self.widget_income)
        self.last_12_months_income.setObjectName("last_12_months_income")
        self.last_12_months_income.setMinimumSize(QSize(150, 28))
        self.last_12_months_income.setMaximumSize(QSize(150, 28))
        self.last_12_months_income.setFont(font2)
        self.last_12_months_income.setCursor(QCursor(Qt.PointingHandCursor))
        self.last_12_months_income.setIcon(icon8)
        self.last_12_months_income.setIconSize(QSize(18, 18))
        self.last_12_months_income.setCheckable(True)
        self.last_12_months_income.setChecked(True)
        self.last_12_months_income.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.last_12_months_income, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.previous_year_income = QPushButton(self.widget_income)
        self.previous_year_income.setObjectName("previous_year_income")
        self.previous_year_income.setMinimumSize(QSize(140, 28))
        self.previous_year_income.setMaximumSize(QSize(140, 28))
        self.previous_year_income.setFont(font2)
        self.previous_year_income.setCursor(QCursor(Qt.PointingHandCursor))
        self.previous_year_income.setIcon(icon9)
        self.previous_year_income.setIconSize(QSize(18, 18))
        self.previous_year_income.setCheckable(True)
        self.previous_year_income.setAutoRepeat(True)
        self.previous_year_income.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.previous_year_income)

        self.gridLayout_6.addLayout(self.horizontalLayout_6, 1, 0, 1, 2)

        self.verticalLayout_2.addLayout(self.gridLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(19, 18, 19, 15)
        self.check_labels_income = QCheckBox(self.widget_income)
        self.check_labels_income.setObjectName("check_labels_income")
        self.check_labels_income.setFont(font3)
        self.check_labels_income.setChecked(True)

        self.verticalLayout.addWidget(self.check_labels_income)

        self.check_average_income = QCheckBox(self.widget_income)
        self.check_average_income.setObjectName("check_average_income")
        self.check_average_income.setFont(font3)

        self.verticalLayout.addWidget(self.check_average_income)

        self.check_total_income = QCheckBox(self.widget_income)
        self.check_total_income.setObjectName("check_total_income")
        self.check_total_income.setFont(font3)
        self.check_total_income.setChecked(True)

        self.verticalLayout.addWidget(self.check_total_income)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout_431.addWidget(self.widget_income, 0, 2, 4, 1)

        self.income.setWidget(self.dockWidgetContents_231)

        self.gridLayout_3.addWidget(self.income, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.graphs)
        self.page = QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
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
        MainWindow.setWindowTitle(QCoreApplication.translate(b"MainWindow", "MainWindow", None))
        self.actionDashboard.setText(QCoreApplication.translate(b"MainWindow", "Dashboard", None))
        # if QT_CONFIG(tooltip)
        self.actionDashboard.setToolTip(QCoreApplication.translate(b"MainWindow", "Dashboard", None))
        # endif // QT_CONFIG(tooltip)
        self.actionMenu.setText(QCoreApplication.translate(b"MainWindow", "Menu", None))
        # if QT_CONFIG(tooltip)
        self.actionMenu.setToolTip(QCoreApplication.translate(b"MainWindow", "Menu", None))
        # endif // QT_CONFIG(tooltip)
        self.actionGraph.setText(QCoreApplication.translate(b"MainWindow", "Graph", None))
        # if QT_CONFIG(tooltip)
        self.actionGraph.setToolTip(QCoreApplication.translate(b"MainWindow", "Graphs", None))
        # endif // QT_CONFIG(tooltip)
        self.actionInsights.setText(QCoreApplication.translate(b"MainWindow", "Insights", None))
        # if QT_CONFIG(tooltip)
        self.actionInsights.setToolTip(QCoreApplication.translate(b"MainWindow", "Insights", None))
        # endif // QT_CONFIG(tooltip)
        self.menuLabel.setText(QCoreApplication.translate(b"MainWindow", "Dashboard", None))
        # if QT_CONFIG(tooltip)
        self.alerts.setToolTip(QCoreApplication.translate(b"MainWindow", "Notifications", None))
        # endif // QT_CONFIG(tooltip)
        self.alerts.setText("")
        # if QT_CONFIG(tooltip)
        self.settings.setToolTip(QCoreApplication.translate(b"MainWindow", "Settings", None))
        # endif // QT_CONFIG(tooltip)
        self.settings.setText("")
        self.transactions.setWindowTitle(QCoreApplication.translate(b"MainWindow", "Transactions", None))
        self.accounts.setWindowTitle(QCoreApplication.translate(b"MainWindow", "Balance", None))
        self.spending.setWindowTitle(QCoreApplication.translate(b"MainWindow", "Spending", None))
        self.savings.setWindowTitle(QCoreApplication.translate(b"MainWindow", "Shortcuts", None))
        self.monthlyExpenses.setWindowTitle(QCoreApplication.translate(b"MainWindow", "Expenses Distribution", None))
        self.expenses.setWindowTitle(QCoreApplication.translate(b"MainWindow", "Expenses", None))
        self.toolButton_icon_category_2.setText(QCoreApplication.translate(b"MainWindow", "...", None))
        self.expenses_choice.setItemText(0, QCoreApplication.translate(b"MainWindow", "All", None))
        self.expenses_choice.setItemText(1, QCoreApplication.translate(b"MainWindow", "Restaurants", None))
        self.expenses_choice.setItemText(2, QCoreApplication.translate(b"MainWindow", "Gas", None))

        self.dateEdit_expenses_from.setDisplayFormat(QCoreApplication.translate(b"MainWindow", "MMMM-yyyy", None))
        self.label_from_income_2.setText(QCoreApplication.translate(b"MainWindow", "From:", None))
        self.dateEdit_expenses_to.setDisplayFormat(QCoreApplication.translate(b"MainWindow", "MMMM-yyyy", None))
        # if QT_CONFIG(tooltip)
        self.refresh_expenses.setToolTip(QCoreApplication.translate(b"MainWindow", "Refresh graph", None))
        # endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate(b"MainWindow", "To:", None))
        self.this_year_expenses.setText(QCoreApplication.translate(b"MainWindow", "This year ", None))
        self.last_12_months_expenses.setText(QCoreApplication.translate(b"MainWindow", "Last 12 months", None))
        self.previous_year_expenses.setText(QCoreApplication.translate(b"MainWindow", "Previous year", None))
        self.check_labels_expenses.setText(QCoreApplication.translate(b"MainWindow", "Show labels", None))
        self.check_average_expenses.setText(QCoreApplication.translate(b"MainWindow", "Show average", None))
        self.check_total_expenses.setText(QCoreApplication.translate(b"MainWindow", "Show total amount", None))
        self.income.setWindowTitle(QCoreApplication.translate(b"MainWindow", "Income", None))
        self.toolButton_icon_category.setText(QCoreApplication.translate(b"MainWindow", "...", None))
        self.income_choice.setItemText(0, QCoreApplication.translate(b"MainWindow", "All", None))
        self.income_choice.setItemText(1, QCoreApplication.translate(b"MainWindow", "Wages", None))
        self.income_choice.setItemText(2, QCoreApplication.translate(b"MainWindow", "Gifts", None))

        self.label_from_income.setText(QCoreApplication.translate(b"MainWindow", "From:", None))
        self.dateEdit_income_from.setDisplayFormat(QCoreApplication.translate(b"MainWindow", "MMMM-yyyy", None))
        self.label_2.setText(QCoreApplication.translate(b"MainWindow", "To:", None))
        self.dateEdit_income_to.setDisplayFormat(QCoreApplication.translate(b"MainWindow", "MMMM-yyyy", None))
        # if QT_CONFIG(tooltip)
        self.refresh_income.setToolTip(QCoreApplication.translate(b"MainWindow", "Refresh graph", None))
        # endif // QT_CONFIG(tooltip)
        self.this_year_income.setText(QCoreApplication.translate(b"MainWindow", "This year ", None))
        self.last_12_months_income.setText(QCoreApplication.translate(b"MainWindow", "Last 12 months", None))
        self.previous_year_income.setText(QCoreApplication.translate(b"MainWindow", "Previous year", None))
        self.check_labels_income.setText(QCoreApplication.translate(b"MainWindow", "Show labels", None))
        self.check_average_income.setText(QCoreApplication.translate(b"MainWindow", "Show average", None))
        self.check_total_income.setText(QCoreApplication.translate(b"MainWindow", "Show total amount", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate(b"MainWindow", "toolBar", None))
    # retranslateUi
