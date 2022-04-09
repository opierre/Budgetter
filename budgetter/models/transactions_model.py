import typing
from datetime import datetime

from PySide2.QtCore import QAbstractListModel, Qt, QSortFilterProxyModel, QModelIndex, QDate


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

    def add_transaction(self):
        """
        Call for add_transaction in source model

        :return: None
        """

        self.beginInsertRows(QModelIndex(), 0, 0)
        self.sourceModel().add_transaction()
        self.endInsertRows()

    def modify_transaction(self, index, value):
        """
        Call for modifyTransaction in source model
        :param index: index in filtered model
        :param value: value
        :return: None
        """

        index_from_source = self.mapToSource(index)
        self.sourceModel().setData(index_from_source, value, Qt.DisplayRole)

    def filterAcceptsRow(self, source_row, source_parent):
        """
        Override filterAcceptsRow()

        :param source_row: source_row
        :param source_parent: source_parent
        :return: (bool)
        """

        src_model = self.sourceModel()
        source_index = src_model.index(source_row, 0)
        transaction = source_index.data(Qt.DisplayRole)

        if self.type == 'All' and self.account == 'All':
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
        elif self.type == 'All' and self.account != 'All':
            result = transaction["account"] == self.account
        elif self.type != 'All' and self.account == 'All':
            result = transaction["type"] == self.type
        elif self.type != 'All' and self.account != 'All':
            result = (transaction["type"] == self.type) and (transaction["account"] == self.account)
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

        left_data_date = self.sourceModel().data(source_left, Qt.DisplayRole)["date"]
        right_data_date = self.sourceModel().data(source_right, Qt.DisplayRole)["date"]

        left_date = datetime.strptime(left_data_date, "%d/%m/%Y")
        right_date = datetime.strptime(right_data_date, "%d/%m/%Y")

        return left_date < right_date


class TransactionsModel(QAbstractListModel):
    """
    Transactions model
    """

    def __init__(self, transactions=None):
        super().__init__()

        # Store transactions
        self.transactions = transactions or {}

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        """
        Override data() from QAbstractListModel

        :param index: (QModelIndex) index
        :param role: role
        :return: according to role (text, ...)
        """

        if index.isValid() and role == Qt.DisplayRole:
            transaction = self.transactions[index.row()]

            # Return current transaction list
            return transaction
        else:
            return None

    def setData(self, index: QModelIndex, value: typing.Any, role=Qt.ItemDataRole.EditRole) -> True:
        """
        Override setData() from QAbstractListModel

        :param index: index
        :param value: value
        :param role: role
        :return: True
        """

        self.transactions[index.row()]["name"] = value["name"]
        self.transactions[index.row()]["category"] = value["category"]
        self.transactions[index.row()]["amount"] = value["amount"]
        self.transactions[index.row()]["date"] = value["date"]
        self.transactions[index.row()]["account"] = value["account"]
        self.transactions[index.row()]["type"] = value["type"]
        self.transactions[index.row()]["means"] = value["means"]
        self.transactions[index.row()]["comment"] = value["comment"]

        self.dataChanged.emit(index, index)

        return True

    def rowCount(self, index: QModelIndex = QModelIndex()):
        """
        Override rowCount() from QAbstractListModel

        :param index: index
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

    def add_transaction(self):
        """
        Add transaction to model

        :return: None
        """

        self.beginInsertRows(QModelIndex(), 0, 0)
        previous_type = self.data(self.index(0, 0, QModelIndex()), Qt.DisplayRole)["type"]
        current_date = QDate.currentDate().toString("dd/MM/yyyy")
        self.transactions.insert(0, {"name": "Enter name", "category": "", "amount": 0, "date": current_date,
                                     "account": "", "type": previous_type, "means": "Virement", "comment": ""})
        self.endInsertRows()

    def flags(self, index):
        """
        Override flags()

        :param index: index
        :return: flags
        """

        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
