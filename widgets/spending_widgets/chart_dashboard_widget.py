from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import QPainter, QColor, QLinearGradient, QBrush, QPen
from PySide2.QtWidgets import QWidget


class ChartDashboard(QWidget):
    """
    Chart Dashboard
    """

    def __init__(self, parent=None):
        super(ChartDashboard, self).__init__(parent)

        """ Store current month """
        self.current_month = 5

    def set_current_month(self, month):
        """
        Update current month
        :param month: current month
        :return: void
        """

        self.current_month = month

    def paintEvent(self, event):
        """
        Override paintEvent()
        :param event: QEvent
        :return: void
        """

        """ Get painter """
        painter = QPainter(self)

        """ Configure painter """
        painter.setPen(Qt.NoPen)

        """ Set gradient """
        gradient = QLinearGradient(self.rect().x(), self.rect().y(), self.rect().width(), self.rect().height())
        gradient.setColorAt(0, QColor("#199DE5"))
        gradient.setColorAt(1, QColor("#0154C8"))
        brush = QBrush(gradient)
        painter.setBrush(brush)

        """ Draw background """
        painter.drawRoundedRect(self.rect(), 5, 5)

        """ Draw upper line """
        self.draw_separator(painter)

        """ Draw month buttons """
        self.draw_months(painter)

    def draw_separator(self, painter):
        """
        Draw upper separator between months and line
        :param painter: painter
        :return: void
        """

        """ Configure pen """
        pen = QPen()
        pen.setColor(QColor(255, 255, 255))
        pen.setWidthF(1.5)
        painter.setPen(pen)
        painter.setOpacity(0.06)

        """ Draw line """
        painter.drawLine(self.rect().x(), self.rect().y() + self.rect().height() * 1/5,
                         self.rect().width(), self.rect().y() + self.rect().height() * 1/5)

    def draw_months(self, painter):
        """
        Draw months as buttons
        :param painter: painter
        :return: void
        """

        """ Get current month """
        current_month = QDate.currentDate().month()


