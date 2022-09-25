from PySide6.QtCore import QTimer, Signal, QStringListModel
from PySide6.QtGui import QColor, QDoubleValidator, Qt
from PySide6.QtWidgets import QWidget, QCompleter

from budgetter.utils.tools import update_style
from budgetter.view.skeletons.AddAccount import Ui_AddAccount


class AddAccountDialog(QWidget):
    """
    Add account dialog content
    """

    # Signal emitted to add new account with name, amount, bank identifier
    addAccount = Signal(str, str, int)

    def __init__(self, bank_ids: dict, parent=None):
        super().__init__(parent)

        # Store dialog content
        self.content = Ui_AddAccount()
        self.content.setupUi(self)

        # Store bank identifiers
        self.bank_ids = bank_ids

        # Store completer for bank choices
        self.bank_completer = QCompleter(self.content.account_bank)

        # Configure widgets
        self.configure()

    def configure(self):
        """
        Configure all widgets

        :return: None
        """

        # Configure account name attributes
        self.content.account_name.set_label('Account Name')
        self.content.account_name.set_label_background_color(QColor("#1C293B"))
        self.content.account_name.set_text_color(QColor(255, 255, 255, 255))
        self.content.account_name.set_label_color(QColor(224, 224, 224, 150))

        # Configure amount attributes
        self.content.account_amount.set_label('Initial Amount')
        self.content.account_amount.set_label_background_color(QColor("#1C293B"))
        self.content.account_amount.set_text_color(QColor(255, 255, 255, 255))
        self.content.account_amount.set_label_color(QColor(224, 224, 224, 150))
        self.content.account_amount.setValidator(QDoubleValidator(0, 100000, 2))
        self.content.account_amount.set_trailing_symbol("€")

        # Configure date edit
        self.content.account_amount_date.set_label('Date')
        self.content.account_amount_date.set_label_background_color(QColor("#1C293B"))
        self.content.account_amount_date.set_text_color(QColor(255, 255, 255, 255))
        self.content.account_amount_date.set_label_color(QColor(224, 224, 224, 150))

        # Configure combobox for bank choice
        self.content.account_bank.set_label('Bank')
        self.content.account_bank.set_label_background_color(QColor("#1C293B"))
        self.content.account_bank.set_text_color(QColor(255, 255, 255, 255))
        self.content.account_bank.set_label_color(QColor(224, 224, 224, 150))
        self.bank_completer.setModel(QStringListModel(self.bank_ids.keys()))
        self.bank_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.bank_completer.setCompletionMode(QCompleter.InlineCompletion)
        self.content.account_bank.setCompleter(self.bank_completer)

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

        if account_name != '' and \
                account_amount != '' and \
                account_amount_date != '' and \
                account_bank != '':
            # Find corresponding bank identifier
            bank_id = self.bank_ids.get(account_bank, None)
            if bank_id is None:
                print('Error in bank id')
                return

            # Emit signal to close popup and add new account
            self.addAccount.emit(account_name, account_amount, bank_id)
            return

        if account_name == '':
            self.warn_widget(self.content.account_name)
        if account_amount == '':
            self.warn_widget(self.content.account_amount)
        if account_amount_date == '':
            self.warn_widget(self.content.account_amount_date)
        if account_bank == '':
            self.warn_widget(self.content.account_bank)

    @staticmethod
    def warn_widget(widget: QWidget):
        """
        Make widget red highlighted

        :param widget: widget to highlight
        :return: None
        """

        back_style_sheet = widget.styleSheet()
        QTimer.singleShot(0, lambda: update_style(widget, "  border: 2px solid #e84134;"
                                                          "  border-radius: 5px;"
                                                          "  padding-left: 9px"))
        QTimer.singleShot(2000, lambda: update_style(widget, back_style_sheet))
