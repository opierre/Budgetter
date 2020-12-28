from PySide2.QtCore import QAbstractListModel, Qt


class DistributionModel(QAbstractListModel):
    """
    Distribution model
    """

    def __init__(self, categories=None):
        super().__init__()

        """ Store categories """
        self.categories = categories or []

        """ Store sort direction - Default: UP """
        self.sortOrder = 1

    def data(self, index, role):
        """
        Override data() from QAbstractListModel
        :param index: index
        :param role: role
        :return: according to role (text, ...)
        """

        if index.isValid() and role == Qt.DisplayRole:
            category = self.categories[index.row()]

            """ Return current category list """
            return category

    def rowCount(self, index):
        """
        Override rowCount() from QAbstractListModel
        :param index: index
        :return: length of datas
        """

        return len(self.categories)
