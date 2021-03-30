from PySide2.QtCore import Qt, QSize, QRect
from PySide2.QtGui import QPainter, QPen, QColor, QFont, QFontMetrics
from PySide2.QtWidgets import QWidget


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

        """ Set fixed size """
        self.setFixedSize(200, 200)

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
        pen.setWidthF(18.0)
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

            """ Configure rectangle """
            rect = QRect(self.rect().x()+10, self.rect().y()+10, self.rect().width()-20, self.rect().height()-20)
            rect.moveCenter(self.rect().center())

            """ Draw arc """
            painter.drawArc(rect, start_angle * 16, span_angle * 16)

            """ Re-draw first one in case of last to hide overlapping """
            if current_index == last_index:
                """ Set pen color """
                pen.setColor(self.colors[0])
                painter.setPen(pen)

                """ Configure rectangle """
                rect = QRect(self.rect().x()+10, self.rect().y()+10, self.rect().width()-20, self.rect().height()-20)
                rect.moveCenter(self.rect().center())

                """ Draw arc """
                painter.drawArc(rect, first_start_angle * 16, first_span_angle * 16 * 1 / 10)

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
        fontMetrics = QFontMetrics(font)
        pixelsWidth = fontMetrics.width("Current balance")
        pixelsHeight = fontMetrics.height()

        """ Set text """
        rect = QRect(self.rect().x() + 10, self.rect().y() + 10, self.rect().width() - 20, self.rect().height() - 20)
        rect.moveCenter(self.rect().center())
        painter.drawText(rect, Qt.AlignHCenter | Qt.AlignVCenter, "Current balance")

        painter.end()
