from typing import Any

from PySide6.QtCore import QObject, Signal

from budgetter.view.panels.home_panel.accounts import Accounts
from budgetter.view.panels.home_panel.distribution import Distribution
from budgetter.view.panels.home_panel.savings import Savings
from budgetter.view.panels.home_panel.spending import Spending
from budgetter.view.panels.home_panel.transactions import Transactions


class Home(QObject):
    """
    Home Panel to handle Accounts/Distribution/Transactions
    """

    # Signals list
    addAccountController = Signal(str, str, int, str)

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

    def display_saving_tooltip(self):
        """
        Display saving tooltip after window resized

        :return: None
        """

        self._savings.display_tooltip()

    def handle_error(self, error: (Exception, Any, str)):
        """
        Handle error from API call

        :param error: tuple with exception type, value returned and traceback
        :return: None
        """

        print("error: ++++++++++ ", error)

    def handle_add_account(self, account: dict):
        """
        Handle add account result from API call

        :param account: account details
        :return: None
        """

        # Add account to model and close popup
        self._accounts.add_account_details(account)

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
