from PySide2.QtCore import QSize, Qt, QRect, QRectF, QModelIndex, QCoreApplication
from PySide2.QtGui import QPen, QColor, QPainter, QFont, QFontMetrics
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QItemDelegate, QStyleOptionViewItem

from budgetter.utils.tools import convert_amount_to_str


class AccountDelegate(QItemDelegate):
    """
    Account Delegate
    """

    def __init__(self, *args, parent=None):
        QItemDelegate.__init__(self, parent, *args)

        # Store font for values
        self.font = QFont()

    def sizeHint(self, optionQStyleOptionViewItem: QStyleOptionViewItem, index: QModelIndex):
        """
        Override sizeHint

        :param optionQStyleOptionViewItem: (QStyleOptionViewItem) optionQStyleOptionViewItem
        :param index: (QModelIndex) index
        :return: QSize(10, 70)
        """

        return QSize(10, 70)

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        """
        Override paint

        :param painter: (QPainter) painter
        :param option: (QStyleOptionViewItem) option
        :param index: (QModelIndex) index
        :return: None
        """

        painter.save()

        # Get values
        value = index.data(Qt.DisplayRole)
        bank = value[0]
        account_name = value[1]
        amount = convert_amount_to_str(value[2]) + " €"
        trend = value[3]
        color = QColor(value[4])

        # Draw bottom border
        painter.setPen(QPen(QColor("#344457")))
        painter.setBrush(Qt.NoBrush)
        painter.drawLine(option.rect.x()+option.rect.width()*1/30, option.rect.y()+option.rect.height()-1,
                         option.rect.width()-+option.rect.width()*1/30, option.rect.y()+option.rect.height()-1)

        painter.setRenderHint(QPainter.Antialiasing)

        # Draw item background
        painter.setPen(QPen(QColor("#26374C")))
        painter.setBrush(QColor("transparent"))
        rect_background = QRect(option.rect.x()+option.rect.width()*1/30, option.rect.y()+option.rect.height()*1/5,
                                option.rect.width()-+option.rect.width()*2/30,
                                option.rect.height()-option.rect.height()*2/5)
        painter.drawRect(rect_background)

        # Draw left icon background
        painter.setPen(QPen(color))
        painter.setBrush(color)
        painter.setOpacity(0.8)
        rect_icon = QRect(rect_background.x()+option.rect.width()*1/60, rect_background.y()-option.rect.height()*1/30,
                          rect_background.height()+option.rect.height()*1/5,
                          rect_background.height()+option.rect.height()*1/30)
        painter.drawRoundedRect(rect_icon, 1.0, 1.0)

        # Draw icon and render svg
        painter.setOpacity(1)
        painter.setPen(QPen(Qt.transparent))
        painter.setBrush(QColor("transparent"))
        rect_svg = QRect(rect_icon.x(), rect_icon.y()+5, rect_icon.width(), rect_icon.height()-10)
        painter.drawRect(rect_svg)

        if bank.lower() == "Caisse d'Epargne".lower():
            svg_render = QSvgRenderer(":/images/images/Caisse_depargne_Logo_bank.svg")
        elif bank.lower() == "Crédit Agricole".lower():
            svg_render = QSvgRenderer(":/images/images/Crédit_Agricole _bank.svg")
        else:
            svg_render = QSvgRenderer(":/images/images/Caisse_depargne_Logo_bank.svg")
        svg_render.setAspectRatioMode(Qt.KeepAspectRatio)
        svg_render.render(painter, rect_svg)

        # Set font on painter for account name
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set category painter color
        painter.setPen(QPen(Qt.white))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.width(account_name)
        pixels_height = font_metrics.height()

        # Set category on top
        rect_category = QRect(rect_icon.x()+rect_icon.width()+option.rect.width()*1/30,
                              rect_icon.y()+option.rect.height()*1/30, pixels_width, pixels_height)
        painter.drawText(rect_category, int(Qt.AlignLeft | Qt.AlignVCenter), account_name)

        # Set font on painter for account label
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        # Set number of transactions pen color
        painter.setPen(QPen(QColor("#75879B")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.width('Account')
        pixels_height = font_metrics.height()

        # Set number of transactions beside category
        rect_transaction = QRect(rect_category.x(), rect_category.y()+rect_category.height()+option.rect.height()*1/10,
                                 pixels_width, pixels_height)
        painter.drawText(rect_transaction, int(Qt.AlignLeft | Qt.AlignVCenter),
                         QCoreApplication.translate("account_delegate", 'Account'))

        # Set font on painter for amount
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set amount pen color
        painter.setPen(QPen(QColor("white")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.width(amount)
        pixels_height = font_metrics.height()

        # Set amount on right corner
        rect_amount = QRect(rect_background.width()+rect_background.x()-pixels_width-option.rect.width()*1/50,
                            rect_category.y(), pixels_width, pixels_height)
        painter.drawText(rect_amount, int(Qt.AlignRight | Qt.AlignVCenter), amount)

        # Set rect for trend drawing
        rect_svg = QRectF(rect_amount.x() - 24, rect_amount.y(), 18, 18)

        # Draw trend
        if trend == "UP":
            svg_renderer = QSvgRenderer(":/images/images/north_white_18dp.svg")
        elif trend == "DOWN":
            svg_renderer = QSvgRenderer(":/images/images/south_white_18dp.svg")
        else:
            svg_renderer = QSvgRenderer(":/images/images/south_white_18dp.svg")
        svg_renderer.render(painter, rect_svg)

        # Set font on painter for balance label
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        # Set percentage pen color
        painter.setPen(QPen(QColor("#75879B")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.width('Balance')
        pixels_height = font_metrics.height()

        # Set percentage beside amount
        rect_perc = QRect(rect_background.width()+rect_background.x()-pixels_width-option.rect.width()*1/50,
                          rect_transaction.y(), pixels_width, pixels_height)
        painter.drawText(rect_perc, int(Qt.AlignRight | Qt.AlignVCenter),
                         QCoreApplication.translate("account_delegate", 'Balance'))

        painter.restore()