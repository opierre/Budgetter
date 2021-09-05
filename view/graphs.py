from PySide2.QtCore import QObject

from view.graphs_panel.expenses import Expenses
from view.graphs_panel.income import Income
from view.home_panel.accounts import Accounts
from view.home_panel.distribution import Distribution
from view.home_panel.savings import Savings
from view.home_panel.spending import Spending
from view.home_panel.transactions import Transactions


class Graphs(QObject):
    """
    Graphs Panel to handle Income/Expenses graphs
    """

    def __init__(self, parent, gui):
        super(Graphs, self).__init__()

        """ Store windows and gui """
        self.uiSetup = gui
        self.mainWindow = parent

        """ Income groupBox """
        self._income = Income(gui)

        """ Expenses groupBox """
        self._expenses = Expenses(gui)

        """ Connect slots and signals """
        self.connect_home_slots_and_signals()

    def connect_home_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        print('coucou')
