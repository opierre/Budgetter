import math
from math import cos, pi, sin, sqrt

from PySide2.QtCore import Qt, QSize, QRect, QPointF, QRectF
from PySide2.QtGui import QPainter, QPen, QColor, QFont, QFontMetrics
from PySide2.QtWidgets import QWidget

from utils.tools import convert_amount_to_str


class DonutChart(QWidget):
    """
    Donut chart
    """
    
    def __init__(self, parent=None):
        super(DonutChart, self).__init__(parent)

        """ Store slices """
        self._slices = []

        """ Store colors """
        self.colors = [QColor("#1CA9E9"), QColor("#0154C8"), QColor("#26C1C9"), QColor("#6658CB")]

        """ Store total amount """
        self.total_amount = 0

        """ Store trend """
        self.trend = "FLAT"

        """ Set fixed size """
        self.setFixedSize(210, 210)

        """ Set margins """
        self.setContentsMargins(0, 0, 0, 0)

    def add_slice(self, percentage):
        """
        Add slice with percentage value
        :param percentage: percentage value
        :return: void
        """

        self._slices.append(percentage)

    def paintEvent(self, event):
        """
        Override paintEvent()
        :param event: event
        :return: void
        """

        painter = QPainter()

        painter.begin(self)

        """ Improve rendering """
        painter.setRenderHint(QPainter.Antialiasing)

        """ Configure pen """
        pen = QPen()
        pen.setWidthF(22.5)
        pen.setCapStyle(Qt.RoundCap)

        """ Draw slices """
        self.draw_slices(pen, painter)

        """ Draw middle text """
        self.draw_total_amount(pen, painter)

    def draw_slices(self, pen, painter):
        """
        Draw each slice
        :param pen: pen
        :param painter: painter
        :return: void
        """

        first_start_angle = 0
        first_span_angle = 0
        previous_end_angle = 0
        current_index = 0
        last_index = len(self._slices)

        """ Configure rectangle """
        rect_origins = QRect(self.rect().x() + 10, self.rect().y() + 10,
                             self.rect().width() - 30, self.rect().height() - 30)
        rect_origins.moveCenter(self.rect().center())

        for current_slice in self._slices:
            """ Set span angles """
            span_angle = current_slice * 360 / 100

            """ Set start angle """
            if previous_end_angle == 0:
                start_angle = (180 - span_angle) / 2
                previous_end_angle = start_angle + span_angle

                """ Store first value for re-draw """
                first_start_angle = start_angle
                first_span_angle = span_angle
            else:
                start_angle = previous_end_angle
                previous_end_angle = start_angle + span_angle

            """ Set pen color """
            pen.setColor(self.colors[current_index])
            painter.setPen(pen)

            """ Update current index """
            current_index += 1

            """ Draw arc """
            painter.drawArc(rect_origins, start_angle * 16, span_angle * 16)

            """ Configure font for slice percentage """
            font = QFont()
            font.setFamily(u"Roboto")
            font.setPointSize(8)
            painter.setFont(font)

            """ Set pen color """
            pen.setColor(QColor("white"))
            painter.setPen(pen)

            """ Compute middle arc coordinates """
            x_label = self.rect().center().x() + (rect_origins.width() / 2.0) * math.cos(
                (start_angle + span_angle / 2) * math.pi / 180) - 7
            y_label = self.rect().center().y() - (rect_origins.width() / 2.0) * math.sin(
                (start_angle + span_angle / 2) * math.pi / 180) - 6

            """ Get text width """
            label_perc = str(current_slice) + "%"
            font_metrics = QFontMetrics(font)
            pixels_width = font_metrics.width(label_perc)
            pixels_height = font_metrics.height()
            rect_label = QRectF(x_label, y_label, pixels_width, pixels_height)

            painter.drawText(rect_label, Qt.AlignLeft | Qt.AlignVCenter, label_perc)

            """ Re-draw first one in case of last to hide overlapping """
            if current_index == last_index:
                """ Set pen color """
                pen.setColor(self.colors[0])
                painter.setPen(pen)

                """ Draw arc """
                painter.drawArc(rect_origins, first_start_angle * 16, first_span_angle * 16 * 1 / 10)

    def draw_total_amount(self, pen, painter):
        """
        Draw total amouint in middle of rectangle
        :param pen: pen
        :param painter: painter
        :return: void
        """

        """ Configure font for description """
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        painter.setFont(font)

        """ Set pen color """
        pen.setColor(QColor("#C4C9CF"))
        painter.setPen(pen)

        """ Get font metrics """
        text = "Current balance"
        fontMetrics = QFontMetrics(font)
        pixelsWidth = fontMetrics.width(text)
        pixelsHeight = fontMetrics.height()

        """ Set text """
        rect_description = QRect(self.rect().x(), self.rect().y(), pixelsWidth, pixelsHeight)
        rect_description.moveCenter(self.rect().center())
        rect_description.moveBottom(rect_description.y() + rect_description.height() / 2)
        painter.drawText(rect_description, Qt.AlignHCenter | Qt.AlignVCenter, text)
        # painter.drawRect(rect_description)

        """ Configure font for total amount """
        font.setFamily(u"Roboto Medium")
        font.setPointSize(14)
        painter.setFont(font)

        """ Set pen color """
        pen.setColor(QColor("white"))
        painter.setPen(pen)

        """ Get font metrics """
        total_amount_str = convert_amount_to_str(self.total_amount)
        value = total_amount_str + " €"
        fontMetrics = QFontMetrics(font)
        pixelsWidth = fontMetrics.width(value)
        pixelsHeight = fontMetrics.height()

        """ Set value """
        rect_value = QRect(self.rect().x(), self.rect().y(), pixelsWidth, pixelsHeight)
        rect_value.moveCenter(self.rect().center())
        rect_value.moveTop(rect_value.y() - rect_value.height() / 2)
        painter.drawText(rect_value, Qt.AlignHCenter | Qt.AlignVCenter, value)
        #painter.drawRect(rect_value)

        painter.end()

    def set_total_amount(self, total_amount):
        """
        Update total amount
        :param total_amount: total amount
        :return: void
        """

        self.total_amount = total_amount

    def set_trend(self, trend):
        """
        Update trend
        :param trend: "FLAT"/"UP"/"DOWN"
        :return: void
        """

        self.trend = trend
