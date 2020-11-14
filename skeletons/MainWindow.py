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
from widgets.card import Card

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1139, 786)
        icon = QIcon()
        icon.addFile(u":/images/images/bold-36px-#2ABFB0.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#MainWindow \n"
"{\n"
"	background: #394957;\n"
"}\n"
"\n"
"#menuBar \n"
"{\n"
"	background: #253746;\n"
"}\n"
"\n"
"QGroupBox \n"
"{\n"
"	background-color: #253746;\n"
"	border-radius: 5px;\n"
"	margin-top: 6ex;\n"
"	margin-left: 1ex;\n"
"	margin-right: 1ex;\n"
"	padding-top: 30px;\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"	background-color: transparent;\n"
"	color: rgba(255, 255, 255, 230);\n"
"	padding: 0 4px;\n"
"	margin-bottom: -35px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"}\n"
"\n"
"QLineEdit \n"
"{\n"
"	border-bottom: 1px solid #309db5;\n"
"	border-radisu: 0px;\n"
"	padding: 0 8px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	selection-background-color: #309db5;\n"
"}\n"
"\n"
"QLineEdit ::hover\n"
"{\n"
"	border-bottom: 1px solid white;\n"
"	border-radisu: 0px;\n"
"	padding: 0 8px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	selection-background-color: #309db5;\n"
"}\n"
"\n"
"QLineEdit ::disabled\n"
"{\n"
"	border-bottom: 1px solid grey;\n"
"	border-ra"
                        "disu: 0px;\n"
"	padding: 0 8px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	selection-background-color: #309db5;\n"
"}\n"
"\n"
"QPushButton \n"
"{\n"
"	background-color: #309db5;\n"
"	border-radiius: 5px;\n"
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
"	border-color: #309db5;\n"
"	color: white;\n"
"	padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox ::hover\n"
"{\n"
"	background-color: transparent;\n"
"	border-bottom-style: outset;\n"
"	border-bottom-width: 1px;\n"
"	border-radius: 0px;\n"
"	border-color: white;\n"
"	color: white;\n"
"	padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox ::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	border-bottom-style: outset;\n"
"	border-bottom-width: 1px;\n"
"	border-radius: 0px;\n"
"	border-color: grey;\n"
"	color: grey;\n"
"	padding-left: 4px;\n"
"}\n"
"\n"
""
                        "QComboBox::drop-down\n"
"{\n"
"	border: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url();\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	padding-right: 10px;\n"
"	padding-top: 1px\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"	image: url();\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	padding-right: 10px;\n"
"	padding-top: 1px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled\n"
"{\n"
"	image: url();\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	padding-right: 10px;\n"
"	padding-top: 1px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"	background: #394957;\n"
"	color: white;\n"
"	border-top-style: inset;\n"
"	border-width: 1px;\n"
"	border-radius: 0px;\n"
"	border-color: #309db5;\n"
"	selection-bckground-color: #309db5;\n"
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
""
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
"	image: url(:/images/images/receipt-20px-#72C1F2.png);\n"
"}\n"
"\n"
"QPushButton#menu, QPushButton#settings {\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 6px 6px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#menu:hover, QPushButton#settings:hover {\n"
"	b"
                        "ackground-color: rgba(255, 255, 255, 35);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: transparent;\n"
"	padding: 6px 6px;\n"
"	color: white;\n"
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
"QPushButton#menu:pressed, QPushButton#settings:pressed {\n"
"	background-color: rgba(255, 255, 255, 80);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: transparent;\n"
"	padding: 6px 6px;\n"
"	color: white;\n"
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
"	backgr"
                        "ound-color: #1F4373;\n"
