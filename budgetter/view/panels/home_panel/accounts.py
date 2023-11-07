from PySide6.QtCore import QObject, QCoreApplication, QSize, Signal, QEventLoop
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListView, QWidget, QHBoxLayout

from budgetter.models.accounts_model import AccountsModel
from budgetter.view.widgets.balance_widgets.account_delegate import AccountDelegate
from budgetter.view.widgets.balance_widgets.donut_chart_widget import DonutChart
from budgetter.view.widgets.dialog import Dialog
from budgetter.view.widgets.dialog_widgets.add_account import AddAccountDialog
from budgetter.view.widgets.dialog_widgets.add_bank import AddBankDialog
from budgetter.view.widgets.dialog_widgets.color_picker import ColorPickerDialog
from budgetter.view.widgets.toaster.toaster import Toaster, ToasterType


class Accounts(QObject):
    """
    Accounts
    """

    # Signals list
    addAccountCall = Signal(str, str, int, str, str)
    addBankCall = Signal(str)

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

        # Store dialogs for adding account
        self.dialogs = []

        # Store local event loop
        self._event_loop = QEventLoop()

        # Model to handle data in accounts list
        self.accounts_model = AccountsModel()

        self.accounts_list.setModel(self.accounts_model)
        self.accounts_list.setItemDelegate(self.account_delegate)

        # DonutChart to display balance distribution
        self.balance_chart = DonutChart()
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
        self.ui_setup.accounts.set_title(
            QCoreApplication.translate("accounts", "Balance")
        )
        self.ui_setup.accounts.set_button_tooltip(
            QCoreApplication.translate("accounts", "Add new account")
        )

        # Hide all widgets in title bar
        self.ui_setup.accounts.disable_search_bar()
        self.ui_setup.accounts.disable_upload()

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

        self.bank_identifiers = banks
        self.accounts_model.set_banks(banks)

    def add_account(self, account_info: dict = None):
        """
        Open dialog to add new account

        :param account_info: account info to rely on before adding
        :return: None
        """

        # Set dialog content
        dialog_content = AddAccountDialog(
            self.bank_identifiers, self.main_window, account_info=account_info
        )

        # Set icon
        header_icon = QIcon()
        header_icon.addFile(
            ":/images/images/account_balance_wallet_FILL0_wght400_GRAD0_opsz48.svg",
            QSize(24, 24),
            QIcon.Mode.Disabled,
            QIcon.State.On,
        )

        # Connect signal from popup to add new account
        dialog_content.addAccount.connect(self.pre_add_account)

        # Connect signal to open color picker
        dialog_content.openColorDialog.connect(self.open_color_dialog)

        # Open dialog
        self.dialogs.append(
            Dialog(
                QCoreApplication.translate("Accounts", "Add Account", None),
                header_icon,
                dialog_content,
                self.main_window,
                closable=account_info is None,
            )
        )

        # Connect signal coming from click on Confirm button
        self.dialogs[-1].confirm.connect(dialog_content.check_inputs)
        self.dialogs[-1].escape.connect(self.escape_dialog)

        # Set focus on first widget when opening
        dialog_content.content.account_name.setFocus()

        # Start event loop
        self._event_loop.exec()

    def open_color_dialog(self):
        """
        Open color picker dialog

        :return: None
        """

        # Set dialog content
        dialog_content = ColorPickerDialog(self.main_window)

        # Set icon
        header_icon = QIcon()
        header_icon.addFile(
            ":/images/images/palette_FILL0_wght500_GRAD0_opsz48_white.svg",
            QSize(24, 24),
            QIcon.Mode.Disabled,
            QIcon.State.On,
        )

        # Hide previous dialog
        self.dialogs[-1].hide()

        # Open dialog
        self.dialogs.append(
            Dialog(
                QCoreApplication.translate("Accounts", "Color Picker"),
                header_icon,
                dialog_content,
                self.main_window,
            )
        )

        # Connect signal coming from click on Confirm button
        self.dialogs[-1].confirm.connect(dialog_content.check_inputs)
        self.dialogs[-1].escape.connect(self.escape_dialog)

        # Connect signal from popup to add new account
        dialog_content.colorSelected.connect(self.update_color)

        # Set focus on first widget when opening
        dialog_content.content.color_edit.setFocus()

    def update_color(self, color: str):
        """
        Update selected color

        :param color: color
        :return: None
        """

        # Close previous popup
        self.dialogs[-1].close()
        self.dialogs.pop()

        # Update color
        self.dialogs[-1].show(False)
        self.dialogs[-1].central_widget().update_color(color)

    def escape_dialog(self):
        """
        Escape current dialog

        :return: None
        """

        # Close current popup
        self.dialogs[-1].close()
        self.dialogs.pop()

        # Quit event loop
        self._event_loop.quit()

        if len(self.dialogs) > 0:
            self.dialogs[-1].show(False)

    def pre_add_account(
            self,
            name: str,
            amount: str,
            bank_id: int,
            date: str,
            new_bank_name: str,
            color: str,
    ):
        """
        Check bank already exists

        :param name: account name
        :param amount: amount
        :param bank_id: bank identifier
        :param date: date
        :param new_bank_name: new bank name
        :param color: color for account
        :return: None
        """

        if bank_id == -1:
            # Hide previous dialog
            self.dialogs[-1].hide()

            # Set dialog content
            dialog_content = AddBankDialog(new_bank_name, self.main_window)

            # Set icon
            header_icon = QIcon()
            header_icon.addFile(
                ":/images/images/account_balance_wallet_FILL1_wght400_GRAD0_opsz48.svg",
                QSize(24, 24),
                QIcon.Mode.Disabled,
                QIcon.State.On,
            )

            # Open dialog
            self.dialogs.append(
                Dialog(
                    QCoreApplication.translate("Accounts", "Add Bank"),
                    header_icon,
                    dialog_content,
                    self.main_window,
                    show_overlay=False,
                )
            )

            # Connect signal from popup to add new bank
            dialog_content.addBank.connect(self.addBankCall.emit)

            # Connect signal coming from click on Confirm button
            self.dialogs[-1].confirm.connect(dialog_content.check_inputs)
            self.dialogs[-1].escape.connect(self.escape_dialog)

            # Set focus on first widget when opening
            dialog_content.content.bank_name.setFocus()

        else:
            self.addAccountCall.emit(name, amount, bank_id, date, color)

    def bank_added(self, bank: dict):
        """
        Handle bank added

        :param bank: bank details
        :return: None
        """

        # Show notification on bank added
        _ = Toaster("Bank added", ToasterType.SUCCESS, self.main_window)

        # Update models
        self.bank_identifiers[bank.get("name")] = bank.get("id")
        self.accounts_model.add_bank({bank.get("id"): bank.get("name")})

        # Close current popup and show previous one again
        self.dialogs[-1].close()
        self.dialogs.pop(-1)
        self.dialogs[-1].show(False)

    def add_account_details(self, account: dict):
        """
        Add account to current view and model and close opened dialog

        :param account: account details
        :return: None
        """

        # Add account in model
        self.accounts_model.add_account(account)
        self.dialogs[-1].close()
        self.dialogs.pop(-1)

        # Update balance widget
        self.balance_chart.add_slice(float(account.get("amount")), account.get("color"))

        # Open toaster
        _ = Toaster("Account added", ToasterType.SUCCESS, self.main_window)

        # Stop event loop
        self._event_loop.quit()

    def set_accounts(self, accounts: list):
        """
        Store accounts for popups

        :param accounts: accounts to set
        :return: None
        """

        for account in accounts:
            self.account_identifiers[account.get("name")] = account.get("id")
            # Update model
            self.accounts_model.add_account(account)

            # Update balance widget
            self.balance_chart.add_slice(
                float(account.get("amount")), account.get("color")
            )

    def handle_convert_ofx(self, header: dict):
        """
        Handle conversion from OFX to check new accounts to create

        :param header: header data
        :return: None
        """

        # Update info on dialog
        new_accounts = []
        for account in header.get("accounts", []):
            if account.get("account_id", "") not in self.account_identifiers:
                new_accounts.append(account)

        # Open new dialogs to create new accounts
        if new_accounts:
            i = 0
            for account in new_accounts:
                print(i)
                self.add_account(account)
