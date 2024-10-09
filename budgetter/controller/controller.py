import json

from PySide6.QtCore import QTimer, QUrl
from PySide6.QtWebSockets import QWebSocket

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

        # Web socket client
        self.ws_dashboard_client = QWebSocket()
        self.ws_budgetter_client = QWebSocket()

        # Configure widgets
        self.configure()

        # Connect all signals/slots
        self.connect_slots_and_signals()

        # Show FullScreen
        QTimer.singleShot(50, self.main_window.show)

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
        self.home_panel.postTransactionsController.connect(self.home_threads.add_transactions)
        self.home_panel.addTransactionController.connect(
            self.home_threads.add_transaction_worker
        )
        self.home_panel.importTransactionsController.connect(
            self.home_threads.import_ofx
        )
        self.home_panel.removeTransactionController.connect(
            self.home_threads.remove_transaction_worker
        )
        self.home_panel.editTransactionController.connect(
            self.home_threads.edit_transaction_worker
        )

        # Connect dashboard threads results to display
        self.home_threads.errorDashboard.connect(self.home_panel.handle_error)
        self.home_threads.accountAdded.connect(self.home_panel.handle_add_account)
        self.home_threads.bankAdded.connect(self.home_panel.handle_add_bank)
        self.home_threads.transactionAdded.connect(
            self.home_panel.handle_add_transactions
        )
        self.home_threads.transactionEdited.connect(
            self.home_panel.handle_edit_transaction
        )
        self.home_threads.transactionRemoved.connect(
            self.home_panel.handle_remove_transaction
        )
        self.home_threads.transactionsFound.connect(
            self.home_panel.handle_set_transactions
        )
        self.home_threads.banksFound.connect(self.home_panel.handle_get_banks)
        self.home_threads.banksFound.connect(self.home_threads.get_accounts_worker)
        self.home_threads.accountsFound.connect(self.home_panel.handle_get_accounts)
        self.home_threads.accountsFound.connect(
            self.home_threads.get_transactions_worker
        )
        self.home_threads.transactionsPosted.connect(self.home_panel.handle_add_transactions)

        # Connect web socket
        self.ws_dashboard_client.textMessageReceived.connect(self.home_panel.update_on_ws)
        self.ws_budgetter_client.textMessageReceived.connect(self.dispatch_global_ws)

        QTimer.singleShot(500, self.home_threads.get_banks_worker)

    def configure(self):
        """
        Configure all widgets

        :return: None
        """

        # Configure web sockets
        self.ws_dashboard_client.open(QUrl("ws://127.0.0.1:8080/ws/dashboard/"))
        self.ws_budgetter_client.open(QUrl("ws://127.0.0.1:8080/ws/budgetter/"))

    def dispatch_global_ws(self, ws_data: str):
        """
        Handle data received on web socket

        :param ws_data: data from ws
        :return: None
        """

        dict_data = json.loads(ws_data)
        print(ws_data)

        function_completed = dict_data.get("data", {}).get("function_completed", "")
        result = dict_data.get("data", {}).get("result", {})

        if function_completed == "import_ofx_to_database":
            # Close import dialog and open toaster
            # Open dialogs if new accounts were created
            self.home_panel.handle_import_completed(result)
