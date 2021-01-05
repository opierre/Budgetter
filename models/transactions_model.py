from PySide2.QtCore import QAbstractListModel, Qt


class TransactionsModel(QAbstractListModel):
    """
    Transactions model
    """

    def __init__(self, transactions=None):
        super().__init__()

        """ Store transactions """
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
