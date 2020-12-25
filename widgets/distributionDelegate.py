from PySide2 import QtCore
from PySide2.QtCore import QSize, Qt, QRect
from PySide2.QtGui import QPen, QColor, QPainter
from PySide2.QtSvg import QSvgRenderer
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
        return QSize(10, 100)

    def paint(self, painter, option, index):
        painter.save()

        """ Draw bottom border """
        painter.setPen(QPen("#344457"))
        # painter.setPen(QPen("green"))
        painter.setBrush(Qt.NoBrush)
        painter.drawLine(option.rect.x()+20, option.rect.y()+option.rect.height()-5,
                         option.rect.width()-20, option.rect.y()+option.rect.height()-5)

        painter.setRenderHint(QPainter.Antialiasing)

        """ Draw item background """
        painter.setPen(QPen("#26374C"))
        # painter.setBrush(QColor("#26374C"))
        painter.setBrush(QColor("red"))
        painter.drawRect(option.rect.x()+20, option.rect.y()+10,
                         option.rect.width()-40, option.rect.height()-25)

        """ Draw left icon background """
        painter.setPen(QPen("#1A537D"))
        painter.setBrush(QColor("#1A537D"))
        rect = QRect(option.rect.x()+20, option.rect.y()+20,
                     option.rect.x()+65, option.rect.height()-45)
        painter.drawRoundedRect(rect, 1.0, 1.0)

        """ Draw icon and render svg """
        painter.setPen(QPen("transparent"))
        painter.setBrush(QColor("transparent"))
        rect = QRect(option.rect.x()+30, option.rect.y()+30,
                     option.rect.x()+45, option.rect.height()-65)
        painter.drawRect(rect)

        svgRender = QSvgRenderer(":/images/images/restaurant-white-18dp.svg")
        svgRender.setAspectRatioMode(Qt.KeepAspectRatio)
        svgRender.render(painter, rect)

        # # set background color
        # painter.setPen(QPen(Qt.NoPen))
        # if option.state & QStyle.State_Selected:
        #     painter.setBrush(QBrush(Qt.red))
        # else:
        #     painter.setBrush(QBrush(Qt.white))
        # painter.drawRect(option.rect)
        #
        # set text color
        # painter.setPen(QPen(Qt.black))
        # value = index.data(Qt.DisplayRole)
        # if True:
        #     text = str(value)
        #     painter.drawText(option.rect, Qt.AlignLeft, text)

        painter.restore()

