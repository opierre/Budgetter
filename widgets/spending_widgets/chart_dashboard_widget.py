from PySide2.QtCore import Qt, QDate, QRect, QRectF
from PySide2.QtGui import QPainter, QColor, QLinearGradient, QBrush, QPen, QFont
from PySide2.QtWidgets import QWidget, QPushButton, QStyleOptionButton, QStyle, QButtonGroup, QGridLayout
from PySide2.QtCharts import QtCharts

from utils.tools import convert_amount_to_str
from widgets.spending_widgets.spending_chart_widget import SpendingChart


class ChartDashboard(QWidget):
    """
    Chart Dashboard
    """

    def __init__(self, parent=None):
        super(ChartDashboard, self).__init__(parent)

        """ Store current month """
        self.current_month = 5

        """ Store buttons """
        self.months = [QPushButton(self),
                       QPushButton(self),
                       QPushButton(self),
                       QPushButton(self),
                       QPushButton(self),
                       QPushButton(self)]

        """ Store values for months """
        self.values = [2589, 1809, 1026, 1547, 1258, 987]

        """ Set buttons group exclusive """
        self.button_group = QButtonGroup()

        """ Get all months """
        self.get_months()

        """ Store chart """
        self.chart = SpendingChart()
        self.chart_view = QtCharts.QChartView(self.chart)
        self._layout = QGridLayout(self)
        self._layout.addWidget(self.chart_view)

        """ Configure widgets """
        self.configure_widgets()

        """ Connect slots and signals """
        self.connect_slots_and_signals()

    def configure_widgets(self):
        """
        Configure child widgets
        :return: void
        """

        """ Set buttons group exclusive """
        self.button_group.setExclusive(True)
        self.months[-1].setChecked(True)

        """ Configure chart view """
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setVisible(True)

        """ Configure chart """
        self.chart.set_values(self.values)
        self.chart.layout().setContentsMargins(0, 0, 0, 0)

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals
        :return: void
        """

        """ Connect click on button to update current month """
        self.button_group.buttonClicked.connect(self.update)

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

    def set_values(self, values):
        """
        Set value for each month
        :param values: values [1 --> 6]
        :return: void
        """

        self.values.clear()

        for value in enumerate(values):
            self.values.append(value)

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

        """ Draw amount for selected month """
        rectangle_amount = self.draw_amount(painter)

        """ Draw period underneath amount """
        rectangle_period = self.draw_period(painter, rectangle_amount)

        """ Draw values """
        self.draw_values(painter, rectangle_period)

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

        painter.setPen(Qt.NoPen)
        painter.setOpacity(1)

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

                if self.months[index].isChecked() is True:
                    """ Set white gradient """
                    rectangle_background = QRect(button_rectangle.x(),
                                                 button_rectangle.y() + button_rectangle.height(),
                                                 button_rectangle.width(),
                                                 self.rect().height())
                    gradient = QLinearGradient(rectangle_background.x(),
                                               rectangle_background.y(),
                                               rectangle_background.x(),
                                               rectangle_background.height())
                    gradient.setColorAt(0, QColor(255, 255, 255, 30))
                    gradient.setColorAt(1, QColor(255, 255, 255, 5))
                    brush = QBrush(gradient)
                    painter.setBrush(brush)

                    """ Draw gradient """
                    painter.drawRect(rectangle_background)

                    """ Update current month """
                    self.current_month = index

    def draw_amount(self, painter):
        """
        Draw amount for selected month
        :param painter: painter
        :return: rectangle where amount has been drawn
        """

        """ Set rectangle """
        rectangle_amount = QRectF(self.rect().x() + self.rect().width() * 1 / 24,
                                  self.rect().y() + self.rect().height() * 1 / 4,
                                  self.rect().width() / 4.5,
                                  28)

        """ Configure pen and painter """
        pen = QPen(QColor("white"), 1, c=Qt.RoundCap)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.setFont(QFont("Roboto Black", 18, QFont.Normal))

        """ Set text """
        text = convert_amount_to_str(self.values[self.current_month]) + " €"
        painter.drawText(rectangle_amount, Qt.AlignCenter, text)

        return rectangle_amount

    def draw_period(self, painter, rectangle_amount):
        """
        Draw period for selected month
        :param painter: painter
        :param rectangle_amount: upper rectangle
        :return: rectangle where period has been drawn
        """

        """ Set rectangle """
        rectangle_period = QRectF(rectangle_amount.x(),
                                  rectangle_amount.y() + rectangle_amount.height(),
                                  rectangle_amount.width(),
                                  rectangle_amount.height())

        """ Configure pen and painter """
        pen = QPen(QColor("#c4c9cf"), 1, c=Qt.RoundCap)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.setOpacity(0.8)
        painter.setFont(QFont("Roboto Medium", 8, QFont.Normal))

        """ Set text """
        month_number = (QDate.currentDate().month() - (5 - self.current_month)) % 12
        if month_number == 0:
            month_number = 12
        days_in_month = QDate(QDate.currentDate().year(), month_number, 1).daysInMonth()
        text = "01 " + self.months[self.current_month].text() + ' - ' + str(days_in_month) + " " + \
               self.months[self.current_month].text()
        painter.drawText(rectangle_period, Qt.AlignCenter, text)
        painter.setOpacity(1)

        return rectangle_period

    def draw_values(self, painter, rectangle_period):
        """
        Draw points for each value
        :param painter: painter
        :param rectangle_period: rectangle with period
        :return: void
        """

        """ Draw chart view """
        self.chart_view.setGeometry(self.rect().x(), rectangle_period.y(),
                                    self.rect().width(),
                                    self.rect().height() - rectangle_period.y())

        self.chart_view.setVisible(True)
