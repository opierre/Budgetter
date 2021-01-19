from PySide2.QtGui import QColor
from PySide2.QtWidgets import QGraphicsDropShadowEffect

from skeletons.MainWindow import Ui_MainWindow
from view.menu_view import Menu
from view.home import Home
from widgets.custom_window import CustomWindow


class Controller:
    """
    Controller class
    """

    def __init__(self):

        """ Create MainWindow """
        self.mainWindow = CustomWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)

        # """ Store effects """
        # self.effectAccounts = QGraphicsDropShadowEffect()
        # self.effectDistribution = QGraphicsDropShadowEffect()
        # self.effectTransactions = QGraphicsDropShadowEffect()

        """ Configure main effect and apply """
        # self.configureGraphicalEffects()

        """ Left Drawer """
        self.menuDrawer = Menu(self.mainWindow, self.ui)

        """ Home Panel """
        self.homePanel = Home(self.mainWindow, self.ui)

        """ Connect all signals/slots """
        self.connectSlotsAndSignals()

        """ Show FullScreen """
        self.mainWindow.showMaximized()

    # def configureGraphicalEffects(self):
    #     """
    #     Apply all grpahical effects to main widgets
    #     :return: void
    #     """
    #
    #     """ Configure effect """
    #     self.effectAccounts.setBlurRadius(10)
    #     self.effectAccounts.setColor(QColor(37, 55, 70, 120))
    #     self.effectAccounts.setXOffset(5)
    #     self.effectAccounts.setYOffset(8)
    #     self.effectDistribution.setBlurRadius(10)
    #     self.effectDistribution.setColor(QColor(37, 55, 70, 120))
    #     self.effectDistribution.setXOffset(5)
    #     self.effectDistribution.setYOffset(8)
    #     self.effectTransactions.setBlurRadius(10)
    #     self.effectTransactions.setColor(QColor(37, 55, 70, 120))
    #     self.effectTransactions.setXOffset(5)
    #     self.effectTransactions.setYOffset(8)
    #
    #     """ Apply effect to all groupbox """
    #     self.ui.accounts.setGraphicsEffect(self.effectAccounts)
    #     self.ui.transactions.setGraphicsEffect(self.effectDistribution)
    #     self.ui.distribution.setGraphicsEffect(self.effectTransactions)

    def connectSlotsAndSignals(self):
        """
        Connect all slots and signals
        :return: void
        """

        """ Connect Custom Windows resize to resize drawer """
        print('coucou')
