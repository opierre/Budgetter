import json
from typing import Any, Tuple, Union

from PySide6.QtCore import QObject, Signal

from budgetter.view.panels.home_panel.accounts import Accounts
from budgetter.view.panels.home_panel.distribution import Distribution
from budgetter.view.panels.home_panel.savings import Savings
from budgetter.view.panels.home_panel.spending import Spending
from budgetter.view.panels.home_panel.transactions import Transactions
from budgetter.view.widgets.toaster.toaster import Toaster, ToasterType


class Home(QObject):
    """
    Home Panel to handle Accounts/Distribution/Transactions
    """

    # Signals list
    addAccountController = Signal(str, str, str, int, str, str)
    addBankController = Signal(str)
    postTransactionsController = Signal(dict)
    addTransactionController = Signal(str, str, str, str, str, str, str, int)
    importTransactionsController = Signal(str)
    removeTransactionController = Signal(int)
    editTransactionController = Signal(str, str, str, str, str, str, str, int, int)

    def __init__(self, parent, gui):
        super().__init__()

        # Store windows and gui
        self.ui_setup = gui
        self.main_window = parent

        # Accounts groupBox
        self._accounts = Accounts(gui, parent)

        # Spending groupBox
        self._spending = Spending(gui)

        # Distribution groupBox
        self._distribution = Distribution(gui)

        # Transactions groupBox
        self._transactions = Transactions(gui, parent)

        # Savings groupbox
        self._savings = Savings(gui)

        # Connect slots and signals
        self.connect_home_slots_and_signals()

    def connect_home_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect signals from accounts
        self._accounts.addAccountCall.connect(self.addAccountController.emit)
        self._accounts.addBankCall.connect(self.addBankController.emit)
        self._accounts.postTransactionsCall.connect(
            self.postTransactionsController.emit
        )
        self._transactions.addTransaction.connect(self.addTransactionController.emit)
        self._transactions.importTransactions.connect(
            self.importTransactionsController.emit
        )
        self._transactions.removeTransaction.connect(
            self.removeTransactionController.emit
        )
        self._transactions.editTransaction.connect(self.editTransactionController.emit)

    def handle_error(self, error: Tuple[Exception, Any, str]):
        """
        Handle error from API call

        :param error: tuple with exception type, value returned and traceback
        :return: None
        """

        # Show notification on bank added
        _ = Toaster(
            f"Action on transaction failed due to: {error[2]}",
            ToasterType.ERROR,
            self.main_window,
        )

    def handle_add_account(self, account: dict):
        """
        Handle add account result from API call

        :param account: account details
        :return: None
        """

        # Add account to model and close popup
        self._accounts.add_account_details(account)
        self._transactions.add_account_details(account)

    def handle_add_bank(self, bank: dict):
        """
        Handle add bank result from API call

        :param bank: bank details
        :return: None
        """

        # Set bank ID to ad account popup
        self._accounts.bank_added(bank)

    def handle_set_transactions(self, transactions: list):
        """
        Handle set transactions result from API call

        :param transactions: transactions from db
        :return: None
        """

        self._transactions.set_transactions(transactions)

    def handle_add_transactions(self, transactions: Union[dict, list]):
        """
        Handle add transactions result from API call

        :param transactions: transaction details
        :return: None
        """

        self._transactions.transactions_added(transactions)

    def handle_edit_transaction(self, transaction: dict):
        """
        Handle edit transaction result from API call

        :param transaction: transaction details
        :return: None
        """

        self._transactions.transaction_edited(transaction)

    def handle_remove_transaction(self):
        """
        Handle delete transaction result from API call

        :return: None
        """

        self._transactions.transaction_removed()

    def handle_get_banks(self, bank_list: list):
        """
        Handle banks retrieved from API call

        :param bank_list: list with all banks
        :return: None
        """

        self._accounts.set_banks(bank_list)

    def handle_get_accounts(self, accounts_list: list):
        """
        Handle accounts retrieved from API call

        :param accounts_list: list with all accounts
        :return: None
        """

        self._accounts.set_accounts(accounts_list)
        self._transactions.set_accounts(accounts_list)

    def handle_convert_ofx(self, result: Tuple[dict, dict, str]):
        """
        Handle OFX data converted to dict

        :param result: result from thread
        :return: None
        """

        header, data, message = result

        self._transactions.handle_convert_ofx(header, message)
        self._accounts.handle_convert_ofx(header, data)

    def update_on_ws(self, ws_data: str):
        """
        Handle data received on web socket

        :param ws_data: data from ws
        :return: None
        """

        dict_data = json.loads(ws_data)
        self._accounts.update_accounts(dict_data.get("data", {}).get("accounts", {}))
