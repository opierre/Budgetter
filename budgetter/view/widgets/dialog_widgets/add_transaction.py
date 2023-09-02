from datetime import datetime

from PySide6.QtCore import QStringListModel, QTimer, Signal
from PySide6.QtGui import QColor, QDoubleValidator, Qt, QFont
from PySide6.QtWidgets import QWidget, QCompleter, QButtonGroup, QRadioButton

from budgetter.utils.defines import TransactionType
from budgetter.utils.tools import update_style
from budgetter.view.skeletons.AddTransaction import Ui_AddTransaction
from budgetter.view.widgets.transaction_widgets.means_widget import MeanType

TRANSACTION_COLOR = {
    "Expenses": QColor(254, 77, 151, 255),
    "Dépenses": QColor(254, 77, 151, 255),
    "Income": QColor(109, 210, 48, 255),
    "Revenus": QColor(109, 210, 48, 255),
    "Internal": QColor(250, 202, 0, 255),
    "Interne": QColor(250, 202, 0, 255),
}


class AddEditTransactionDialog(QWidget):
    """
    Add/edit transaction dialog content
    """

    # Signal emitted to add new transaction with type, category, name, amount, amount date, mean, notes, account ID
    addTransaction = Signal(str, str, str, str, str, str, str, int)

    # Signal emitted to edit transaction with type, category, name, amount, amount date, mean, notes, account ID,
    # transaction ID
    editTransaction = Signal(str, str, str, str, str, str, str, int, int)

    def __init__(self, account_ids: dict, transaction_content=None, parent=None):
        super().__init__(parent)

        # Store dialog content
        self.content = Ui_AddTransaction()
        self.content.setupUi(self)

        # Store account identifiers
        self.account_ids = account_ids

        # Store radio button group
        self.mean_group = QButtonGroup()

        # Store transaction group
        self.transaction_type_group = QButtonGroup()

        # Store completer for account choice
        self.account_completer = QCompleter(self.content.account)

        # Store mode
        self._transaction_id = transaction_content.get('id') if transaction_content is not None else -1

        # Configure widgets
        self.configure(transaction_content)

        # Connect signals
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals from this panel

        :return: None
        """

        # Connect clicked type/mean to update style
        self.transaction_type_group.buttonClicked.connect(self.update_style)
        self.mean_group.buttonClicked.connect(self.update_style)

    def update_style(self, button_clicked: QRadioButton) -> None:
        """
        Update font and color

        :return: None
        """

        if button_clicked in self.transaction_type_group.buttons():
            group = self.transaction_type_group
        else:
            group = self.mean_group

        for button in group.buttons():
            # Set font normal
            font = button.font()
            font.setWeight(QFont.Normal)
            button.setFont(font)

            # Set color
            button.setStyleSheet("color: rgba(255, 255, 255, 210);")

        # Set bold font
        font = button_clicked.font()
        font.setWeight(QFont.Bold)
        button_clicked.setFont(font)

        # Set color
        if group == self.transaction_type_group:
            button_clicked.setStyleSheet(
                f"color: rgba({TRANSACTION_COLOR.get(button_clicked.text()).red()},"
                f"{TRANSACTION_COLOR.get(button_clicked.text()).green()},"
                f"{TRANSACTION_COLOR.get(button_clicked.text()).blue()},"
                f"{TRANSACTION_COLOR.get(button_clicked.text()).alpha()});"
            )
        else:
            button_clicked.setStyleSheet("color: rgba(1, 144, 234, 255);")

    def configure(self, transaction_content):
        """
        Configure all widgets

        :param transaction_content: transaction content to edit
        :return: None
        """

        # Configure name attributes
        self.content.name.set_label("Label")
        self.content.name.set_label_background_color(QColor("#1C293B"))
        self.content.name.set_text_color(QColor(255, 255, 255, 255))
        self.content.name.set_label_color(QColor(224, 224, 224, 150))
        if transaction_content is not None:
            self.content.name.setText(transaction_content.get('name'))

        # Configure notes attributes
        self.content.notes.set_label("Notes")
        self.content.notes.set_label_background_color(QColor("#1C293B"))
        self.content.notes.set_text_color(QColor(255, 255, 255, 255))
        self.content.notes.set_label_color(QColor(224, 224, 224, 150))
        if transaction_content is not None:
            self.content.notes.setText(transaction_content.get('comment'))

        # Configure amount attributes
        self.content.amount.set_label("Amount")
        self.content.amount.set_label_background_color(QColor("#1C293B"))
        self.content.amount.set_text_color(QColor(255, 255, 255, 255))
        self.content.amount.set_label_color(QColor(224, 224, 224, 150))
        self.content.amount.setValidator(QDoubleValidator(0, 100000, 2))
        self.content.amount.set_trailing_symbol("€")
        if transaction_content is not None:
            self.content.amount.setText(transaction_content.get('amount'))

        # Configure date edit
        self.content.date.set_label("Date")
        self.content.date.set_label_background_color(QColor("#1C293B"))
        self.content.date.set_text_color(QColor(255, 255, 255, 255))
        self.content.date.set_label_color(QColor(224, 224, 224, 150))
        if transaction_content is not None:
            date = transaction_content.get('date')
            formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
            self.content.date.setText(formatted_date)

        # Configure combobox for account choice
        self.content.account.set_label("Account")
        self.content.account.set_label_background_color(QColor("#1C293B"))
        self.content.account.set_text_color(QColor(255, 255, 255, 255))
        self.content.account.set_label_color(QColor(224, 224, 224, 150))
        self.account_completer.setModel(QStringListModel(self.account_ids.values()))
        self.account_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.account_completer.setCompletionMode(QCompleter.InlineCompletion)
        self.content.account.setCompleter(self.account_completer)
        if transaction_content is not None:
            self.content.account.setText(
                self.account_ids.get(transaction_content.get('account'))
            )

        # Add all means to one group
        self.mean_group.addButton(self.content.card)
        self.mean_group.addButton(self.content.money_transfer)
        self.mean_group.addButton(self.content.cash)
        if transaction_content is not None:
            mean = transaction_content.get('mean')
            if mean == MeanType.CARD:
                self.content.card.setChecked(True)
            elif mean == MeanType.CASH:
                self.content.cash.setChecked(True)
            elif mean == MeanType.TRANSFER:
                self.content.money_transfer.setChecked(True)

        # Add all transaction types to one group
        self.transaction_type_group.addButton(self.content.expenses)
        self.transaction_type_group.addButton(self.content.income)
        self.transaction_type_group.addButton(self.content.transfer)
        if transaction_content is not None:
            transaction_type = transaction_content.get('mean')
            if transaction_type == TransactionType.INCOME:
                self.content.income.setChecked(True)
            elif transaction_type == TransactionType.EXPENSES:
                self.content.expenses.setChecked(True)
            elif transaction_type == TransactionType.INTERNAL:
                self.content.transfer.setChecked(True)

        # Set initial color on expenses/card
        self.update_style(self.content.expenses)
        self.update_style(self.content.card)

    def check_inputs(self):
        """
        Check every inputs on opened dialog

        :return: None
        """

        # Retrieve values
        label = self.content.name.text()
        amount = self.content.amount.text()
        amount_date = self.content.date.text()
        account = self.content.account.text()
        mean = self.mean_group.checkedButton().text().lower()
        transaction_type = self.transaction_type_group.checkedButton().text()
        notes = self.content.notes.text()

        if label != "" and amount != "" and amount_date != "" and account != "":
            # Find corresponding bank identifier
            account_id = None
            for ident, name in self.account_ids.items():
                if name == account:
                    account_id = ident
                    break
            if account_id is None:
                print("Error in account id")
                return

            # Emit signal to close popup and add new transaction
            if self._transaction_id == -1:
                self.addTransaction.emit(
                    transaction_type,
                    0,
                    label,
                    amount,
                    amount_date,
                    mean,
                    notes,
                    account_id,
                )
            else:
                self.editTransaction.emit(
                    transaction_type,
                    0,
                    label,
                    amount,
                    amount_date,
                    mean,
                    notes,
                    account_id,
                    self._transaction_id
                )
            return

        if label == "":
            self.warn_widget(self.content.name)
        if amount == "":
            self.warn_widget(self.content.amount)
        if amount_date == "":
            self.warn_widget(self.content.date)
        if account == "":
            self.warn_widget(self.content.account)

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
