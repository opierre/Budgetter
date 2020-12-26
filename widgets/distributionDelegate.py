from PySide2 import QtCore
from PySide2.QtCore import QSize, Qt, QRect
from PySide2.QtGui import QPen, QColor, QPainter, QFont, QFontMetrics
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QItemDelegate

from widgets.distributionItem import DistributionItem


class DistributionDelegate(QItemDelegate):
    """
    Distribution Delegate
    """

    def __init__(self, parent=None, *args):
        QItemDelegate.__init__(self, parent, *args)

        """ Store font for values """
        self.font = QFont()

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
        return QSize(10, 90)

    def paint(self, painter, option, index):
        painter.save()

        """ Draw bottom border """
        painter.setPen(QPen(QColor("#344457")))
        # painter.setPen(QPen("green"))
        painter.setBrush(Qt.NoBrush)
        painter.drawLine(option.rect.x()+20, option.rect.y()+option.rect.height()-5,
                         option.rect.width()-20, option.rect.y()+option.rect.height()-5)

        painter.setRenderHint(QPainter.Antialiasing)

        """ Draw item background """
        painter.setPen(QPen(QColor("#26374C")))
        # painter.setBrush(QColor("#26374C"))
        painter.setBrush(QColor("transparent"))
        painter.drawRect(option.rect.x()+20, option.rect.y()+10,
                         option.rect.width()-40, option.rect.height()-25)

        """ Draw left icon background """
        painter.setPen(QPen(QColor("#1A537D")))
        painter.setBrush(QColor("#1A537D"))
        rectIcon = QRect(option.rect.x()+20, option.rect.y()+20,
                         option.rect.x()+45, option.rect.height()-45)
        painter.drawRoundedRect(rectIcon, 1.0, 1.0)

        """ Draw icon and render svg """
        painter.setPen(QPen(Qt.transparent))
        painter.setBrush(QColor("transparent"))
        rectSvg = QRect(rectIcon.x()+10, rectIcon.y()+10,
                        rectIcon.width()-20, rectIcon.height()-20)
        painter.drawRect(rectSvg)

        svgRender = QSvgRenderer(":/images/images/restaurant-white-18dp.svg")
        svgRender.setAspectRatioMode(Qt.KeepAspectRatio)
        svgRender.render(painter, rectSvg)

        """ Set font on painter for category """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Get category value [0] """
        painter.setPen(QPen(Qt.white))
        value = index.data(Qt.DisplayRole)
        category = str(value[0])

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width(category)

        """ Set category on top """
        painter.drawText(rectIcon.width()+35, rectIcon.y(),
                         pixelsWidth, rectIcon.y(),
                         Qt.AlignLeft, category)

        """ Set font on painter for number of transactions """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(9)
        painter.setFont(self.font)

        """ Get number of transactions value [1] """
        painter.setPen(QPen(QColor("#75879B")))
        value = index.data(Qt.DisplayRole)
        nbTransactions = str(value[1])

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width(nbTransactions)

        """ Set number of transactions beside category """
        painter.drawText(rectIcon.width() + 35, rectIcon.y()+25,
                         pixelsWidth, rectIcon.y()+25,
                         Qt.AlignLeft, nbTransactions)

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

