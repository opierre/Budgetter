from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter, QColor, QLinearGradient, QBrush
from PySide2.QtWidgets import QWidget


class ChartDashboard(QWidget):
    """
    Chart Dashboard
    """

    def __init__(self, parent=None):
        super(ChartDashboard, self).__init__(parent)

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

