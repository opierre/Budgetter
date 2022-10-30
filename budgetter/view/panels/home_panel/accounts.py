from PySide6.QtCore import QObject, QCoreApplication, QSize, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListView, QWidget, QHBoxLayout

from budgetter.models.accounts_model import AccountsModel
from budgetter.view.widgets.balance_widgets.account_delegate import AccountDelegate
from budgetter.view.widgets.balance_widgets.donut_chart_widget import DonutChart
from budgetter.view.widgets.dialog import Dialog
from budgetter.view.widgets.dialog_widgets.add_account import AddAccountDialog


class Accounts(QObject):
    """
    Accounts
    """

    # Signals list
    addAccountCall = Signal(str, str, int)

    def __init__(self, gui, main_window):
        super().__init__()

        # Store gui and main window
        self.ui_setup = gui
        self.main_window = main_window

        # Store item delegate
        self.account_delegate = AccountDelegate()

        # ListView to display all accounts
        self.accounts_list = QListView()

        # Store bank identifiers
        self.bank_identifiers = {}

        # Store accounts identifiers
        self.account_identifiers = {}

        # Store dialog for adding account
        self.dialog = None

        # Model to handle data in accounts list
        self.accounts_model = AccountsModel()

        self.accounts_list.setModel(self.accounts_model)
        self.accounts_list.setItemDelegate(self.account_delegate)

        # DonutChart to display balance distribution
        self.balance_chart = DonutChart()
        # self.balance_chart.add_slice(39)
        # self.balance_chart.add_slice(21)
        # self.balance_chart.add_slice(40)
        self.balance_chart.set_total_amounts(0, 0)

        # Configure layout
        self.configure_layout()

        # Configure title bar
        self.configure_title_bar()

        # Connect Account groupBox
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals from this panel

        :return: None
        """

        # Connect click on add in title bar to open dialog
        self.ui_setup.accounts.titleBarClicked.connect(self.add_account)

    def configure_title_bar(self):
        """
        Configure TitleBar with icon

        :return: None
        """

        # Set title
        self.ui_setup.accounts.set_title(QCoreApplication.translate("accounts", "Balance"))
        self.ui_setup.accounts.set_button_tooltip(QCoreApplication.translate("accounts", "Add new account"))

        # Hide all widgets in title bar
        self.ui_setup.accounts.disable_search_bar()

    def configure_layout(self):
        """
        Configure layout inside of Container

        :return: None
        """

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setSpacing(30)
        layout.addWidget(self.balance_chart)
        self.accounts_list.setViewportMargins(0, 10, 0, 10)
        layout.addWidget(self.accounts_list)
        layout.setContentsMargins(20, 10, 10, 10)

        self.ui_setup.accounts.setWidget(widget)

    def set_banks(self, banks: list):
        """
        Store banks for popups

        :param banks: banks to set
        :return: None
        """

        for bank in banks:
            self.bank_identifiers[bank.get('name')] = bank.get('id')
            self.accounts_model.add_bank({bank.get('id'): bank.get('name')})

    def add_account(self):
        """
        Open dialog to add new account

        :return: None
        """

        # Set dialog content
        dialog_content = AddAccountDialog(self.bank_identifiers, self.main_window)

        # Set icon
        header_icon = QIcon()
        header_icon.addFile(":/images/images/account_balance_wallet_FILL1_wght400_GRAD0_opsz48.svg",
                            QSize(24, 24), QIcon.Disabled, QIcon.On)

        # Open dialog
        self.dialog = Dialog(QCoreApplication.translate("Accounts", 'Add Account'), header_icon, dialog_content,
                             self.main_window)

        # Connect signal from popup to add new account
        dialog_content.addAccount.connect(self.addAccountCall.emit)

        # Connect signal coming from click on Confirm button
        self.dialog.confirm.connect(dialog_content.check_inputs)

        # Set focus on first widget when opening
        dialog_content.content.account_name.setFocus()

    def add_account_details(self, account: dict):
        """
        Add account to current view and model and close opened dialog

        :param account: account details
        :return: None
        """

        self.accounts_model.add_account(account)
        self.dialog.close()

    def set_accounts(self, accounts: list):
        """
        Store accounts for popups

        :param accounts: accounts to set
        :return: None
        """

        for account in accounts:
            self.account_identifiers[account.get('name')] = account.get('id')
            # Update model
            self.accounts_model.add_account(account)
