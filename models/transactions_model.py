from PySide2.QtCore import QAbstractListModel, Qt, QSortFilterProxyModel, QModelIndex


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

    def updateFilter(self, newFilter):
        """
        Update current filter
        :param newFilter: filter to set
        :return: void
        """

        self.type = newFilter
        self.invalidateFilter()

    def addFilter(self, newFilter):
        """
        Add current filter
        :param newFilter: filter to set
        :return: void
        """

        self.account = newFilter
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        """
        Override filterAcceptsRow
        :param source_row: source_row
        :param source_parent: source_parent
        :return: void
        """

        src_model = self.sourceModel()
        source_index = src_model.index(source_row, 0)
        transaction = source_index.data(Qt.DisplayRole)

        if self.type == 'All' and self.account == 'All':
            return True
        elif self.type == 'All' and self.account != 'All':
            return transaction[-2] == self.account
        elif self.type != 'All' and self.account == 'All':
            return transaction[-1] == self.type
        elif self.type != 'All' and self.account != 'All':
            return (transaction[-1] == self.type) and (transaction[-2] == self.account)


class TransactionsModel(QAbstractListModel):
    """
    Transactions model
    """

    def __init__(self, transactions=None):
        super().__init__()

        """ Store transactions - Name/Category/Amount/Date/Account/IncomeOrExpense """
        self.transactions = transactions or []

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

    def rowCount(self, index):
        """
        Override rowCount() from QAbstractListModel
        :param index: index
        :return: length of datas
        """

        return len(self.transactions)

    def deleteTransaction(self, index):
        """
        Remove transaction from model according to index
        :param index: index in model
        :return: void
        """

        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        self.transactions.pop(index.row())
        self.endRemoveRows()
