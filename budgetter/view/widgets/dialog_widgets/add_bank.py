import os
import shutil

from PySide6.QtCore import QTimer, Signal, QSize
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QWidget, QFileDialog

from budgetter.utils.tools import update_style
from budgetter.view.skeletons.AddBank import Ui_AddBank


class AddBankDialog(QWidget):
    """
    Add bank dialog content
    """

    # Signal emitted to add new bank with name
    addBank = Signal(str)

    def __init__(self, bank_name: str, parent=None):
        super().__init__(parent)

        # Store dialog content
        self.content = Ui_AddBank()
        self.content.setupUi(self)

        # Store bank name
        self.bank_name = bank_name
        self.content.bank_name.setText(bank_name)

        # Store bank icon path
        self.bank_icon_path = ""

        # Configure widgets
        self.configure()

        # Connect slots and signals
        self.connect_slot_sand_signals()

    def configure(self):
        """
        Configure all widgets

        :return: None
        """

        # Configure account name attributes
        self.content.bank_name.set_label("Bank Name")
        self.content.bank_name.set_label_background_color(QColor("#1C293B"))
        self.content.bank_name.set_text_color(QColor(255, 255, 255, 255))
        self.content.bank_name.set_label_color(QColor(224, 224, 224, 150))

    def connect_slot_sand_signals(self):
        """
        Connect all slots and signals from within dialog

        :return: None
        """

        # Connect click on tool button to select logo for bank
        self.content.bank_logo.clicked.connect(self.select_logo)

    def select_logo(self):
        """
        Select a logo for current new bank

        :return: None
        """

        # Open OS dialog to select file
        file_name, _ = QFileDialog.getOpenFileName(
            self.parent(),
            "Select a logo for this new bank",
            os.path.expanduser("~"),
            "Image Files (*.png *.svg)",
        )

        # Store path for download
        self.bank_icon_path = os.path.abspath(file_name)

        # Set icon
        if file_name == "":
            file_name = ":/images/images/image_FILL0_wght400_GRAD0_opsz48.svg"
        icon = QIcon()
        icon.addFile(file_name, QSize(40, 40), QIcon.Mode.Normal, QIcon.State.On)
        self.content.bank_logo.setIcon(icon)

    def check_inputs(self):
        """
        Check every inputs on opened dialog

        :return: None
        """

        # Retrieve values
        bank_name = self.content.bank_name.text()

        if bank_name != "":
            # Register icon in current folder
            bank_logo_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "resources",
                "bank_logo",
                bank_name.lower().replace(" ", "_") + "_logo.svg",
            )
            shutil.copyfile(self.bank_icon_path, bank_logo_path)

            # Emit signal to close popup and add new account
            self.addBank.emit(bank_name)
            return

        if bank_name == "":
            self.warn_widget(self.content.bank_name)

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
