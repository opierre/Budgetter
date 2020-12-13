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
from widgets.slidingStackedWidget import SlidingStackedWidget
from widgets.thumbnail import Thumbnail

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1137, 786)
        icon = QIcon()
        icon.addFile(u":/images/images/bold-36px-#2ABFB0.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#MainWindow \n"
"{\n"
"	background: #060E1B;\n"
"}\n"
"\n"
"#menuBar \n"
"{\n"
"	background: #060E1B;\n"
"}\n"
"\n"
"QGroupBox \n"
"{\n"
"	background-color: #141C26;\n"
"	border-radius: 5px;\n"
"	border-color: #141C26;\n"
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
"	border-bottom: 1px solid #309db5;\n"
"	border-radisu: 0px;\n"
"	padding: 0 8px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	selection-background-color: #309db5;\n"
"}\n"
"\n"
"QLineEdi"
                        "t ::hover\n"
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
"	border-radisu: 0px;\n"
"	padding: 0 8px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	selection-background-color: #309db5;\n"
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
"	colo"
                        "r: white;\n"
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
""
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
"	ima"
                        "ge: url(:/images/images/receipt-20px-#72C1F2.png);\n"
"}\n"
"\n"
"QPushButton#menu, QPushButton#settings, QPushButton#alerts {\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 6px 6px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#menu:hover, QPushButton#settings:hover, QPushButton#alerts:hover {\n"
"	background-color: rgba(255, 255, 255, 35);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-radius: 2px;\n"
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
"QPushButton#menu:pressed, QPushButton#settings:pressed, QPushButton#alerts:pressed {\n"
"	background-color: rgba(255, 255, 255, 80);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-radius: 2px;\n"
"	border-color: transparent;\n"
""
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
"	background-color: #141B25;\n"
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
"    color: #BBBDC7;\n"
"}\n"
"\n"
"QPushButton#pushButtonHome:hover:!checked {\n"
"    background-color: transparent;\n"
"    border-style: none;\n"
"    padding: 3px 3px;\n"
"	color: white;\n"
"	icon: url(:/images/images/home-hovered-36dp.svg);\n"
"}\n"
"\n"
"QPushButton#pushButtonManage:hover:!checked {\n"
"    back"
                        "ground-color: transparent;\n"
"    border-style: none;\n"
"    padding: 3px 3px;\n"
"	color: white;\n"
"	icon: url(:/images/images/account_balance_wallet-hovered-36dp.svg);\n"
"}\n"
"\n"
"QPushButton#pushButtonAnalytics:hover:!checked {\n"
"    background-color: transparent;\n"
"    border-style: none;\n"
"    padding: 3px 3px;\n"
"	color: white;\n"
"	icon: url(:/images/images/analytics-hovered-36dp.svg);\n"
"}\n"
"\n"
"QPushButton#pushButtonHome:checked, QPushButton#pushButtonManage:checked,\n"
"QPushButton#pushButtonAnalytics:checked {\n"
"	color: #498DF4;\n"
"}\n"
"\n"
"QFrame[frameShape=\"4\"] {\n"
"	color: #060E1B;\n"
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
"Card::title\n"
"{\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	padding: 0 14px;\n"
"	margin-bottom: -55px;\n"
"	subcontrol-origin: margin;\n"
""
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
"Card > QPushButton#monthTrend[positive=\"none\"] {\n"
"	color: white;\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"	padding: 0"
                        "px 0px;\n"
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
"	margin-bottom: 0px;\n"
"}\n"
"\n"
"QPushButton#logoExpense\n"
"{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border-color: transparent;\n"
"	col"
                        "or: white;\n"
"}\n"
"\n"
"QLabel#categoryExpense {\n"
"	color: #a2a3ae;\n"
"	font-family: \"Roboto\";\n"
"	font-size: 12pt;\n"
"	margin-bottom: 20px;\n"
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
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(15, 0, 15, 15)
        self.transactions = QGroupBox(self.dashboard)
        self.transactions.setObjectName(u"transactions")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(14)
        self.transactions.setFont(font)
        self.transactions.setCheckable(False)
        self.gridLayout_5 = QGridLayout(self.transactions)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableView = QTableView(self.transactions)
        self.tableView.setObjectName(u"tableView")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setFrameShape(QFrame.NoFrame)

        self.gridLayout_5.addWidget(self.tableView, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.transactions, 1, 0, 1, 2)

        self.distribution = QGroupBox(self.dashboard)
        self.distribution.setObjectName(u"distribution")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(13)
        self.distribution.setFont(font1)
        self.gridLayout_6 = QGridLayout(self.distribution)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.expense1 = Thumbnail(self.distribution)
        self.expense1.setObjectName(u"expense1")
        self.expense1.setMinimumSize(QSize(150, 200))
        self.expense1.setMaximumSize(QSize(150, 200))

        self.gridLayout_6.addWidget(self.expense1, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.distribution, 0, 2, 2, 1)

        self.accounts = QGroupBox(self.dashboard)
        self.accounts.setObjectName(u"accounts")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.accounts.sizePolicy().hasHeightForWidth())
        self.accounts.setSizePolicy(sizePolicy1)
        self.accounts.setMaximumSize(QSize(16777215, 250))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.accounts.setFont(font2)
        self.accounts.setCheckable(False)
        self.horizontalLayout_3 = QHBoxLayout(self.accounts)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.card1 = Card(self.accounts)
        self.card1.setObjectName(u"card1")
        self.card1.setMinimumSize(QSize(383, 243))
        self.card1.setMaximumSize(QSize(383, 243))
        self.gridLayout_4 = QGridLayout(self.card1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.horizontalLayout_3.addWidget(self.card1)


        self.gridLayout_2.addWidget(self.accounts, 0, 0, 1, 2)

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

        self.menuLabel = QLabel(self.menuBar)
        self.menuLabel.setObjectName(u"menuLabel")
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(15)
        self.menuLabel.setFont(font3)

        self.horizontalLayout.addWidget(self.menuLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.alerts = QPushButton(self.menuBar)
        self.alerts.setObjectName(u"alerts")
        self.alerts.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/notification_important-empty-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.alerts.setIcon(icon2)
        self.alerts.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.alerts)

        self.settings = QPushButton(self.menuBar)
        self.settings.setObjectName(u"settings")
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/settings-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon3)
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
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonHome = QPushButton(self.navigation)
        self.pushButtonHome.setObjectName(u"pushButtonHome")
        self.pushButtonHome.setMaximumSize(QSize(250, 34))
        font4 = QFont()
        font4.setFamily(u"Roboto")
        font4.setPointSize(12)
        self.pushButtonHome.setFont(font4)
        self.pushButtonHome.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/home-checked-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHome.setIcon(icon4)
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
        self.pushButtonManage.setFont(font4)
        self.pushButtonManage.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/account_balance_wallet-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonManage.setIcon(icon5)
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
        self.pushButtonAnalytics.setFont(font4)
        self.pushButtonAnalytics.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/images/images/analytics-white-36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAnalytics.setIcon(icon6)
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
        self.labelLogo.setPixmap(QPixmap(u":/images/images/bold-36px-#3889F2.png"))
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
        self.transactions.setTitle(QCoreApplication.translate("MainWindow", u"Recent Transactions", None))
        self.distribution.setTitle(QCoreApplication.translate("MainWindow", u"Monthly Expenses", None))
        self.expense1.setTitle("")
        self.accounts.setTitle("")
        self.card1.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.total.setTitle(QCoreApplication.translate("MainWindow", u"Total", None))
        self.savings.setTitle(QCoreApplication.translate("MainWindow", u"Savings", None))
        self.menu.setText("")
        self.menuLabel.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.alerts.setToolTip(QCoreApplication.translate("MainWindow", u"Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.alerts.setText("")
#if QT_CONFIG(tooltip)
        self.settings.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
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

