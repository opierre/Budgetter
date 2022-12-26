from PySide6.QtCore import QTimer, Signal, QRegularExpression, QRegularExpressionMatch
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget

from budgetter.utils.tools import update_style
from budgetter.view.skeletons.ColorPicker import Ui_ColorPicker


class ColorPickerDialog(QWidget):
    """
    Add account dialog content
    """

    # Signal emitted with new color
    colorSelected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store dialog content
        self.content = Ui_ColorPicker()
        self.content.setupUi(self)

        # Store current color
        self._color_dialog = None
        self._color = QColor("white")

        # Configure widgets
        self.configure()

        # Connect slots and signals
        self.connect_slots_and_signals()

    def configure(self):
        """
        Configure all widgets

        :return: None
        """

        # Configure color edit attributes
        self.content.color_edit.set_label('HEX Color')
        self.content.color_edit.set_label_background_color(QColor("#1C293B"))
        self.content.color_edit.set_text_color(QColor(255, 255, 255, 255))
        self.content.color_edit.set_label_color(QColor(224, 224, 224, 150))
        self.content.color_edit.set_trailing_symbol("#")

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals for current dialog

        :return: None
        """

        # Connect new entry in text edit to update displayed color
        self.content.color_edit.textChanged.connect(self.display_color)

    def display_color(self, color_text: str):
        """
        Update display color

        :param color_text: color to set
        :return: None
        """

        if color_text == '':
            self.content.color_choice.setStyleSheet(
                "background-radius: 2px;\nbackground-color: #26374d;\n"
                "border: 2px solid #2b405b;\nborder-radius: 2px;")
        else:
            # Check color
            hex_reg_exp = QRegularExpression("^[0-9A-F]{6}$", QRegularExpression.CaseInsensitiveOption)
            match: QRegularExpressionMatch = hex_reg_exp.match(color_text)
            if match.hasMatch():
                self.content.color_choice.setStyleSheet(
                    f"background-radius: 2px;\nbackground-color: #{color_text};\n"
                    "border: 2px solid #0190EA;\nborder-radius: 2px;")
            else:
                self.content.color_choice.setStyleSheet(
                    "background-radius: 2px;\nbackground-color: #26374d;\n"
                    "border: 2px solid #2b405b;\nborder-radius: 2px;")

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
                    bank_id = -1

                # Emit signal to close popup and add new account
                self.addAccount.emit(account_name, account_amount, bank_id, account_amount_date,
                                     account_bank)
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
