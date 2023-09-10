from PySide6.QtCore import Signal
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QLineEdit

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

        # Set browse icon
        # TODO: browse icon
        browse_icon = QIcon(":/images/images/hdr_weak_black_18dp_expenses.svg")
        browse_action = QAction(browse_icon, "")
        self.content.import_path.addAction(
            browse_action, QLineEdit.ActionPosition.TrailingPosition
        )

    def get_ofx_path(self):
        """
        Emit current OFX path

        :return: None
        """

        self.importTransactions.emit(self.content.import_path.text())
