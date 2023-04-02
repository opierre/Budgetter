from PySide6.QtCore import QTimer, Signal, QStringListModel, QSize
from PySide6.QtGui import QColor, QDoubleValidator, Qt, QIcon
from PySide6.QtWidgets import QWidget, QCompleter

from budgetter.utils.tools import update_style
from budgetter.view.skeletons.AddAccount import Ui_AddAccount


class AddAccountDialog(QWidget):
    """
    Add account dialog content
    """

    # Signal emitted to add new account with name, amount, bank identifier, date, new bank name, color
    addAccount = Signal(str, str, int, str, str, str)

    # Signal emitted to open color picker dialog
    openColorDialog = Signal()

    def __init__(self, bank_ids: dict, parent=None):
        super().__init__(parent)

        # Store dialog content
        self.content = Ui_AddAccount()
        self.content.setupUi(self)

        # Store bank identifiers
        self.bank_ids = bank_ids

        # Store current color
        self._color_dialog = None
        self._color = "white"

        # Store completer for bank choices
        self.bank_completer = QCompleter(self.content.account_bank)

        # Configure widgets
        self.configure()

        # Connect slots and signals
        self.connect_slots_and_signals()

    def configure(self):
        """
        Configure all widgets

        :return: None
        """

        # Configure account name attributes
        self.content.account_name.set_label("Account Name")
        self.content.account_name.set_label_background_color(QColor("#1C293B"))
        self.content.account_name.set_text_color(QColor(255, 255, 255, 255))
        self.content.account_name.set_label_color(QColor(224, 224, 224, 150))

        # Configure amount attributes
        self.content.account_amount.set_label("Initial Amount")
        self.content.account_amount.set_label_background_color(QColor("#1C293B"))
        self.content.account_amount.set_text_color(QColor(255, 255, 255, 255))
        self.content.account_amount.set_label_color(QColor(224, 224, 224, 150))
        self.content.account_amount.setValidator(QDoubleValidator(0, 100000, 2))
        self.content.account_amount.set_trailing_symbol("€")

        # Configure date edit
        self.content.account_amount_date.set_label("Date")
        self.content.account_amount_date.set_label_background_color(QColor("#1C293B"))
        self.content.account_amount_date.set_text_color(QColor(255, 255, 255, 255))
        self.content.account_amount_date.set_label_color(QColor(224, 224, 224, 150))

        # Configure combobox for bank choice
        self.content.account_bank.set_label("Bank")
        self.content.account_bank.set_label_background_color(QColor("#1C293B"))
        self.content.account_bank.set_text_color(QColor(255, 255, 255, 255))
        self.content.account_bank.set_label_color(QColor(224, 224, 224, 150))
        self.bank_completer.setModel(QStringListModel(self.bank_ids.keys()))
        self.bank_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.bank_completer.setCompletionMode(QCompleter.InlineCompletion)
        self.content.account_bank.setCompleter(self.bank_completer)

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals from this panel

        :return: None
        """

        # Connect click on palette to open color dialog
        self.content.color_picker.clicked.connect(self.open_color_dialog)

    def open_color_dialog(self):
        """
        Open dialog to let user pick a color for current account

        :return: None
        """

        # Emit signal to open color picker dialog
        self.openColorDialog.emit()

    def update_color(self, color: str):
        """
        Update current selected color

        :param color: color to set
        :return: None
        """

        # Update color
        self._color = color

        # Transform color to reduce opacity
        transparent_color = QColor(color)

        # Update icon and stylesheet
        palette_icon = QIcon()
        if color != "":
            self.content.color_picker.setStyleSheet(
                f"background-color: rgba({transparent_color.red()},"
                f"{transparent_color.green()}, {transparent_color.blue()}, 128);"
            )
            palette_icon.addFile(
                ":/images/images/palette_FILL0_wght500_GRAD0_opsz48_white.svg",
                QSize(24, 24),
                QIcon.Mode.Normal,
                QIcon.State.On,
            )
        else:
            self.content.color_picker.setStyleSheet(f"background-color: transparent;")
            palette_icon.addFile(
                ":/images/images/palette_FILL0_wght500_GRAD0_opsz48.svg",
                QSize(24, 24),
                QIcon.Mode.Normal,
                QIcon.State.On,
            )
        self.content.color_picker.setIcon(palette_icon)

    def check_inputs(self):
        """
        Check every inputs on opened dialog

        :return: None
        """

        # Retrieve values
        account_name = self.content.account_name.text()
        account_amount = self.content.account_amount.text()
        account_amount_date = self.content.account_amount_date.text()
        account_bank = self.content.account_bank.text()

        if (
                account_name != ""
                and account_amount != ""
                and account_amount_date != ""
                and account_bank != ""
        ):
            # Find corresponding bank identifier
            bank_id = self.bank_ids.get(account_bank, None)
            if bank_id is None:
                bank_id = -1

            # Emit signal to close popup and add new account
            self.addAccount.emit(
                account_name,
                account_amount,
                bank_id,
                account_amount_date,
                account_bank,
                self._color,
            )
            return

        if account_name == "":
            self.warn_widget(self.content.account_name)
        if account_amount == "":
            self.warn_widget(self.content.account_amount)
        if account_amount_date == "":
            self.warn_widget(self.content.account_amount_date)
        if account_bank == "":
            self.warn_widget(self.content.account_bank)

    @staticmethod
    def warn_widget(widget: QWidget):
        """
        Make widget red highlighted

        :param widget: widget to highlight
        :return: None
        """

        back_style_sheet = widget.styleSheet()
        QTimer.singleShot(
            0,
            lambda: update_style(
                widget,
                "  border: 2px solid #e84134;"
                "  border-radius: 5px;"
                "  padding-left: 9px",
            ),
        )
        QTimer.singleShot(2000, lambda: update_style(widget, back_style_sheet))
