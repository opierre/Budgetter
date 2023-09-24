import os

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QFileDialog

from budgetter.view.skeletons.ImportTransactions import Ui_ImportTransactions


class ImportTransactionsDialog(QWidget):
    """
    Import transactions dialog content
    """

    # Signal emitted to import transactions
    importTransactions = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store dialog content
        self.content = Ui_ImportTransactions()
        self.content.setupUi(self)

        # Configure widgets
        self.configure()

    def configure(self):
        """
        Configure all widgets

        :return: None
        """

        # Set browse icon with rescale mode
        browse_action = self.content.import_path.addAction(
            QIcon(":/images/images/folder_open_FILL1_wght500_GRAD0_opsz24.svg"),
            QLineEdit.ActionPosition.TrailingPosition,
        )
        browse_action.triggered.connect(self.load_ofx)

        # Hide header info first
        self.content.header_info.setVisible(False)

    def get_ofx_path(self):
        """
        Emit current OFX path

        :return: None
        """

        self.importTransactions.emit(self.content.import_path.text())

    def load_ofx(self):
        """
        Open OS dialog to search for OFX to download

        :return: None
        """

        # Open OS dialog to select file
        file_name, _ = QFileDialog.getOpenFileName(
            self.parent(),
            "Load OFX file",
            os.path.expanduser("~"),
            "All files (*); OFX files (*.ofx)",
        )

        if file_name:
            self.content.import_path.setText(file_name)
