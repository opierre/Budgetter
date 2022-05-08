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
        self.content.account_amount.set_input_line_color(QColor(224, 224, 224, 150))
        self.content.account_amount.set_text_color(QColor(255, 255, 255, 255))
        self.content.account_amount.set_ink_color(QColor("#199DE5"))
        self.content.account_amount.set_label_color(QColor(224, 224, 224, 150))
        self.content.account_amount.setValidator(QDoubleValidator(0, 100000, 2))
        self.content.account_amount.set_trailing_symbol("€")

        # Configure date edit
        self.content.account_amount_date.setFixedHeight(self.content.account_amount.sizeHint().height())
