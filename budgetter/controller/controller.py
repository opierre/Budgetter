from PySide6.QtCore import QTimer

from budgetter.services.dashboard import Dashboard
from budgetter.view.panels.graphs import Graphs
from budgetter.view.panels.home import Home
from budgetter.view.panels.menu_view import Menu
from budgetter.view.skeletons.MainWindow import Ui_MainWindow
from budgetter.view.widgets.custom_window import CustomWindow


class Controller:
    """
    Controller class
    """

    def __init__(self):
        # Create MainWindow
        self.main_window = CustomWindow()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self.main_window)

        # Left Drawer
        self.menu_drawer = Menu(self.main_window, self.gui)

        # Home Panel
        self.home_panel = Home(self.main_window, self.gui)

        # Graphs Panel
        self.graphs_panel = Graphs(self.main_window, self.gui)

        # Home threads
        self.home_threads = Dashboard()

        # Connect all signals/slots
        self.connect_slots_and_signals()

        # Show FullScreen
        self.main_window.showMaximized()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect home panel signals to worker execution
        self.home_panel.addAccountController.connect(
            self.home_threads.add_account_worker
        )
        self.home_panel.addBankController.connect(self.home_threads.add_bank_worker)
        self.home_panel.addTransactionController.connect(
            self.home_threads.add_transaction_worker
        )

        # Connect dashboard threads results to display
        self.home_threads.errorDashboard.connect(self.home_panel.handle_error)
        self.home_threads.accountAdded.connect(self.home_panel.handle_add_account)
        self.home_threads.bankAdded.connect(self.home_panel.handle_add_bank)
        self.home_threads.transactionAdded.connect(
            self.home_panel.handle_add_transaction
        )
        self.home_threads.transactionsFound.connect(
            self.home_panel.handle_set_transactions
        )
        self.home_threads.banksFound.connect(self.home_panel.handle_get_banks)
        self.home_threads.banksFound.connect(self.home_threads.get_accounts_worker)
        self.home_threads.accountsFound.connect(self.home_panel.handle_get_accounts)
        self.home_threads.accountsFound.connect(self.home_threads.get_transactions_worker)

        QTimer.singleShot(500, self.home_threads.get_banks_worker)
