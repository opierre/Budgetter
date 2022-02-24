from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex


class DistributionModel(QAbstractListModel):
    """
    Distribution model
    """

    def __init__(self, categories=None):
        super().__init__()

        # Store categories
        self.categories = categories or []

    def data(self, index: QModelIndex, role: Qt.ItemDataRole = None):
        """
        Override data() from QAbstractListModel

        :param index: index
        :param role: role
        :return: according to role (text, ...)
        """

        if index.isValid() and role == Qt.DisplayRole:
            category = self.categories[index.row()]

            # Return current category list
            return category

    def rowCount(self, index: QModelIndex = QModelIndex()):
        """
        Override rowCount() from QAbstractListModel

        :param index: index
        :return: length of datas
        """

        return len(self.categories)
