from PySide6.QtCore import QObject, Qt, QSize, QCoreApplication, Signal
from PySide6.QtGui import QIcon, QShortcut, QKeySequence
from PySide6.QtWidgets import (
    QVBoxLayout,
    QStatusBar,
    QWidget,
    QPushButton,
    QListView,
    QFrame,
)

from budgetter.models.transactions_model import (
    TransactionsModel,
    TransactionsFilterModel,
)
from budgetter.view.widgets.dialog import Dialog
from budgetter.view.widgets.dialog_widgets.add_transaction import AddTransactionDialog
from budgetter.view.widgets.status_bar import StatusBar
from budgetter.view.widgets.toaster.toaster import Toaster, ToasterType
from budgetter.view.widgets.transaction_widgets.transaction_delegate import (
    TransactionDelegate,
)


class Transactions(QObject):
    """
    Transactions
    """

    # Signal emitted to add new transaction with type, category, name, amount, amount date, mean, notes, account ID
    addTransaction = Signal(str, str, str, str, str, str, str, int)

    def __init__(self, gui, parent):
        super().__init__()

        # Store gui and main window
        self.ui_setup = gui
        self.main_window = parent

        # Store custom/classic status bar
        self.custom_status_bar = StatusBar()
        self.status_bar = QStatusBar()

        # Store accounts identifiers
        self.account_identifiers = {}

        # Store dialogs for adding account
        self.dialogs = []

        # Store shortcut for adding a transaction
        self.transaction_shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_T), self)

        # All button - Type
        self.all = QPushButton(QCoreApplication.translate("transactions", "All"))

        # Expenses button - Type
        self.expenses = QPushButton(
            QCoreApplication.translate("transactions", "Expenses")
        )

        # Incomes button - Type
        self.income = QPushButton(QCoreApplication.translate("transactions", "Income"))

        # Transfers button - Type
        self.transfer = QPushButton(
            QCoreApplication.translate("transactions", "Transfer")
        )

        # All button - Account
        self.all_account = QPushButton(
            QCoreApplication.translate("transactions", "All")
        )
        self.accounts = []

        # Store item delegate
        self.transaction_delegate = TransactionDelegate()

        # ListView to display all transactions
        self.transactions_listview = QListView()

        # Model for filtering
        self.transactions_filter_model = TransactionsFilterModel()

        self.transactions_model = TransactionsModel()

        # Configure status bar
        self.configure_status_bar()

        # Configure layout
        self.configure_layout()

        # Configure List view
        self.configure_list_view()

        # Configure TitleBar
        self.configure_title_bar()

        # Connect all widgets
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect signal from Delete button in list view to delete item
        self.transaction_delegate.transactionDeletePressed.connect(
            self.delete_transaction
        )

        # Connect signal from Apply button in list view to modify item
        self.transaction_delegate.transactionModified.connect(self.modify_transaction)

        # Connect signal from comment hovered button in list view to open menu with comment content
        self.transaction_delegate.commentHovered.connect(self.display_comment)

        # Connect signal from click/edit on +/search button
        self.ui_setup.transactions.titleBarClicked.connect(self.add_transaction)
        self.ui_setup.transactions.titleBarSearched.connect(self.search_transaction)

        # Update filtering when click on button in status bar
        self.expenses.clicked.connect(
            self.update_current_filtering
        )  # pylint: disable=no-member
        self.income.clicked.connect(
            self.update_current_filtering
        )  # pylint: disable=no-member
        self.all.clicked.connect(
            self.update_current_filtering
        )  # pylint: disable=no-member
        self.transfer.clicked.connect(
            self.update_current_filtering
        )  # pylint: disable=no-member

        # Update filtering when click on button in status bar
        self.all_account.clicked.connect(self.add_filter)  # pylint: disable=no-member

        # Connect shortcut to add new transaction
        self.transaction_shortcut.activated.connect(
            self.add_transaction
        )  # pylint: disable=no-member

    def transaction_added(self, transaction: dict):
        """
        Handle transaction added

        :param transaction: transaction details
        :return: None
        """

        # Show notification on bank added
        _ = Toaster("Transaction added", ToasterType.SUCCESS, self.main_window)

        # Update models
        transaction.update(
            {
                "account_name": self.account_identifiers.get(
                    transaction.get("account")
                )
            }
        )
        self.transactions_filter_model.add_transaction(transaction)

        # Close current popup and show previous one again
        self.dialogs[-1].close()
        self.dialogs.pop(-1)

    def display_comment(self, rectangle, index):
        """
        Display comment for current index

        :param rectangle: rectangle position
        :param index: current index hovered
        :return: None
        """

        pass

    def delete_transaction(self, index):
        """
        Delete transaction on Delete click

        :param index: index in model
        :return: None
        """

        # Remove transaction from model
        self.transactions_filter_model.delete_transaction(index)

    def set_accounts(self, accounts: list):
        """
        Store accounts for popups

        :param accounts: accounts to set
        :return: None
        """

        # Clear previous accounts
        self.account_identifiers.clear()
        self.accounts.clear()

        for account in accounts:
            # Store identifier
            self.account_identifiers[account.get("id")] = account.get("name")

            # Create new button
            new_account_filter = QPushButton(account.get("name"))
            new_account_filter.clicked.connect(self.add_filter)
            new_account_filter.setProperty("activated", "false")
            new_account_filter.update()
            new_account_filter.setCursor(Qt.CursorShape.PointingHandCursor)
            self.status_bar.addWidget(new_account_filter)

            # Update footer for list view
            self.accounts.append(new_account_filter)

    def set_transactions(self, transactions: list):
        """
        Set transactions in list views

        :param transactions: transactions to set
        :return: None
        """

        for transaction in transactions:
            transaction.update(
                {
                    "account_name": self.account_identifiers.get(
                        transaction.get("account")
                    )
                }
            )
        self.transactions_model.setup_transactions(transactions)

    def add_transaction(self):
        """
        Add transaction on + click

        :return: None
        """

        # Set dialog content
        dialog_content = AddTransactionDialog(
            self.account_identifiers, self.main_window
        )

        # Set icon
        header_icon = QIcon()
        header_icon.addFile(
            ":/images/images/receipt_long_FILL1_wght400_GRAD0_opsz48.svg",
            QSize(24, 24),
            QIcon.Mode.Disabled,
            QIcon.State.On,
        )

        # Open dialog
        self.dialogs.append(
            Dialog(
                QCoreApplication.translate("Transactions", "Add Transaction"),
                header_icon,
                dialog_content,
                self.main_window,
            )
        )

        # Connect signal from popup to add new account
        dialog_content.addTransaction.connect(self.addTransaction.emit)

        # Connect signal coming from click on Confirm button
        self.dialogs[-1].confirm.connect(dialog_content.check_inputs)
        self.dialogs[-1].escape.connect(self.escape_dialog)

        # Set focus on first widget when opening
        dialog_content.content.name.setFocus()

    def escape_dialog(self):
        """
        Escape current dialog

        :return: None
        """

        # Close current popup
        self.dialogs[-1].close()
        self.dialogs.pop()

        if len(self.dialogs) > 0:
            self.dialogs[-1].show(False)

    def search_transaction(self, content: str, search_field: str):
        """
        Search transaction as filter

        :param content: content to look for in transactions
        :param search_field: search field
        :return: None
        """

        # Look for name/date/amount
        if "name" in search_field.lower():
            # Filter model
            self.transactions_filter_model.update_search_filter("name", content)
        elif "date" in search_field.lower():
            # Filter model
            self.transactions_filter_model.update_search_filter("date", content)
        elif "amount" in search_field.lower():
            # Filter model
            self.transactions_filter_model.update_search_filter("amount", content)
        else:
            # Reset filter model
            self.transactions_filter_model.update_search_filter(None, None)

    def modify_transaction(self, index):
        """
        Modify transaction content on Apply click

        :param index: index in model
        :return: None
        """

        # value = {"name": self.edit_name.text(), "category": self.edit_category_name.text(),
        #          "amount": self.edit_amount.value(), "date": self.edit_date.date().toString("dd/MM/yyyy"),
        #          "account": self.edit_account.currentText(), "type": self.edit_exp_or_inc.active_type(),
        #          "means": self.edit_mean.active_type(), "comment": ""}

        # Remove transaction from model
        # self.transactions_filter_model.modify_transaction(self.transaction_delegate.editable, value)

        # TODO: to remove
        # rest_client = RestClient().POST("http://127.0.0.1:8000/dashboard/transaction/", value)

    def configure_layout(self):
        """
        Configure layout inside of Container

        :return: None
        """

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.transactions_listview)
        layout.addWidget(self.status_bar)
        layout.setContentsMargins(0, 10, 0, 0)

        self.ui_setup.transactions.setWidget(widget)

    def configure_list_view(self):
        """
        Configure transactions list view to handle events/model

        :return: None
        """

        # Set proxy model
        self.transactions_filter_model.setSourceModel(self.transactions_model)

        # Date re-filtered if model changed
        self.transactions_filter_model.setDynamicSortFilter(True)
        self.transactions_filter_model.sort(0, Qt.DescendingOrder)

        # Set model
        self.transactions_listview.setModel(self.transactions_filter_model)

        # Set mouse tracking
        self.transactions_listview.setMouseTracking(True)

        # Set item delegate"""
        self.transactions_listview.setItemDelegate(self.transaction_delegate)

    def configure_status_bar(self):
        """
        Configure status bar

        :return: None
        """

        # Set states for activation
        self.all.setProperty("activated", "true")
        self.all.update()
        self.expenses.setProperty("activated", "false")
        self.expenses.update()
        self.income.setProperty("activated", "false")
        self.income.update()
        self.transfer.setProperty("activated", "false")
        self.transfer.update()

        # Set states for activation
        self.all_account.setProperty("activated", "true")
        self.all_account.update()

        # Set cursor for left buttons
        self.all.setCursor(Qt.CursorShape.PointingHandCursor)
        self.expenses.setCursor(Qt.CursorShape.PointingHandCursor)
        self.expenses.setIconSize(QSize(18, 18))
        self.expenses.setIcon(QIcon(":/images/images/hdr_weak_black_18dp_expenses.svg"))
        self.income.setCursor(Qt.CursorShape.PointingHandCursor)
        self.income.setIconSize(QSize(18, 18))
        self.income.setIcon(QIcon(":/images/images/hdr_weak_black_18dp_income.svg"))
        self.transfer.setCursor(Qt.CursorShape.PointingHandCursor)
        self.transfer.setIconSize(QSize(18, 18))
        self.transfer.setIcon(QIcon(":/images/images/hdr_weak_black_18dp_transfer.svg"))

        # Set cursor for left buttons
        self.all_account.setCursor(Qt.CursorShape.PointingHandCursor)

        # Add custom status bar to classic one
        self.status_bar.addPermanentWidget(self.custom_status_bar)

        # Add buttons on left corner
        self.status_bar.addWidget(self.all)
        self.status_bar.addWidget(self.expenses)
        self.status_bar.addWidget(self.income)
        self.status_bar.addWidget(self.transfer)

        # Add separator
        vline = QFrame()
        vline.setFrameShape(QFrame.VLine)
        vline.setFixedHeight(self.all.sizeHint().height() * 1.2)
        vline.setStyleSheet("color: #344457;")
        self.status_bar.addWidget(vline)

        # Add buttons on left corner
        self.status_bar.addWidget(self.all_account)

        # Disable size grip
        self.status_bar.setSizeGripEnabled(False)

        # Hide settings
        self.custom_status_bar.hide_settings()

    def configure_title_bar(self):
        """
        Configure TitleBar with icon

        :return: None
        """

        # Set title
        self.ui_setup.transactions.set_title(
            QCoreApplication.translate("transactions", "Transactions")
        )
        self.ui_setup.transactions.set_button_tooltip(
            QCoreApplication.translate("transactions", "Add transaction")
        )

    def update_current_filtering(self):
        """
        Update current filtering after click on button

        :return: None
        """

        # Retrieve sender
        py_object = self.sender()

        # Retrieve current text
        new_filter = py_object.text()

        # Update filter
        self.transactions_filter_model.update_filter(new_filter)

        # Update activated state
        if new_filter in {"All", "Tout"}:
            self.all.setProperty("activated", "true")
            self.expenses.setProperty("activated", "false")
            self.income.setProperty("activated", "false")
            self.transfer.setProperty("activated", "false")
        elif new_filter in {"Expenses", "Dépenses"}:
            self.all.setProperty("activated", "false")
            self.expenses.setProperty("activated", "true")
            self.income.setProperty("activated", "false")
            self.transfer.setProperty("activated", "false")
        elif new_filter in {"Income", "Revenus"}:
            self.all.setProperty("activated", "false")
            self.expenses.setProperty("activated", "false")
            self.income.setProperty("activated", "true")
            self.transfer.setProperty("activated", "false")
        else:
            self.all.setProperty("activated", "false")
            self.expenses.setProperty("activated", "false")
            self.income.setProperty("activated", "false")
            self.transfer.setProperty("activated", "true")

        # Update style
        self.all.style().unpolish(self.all)
        self.all.style().polish(self.all)
        self.expenses.style().unpolish(self.expenses)
        self.expenses.style().polish(self.expenses)
        self.income.style().unpolish(self.income)
        self.income.style().polish(self.income)
        self.transfer.style().unpolish(self.transfer)
        self.transfer.style().polish(self.transfer)

    def add_filter(self):
        """
        Add filter to current filtering after click on button

        :return: None
        """

        # Retrieve sender
        py_object = self.sender()

        # Retrieve current text
        new_filter = py_object.text()

        # Add filter
        self.transactions_filter_model.add_filter(new_filter)

        # Update activated state
        if new_filter == "All":
            self.all_account.setProperty("activated", "true")
            for account in self.accounts:
                account.setProperty("activated", "false")
        else:
            self.all_account.setProperty("activated", "false")
            for account in self.accounts:
                if new_filter == account.text():
                    account.setProperty("activated", "true")
                else:
                    account.setProperty("activated", "false")

        # Update style
        self.all_account.style().unpolish(self.all_account)
        self.all_account.style().polish(self.all_account)
        for account in self.accounts:
            account.style().unpolish(account)
            account.style().polish(account)
