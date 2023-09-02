from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from budgetter.view.skeletons.RemoveTransaction import Ui_RemoveTransaction


class RemoveTransactionDialog(QWidget):
    """
    Remove transaction dialog content
    """

    # Signal emitted to remove transaction with ID
    removeTransaction = Signal(int)

    def __init__(self, transaction_id: int, parent=None):
        super().__init__(parent)

        # Store transaction ID
        self._transaction_id = transaction_id

        # Store dialog content
        self.content = Ui_RemoveTransaction()
        self.content.setupUi(self)

    def confirm_removal(self):
        """
        Emit signal to delete entry from database

        :return: None
        """

        self.removeTransaction.emit(self._transaction_id)
