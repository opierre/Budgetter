from PySide6.QtCore import QSize, Qt, QRect
from PySide6.QtGui import QPen, QColor, QPainter, QFont, QFontMetrics
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QItemDelegate


class DistributionDelegate(QItemDelegate):
    """
    Distribution Delegate
    """

    def __init__(self, *args, parent=None):
        QItemDelegate.__init__(self, parent, *args)

        # Store font for values
        self.font = QFont()

    def sizeHint(self, _option_qstyle_option_view_item, _index):
        """
        Override sizeHint

        :param _option_qstyle_option_view_item: optionQStyleOptionViewItem
        :param _index: index
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

        # Get values
        value = index.data(Qt.DisplayRole)
        category = str(value[0])
        nb_transactions = str(value[1])
        if int(nb_transactions) > 1:
            nb_transactions += " transactions"
        else:
            nb_transactions += " transaction"
        amount = value[2]
        amount = f"{amount:,.2f}".replace(",", " ") + " €"
        percentage = str(value[3]) + "%"

        # Draw bottom border
        painter.setPen(QPen(QColor("#344457")))
        painter.setBrush(Qt.NoBrush)
        painter.drawLine(option.rect.x() + option.rect.width() * 1 / 30, option.rect.y() + option.rect.height() - 1,
                         option.rect.width() - +option.rect.width() * 1 / 30,
                         option.rect.y() + option.rect.height() - 1)

        painter.setRenderHint(QPainter.Antialiasing)

        # Draw item background
        painter.setPen(QPen(QColor("#26374C")))
        painter.setBrush(QColor("transparent"))
        rect_background = QRect(option.rect.x() + option.rect.width() * 1 / 30,
                                option.rect.y() + option.rect.height() * 1 / 5,
                                option.rect.width() - option.rect.width() * 2 / 30,
                                option.rect.height() - option.rect.height() * 2 / 5)
        painter.drawRect(rect_background)

        # Draw percentage background
        painter.setPen(QPen(QColor("#21415D")))
        painter.setBrush(QColor("#21415D"))
        rect_percentage = QRect(
            rect_background.x() + rect_background.width() - (
                    rect_background.width() - (option.rect.width() * 1 / 3)) * (value[3] / 100),
            option.rect.y() + 10,
            (rect_background.width() - (option.rect.width() * 1 / 3)) * (value[3] / 100),
            option.rect.height() - 20)
        painter.drawRoundedRect(rect_percentage, 3.0, 3.0)

        # Draw left icon background
        painter.setPen(QPen(QColor("#1A537D")))
        painter.setBrush(QColor("#1A537D"))
        rect_icon = QRect(rect_background.x() + option.rect.width() * 1 / 60,
                          rect_background.y() - option.rect.height() * 1 / 30,
                          rect_background.height() + option.rect.height() * 2 / 30,
                          rect_background.height() + option.rect.height() * 2 / 30)
        painter.drawRoundedRect(rect_icon, 1.0, 1.0)

        # Draw icon and render svg
        painter.setPen(QPen(Qt.transparent))
        painter.setBrush(QColor("transparent"))
        rect_svg = QRect(rect_icon.x() + 10, rect_icon.y() + 10,
                         rect_icon.width() - 20, rect_icon.height() - 20)
        painter.drawRect(rect_svg)

        if category == "Restaurants":
            svg_render = QSvgRenderer(":/images/images/restaurant-white-18dp.svg")
        elif category == "Transport":
            svg_render = QSvgRenderer(":/images/images/directions_car-white-18dp.svg")
        elif category == "Groceries":
            svg_render = QSvgRenderer(":/images/images/local_grocery_store-white-18dp.svg")
        else:
            svg_render = QSvgRenderer(":/images/images/restaurant-white-18dp.svg")
        svg_render.setAspectRatioMode(Qt.KeepAspectRatio)
        svg_render.render(painter, rect_svg)

        # Set font on painter for category
        self.font.setFamily("Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set category painter color
        painter.setPen(QPen(Qt.white))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.horizontalAdvance(category)
        pixels_height = font_metrics.height()

        # Set category on top
        rect_category = QRect(rect_icon.x() + rect_icon.width() + option.rect.width() * 1 / 50,
                              rect_icon.y() + option.rect.height() * 1 / 30,
                              pixels_width, pixels_height)
        painter.drawText(rect_category, int(Qt.AlignLeft | Qt.AlignVCenter), category)

        # Set font on painter for number of transactions
        self.font.setFamily("Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        # Set number of transactions pen color
        painter.setPen(QPen(QColor("#75879B")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.horizontalAdvance(nb_transactions)
        pixels_height = font_metrics.height()

        # Set number of transactions beside category
        rect_transaction = QRect(rect_category.x(),
                                 rect_category.y() + rect_category.height() + option.rect.height() * 1 / 10,
                                 pixels_width, pixels_height)
        painter.drawText(rect_transaction, int(Qt.AlignLeft | Qt.AlignVCenter), nb_transactions)

        # Set font on painter for amount
        self.font.setFamily("Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set amount pen color
        painter.setPen(QPen(QColor("white")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.horizontalAdvance(amount)
        pixels_height = font_metrics.height()

        # Set amount on right corner
        rect_amount = QRect(rect_background.width() + rect_background.x() - pixels_width - option.rect.width() * 1 / 50,
                            rect_category.y() + option.rect.height() * 2 / 50,
                            pixels_width, pixels_height)
        painter.drawText(rect_amount, int(Qt.AlignRight | Qt.AlignVCenter), amount)

        # Set font on painter for percentage
        self.font.setFamily("Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        # Set percentage pen color
        painter.setPen(QPen(QColor("#75879B")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.horizontalAdvance(percentage)
        pixels_height = font_metrics.height()

        # Set percentage beside amount
        rect_perc = QRect(rect_background.width() + rect_background.x() - pixels_width - option.rect.width() * 1 / 50,
                          rect_transaction.y(), pixels_width, pixels_height)
        painter.drawText(rect_perc, int(Qt.AlignRight | Qt.AlignVCenter), percentage)

        painter.restore()
