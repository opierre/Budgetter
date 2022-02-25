from PySide2.QtCore import Qt, QRect, QRectF
from PySide2.QtGui import QPainter, QPen, QColor, QFont, QFontMetrics, QPaintEvent, QBrush, QConicalGradient, \
    QMouseEvent
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QWidget

from budgetter.utils.tools import convert_amount_to_str


class DonutChart(QWidget):
    """
    Donut chart
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store slices
        self._slices = []

        # Store colors
        self.colors = [QColor("#1CA9E9"), QColor("#0154C8"), QColor("#26C1C9"), QColor("#6658CB")]

        # Store total amount
        self.total_amount = 0
        self.previous_month_total_amount = 0

        # Store trend
        self.trend = "UP"

        # Store percentage
        self.percentage = 0

        # Set fixed size
        self.setFixedSize(210, 210)

        # Set margins
        self.setContentsMargins(0, 0, 0, 0)

    def add_slice(self, percentage: int):
        """
        Add slice with percentage value

        :param percentage: (int) percentage value
        :return: None
        """

        self._slices.append(percentage)

    def mousePressEvent(self, eventQMouseEvent: QMouseEvent):
        """
        Override mousePressEvent()

        :param eventQMouseEvent: QMouseEvent
        :return: None
        """

        pass

    def paintEvent(self, event: QPaintEvent):
        """
        Override paintEvent()

        :param event: (QPaintEvent) event
        :return: None
        """

        painter = QPainter()

        painter.begin(self)

        # Improve rendering
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw slices background
        self.draw_background(painter)

        # Configure pen
        pen = QPen()
        pen.setWidthF(22.5)
        pen.setCapStyle(Qt.RoundCap)
        painter.setOpacity(1)

        # Draw slices
        self.draw_slices(pen, painter)

        # Draw middle text
        self.draw_total_amount(pen, painter)

    def draw_background(self, painter: QPainter):
        """
        Draw background as shadow effect

        :param painter: painter
        :return: None
        """

        # Configure pen
        pen = QPen()
        pen.setWidthF(1.0)
        pen.setCapStyle(Qt.RoundCap)
        pen.setColor(QColor("#1C293B"))
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor("#1C293B")))
        painter.setOpacity(1)

        # Configure rectangle
        rect_origins = QRectF(self.rect().center().x(), self.rect().center().y(),
                              self.rect().width() / 1.5, self.rect().height() / 1.5)
        rect_origins.moveCenter(self.rect().center())

        # Draw arc
        painter.drawEllipse(rect_origins)

    def draw_slices(self, pen: QPen, painter: QPainter):
        """
        Draw each slice

        :param pen: (QPen) pen
        :param painter: (QPainter) painter
        :return: None
        """

        previous_end_angle = 0
        current_index = 0

        # Configure rectangle
        rect_origins = QRectF(self.rect().center().x(), self.rect().center().y(),
                              self.rect().width() / 1.2, self.rect().height() / 1.2)
        rect_origins.moveCenter(self.rect().center())

        for current_slice in self._slices:
            # Set span angles
            span_angle = current_slice * 360 / 100

            # Set start angle
            if previous_end_angle == 0:
                start_angle = (180 - span_angle) / 2
                previous_end_angle = start_angle + span_angle
            else:
                start_angle = previous_end_angle
                previous_end_angle = start_angle + span_angle

            # Set gradient on arcs
            gradient = QConicalGradient()
            gradient.setCenter(rect_origins.center())
            gradient.setAngle(start_angle)
            gradient.setColorAt(current_slice / 100, QColor("transparent"))
            gradient.setColorAt(0, QColor(self.colors[current_index]))
            pen.setBrush(QBrush(gradient))
            painter.setPen(pen)

            # Draw arc
            painter.drawArc(rect_origins, start_angle * 16, span_angle * 16)
            painter.setOpacity(1.0)

            # Re-draw first one in case of last to hide overlapping
            # Set pen color
            pen.setColor(self.colors[current_index])
            painter.setPen(pen)

            # Draw arc
            painter.drawArc(rect_origins, start_angle * 16, span_angle * 16 * 1 / 100)

            # Update current index
            current_index += 1

    def draw_total_amount(self, pen, painter):
        """
        Draw total amouint in middle of rectangle

        :param pen: (QPen) pen
        :param painter: (QPainter) painter
        :return: None
        """

        # Configure font for description
        font = QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        painter.setFont(font)

        # Set pen color
        pen.setColor(QColor(196, 201, 207, 180))
        painter.setPen(pen)

        # Get font metrics
        previous_month_total_amount_str = convert_amount_to_str(self.previous_month_total_amount)
        previous_value = previous_month_total_amount_str + " €"
        font_metrics = QFontMetrics(font)
        pixels_width = font_metrics.width(previous_value)
        pixels_height = font_metrics.height()

        # Set text
        rect_description = QRect(self.rect().x(), self.rect().y(), pixels_width, pixels_height)
        rect_description.moveCenter(self.rect().center())
        rect_description.moveTop(rect_description.y() + rect_description.height() / 2 + 7)
        painter.drawText(rect_description, int(Qt.AlignHCenter | Qt.AlignVCenter), previous_value)

        # Set pen color
        value = str(self.percentage) + "%"
        if self.trend == "UP":
            value = "+" + value
            pen.setColor(QColor(109, 210, 48, 180))
        elif self.trend == "DOWN":
            value = "-" + value
            pen.setColor(QColor(226, 74, 141, 180))
        else:
            value = "~" + value
            pen.setColor(QColor(255, 255, 255, 180))
        painter.setPen(pen)

        # Get font metrics
        font_metrics = QFontMetrics(font)
        pixels_width = font_metrics.width(value)
        pixels_height = font_metrics.height()

        # Set text
        rect_percentage = QRect(self.rect().x(), self.rect().y(), pixels_width, pixels_height)
        rect_percentage.moveCenter(self.rect().center())
        rect_percentage.moveTop(rect_percentage.y() + rect_percentage.height() / 2 + 35)
        painter.drawText(rect_percentage, int(Qt.AlignHCenter | Qt.AlignVCenter), value)

        # Configure font for total amount
        font.setFamily("Roboto Medium")
        font.setPointSize(14)
        painter.setFont(font)

        # Set pen color
        pen.setColor(QColor("white"))
        painter.setPen(pen)

        # Get font metrics
        total_amount_str = convert_amount_to_str(self.total_amount)
        value = total_amount_str + " €"
        font_metrics = QFontMetrics(font)
        pixels_width = font_metrics.width(value)
        pixels_height = font_metrics.height()

        # Set value
        rect_value = QRect(self.rect().x(), self.rect().y(), pixels_width, pixels_height)
        rect_value.moveCenter(self.rect().center())
        rect_value.moveBottom(rect_value.y() + rect_value.height() / 2.0)
        painter.drawText(rect_value, int(Qt.AlignHCenter | Qt.AlignVCenter), value)

        # Set trend
        rect_trend = QRect(self.rect().x(), self.rect().y(), 24, 24)
        rect_trend.moveCenter(self.rect().center())
        rect_trend.moveTop(rect_description.y() - rect_description.height() - 50)

        if self.trend == "UP":
            svg_render = QSvgRenderer(":/images/images/trending_up_white_24dp.svg")
        elif self.trend == "DOWN":
            svg_render = QSvgRenderer(":/images/images/trending_down_white_24dp.svg")
        else:
            svg_render = QSvgRenderer(":/images/images/trending_flat_white_24dp.svg")
        svg_render.setAspectRatioMode(Qt.KeepAspectRatio)
        svg_render.render(painter, rect_trend)

        painter.end()

    def set_total_amounts(self, total_amount: float, previous_month_total_amount: float):
        """
        Update total amount

        :param total_amount: (float) total amount
        :param previous_month_total_amount: (float) previous month total amount
        :return: None
        """

        # Update values
        self.total_amount = total_amount
        self.previous_month_total_amount = previous_month_total_amount

        # Set trend
        if self.previous_month_total_amount > self.total_amount:
            self.trend = "DOWN"
        elif self.previous_month_total_amount == self.total_amount:
            self.trend = "FLAT"
        else:
            self.trend = "UP"

        # Compute diff
        self.percentage = round(abs(previous_month_total_amount - total_amount) / previous_month_total_amount * 100)
