import time

from PySide2.QtCore import QObject

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

        """ Initialize Drawer """
        # self.drawer = Drawer(self.mainWindow)

        """ Connect slots and signals """
        self.connectMenuSlotsAndSignals()

    def connectMenuSlotsAndSignals(self):
        """
        Connect all slots and signals
        :return: void
        """

        """ Connect click on menu button in top bar to opening drawer """
        self.uiSetup.menu.clicked.connect(self.handleDrawer)

    def handleDrawer(self):
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
