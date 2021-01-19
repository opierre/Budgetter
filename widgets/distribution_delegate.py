from PySide2.QtCore import QSize, Qt, QRect
from PySide2.QtGui import QPen, QColor, QPainter, QFont, QFontMetrics
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QItemDelegate


class DistributionDelegate(QItemDelegate):
    """
    Distribution Delegate
    """

    def __init__(self, parent=None, *args):
        QItemDelegate.__init__(self, parent, *args)

        """ Store font for values """
        self.font = QFont()

    def sizeHint(self, optionQStyleOptionViewItem, index):
        return QSize(10, 70)

    def paint(self, painter, option, index):
        painter.save()

        """ Get values """
        value = index.data(Qt.DisplayRole)
        category = str(value[0])
        nbTransactions = str(value[1])
        if int(nbTransactions) > 1:
            nbTransactions += " transactions"
        else:
            nbTransactions += " transaction"
        amount = value[2]
        amount = "{:,.2f}".format(amount).replace(",", " ") + " €"
        percentage = str(value[3]) + "%"

        """ Draw bottom border """
        painter.setPen(QPen(QColor("#344457")))
        painter.setBrush(Qt.NoBrush)
        painter.drawLine(option.rect.x()+20, option.rect.y()+option.rect.height()-1,
                         option.rect.width()-20, option.rect.y()+option.rect.height()-1)

        painter.setRenderHint(QPainter.Antialiasing)

        """ Draw item background """
        painter.setPen(QPen(QColor("#26374C")))
        painter.setBrush(QColor("transparent"))
        rectBackground = QRect(option.rect.x()+20, option.rect.y()+12,
                               option.rect.width()-40, option.rect.height()-25)
        painter.drawRect(rectBackground)

        """ Draw left icon background """
        painter.setPen(QPen(QColor("#1A537D")))
        painter.setBrush(QColor("#1A537D"))
        rectIcon = QRect(option.rect.x()+20, option.rect.y()+12,
                         option.rect.x()+45, option.rect.height()-25)
        painter.drawRoundedRect(rectIcon, 1.0, 1.0)

        """ Draw icon and render svg """
        painter.setPen(QPen(Qt.transparent))
        painter.setBrush(QColor("transparent"))
        rectSvg = QRect(rectIcon.x()+10, rectIcon.y()+10,
                        rectIcon.width()-20, rectIcon.height()-20)
        painter.drawRect(rectSvg)

        if category == "Restaurants":
            svgRender = QSvgRenderer(":/images/images/restaurant-white-18dp.svg")
        elif category == "Transport":
            svgRender = QSvgRenderer(":/images/images/directions_car-white-18dp.svg")
        elif category == "Groceries":
            svgRender = QSvgRenderer(":/images/images/local_grocery_store-white-18dp.svg")
        svgRender.setAspectRatioMode(Qt.KeepAspectRatio)
        svgRender.render(painter, rectSvg)

        """ Set font on painter for category """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        """ Set category painter color """
        painter.setPen(QPen(Qt.white))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width(category)
        pixelsHeight = fontMetrics.height()

        """ Set category on top """
        painter.drawText(rectIcon.width()+35, rectIcon.y(),
                         pixelsWidth, pixelsHeight,
                         Qt.AlignLeft | Qt.AlignVCenter, category)

        """ Set font on painter for number of transactions """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set number of transactions pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width(nbTransactions)
        pixelsHeight = fontMetrics.height()

        """ Set number of transactions beside category """
        painter.drawText(rectIcon.width() + 35, rectIcon.y()+25,
                         pixelsWidth, pixelsHeight,
                         Qt.AlignLeft | Qt.AlignVCenter, nbTransactions)

        """ Draw percentage background """
        painter.setPen(QPen(QColor("#21405D")))
        painter.setBrush(QColor("#21405D"))
        rectPercentage = QRect(rectBackground.x()+rectBackground.width(), option.rect.y()+10,
                               -(rectBackground.width()-(rectIcon.x()+rectIcon.width()+35+112+20))*(value[3]/100),
                               option.rect.height()-20)
        painter.drawRoundedRect(rectPercentage, 1.0, 1.0)

        """ Set font on painter for amount """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        """ Set amount pen color """
        painter.setPen(QPen(QColor("white")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsHeight = fontMetrics.height()

        """ Set amount on right corner """
        rectAmount = QRect(rectBackground.width()+rectBackground.x()-106, rectIcon.y()+2,
                           96, pixelsHeight)
        painter.drawText(rectAmount, Qt.AlignRight | Qt.AlignVCenter, amount)

        """ Set font on painter for percentage """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set percentage pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsHeight = fontMetrics.height()

        """ Set percentage beside amount """
        rectPerc = QRect(rectBackground.width()+rectBackground.x()-56, rectIcon.y()+25,
                         46, pixelsHeight)
        painter.drawText(rectPerc, Qt.AlignRight | Qt.AlignVCenter, percentage)

        painter.restore()
