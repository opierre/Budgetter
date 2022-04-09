from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex


class AccountsModel(QAbstractListModel):
    """
    Accounts model
    """

    def __init__(self, categories=None):
        super().__init__()

        # Store accounts
        self.accounts = categories or []

    def data(self, index: QModelIndex, role: Qt.ItemDataRole = None):
        """
        Override data() from QAbstractListModel

        :param index: index
        :param role: role
        :return: according to role (text, ...)
        """

        if index.isValid() and role == Qt.DisplayRole:
            account = self.accounts[index.row()]

            # Return current account list
            return account
        else:
            return None

    def rowCount(self, index: QModelIndex = QModelIndex()):
        """
        Override rowCount() from QAbstractListModel

        :param index: index
        :return: length of datas
        """

        return len(self.accounts)
