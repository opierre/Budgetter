from typing import Union, List

from PySide6.QtCore import QObject, Qt, QSize, QCoreApplication, Signal, QTimer
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
from budgetter.view.widgets.dialog_widgets.add_transaction import (
    AddEditTransactionDialog,
)
from budgetter.view.widgets.dialog_widgets.import_transactions import (
    ImportTransactionsDialog,
)
from budgetter.view.widgets.dialog_widgets.remove_transaction import (
    RemoveTransactionDialog,
)
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

    # Signal emitted to remove transaction with transaction ID
    removeTransaction = Signal(int)

    # Signal emitted with OFX file path
    importTransactions = Signal(str)

    # Signal emitted to edit transaction with type, category, name, amount, amount date, mean, notes, account ID,
    # transaction ID
    editTransaction = Signal(str, str, str, str, str, str, str, int, int)

    def __init__(self, gui, parent):
        super().__init__()

        # Store gui and main window
        self.ui_setup = gui
        self.main_window = parent

        # Store custom/classic status bar
        self.custom_status_bar = StatusBar()
        self.status_bar = QStatusBar()

        # Store accounts identifiers
        self.account_identifiers = []

        # Store dialogs for adding account
        self.dialogs = []

        # All button - Type
        self.all = QPushButton(QCoreApplication.translate("transactions", "All", None))

        # Expenses button - Type
        self.expenses = QPushButton(
            QCoreApplication.translate("transactions", "Expenses", None)
        )

        # Incomes button - Type
        self.income = QPushButton(
            QCoreApplication.translate("transactions", "Income", None)
        )

        # Transfers button - Type
        self.transfer = QPushButton(
            QCoreApplication.translate("transactions", "Transfer", None)
        )

        # All button - Account
        self.all_account = QPushButton(
            QCoreApplication.translate("transactions", "All", None)
        )
        self.accounts = []

        # Store item delegate
        self.transaction_delegate = TransactionDelegate()

        # ListView to display all transactions
        self.transactions_listview = QListView()

        # Model for filtering
        self.transactions_filter_model = TransactionsFilterModel()
        self.transactions_model = TransactionsModel()

        # Store shortcut for adding a transaction
        self.transaction_shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_T), self)
        self.delete_shortcut = QShortcut(
            Qt.Key.Key_Delete, self.transactions_listview, context=Qt.WidgetShortcut
        )

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

        # Connect Del key to confirm transaction deletion
        self.delete_shortcut.activated.connect(self.remove_transaction)

        # Connect signal from comment hovered button in list view to open menu with comment content
        self.transaction_delegate.commentHovered.connect(self.display_comment)

        # Connect signal from click/edit on +/search button
        self.ui_setup.transactions.titleBarClicked.connect(self.add_transaction)
        self.ui_setup.transactions.titleBarSearched.connect(self.search_transaction)
        self.ui_setup.transactions.titleBarSecondClicked.connect(
            self.import_transaction
        )

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

        # Connect double click on item to update content
        self.transactions_listview.doubleClicked.connect(self.edit_transaction)

    def add_account_details(self, account: dict):
        """
        Add account to current view and model and close opened dialog

        :param account: account details
        :return: None
        """

        # Add account in model
        accounts = [account]
        accounts.extend(self.account_identifiers)
        self.set_accounts(accounts)

    def remove_transaction(self):
        """
        Open dialog to confirm transaction deletion

        :return: None
        """

        # Get transaction ID
        indexes_list = self.transactions_listview.selectionModel().selectedIndexes()
        transaction_id = indexes_list[0].model().data(indexes_list[0]).get("id")

        # Set dialog content
        dialog_content = RemoveTransactionDialog(transaction_id, self.main_window)

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
                QCoreApplication.translate("Transactions", "Delete Transaction"),
                header_icon,
                dialog_content,
                self.main_window,
            )
        )

        # Connect signal from popup to remove transaction
        dialog_content.removeTransaction.connect(self.removeTransaction.emit)

        # Connect signal coming from click on Confirm button
        self.dialogs[-1].confirm.connect(dialog_content.confirm_removal)
        self.dialogs[-1].escape.connect(self.escape_dialog)

        # Set focus on confirm button
        self.dialogs[-1].set_focus_on_confirm()

    def edit_transaction(self):
        """
        Open dialog to edit transaction

        :return: None
        """

        # Get transaction selected
        indexes_list = self.transactions_listview.selectionModel().selectedIndexes()
        if not indexes_list:
            return
        transaction = indexes_list[0].model().data(indexes_list[0])

        # Set dialog content
        dialog_content = AddEditTransactionDialog(
            self.account_identifiers,
            transaction_content=transaction,
            parent=self.main_window,
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
                QCoreApplication.translate("Transactions", "Edit Transaction"),
                header_icon,
                dialog_content,
                self.main_window,
                confirm_label="UPDATE",
            )
        )

        # Connect signal from popup to remove transaction
        dialog_content.editTransaction.connect(self.editTransaction.emit)

        # Connect signal coming from click on Confirm button
        self.dialogs[-1].confirm.connect(dialog_content.check_inputs)
        self.dialogs[-1].escape.connect(self.escape_dialog)

        # Set focus on first widget when opening
        dialog_content.content.name.setFocus()

    def transaction_removed(self):
        """
        Handle transaction removed

        :return: None
        """

        # Show notification on bank added
        _ = Toaster("Transaction removed", ToasterType.SUCCESS, self.main_window)

        # Update models
        indexes_list = self.transactions_listview.selectionModel().selectedIndexes()
        for index in indexes_list:
            self.transactions_listview.model().removeRow(index.row(), index.parent())

        # Close current popup and show previous one again
        self.dialogs[-1].close()
        self.dialogs.pop(-1)

    def transactions_added(self, transactions: Union[dict, list]):
        """
        Handle transactions added

        :param transactions: transactions details
        :return: None
        """

        # Show notification on bank added
        msg = (
            f"{len(transactions)} transactions "
            if isinstance(transactions, list)
            else "Transaction "
        )
        _ = Toaster(f"{msg} added", ToasterType.SUCCESS, self.main_window)

        # Update models
        transactions_list = (
            transactions if isinstance(transactions, list) else [transactions]
        )
        for transaction in transactions_list:
            for account in self.account_identifiers:
                if account.get("id") == transaction.get("account"):
                    transaction.update({"account_name": account.get("name")})
                    break
        self.transactions_filter_model.add_transactions(transactions)

        # Close current popup and show previous one again
        self.dialogs[-1].close()
        self.dialogs.pop(-1)

    def transaction_edited(self, transaction: dict):
        """
        Handle transaction edited

        :param transaction: transaction details
        :return: None
        """

        # Show notification on transaction added
        _ = Toaster("Transaction edited", ToasterType.SUCCESS, self.main_window)

        # Update models
        account_name = ""
        for account in self.account_identifiers:
            if account.get("id") == transaction.get("account"):
                account_name = account.get("name")
                break
        transaction.update({"account_name": account_name})
        self.transactions_filter_model.edit_transaction(transaction)

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

    def set_accounts(self, accounts: List[dict]):
        """
        Store accounts for popups

        :param accounts: accounts to set
        :return: None
        """

        # Clear previous accounts
        self.account_identifiers.clear()
        for account_button in self.accounts:
            self.status_bar.removeWidget(account_button)
        self.accounts.clear()

        for account in accounts:
            # Store identifier
            self.account_identifiers.append(account)

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
            account_name = ""
            for account in self.account_identifiers:
                if account.get("id") == transaction.get("account"):
                    account_name = account.get("name")
                    break
            transaction.update({"account_name": account_name})
        self.transactions_model.setup_transactions(transactions)

    def add_transaction(self):
        """
        Add transaction on + click

        :return: None
        """

        # Set dialog content
        dialog_content = AddEditTransactionDialog(
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

    def import_transaction(self):
        """
        Import transaction on click

        :return: None
        """

        # Set dialog content
        dialog_content = ImportTransactionsDialog(self.main_window)

        # Set icon
        header_icon = QIcon()
        header_icon.addFile(
            ":/images/images/upload_file_FILL0_wght200_GRAD0_opsz24.svg",
            QSize(24, 24),
            QIcon.Mode.Disabled,
            QIcon.State.On,
        )

        # Open dialog
        self.dialogs.append(
            Dialog(
                QCoreApplication.translate("Transactions", "Import Transactions"),
                header_icon,
                dialog_content,
                self.main_window,
                confirm_label=None,
            )
        )

        # Connect signal from popup to import transactions
        dialog_content.importTransactions.connect(self.start_import)
        dialog_content.computeResize.connect(self.dialogs[-1].adjust_size)

        # Connect signal coming from click on escape key
        self.dialogs[-1].escape.connect(self.escape_dialog)

        # Set focus on first widget when opening
        dialog_content.content.import_path.setFocus()
        QTimer.singleShot(500, dialog_content.load_ofx)

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

    def start_import(self, ofx_path: str):
        """
        Emit signal to start import and show progress bar

        :param ofx_path: pah to OFX file to import
        :return: None
        """

        sender = self.sender()
        if isinstance(sender, ImportTransactionsDialog):
            sender.start_import()
        self.importTransactions.emit(ofx_path)

    def handle_convert_ofx(self, header: dict, message: str):
        """
        Handle OFX data converted to dict

        :param header: data header
        :param message: error message
        :return: None
        :return: None
        """

        if message != "":
            self.dialogs[-1].central_widget().set_error(message)

        # Update info on dialog
        new_accounts = []
        for account in header.get("accounts", []):
            if account.get("account_id", "") not in self.account_identifiers:
                new_accounts.append(account)

        self.dialogs[-1].central_widget().set_header_info(
            header.get("count", -1),
            header.get("start_date", "xx/xx/xxxx").strftime("%d/%m/%Y"),
            header.get("end_date", "xx/xx/xxxx").strftime("%d/%m/%Y"),
            new_accounts,
        )
