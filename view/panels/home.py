from PySide2.QtCore import QObject

from view.panels.home_panel.accounts import Accounts
from view.panels.home_panel.distribution import Distribution
from view.panels.home_panel.savings import Savings
from view.panels.home_panel.spending import Spending
from view.panels.home_panel.transactions import Transactions


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

        """ Spending groupBox """
        self._spending = Spending(gui)

        """ Distribution groupBox """
        self._distribution = Distribution(gui)

        """ Transactions groupBox """
        self._transactions = Transactions(gui, parent)

        """ Savings groupbox """
        self._savings = Savings(gui)

        """ Connect slots and signals """
        self.connect_home_slots_and_signals()

    def connect_home_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        print('coucou')

    def display_saving_tooltip(self):
        """
        Display saving tooltip after window resized

        :return: None
        """

        self._savings.display_tooltip()