"	margin-bottom: 0px;\n"
"	margin-top: 0px;\n"
"	border-style: none;\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}\n"
"\n"
"QPushButton#pushButtonHome, QPushButton#pushButtonManage, \n"
"QPushButton#pushButtonAnalytics {\n"
"    background-color: transparent;\n"
"    border-style: none;\n"
"    padding: 3px 3px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#pushButtonHome:hover, QPushButton#pushButtonManage:hover, \n"
"QPushButton#pushButtonAnalytics:hover {\n"
"    background-color: transparent;\n"
"    border-style: none;\n"
"    padding: 3px 3px;\n"
"	color: rgba(255, 255, 255, 128);\n"
"}\n"
"\n"
"QPushButton#pushButtonHome:pressed, QPushButton#pushButtonManage:pressed, \n"
"QPushButton#pushButtonAnalytics:pressed {\n"
"    background-color: transparent;\n"
"    border-style: none;\n"
"    padding: 3px 3px;\n"
"	color: rgba(255, 255, 255, 35);\n"
"}\n"
"\n"
"QPushButton#pushButtonHome:checked, QPushButton#pushButtonManage:checked, \n"
"QPushButton#pushButtonAnalytics:che"
                        "cked {\n"
"	color: #2ABFB0;\n"
"}\n"
"\n"
"QPushButton#pushButtonHome:unchecked, QPushButton#pushButtonManage:unchecked, \n"
"QPushButton#pushButtonAnalytics:unchecked {\n"
"	color: white;\n"
"}\n"
"\n"
"QFrame[frameShape=\"4\"] {\n"
"	color: rgba(128, 128, 128, 128);\n"
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
"Card {\n"
"	background-color: #72C1F2;\n"
"}\n"
"\n"
"Card::title\n"
"{\n"
"	background-color: transparent;\n"
"	color: #253746;\n"
"	padding: 0 14px;\n"
"	margin-bottom: -55px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"}\n"
"\n"
"Card > QPushButton#description {\n"
"	color: #394957;\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 6px 6px;\n"
"	font-family: \"Roboto Light\";\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"Card > QLabel#amount"
                        " {\n"
