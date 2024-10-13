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

    def data(self, index: Union[QModelIndex, QPersistentModelIndex],
             role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole):
        """
        Override data() from QAbstractListModel

        :param index: index
        :param role: role
        :return: according to role (text, ...)
        """

        if (
                isinstance(index, QModelIndex)
                and index.isValid()
                and role == Qt.ItemDataRole.DisplayRole
        ):
            account = self.accounts[index.row()]

            # Return current account list
            result = account

        elif (
                isinstance(index, QModelIndex)
                and index.isValid()
                and role == Qt.ItemDataRole.ToolTipRole
        ):
            account = self.accounts[index.row()]

            # Return current account reference
            result = list(account.keys())[0]
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

    def add_account(self, account: dict):
        """
        Add new account to model

        :param account: account details
        :return: None
        """

        self.beginInsertRows(QModelIndex(), 0, 1)
        data = {
            account.get("account_id"): {
                "bank": account.get("bank"),
                "name": account.get("name"),
                "amount": account.get("amount"),
                "color": account.get("color"),
            }
        }
        self.accounts.append(data)
        self.endInsertRows()

    def update(self, accounts: list[dict]) -> list[dict]:
        """
        Update accounts info

        :param accounts: accounts info
        :return: list of new accounts to add
        """

        accounts_to_add = []

        for account in accounts:
            found = False
            # Parse already stored account to check if it exists
            for index, stored_account in enumerate(self.accounts):
                if list(stored_account.keys())[0] == account.get("account_id"):
                    found = True

                    # Update existing account
                    new_amount = account.get("amount", 0)
                    if new_amount != stored_account.get("amount"):
                        stored_account.update({"amount": new_amount})
                        self.dataChanged.emit(
                            self.index(index, 0), self.index(index, 0)
                        )
                    break

            if found is False:
                # Account not already stored / Account ID not found
                accounts_to_add.append(account)

        return accounts_to_add

    def flags(self, _index):
        """
        Override flags()

        :param _index: index
        :return: flags
        """

        return Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
