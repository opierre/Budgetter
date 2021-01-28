from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QPalette, QIcon
from PySide2.QtWidgets import QStyledItemDelegate, QStyle, QComboBox, QStylePainter, QStyleOptionComboBox, QListView, \
    QStyleOptionViewItem


class CategoryComboBox(QStyledItemDelegate):
    """
    Category combobox with icons
    """

    def __init__(self, parent=None):
        super(CategoryComboBox, self).__init__(parent)

    def paint(self, painter, option, index):
        """
        Override paint()
        :param painter: painter
        :param option: option
        :param index: index
        :return: void
        """

        opt = option
        self.initStyleOption(opt, index)

        opt.decorationSize.setWidth(opt.rect.width())

        self.drawControl(QStyle.CE_ItemViewItem, opt, painter, self)


# class CategoryView(QListView):
#     """
#     Category combobox with icons
#     """
#
#     def __init__(self, parent=None):
#         super(CategoryView, self).__init__(parent)
#
#         self.setViewMode(QListView.IconMode)
#         self.setFlow(QListView.TopToBottom)
#         self.setWrapping(False)
#
#     def viewOptions(self):
#         """
#         Override viewOptions()
#         :return: QStyleOptionViewItem
#         """
#
#         ''' Set icon on the top and center of combo box item '''
#         option = QListView.viewOptions(self)
#         option.decorationAlignment = Qt.AlignHCenter | Qt.AlignVCenter
#         option.decorationPosition = QStyleOptionViewItem.Top
#         option.displayAlignment = Qt.AlignCenter
#         return option