"	color: #253746;\n"
"	text-align: right;\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 0px 0px;\n"
"	margin-bottom: 30px;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 17pt;\n"
"}\n"
"\n"
"Card > QPushButton#monthTrend {\n"
"	color: #253746;\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 0px 0px;\n"
"	margin-bottom: 30px;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 17pt;\n"
"}\n"
"\n"
"QLabel#homeLabel {\n"
"	color: white;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 16pt;\n"
"}")
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(MainWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.gridLayout_2 = QGridLayout(self.dashboard)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(11, 0, 11, 11)
        self.distribution = QGroupBox(self.dashboard)
        self.distribution.setObjectName(u"distribution")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(14)
        self.distribution.setFont(font)
        self.distribution.setCheckable(True)

        self.gridLayout_2.addWidget(self.distribution, 0, 1, 1, 1)

        self.transactions = QGroupBox(self.dashboard)
        self.transactions.setObjectName(u"transactions")
        self.transactions.setFont(font)
        self.transactions.setCheckable(True)
        self.gridLayout_5 = QGridLayout(self.transactions)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableView = QTableView(self.transactions)
        self.tableView.setObjectName(u"tableView")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.tableView, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.transactions, 1, 0, 1, 2)

        self.accounts = QGroupBox(self.dashboard)
        self.accounts.setObjectName(u"accounts")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.accounts.setFont(font1)
        self.accounts.setCheckable(True)
        self.gridLayout_4 = QGridLayout(self.accounts)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea = QScrollArea(self.accounts)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 495, 289))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.card1 = Card(self.scrollAreaWidgetContents)
        self.card1.setObjectName(u"card1")

        self.verticalLayout.addWidget(self.card1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.accounts, 0, 0, 1, 1)

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
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 7, -1, 7)
        self.menu = QPushButton(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/menu-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon1)
        self.menu.setIconSize(QSize(24, 24))
        self.menu.setCheckable(True)

        self.horizontalLayout.addWidget(self.menu)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.homeLabel = QLabel(self.menuBar)
        self.homeLabel.setObjectName(u"homeLabel")
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(16)
        self.homeLabel.setFont(font2)

        self.horizontalLayout.addWidget(self.homeLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.settings = QPushButton(self.menuBar)
        self.settings.setObjectName(u"settings")
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/settings-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon2)
        self.settings.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.settings)


        self.gridLayout.addWidget(self.menuBar, 0, 1, 1, 3)

        self.drawer = Drawer(MainWindow)
        self.drawer.setObjectName(u"drawer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.drawer.sizePolicy().hasHeightForWidth())
        self.drawer.setSizePolicy(sizePolicy2)
        self.drawer.setMinimumSize(QSize(65, 0))
        self.drawer.setMaximumSize(QSize(65, 16777215))
        self.gridLayout_7 = QGridLayout(self.drawer)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.navigation = QFrame(self.drawer)
        self.navigation.setObjectName(u"navigation")
        self.navigation.setFrameShape(QFrame.StyledPanel)
        self.navigation.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.navigation)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, 7, -1, 7)
        self.line = QFrame(self.navigation)
        self.line.setObjectName(u"line")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy3)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_8.addWidget(self.line, 2, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonHome = QPushButton(self.navigation)
        self.pushButtonHome.setObjectName(u"pushButtonHome")
        self.pushButtonHome.setMaximumSize(QSize(250, 34))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(12)
        self.pushButtonHome.setFont(font3)
        self.pushButtonHome.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/home-#2ABFB0-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHome.setIcon(icon3)
        self.pushButtonHome.setIconSize(QSize(28, 28))
        self.pushButtonHome.setCheckable(True)
        self.pushButtonHome.setChecked(True)

        self.horizontalLayout_6.addWidget(self.pushButtonHome)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButtonManage = QPushButton(self.navigation)
        self.pushButtonManage.setObjectName(u"pushButtonManage")
        self.pushButtonManage.setMaximumSize(QSize(250, 34))
        self.pushButtonManage.setFont(font3)
        self.pushButtonManage.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/account_balance_wallet-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonManage.setIcon(icon4)
        self.pushButtonManage.setIconSize(QSize(28, 28))
        self.pushButtonManage.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.pushButtonManage)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButtonAnalytics = QPushButton(self.navigation)
        self.pushButtonAnalytics.setObjectName(u"pushButtonAnalytics")
        self.pushButtonAnalytics.setMaximumSize(QSize(250, 34))
        self.pushButtonAnalytics.setFont(font3)
        self.pushButtonAnalytics.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/analytics-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAnalytics.setIcon(icon5)
        self.pushButtonAnalytics.setIconSize(QSize(28, 28))
        self.pushButtonAnalytics.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.pushButtonAnalytics)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.gridLayout_8.addLayout(self.verticalLayout_2, 4, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 7, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.labelLogo = QLabel(self.navigation)
        self.labelLogo.setObjectName(u"labelLogo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelLogo.sizePolicy().hasHeightForWidth())
        self.labelLogo.setSizePolicy(sizePolicy4)
        self.labelLogo.setMinimumSize(QSize(40, 36))
        self.labelLogo.setMaximumSize(QSize(40, 36))
        self.labelLogo.setPixmap(QPixmap(u":/images/images/bold-36px-#2ABFB0.png"))
        self.labelLogo.setScaledContents(False)
        self.labelLogo.setAlignment(Qt.AlignCenter)
        self.labelLogo.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.labelLogo)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout_8.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)


        self.gridLayout_7.addWidget(self.navigation, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.drawer, 0, 0, 2, 1)


        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Budgetter", None))
        self.distribution.setTitle(QCoreApplication.translate("MainWindow", u"Distribution", None))
        self.transactions.setTitle(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.accounts.setTitle(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.card1.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.total.setTitle(QCoreApplication.translate("MainWindow", u"Total", None))
        self.savings.setTitle(QCoreApplication.translate("MainWindow", u"Savings", None))
        self.menu.setText("")
        self.homeLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Home</span></p></body></html>", None))
        self.settings.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonHome.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonHome.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonManage.setToolTip(QCoreApplication.translate("MainWindow", u"Manager", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonManage.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonAnalytics.setToolTip(QCoreApplication.translate("MainWindow", u"Analytics", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonAnalytics.setText("")
        self.labelLogo.setText("")
    # retranslateUi

