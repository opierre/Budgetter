from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt, QRectF
from PySide2.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics
from PySide2.QtWidgets import QWidget, QGridLayout

from utils.tools import convert_amount_to_str
from view.widgets.bar_widgets.category_chart_widget import CategoryChart


class ChartBars(QWidget):
    """
    Chart with bars per category
    """

    def __init__(self, chart_type: str, parent=None):
        super(ChartBars, self).__init__(parent)

        """ Store chart """
        self.chart = CategoryChart(chart_type)
        self.chart_view = QtCharts.QChartView(self.chart)
        self._layout = QGridLayout(self)
        self._layout.addWidget(self.chart_view)

        """ Store total amount show state """
        self._show_total = True

        """ Store average show state """
        self._show_average = False

        """ Configure widgets """
        self.configure_widgets()

        """ Connect slots and signals """
        self.connect_slots_and_signals()

    def configure_widgets(self):
        """
        Configure child widgets

        :return: None
        """

        """ Configure chart view """
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setVisible(True)

        """ Configure chart """
        # self.chart.set_values(self.values)
        self.chart.layout().setContentsMargins(0, 0, 0, 0)

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        pass

    def set_values(self, values):
        """
        Set value for each month

        :param values: values
        :return: None
        """

        self.chart.set_values(values)
        self.update()

    def show_labels(self, value: bool):
        """
        Display labels on bars

        :param value: True/False
        :return: None
        """

        self.chart.show_labels(value)

    def show_average(self, value: bool):
        """
        Show/hide average line

        :param value: True/False
        :return: None
        """

        self.chart.show_average(value)
        self._show_average = value
        self.update()

    def show_total(self, value: bool):
        """
        Show total amount on top left corner

        :param value: True/False
        :return: None
        """

        self._show_total = value
        self.update()

    def paintEvent(self, event):
        """
        Override paintEvent()

        :param event: QEvent
        :return: None
        """

        """ Get painter """
        painter = QPainter(self)

        """ Configure painter """
        painter.setPen(Qt.NoPen)

        """ Draw average """
        if self._show_average is True:
            self.draw_average(painter)

        """ Draw amount total amount """
        if self._show_total is True:
            self.draw_total_amount(painter)

        """ Draw chart """
        self.draw_values()

    def draw_total_amount(self, painter: QPainter):
        """
        Draw total amount for period

        :param painter: (QPainter) painter
        :return: None
        """

        """ Configure pen and painter """
        pen = QPen(QColor("#9298a8"), 1, c=Qt.RoundCap)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.setFont(QFont("Roboto", 11, QFont.Normal))

        """ Set text """
        text_average = "Average: "
        text_total = "Total: "

        """ Set rectangle according to font metrics """
        font_metrics = QFontMetrics(painter.font())
        text_heigth = font_metrics.height()
        text_width = font_metrics.width(text_average)
        rectangle_total = QRectF(self.rect().x() + 9, self.rect().y(),
                                 text_width, text_heigth)

        painter.drawText(rectangle_total, int(Qt.AlignLeft | Qt.AlignVCenter), text_total)

        """ Set bold font """
        painter.setFont(QFont("Roboto", 11, QFont.Bold))

        """ Set text """
        text_amount = convert_amount_to_str(self.chart.total()) + " €"

        """ Set rectangle according to font metrics """
        font_metrics = QFontMetrics(painter.font())
        text_amount_width = font_metrics.width(text_amount)
        text_heigth = font_metrics.height()
        rectangle_amount = QRectF(rectangle_total.x() + rectangle_total.width() + 9, rectangle_total.y(),
                                  text_amount_width, text_heigth)
        painter.drawText(rectangle_amount, int(Qt.AlignLeft | Qt.AlignVCenter), text_amount)

    def draw_average(self, painter: QPainter):
        """
        Draw average amount for period

        :param painter: (QPainter) painter
        :return: None
        """

        """ Configure pen and painter """
        pen = QPen(QColor("#9298a8"), 1, c=Qt.RoundCap)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.setFont(QFont("Roboto", 11, QFont.Normal))

        """ Set text """
        text_average = "Average: "

        """ Set rectangle according to font metrics """
        font_metrics = QFontMetrics(painter.font())
        text_average_width = font_metrics.width(text_average)
        text_heigth = font_metrics.height()

        if self._show_total is True:
            y_coord = self.rect().y() + 9 + text_heigth
        else:
            y_coord = self.rect().y()

        rectangle_average = QRectF(self.rect().x() + 9, y_coord,
                                   text_average_width, text_heigth)

        painter.drawText(rectangle_average, int(Qt.AlignLeft | Qt.AlignVCenter), text_average)

        """ Set bold font """
        painter.setFont(QFont("Roboto", 11, QFont.Bold))

        """ Set text """
        text_amount = convert_amount_to_str(self.chart.average()) + " €"

        """ Set rectangle according to font metrics """
        font_metrics = QFontMetrics(painter.font())
        text_amount_width = font_metrics.width(text_amount)
        text_heigth = font_metrics.height()
        rectangle_amount = QRectF(rectangle_average.x() + rectangle_average.width() + 9, rectangle_average.y(),
                                  text_amount_width, text_heigth)
        painter.drawText(rectangle_amount, int(Qt.AlignLeft | Qt.AlignVCenter), text_amount)

    def draw_values(self):
        """
        Draw points for each value
        :return: None
        """

        """ Draw chart view """
        self.chart_view.setGeometry(self.rect().x(), self.rect().y(),
                                    self.rect().width(),
                                    self.rect().height())

        self.chart_view.setVisible(True)
