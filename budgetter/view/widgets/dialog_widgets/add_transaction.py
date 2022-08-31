from PySide6.QtCore import QStringListModel, QTimer, Signal
from PySide6.QtGui import QColor, QDoubleValidator, Qt
from PySide6.QtWidgets import QWidget, QCompleter

from budgetter.utils.tools import update_style
from budgetter.view.skeletons.AddTransaction import Ui_AddTransaction


class AddTransactionDialog(QWidget):
    """
    Add transaction dialog content
    """

    # Signal emitted to add new transaction with type, category, name, amount, amount date, mean, notes
    addTransaction = Signal(str, str, str, str, str, str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store dialog content
        self.content = Ui_AddTransaction()
        self.content.setupUi(self)

        # Store completer for bank choices
        self.category_completer = QCompleter(self.content.category)

        # Configure widgets
        self.configure()

    def configure(self):
        """
        Configure all widgets

        :return: None
        """

        # Configure name attributes
        self.content.name.set_label('Label')
        self.content.name.set_label_background_color(QColor("#1C293B"))
        self.content.name.set_text_color(QColor(255, 255, 255, 255))
        self.content.name.set_label_color(QColor(224, 224, 224, 150))

        # Configure notes attributes
        self.content.notes.set_label('Notes')
        self.content.notes.set_label_background_color(QColor("#1C293B"))
        self.content.notes.set_text_color(QColor(255, 255, 255, 255))
        self.content.notes.set_label_color(QColor(224, 224, 224, 150))

        # Configure amount attributes
        self.content.amount.set_label('Amount')
        self.content.amount.set_label_background_color(QColor("#1C293B"))
        self.content.amount.set_text_color(QColor(255, 255, 255, 255))
        self.content.amount.set_label_color(QColor(224, 224, 224, 150))
        self.content.amount.setValidator(QDoubleValidator(0, 100000, 2))
        self.content.amount.set_trailing_symbol("€")

        # Configure date edit
        self.content.date.set_label('Date')
        self.content.date.set_label_background_color(QColor("#1C293B"))
        self.content.date.set_text_color(QColor(255, 255, 255, 255))
        self.content.date.set_label_color(QColor(224, 224, 224, 150))

        # Configure combobox for category choice
        self.content.category.set_label('Category')
        self.content.category.set_label_background_color(QColor("#1C293B"))
        self.content.category.set_text_color(QColor(255, 255, 255, 255))
        self.content.category.set_label_color(QColor(224, 224, 224, 150))
        self.category_completer.setModel(QStringListModel(['Restaurant', 'Car']))
        self.category_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.category_completer.setCompletionMode(QCompleter.InlineCompletion)
        self.content.category.setCompleter(self.category_completer)

    def check_inputs(self):
        """
        Check every inputs on opened dialog

        :return: None
        """

        # Retrieve values
        name = self.content.name.text()
        amount = self.content.amount.text()
        amount_date = self.content.date.text()
        category = self.content.category.text()

        if name != '' and \
                amount != '' and \
                amount_date != '' and \
                category != '':
            # Emit signal to close popup and add new transaction
            self.addTransaction.emit(name, amount, amount_date, category)
            return

        if name == '':
            self.warn_widget(self.content.name)
        if amount == '':
            self.warn_widget(self.content.amount)
        if amount_date == '':
            self.warn_widget(self.content.date)
        if category == '':
            self.warn_widget(self.content.category)

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
