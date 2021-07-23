from PySide2.QtCore import QSize, Qt, QRect, QRectF
from PySide2.QtGui import QPen, QColor, QPainter, QFont, QFontMetrics
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QItemDelegate

from utils.tools import convert_amount_to_str


class AccountDelegate(QItemDelegate):
    """
    Account Delegate
    """

    def __init__(self, parent=None, *args):
        QItemDelegate.__init__(self, parent, *args)

        """ Store font for values """
        self.font = QFont()

    def sizeHint(self, optionQStyleOptionViewItem, index):
        """
        Override sizeHint
        :param optionQStyleOptionViewItem: optionQStyleOptionViewItem
        :param index: index
        :return: QSize(10, 70)
        """

        return QSize(10, 70)

    def paint(self, painter, option, index):
        """
        Override paint
        :param painter: painter
        :param option: option
        :param index: index
        :return: None
        """

        painter.save()

        """ Get values """
        value = index.data(Qt.DisplayRole)
        bank = value[0]
        account_name = value[1]
        amount = convert_amount_to_str(value[2]) + " €"
        trend = value[3]
        color = QColor(value[4])

        """ Draw bottom border """
        painter.setPen(QPen(QColor("#344457")))
        painter.setBrush(Qt.NoBrush)
        painter.drawLine(option.rect.x()+option.rect.width()*1/30, option.rect.y()+option.rect.height()-1,
                         option.rect.width()-+option.rect.width()*1/30, option.rect.y()+option.rect.height()-1)

        painter.setRenderHint(QPainter.Antialiasing)

        """ Draw item background """
        painter.setPen(QPen(QColor("#26374C")))
        painter.setBrush(QColor("transparent"))
        rectBackground = QRect(option.rect.x()+option.rect.width()*1/30, option.rect.y()+option.rect.height()*1/5,
                               option.rect.width()-+option.rect.width()*2/30, option.rect.height()-option.rect.height()*2/5)
        painter.drawRect(rectBackground)

        """ Draw left icon background """
        painter.setPen(QPen(color))
        painter.setBrush(color)
        painter.setOpacity(0.8)
        rectIcon = QRect(rectBackground.x()+option.rect.width()*1/60, rectBackground.y()-option.rect.height()*1/30,
                         rectBackground.height()+option.rect.height()*1/5, rectBackground.height()+option.rect.height()*1/30)
        painter.drawRoundedRect(rectIcon, 1.0, 1.0)

        """ Draw icon and render svg """
        painter.setOpacity(1)
        painter.setPen(QPen(Qt.transparent))
        painter.setBrush(QColor("transparent"))
        rectSvg = QRect(rectIcon.x(), rectIcon.y()+5,
                        rectIcon.width(), rectIcon.height()-10)
        painter.drawRect(rectSvg)

        if bank.lower() == "Caisse d'Epargne".lower():
            svgRender = QSvgRenderer(":/images/images/Caisse_depargne_Logo_bank.svg")
        elif bank.lower() == "Crédit Agricole".lower():
            svgRender = QSvgRenderer(":/images/images/Crédit_Agricole _bank.svg")
        svgRender.setAspectRatioMode(Qt.KeepAspectRatio)
        svgRender.render(painter, rectSvg)

        """ Set font on painter for account name """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        """ Set category painter color """
        painter.setPen(QPen(Qt.white))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width(account_name)
        pixelsHeight = fontMetrics.height()

        """ Set category on top """
        rectCategory = QRect(rectIcon.x()+rectIcon.width()+option.rect.width()*1/30, rectIcon.y()+option.rect.height()*1/30,
                             pixelsWidth, pixelsHeight)
        painter.drawText(rectCategory, Qt.AlignLeft | Qt.AlignVCenter, account_name)

        """ Set font on painter for account label """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set number of transactions pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width('Account')
        pixelsHeight = fontMetrics.height()

        """ Set number of transactions beside category """
        rectTransaction = QRect(rectCategory.x(), rectCategory.y()+rectCategory.height()+option.rect.height()*1/10,
                                pixelsWidth, pixelsHeight)
        painter.drawText(rectTransaction, Qt.AlignLeft | Qt.AlignVCenter, 'Account')

        """ Set font on painter for amount """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        """ Set amount pen color """
        painter.setPen(QPen(QColor("white")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width(amount)
        pixelsHeight = fontMetrics.height()

        """ Set amount on right corner """
        rect_amount = QRect(rectBackground.width()+rectBackground.x()-pixelsWidth-option.rect.width()*1/50,
                            rectCategory.y(), pixelsWidth, pixelsHeight)
        painter.drawText(rect_amount, Qt.AlignRight | Qt.AlignVCenter, amount)

        """ Set rect for trend drawing """
        rect_svg = QRectF(rect_amount.x() - 24, rect_amount.y(), 18, 18)

        """ Draw trend """
        if trend == "UP":
            svg_renderer = QSvgRenderer(":/images/images/north_white_18dp.svg")
        elif trend == "DOWN":
            svg_renderer = QSvgRenderer(":/images/images/south_white_18dp.svg")
        else:
            svg_renderer = QSvgRenderer(":/images/images/south_white_18dp.svg")
        svg_renderer.render(painter, rect_svg)

        """ Set font on painter for balance label """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set percentage pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width('Balance')
        pixelsHeight = fontMetrics.height()

        """ Set percentage beside amount """
        rectPerc = QRect(rectBackground.width()+rectBackground.x()-pixelsWidth-option.rect.width()*1/50, rectTransaction.y(),
                         pixelsWidth, pixelsHeight)
        painter.drawText(rectPerc, Qt.AlignRight | Qt.AlignVCenter, 'Balance')

        painter.restore()
