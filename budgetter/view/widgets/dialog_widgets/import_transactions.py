import os
from typing import List

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QFileDialog

from budgetter.view.skeletons.ImportTransactions import Ui_ImportTransactions


class ImportTransactionsDialog(QWidget):
    """
    Import transactions dialog content
    """

    # Signal emitted to import transactions - File path
    importTransactions = Signal(str)

    # Signal emitted to ask for resize to dialog parent
    computeResize = Signal()

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

        # Hide header info first and progress bar
        self.content.header_info.setVisible(False)
        self.content.import_transactions_progress.setVisible(False)

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
            self.importTransactions.emit(file_name)

    def start_import(self):
        """
        Start import by showing progress bar

        :return: None
        """

        self.content.import_transactions_progress.setVisible(True)
        self.content.import_transactions_progress.setRange(0, 0)

        # Emit signal to resize dialog parent
        self.computeResize.emit()

    def set_header_info(
            self,
            nb_transactions: int,
            start_date: str,
            end_date: str,
            new_accounts: List[dict],
    ):
        """
        Update header info

        :param nb_transactions: number of transactions imported
        :param start_date: start date
        :param end_date: end date
        :param new_accounts: new accounts detected to create
        :return: None
        """

        # Show both widgets for info
        self.content.header_info.setVisible(True)

        # Set content
        if new_accounts:
            accounts_list = ""
            for account in new_accounts:
                accounts_list += f"{account.get('account_id')}\n"
            end_message = (
                f"{len(new_accounts)} new accounts detected: \n{accounts_list}"
            )
            nb_lines = len(accounts_list) + 1
        else:
            end_message = ""
            nb_lines = 0
        message = f"Importing {nb_transactions} transactions from {start_date} to {end_date}...\n{end_message}"
        self.content.header_info.setText(message)
        height_font = self.content.header_info.fontMetrics().height()
        self.content.header_info.setFixedHeight((2 + nb_lines) * height_font)
        self.content.header_info.update()

        # Emit signal to resize dialog parent
        self.computeResize.emit()

    def set_error(self, error: str):
        """
        Update header info with error message

        :param error: error content
        :return: None
        """

        # Show both widgets for info
        self.content.header_info.setVisible(True)
        self.content.import_transactions_progress.setVisible(False)

        # Emit signal to resize dialog parent
        self.computeResize.emit()

        # Set content
        self.content.header_info.setText(
            f"Importing transactions from current file failed: {error}"
        )
