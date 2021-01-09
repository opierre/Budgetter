from PySide2.QtCore import QAbstractListModel, Qt, QSortFilterProxyModel


class TransactionsFilterModel(QSortFilterProxyModel):
    """
    Filter model for transactions 
    """
    
    def __init__(self):
        super(TransactionsFilterModel, self).__init__()

    def filterAcceptsRow(self, source_row, source_parent):
        """
        Override filterAcceptsRow
        :param source_row: source_row
        :param source_parent: source_parent
        :return: void
        """

        # src_model = self.sourceModel()
        # src_index = src_model.index(src_row, 0)
        # item_var = src_index.data(Qt.DisplayRole)
        # item_int = int(item_var.toPyObject())
        # return (item_int >= 60)


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

        self.transactions.pop(index.row())
        self.dataChanged.emit(index, index)
