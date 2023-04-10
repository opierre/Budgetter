from typing import Union

from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex, QPersistentModelIndex


class DistributionModel(QAbstractListModel):
    """
    Distribution model
    """

    def __init__(self, categories=None):
        super().__init__()

        # Store categories
        self.categories = categories or []

    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int = -1):
        """
        Override data() from QAbstractListModel

        :param index: index
        :param role: role
        :return: according to role (text, ...)
        """

        if index.isValid() and role == Qt.ItemDataRole.DisplayRole:
            category = self.categories[index.row()]

            # Return current category list
            result = category
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

        return len(self.categories)
