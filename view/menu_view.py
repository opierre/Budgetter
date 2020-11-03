import time

from PySide2.QtCore import QObject
from PySide2.QtGui import QIcon

from widgets.drawer import Drawer


class Menu(QObject):
    """
    Menu class to handle tool bar and left drawer
    """

    def __init__(self, parent, gui):
        super(Menu, self).__init__()

        """ Store windows and gui """
        self.uiSetup = gui
        self.mainWindow = parent

        """ Connect slots and signals """
        self.connectMenuSlotsAndSignals()

    def connectMenuSlotsAndSignals(self):
        """
        Connect all slots and signals
        :return: void
        """

        """ Connect click on menu button in top bar to opening drawer """
        self.uiSetup.menu.clicked.connect(self.handleDrawerExpand)

        """ Connect click on buttons in drawer """
        self.uiSetup.pushButtonHome.clicked.connect(lambda: self.changePage(0))
        self.uiSetup.pushButtonManage.clicked.connect(lambda: self.changePage(1))
        self.uiSetup.pushButtonAnalytics.clicked.connect(lambda: self.changePage(2))

    def handleDrawerExpand(self):
        """
        Expand or collapse drawer according to Menu button state
        :return: void
        """

        if self.uiSetup.menu.isChecked():
            """ Expand drawer """
            self.uiSetup.drawer.expand()

            """ Show labels """
            self.uiSetup.pushButtonHome.setText("  Home")
            self.uiSetup.pushButtonManage.setText("  Manage")
            self.uiSetup.pushButtonAnalytics.setText("  Analytics")
        else:
            """ Collapse drawer """
            self.uiSetup.drawer.collapse()

            """ Hide labels """
            self.uiSetup.pushButtonHome.setText("")
            self.uiSetup.pushButtonManage.setText("")
            self.uiSetup.pushButtonAnalytics.setText("")

    def changePage(self, pageNumber):
        """
        Change page by clicking on button in drawer
        :param pageNumber: page number to go to
        :return: void
        """

        self.uiSetup.stackedWidget.setCurrentIndex(pageNumber)

        if pageNumber == 0:
            """ Set Home button enlighted """
            self.uiSetup.pushButtonHome.setIcon(QIcon(":/images/images/home-#2ABFB0-36dp.svg"))

            """ Set other buttons to OFF """
            self.uiSetup.pushButtonManage.setIcon(QIcon(":/images/images/account_balance_wallet-white-36dp.svg"))
            self.uiSetup.pushButtonAnalytics.setIcon(QIcon(":/images/images/analytics-white-36dp.svg"))

        elif pageNumber == 1:
            """ Set Manage button enlighted """
            self.uiSetup.pushButtonManage.setIcon(QIcon(":/images/images/account_balance_wallet-#2ABFB0-36dp.svg"))

            """ Set other buttons to OFF """
            self.uiSetup.pushButtonHome.setIcon(QIcon(":/images/images/home-white-36dp.svg"))
            self.uiSetup.pushButtonAnalytics.setIcon(QIcon(":/images/images/analytics-white-36dp.svg"))

        elif pageNumber == 2:
            """ Set Analytics button enlighted """
            self.uiSetup.pushButtonAnalytics.setIcon(QIcon(":/images/images/analytics-#2ABFB0-36dp.svg"))

            """ Set other buttons to OFF """
            self.uiSetup.pushButtonHome.setIcon(QIcon(":/images/images/home-white-36dp.svg"))
            self.uiSetup.pushButtonManage.setIcon(QIcon(":/images/images/account_balance_wallet-white-36dp.svg"))
