from PySide2.QtCore import QObject

from view.home_panel.accounts import Accounts
from view.home_panel.distribution import Distribution
from view.home_panel.transactions import Transactions


class Home(QObject):
    """
    Home Panel to handle Accounts/Distribution/Transactions
    """

    def __init__(self, parent, gui):
        super(Home, self).__init__()

        """ Store windows and gui """
        self.uiSetup = gui
        self.mainWindow = parent

        """ Accounts groupBox """
        self._accounts = Accounts(gui)

        """ Distribution groupBox """
        self._distribution = Distribution(gui)

        """ Transactions groupBox """
        self._transactions = Transactions(gui, parent)

        """ Connect slots and signals """
        self.connectHomeSlotsAndSignals()

    def connectHomeSlotsAndSignals(self):
        """
        Connect all slots and signals
        :return: void
        """

        print('coucou')
