from datetime import datetime

from PySide2.QtCore import QAbstractListModel, Qt, QSortFilterProxyModel, QModelIndex, QDate


class TransactionsFilterModel(QSortFilterProxyModel):
    """
    Filter model for transactions 
    """
    
    def __init__(self):
        super(TransactionsFilterModel, self).__init__()

        """ Default Filter for Income/Expenses """
        self.type = "All"

        """ Default Filter for Accounts """
        self.account = "All"

        """ Filters for search bar """
        self.search = None
        self.search_value = None

    def update_filter(self, new_filter):
        """
        Update current filter
        :param new_filter: filter to set
        :return: void
        """

        self.type = new_filter
        self.invalidateFilter()

    def update_search_filter(self, search_filter, search_value):
        """
        Update current filter on search bar
        :param search_filter: filter to set
        :param search_value: filter value to set
        :return: void
        """

        self.search = search_filter
        self.search_value = search_value
        self.invalidateFilter()

    def add_filter(self, new_filter):
        """
        Add current filter
        :param new_filter: filter to set
        :return: void
        """

        self.account = new_filter
        self.invalidateFilter()

    def delete_transaction(self, index):
        """
        Call for deleteTransaction in source model
        :param index: index in filtered model
        :return: void
        """

        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        indexFromSource = self.mapToSource(index)
        self.sourceModel().delete_transaction(indexFromSource)
        self.endRemoveRows()

    def add_transaction(self):
        """
        Call for add_transaction in source model
        :return: void
        """

        self.beginInsertRows(QModelIndex(), 0, 0)
        self.sourceModel().add_transaction()
        self.endInsertRows()

    def modify_transaction(self, index, value):
        """
        Call for modifyTransaction in source model
        :param index: index in filtered model
        :param value: value
        :return: void
        """

        indexFromSource = self.mapToSource(index)
        self.sourceModel().setData(indexFromSource, value, Qt.DisplayRole)

    def filterAcceptsRow(self, source_row, source_parent):
        """
        Override filterAcceptsRow
        :param source_row: source_row
        :param source_parent: source_parent
        :return: bool
        """

        src_model = self.sourceModel()
        source_index = src_model.index(source_row, 0)
        transaction = source_index.data(Qt.DisplayRole)

        if self.type == 'All' and self.account == 'All':
            if self.search is not None:
                if "name=" in self.search:
                    return transaction["name"].lower() == self.search_value.lower()
                elif "date=" in self.search:
                    return transaction["date"] == self.search_value
                elif "amount=" in self.search:
                    return transaction["amount"] == self.search_value
                else:
                    return True
            else:
                return True
        elif self.type == 'All' and self.account != 'All':
            return transaction["account"] == self.account
        elif self.type != 'All' and self.account == 'All':
            return transaction["type"] == self.type
        elif self.type != 'All' and self.account != 'All':
            return (transaction["type"] == self.type) and (transaction["account"] == self.account)

    def lessThan(self, source_left, source_right):
        """
        Override lessThan
        :param source_left: source_left
        :param source_right: source_right
        :return: bool
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

        """ Store transactions """
        self.transactions = transactions or dict()

    def data(self, index, role):
        """
        Override data() from QAbstractListModel
        :param index: index
        :param role: role
        :return: according to role (text, ...)
        """

        if index.isValid() and role == Qt.DisplayRole:
            transaction = self.transactions[index.row()]

            """ Return current transaction list """
            return transaction

    def setData(self, index, value, role):
        """
        Override setData() from QAbstractListModel
        :param index: index
        :param value: value
        :param role: role
        :return: according to role (text, ...)
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

    def rowCount(self, index):
        """
        Override rowCount() from QAbstractListModel
        :param index: index
        :return: length of datas
        """

        return len(self.transactions)

    def delete_transaction(self, index):
        """
        Remove transaction from model according to index
        :param index: index in model
        :return: void
        """

        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        self.transactions.pop(index.row())
        self.endRemoveRows()

    def add_transaction(self):
        """
        Add transaction to model
        :return: void
        """

        self.beginInsertRows(QModelIndex(), 0, 0)
        previous_type = self.data(self.index(0, 0, QModelIndex()), Qt.DisplayRole)["type"]
        current_date = QDate.currentDate().toString("dd/MM/yyyy")
        self.transactions.insert(0, {"name": "Name", "category": "", "amount": 0, "date": current_date,
                                     "account": "", "type": previous_type, "means": "Virement", "comment": ""})
        self.endInsertRows()

    def flags(self, index):
        """
        Override flags()
        :param index: index
        :return: flags
        """

        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
