from PySide2.QtCore import Qt, QDate, QRect
from PySide2.QtGui import QPainter, QColor, QLinearGradient, QBrush, QPen
from PySide2.QtWidgets import QWidget, QPushButton, QStyleOptionButton, QStyle


class ChartDashboard(QWidget):
    """
    Chart Dashboard
    """

    def __init__(self, parent=None):
        super(ChartDashboard, self).__init__(parent)

        """ Store current month """
        self.current_month = 1

        """ Store buttons """
        self.months = [QPushButton(), QPushButton(), QPushButton(), QPushButton(), QPushButton(), QPushButton()]

        """ Get all months """
        self.get_months()

    def get_months(self):
        """
        Get months
        :return: void
        """

        """ Get current month """
        current_month_nb = QDate.currentDate().month()
        current_month = QDate.currentDate().longMonthName(current_month_nb)
        self.months[5].setText(current_month.upper()[0:3])

        """ Get 5 previous month and update stylesheet """
        for index in range(1, 6):
            if current_month_nb == 1:
                current_month_nb = 13
            previous_month = QDate.currentDate().longMonthName(current_month_nb - 1)
            self.months[5 - index].setText(previous_month.upper()[0:3])
            self.months[5 - index].setStyleSheet("background-color: transparent; color: red;")
            self.months[5 - index].setCursor(Qt.PointingHandCursor)

            current_month_nb -= 1

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

        if len(self.months) == 6:
            for index in range(0, 6):
                """ Align rectangle for button """
                button_rectangle = QRect(self.rect().x() + 0 + (self.rect().width() - 0) * index / 6.0,
                                         self.rect().y(),
                                         self.rect().width() / 6.0,
                                         self.rect().height() * 1 / 5)

                # """ Create buttons """
                # optionMore = QStyleOptionButton()
                #
                # optionMore.initFrom(self.months[index])
                # optionMore.text = self.months[index].text()
                # optionMore.rect = button_rectangle
                # optionMore.state = optionMore.state or QStyle.State_MouseOver
                #
                # self.months[index].style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.months[index])

                self.months[index].resize(button_rectangle.size())

                # painter.save()
                # painter.translate(button_rectangle.topLeft())
                self.months[index].render(painter, button_rectangle.topLeft())
                # painter.restore()

