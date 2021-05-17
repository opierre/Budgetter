from PySide2.QtCore import Qt, QDate, QRect
from PySide2.QtGui import QPainter, QColor, QLinearGradient, QBrush, QPen, QFont
from PySide2.QtWidgets import QWidget, QPushButton, QStyleOptionButton, QStyle, QButtonGroup


class ChartDashboard(QWidget):
    """
    Chart Dashboard
    """

    def __init__(self, parent=None):
        super(ChartDashboard, self).__init__(parent)

        """ Store current month """
        self.current_month = 1

        """ Store buttons """
        self.months = [QPushButton(self),
                       QPushButton(self),
                       QPushButton(self),
                       QPushButton(self),
                       QPushButton(self),
                       QPushButton(self)]

        """ Set buttons group exclusive """
        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)

        """ Get all months """
        self.get_months()

    def get_months(self):
        """
        Get months
        :return: void
        """

        stylesheet = "QPushButton"\
                     "{"\
                     "  background-color: transparent; "\
                     "  color: rgba(255, 255, 255, 100);"\
                     "  font-family: \"Roboto Medium\";"\
                     "  font-size: 12pts;"\
                     "  border-top-left-radius: 2px;"\
                     "  border-top-right-radius: 2px;"\
                     "  border-bottom-left-radius: 0px;"\
                     "  border-bottom-right-radius: 0px;"\
                     "}"\
                     "QPushButton::checked" \
                     "{" \
                     "  background-color: rgba(255, 255, 255, 30); " \
                     "  color: rgba(255, 255, 255, 200);" \
                     "  font-family: \"Roboto Black\";" \
                     "  font-size: 12pts;" \
                     "  border-top-left-radius: 2px;"\
                     "  border-top-right-radius: 2px;"\
                     "  border-bottom-left-radius: 0px;"\
                     "  border-bottom-right-radius: 0px;"\
                     "}"

        """ Get current month """
        current_month_nb = QDate.currentDate().month()
        current_month = QDate.currentDate().longMonthName(current_month_nb)
        self.months[5].setText(current_month.upper()[0:3])
        self.months[5].setStyleSheet(stylesheet)
        self.months[5].setCursor(Qt.PointingHandCursor)
        self.months[5].setCheckable(True)
        self.button_group.addButton(self.months[5])

        """ Get 5 previous month and update stylesheet """
        for index in range(1, 6):
            if current_month_nb == 1:
                current_month_nb = 13
            previous_month = QDate.currentDate().longMonthName(current_month_nb - 1)
            self.months[5 - index].setText(previous_month.upper()[0:3])
            self.months[5 - index].setStyleSheet(stylesheet)
            self.months[5 - index].setCursor(Qt.PointingHandCursor)
            self.months[5 - index].setCheckable(True)
            self.button_group.addButton(self.months[5 - index])

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
        painter.drawLine(self.rect().x(), self.rect().y() + self.rect().height() * 1/6,
                         self.rect().width(), self.rect().y() + self.rect().height() * 1/6)

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
                                         self.rect().height() * 1 / 6)

                """ Define buttons positions """
                self.months[index].resize(button_rectangle.size())
                self.months[index].move(button_rectangle.x(), button_rectangle.y())

                if self.months[index].isChecked():
                    print(index)
                    painter.setPen(Qt.NoPen)

                    """ Set gradient """
                    rectangle_background = QRect(button_rectangle.x(),
                                                 button_rectangle.y() + button_rectangle.width(),
                                                 button_rectangle.width(),
                                                 self.rect().height())
                    gradient = QLinearGradient(rectangle_background.x(),
                                               rectangle_background.y(),
                                               rectangle_background.x() + rectangle_background.width(),
                                               rectangle_background.height())
                    print(rectangle_background)
                    gradient.setColorAt(0, QColor(0, 255, 255, 30))
                    gradient.setColorAt(1, QColor(255, 255, 0, 200))
                    brush = QBrush(gradient)
                    painter.setBrush(brush)

                    painter.drawRect(rectangle_background)
