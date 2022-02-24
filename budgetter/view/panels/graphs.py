from PySide2.QtCore import QObject

from budgetter.view.panels.graphs_panel.expenses import Expenses
from budgetter.view.panels.graphs_panel.income import Income


class Graphs(QObject):
    """
    Graphs Panel to handle Income/Expenses graphs
    """

    def __init__(self, parent, gui):
        super().__init__()

        # Store windows and gui
        self.ui_setup = gui
        self.main_window = parent

        # Income groupBox
        self._income = Income(gui)

        # Expenses groupBox
        self._expenses = Expenses(gui)

        # Connect slots and signals
        self.connect_home_slots_and_signals()

    def connect_home_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        print('coucou')
