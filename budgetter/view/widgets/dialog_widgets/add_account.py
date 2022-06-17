from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QColor, QDoubleValidator

from budgetter.view.skeletons.AddAccount import Ui_AddAccount


class AddAccountDialog(QWidget):
    """
    Add account dialgo content
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store dialog content
        self.content = Ui_AddAccount()
        self.content.setupUi(self)

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

        # Configure combobof for bank choice
        self.content.bank_auto_complete.set_label('Bank')
        self.content.bank_auto_complete.set_label_background_color(QColor("#1C293B"))
        self.content.bank_auto_complete.set_text_color(QColor(255, 255, 255, 255))
        self.content.bank_auto_complete.set_label_color(QColor(224, 224, 224, 150))
