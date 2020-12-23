from PySide2 import QtCore
from PySide2.QtCore import QSize, Qt, QRect
from PySide2.QtGui import QPen, QColor
from PySide2.QtWidgets import QItemDelegate

from widgets.distributionItem import DistributionItem


class DistributionDelegate(QItemDelegate):
    """
    Distribution Delegate
    """

    def __init__(self, parent=None, *args):
        QItemDelegate.__init__(self, parent, *args)

    def createEditor(self, parent, option, index):
        editor = DistributionItem()
        # editor.installEventFilter(self)
        return editor

    def setEditorData(self, item, index):
        value = index.model().data(index, QtCore.Qt.DisplayRole)
        item.setValue()

    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def sizeHint(self, optionQStyleOptionViewItem, index):
        return QSize(10, 120)

    def paint(self, painter, option, index):
        painter.save()

        #rect = option.rect()

        """ Draw item background """
        painter.setPen(QPen(Qt.NoPen))
        painter.setBrush(QColor("#26374C"))
        painter.drawRect(option.rect.x(), option.rect.y(),
                         option.rect.width(), option.rect.height()-20)

        """ Draw bottom border """
        painter.setPen(QPen("#344457"))
        painter.setBrush(QColor("blue"))
        painter.drawLine(option.rect.x(), option.rect.y()+option.rect.height()-10,
                         option.rect.width(), option.rect.y()+option.rect.height()-10)

        """ Draw left icon background """
        painter.setPen(QPen("#1A537D"))
        painter.setBrush(QColor("#1A537D"))
        rect = QRect(option.rect.x()+10, option.rect.y()+10,
                     28, 28)
        painter.drawRoundedRect(rect, 20.0, 20.0)

        # # set background color
        # painter.setPen(QPen(Qt.NoPen))
        # if option.state & QStyle.State_Selected:
        #     painter.setBrush(QBrush(Qt.red))
        # else:
        #     painter.setBrush(QBrush(Qt.white))
        # painter.drawRect(option.rect)
        #
        # set text color
        painter.setPen(QPen(Qt.black))
        value = index.data(Qt.DisplayRole)
        if True:
            text = str(value)
            painter.drawText(option.rect, Qt.AlignLeft, text)

        painter.restore()

