from datetime import datetime
from typing import Union, Any, List

from PySide6.QtCore import (
    QAbstractListModel,
    Qt,
    QSortFilterProxyModel,
    QModelIndex,
    QPersistentModelIndex,
)


class TransactionsFilterModel(QSortFilterProxyModel):
    """
    Filter model for transactions
    """

    def __init__(self):
        super().__init__()

        # Default Filter for Income/Expenses
        self.type = "All"

        # Default Filter for Accounts
        self.account = "All"

        # Filters for search bar
        self.search = None
        self.search_value = None

    def update_filter(self, new_filter: str):
        """
        Update current filter

        :param new_filter: (str) filter to set
        :return: None
        """

        self.type = new_filter
        self.invalidateFilter()

    def update_search_filter(self, search_filter: str, search_value: str):
        """
        Update current filter on search bar

        :param search_filter: (str) filter to set
        :param search_value: (str) filter value to set
        :return: None
        """

        self.search = search_filter
        self.search_value = search_value
        self.invalidateFilter()

    def add_filter(self, new_filter: str):
        """
        Add current filter

        :param new_filter: (str) filter to set
        :return: None
        """

        self.account = new_filter
        self.invalidateFilter()

    def delete_transaction(self, index):
        """
        Call for deleteTransaction in source model

        :param index: index in filtered model
        :return: None
        """

        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        index_from_source = self.mapToSource(index)
        self.sourceModel().delete_transaction(index_from_source)
        self.endRemoveRows()

    def add_transaction(self, transaction: dict):
        """
        Call for add_transaction in source model

        :param transaction: transaction to add
        :return: None
        """

        self.beginInsertRows(QModelIndex(), 0, 0)
        self.sourceModel().add_transaction(transaction)
        self.endInsertRows()

    def edit_transaction(self, transaction: dict):
        """
        Call for edit_transaction in source model

        :param transaction: transaction to edit
        :return: None
        """

        index = self.sourceModel().edit_transaction(transaction)
        self.dataChanged.emit(index, index)

    def modify_transaction(self, index, value):
        """
        Call for modifyTransaction in source model
        :param index: index in filtered model
        :param value: value
        :return: None
        """

        index_from_source = self.mapToSource(index)
        self.sourceModel().setData(
            index_from_source, value, Qt.ItemDataRole.DisplayRole
        )

    def filterAcceptsRow(self, source_row, _source_parent):
        """
        Override filterAcceptsRow()

        :param source_row: source_row
        :param _source_parent: source_parent
        :return: (bool)
        """

        src_model = self.sourceModel()
        source_index = src_model.index(source_row, 0)
        transaction = source_index.data(Qt.ItemDataRole.DisplayRole)

        if self.type == "All" and self.account == "All":
            if self.search is not None:
                if "name" in self.search:
                    result = self.search_value.lower() in transaction["name"].lower()
                elif "date" in self.search:
                    result = self.search_value in transaction["date"]
                elif "amount" in self.search:
                    result = str(self.search_value) in str(transaction["amount"])
                else:
                    result = True
            else:
                result = True
        elif self.type == "All" and self.account != "All":
            result = transaction["account"] == self.account
        elif self.type != "All" and self.account == "All":
            result = transaction["transaction_type"].lower() == self.type.lower()
        elif self.type != "All" and self.account != "All":
            result = (transaction["transaction_type"].lower() == self.type.lower()) and (
                    transaction["account"] == self.account
            )
        else:
            result = False

        return result

    def lessThan(self, source_left, source_right):
        """
        Override lessThan()

        :param source_left: source_left
        :param source_right: source_right
        :return: (bool)
        """

        left_data_date = self.sourceModel().data(
            source_left, Qt.ItemDataRole.DisplayRole
        )["date"]
        right_data_date = self.sourceModel().data(
            source_right, Qt.ItemDataRole.DisplayRole
        )["date"]

        left_date = datetime.strptime(left_data_date, "%Y-%m-%d")
        right_date = datetime.strptime(right_data_date, "%Y-%m-%d")

        return left_date < right_date


class TransactionsModel(QAbstractListModel):
    """
    Transactions model
    """

    def __init__(self, transactions: List[dict] = None):
        super().__init__()

        # Store transactions
        self.transactions = transactions or []

    def data(
            self,
            index: Union[QModelIndex, QPersistentModelIndex],
            role=Qt.ItemDataRole.DisplayRole,
    ):
        """
        Override data() from QAbstractListModel

        :param index: (QModelIndex) index
        :param role: role
        :return: according to role (text, ...)
        """

        if (
                isinstance(index, QModelIndex)
                and index.isValid()
                and role == Qt.ItemDataRole.DisplayRole
        ):
            transaction = self.transactions[index.row()]

            # Return current transaction list
            result = transaction
        else:
            result = None

        return result

    def setData(
            self,
            index: Union[QModelIndex, QPersistentModelIndex],
            value: Any,
            _role=Qt.ItemDataRole.EditRole,
    ) -> bool:
        """
        Override setData() from QAbstractListModel

        :param index: index
        :param value: value
        :param _role: role
        :return: bool (always True)
        """

        self.transactions[index.row()].update({"name": value["name"]})
        self.transactions[index.row()].update({"category": value["category"]})
        self.transactions[index.row()].update({"amount": value["amount"]})
        self.transactions[index.row()].update({"date": value["date"]})
        self.transactions[index.row()].update({"account_name": value["account_name"]})
        self.transactions[index.row()].update(
            {"transaction_type": value["transaction_type"]}
        )
        self.transactions[index.row()].update({"mean": value["mean"]})
        self.transactions[index.row()].update({"comment": value["comment"]})

        self.dataChanged.emit(index, index)  # pylint: disable=no-member

        return True

    def rowCount(
            self, _index: Union[QModelIndex, QPersistentModelIndex] = QModelIndex()
    ):
        """
        Override rowCount() from QAbstractListModel

        :param _index: index
        :return: (int) length of datas
        """

        return len(self.transactions)

    def delete_transaction(self, index):
        """
        Remove transaction from model according to index

        :param index: index in model
        :return: None
        """

        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        self.transactions.pop(index.row())
        self.endRemoveRows()

    def add_transaction(self, transaction: dict):
        """
        Add transaction to model

        :param transaction: transaction to add
        :return: None
        """

        self.beginInsertRows(QModelIndex(), 0, 0)
        self.transactions.insert(0, transaction)
        self.endInsertRows()

    def edit_transaction(self, transaction: dict) -> QModelIndex:
        """
        Edit transaction from model

        :param transaction: transaction to edit
        :return: model index updated
        """

        index_updated = QModelIndex()
        for index, existing_transaction in enumerate(self.transactions):
            if existing_transaction.get('id') == transaction.get('id'):
                existing_transaction.update(transaction)
                index_updated = self.index(index, 0)
                self.dataChanged.emit(index_updated, index_updated)
                break

        return index_updated

    def flags(self, _index):
        """
        Override flags()

        :param _index: index
        :return: flags
        """

        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setup_transactions(self, transactions: list):
        """
        Add transactions to model

        :param transactions: transactions as a list
        :return: None
        """

        self.beginInsertRows(QModelIndex(), 0, len(transactions) - 1)
        for transaction in transactions:
            self.transactions.insert(0, transaction)
        self.endInsertRows()
