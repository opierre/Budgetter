from PySide2.QtCore import Qt, QSize, QRect
from PySide2.QtGui import QPainter, QPen, QColor
from PySide2.QtWidgets import QWidget


class DonutChart(QWidget):
    """
    Donut chart
    """
    
    def __init__(self, parent=None):
        super(DonutChart, self).__init__(parent)

        """ Configure size """
        min_size = min(parent.width(), parent.height())
        self.setFixedSize(min_size, min_size)

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
        pen.setWidthF(2.0)
        pen.setColor(QColor("#309db5"))
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)

        """ Set angles """
        start_angle = 0
        span_angle = 340

        """ Configure rectangle """
        rect = QRect(self.rect().x()+10, self.rect().y()+10, self.rect().width()-20, self.rect().height()-20)
        rect.moveCenter(self.rect().center())

        painter.drawRect(self.rect())

        painter.drawArc(rect, start_angle * 16, span_angle * 16)

        painter.end()
