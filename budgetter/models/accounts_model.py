from typing import Union

from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex, QPersistentModelIndex


class AccountsModel(QAbstractListModel):
    """
    Accounts model
    """

    def __init__(self, categories=None):
        super().__init__()

        # Store accounts
        self.accounts = categories or []

        # Store bank idents/name
        self.banks = {}

    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int = -1):
        """
        Override data() from QAbstractListModel

        :param index: index
        :param role: role
        :return: according to role (text, ...)
        """

        if index.isValid() and role == Qt.ItemDataRole.DisplayRole:
            account = self.accounts[index.row()]

            # Return current account list
            result = account
        else:
            result = None

        return result

    def rowCount(
            self, _index: Union[QModelIndex, QPersistentModelIndex] = QModelIndex()
    ):
        """
        Override rowCount() from QAbstractListModel

        :param _index: index
        :return: length of datas
        """

        return len(self.accounts)

    def add_bank(self, bank: dict):
        """
        Add new bank

        :param bank: bank to store
        :return: None
        """

        self.banks.update(bank)

    def add_account(self, account: dict):
        """
        Add new account to model

        :param account: account details
        :return: None
        """

        self.beginInsertRows(QModelIndex(), 0, 1)
        data = {
            "bank": self.banks.get(account.get("bank")),
            "name": account.get("name"),
            "amount": account.get("amount"),
            "color": account.get("color"),
        }
        self.accounts.append(data)
        self.endInsertRows()
