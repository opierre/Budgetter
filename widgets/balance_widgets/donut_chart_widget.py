import math
from math import cos, pi, sin, sqrt

from PySide2.QtCore import Qt, QSize, QRect, QPointF, QRectF, QCoreApplication
from PySide2.QtGui import QPainter, QPen, QColor, QFont, QFontMetrics, QPaintEvent, QBrush
from PySide2.QtSvg import QSvgRenderer
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
        self.trend = "UP"

        """ Set fixed size """
        self.setFixedSize(210, 210)

        """ Set margins """
        self.setContentsMargins(0, 0, 0, 0)

    def add_slice(self, percentage: int):
        """
        Add slice with percentage value

        :param percentage: (int) percentage value
        :return: None
        """

        self._slices.append(percentage)

    def paintEvent(self, event: QPaintEvent):
        """
        Override paintEvent()

        :param event: (QPaintEvent) event
        :return: None
        """

        painter = QPainter()

        painter.begin(self)

        """ Improve rendering """
        painter.setRenderHint(QPainter.Antialiasing)

        """ Draw slices background """
        self.draw_background(painter)

        """ Configure pen """
        pen = QPen()
        pen.setWidthF(22.5)
        pen.setCapStyle(Qt.RoundCap)
        painter.setOpacity(1)

        """ Draw slices """
        self.draw_slices(pen, painter)

        """ Draw middle text """
        self.draw_total_amount(pen, painter)

    def draw_background(self, painter: QPainter):
        """
        Draw background as shadow effect

        :param painter: painter
        :return: None
        """

        """ Configure pen """
        pen = QPen()
        pen.setWidthF(1.0)
        pen.setCapStyle(Qt.RoundCap)
        pen.setColor(QColor("#1C293B"))
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor("#1C293B")))
        painter.setOpacity(1)

        """ Configure rectangle """
        rect_origins = QRectF(self.rect().center().x(), self.rect().center().y(),
                              self.rect().width() / 1.5, self.rect().height() / 1.5)
        rect_origins.moveCenter(self.rect().center())

        """ Draw arc """
        painter.drawEllipse(rect_origins)

    def draw_slices(self, pen: QPen, painter: QPainter):
        """
        Draw each slice

        :param pen: (QPen) pen
        :param painter: (QPainter) painter
        :return: None
        """

        first_start_angle = 0
        first_span_angle = 0
        previous_end_angle = 0
        current_index = 0
        last_index = len(self._slices)

        """ Configure rectangle """
        rect_origins = QRectF(self.rect().center().x(), self.rect().center().y(),
                              self.rect().width() / 1.2, self.rect().height() / 1.2)
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

        :param pen: (QPen) pen
        :param painter: (QPainter) painter
        :return: None
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
        text = QCoreApplication.translate("donut_chart", "Current balance")
        fontMetrics = QFontMetrics(font)
        pixelsWidth = fontMetrics.width(text)
        pixelsHeight = fontMetrics.height()

        """ Set text """
        rect_description = QRect(self.rect().x(), self.rect().y(), pixelsWidth, pixelsHeight)
        rect_description.moveCenter(self.rect().center())
        rect_description.moveTop(rect_description.y() + rect_description.height() / 2 + 7)
        painter.drawText(rect_description, Qt.AlignHCenter | Qt.AlignVCenter, text)

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
        rect_value.moveBottom(rect_value.y() + rect_value.height() / 2)
        painter.drawText(rect_value, Qt.AlignHCenter | Qt.AlignVCenter, value)

        """ Set trend """
        rect_trend = QRect(self.rect().x(), self.rect().y(), 24, 24)
        rect_trend.moveCenter(self.rect().center())
        rect_trend.moveTop(rect_description.y() + rect_description.height() + 6)

        if self.trend == "UP":
            svgRender = QSvgRenderer(":/images/images/trending_up_white_24dp.svg")
        elif self.trend == "DOWN":
            svgRender = QSvgRenderer(":/images/images/trending_down_white_24dp.svg")
        else:
            svgRender = QSvgRenderer(":/images/images/trending_flat_white_24dp.svg")
        svgRender.setAspectRatioMode(Qt.KeepAspectRatio)
        svgRender.render(painter, rect_trend)

        painter.end()

    def set_total_amount(self, total_amount: float):
        """
        Update total amount

        :param total_amount: (float) total amount
        :return: None
        """

        self.total_amount = total_amount

    def set_trend(self, trend: str):
        """
        Update trend

        :param trend: (str) "FLAT"/"UP"/"DOWN"
        :return: None
        """

        self.trend = trend
