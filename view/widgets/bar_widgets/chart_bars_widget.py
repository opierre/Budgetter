from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt, QRectF
from PySide2.QtGui import QPainter, QColor, QPen, QFont
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

        """ Draw amount total amount """
        self.draw_total_amount(painter)

        """ Draw chart """
        self.draw_values()

    def draw_total_amount(self, painter: QPainter):
        """
        Draw total amount for period

        :param painter: (QPainter) painter
        :return: (QRectF) rectangle where amount has been drawn
        """

        """ Set rectangle """
        rectangle_amount = QRectF(self.rect().x(), self.rect().y(),
                                  self.rect().width() / 4.5, 28)

        """ Configure pen and painter """
        pen = QPen(QColor("white"), 1, c=Qt.RoundCap)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.setFont(QFont("Roboto Black", 18, QFont.Normal))

        """ Set text """
        text = "Total: " + convert_amount_to_str(self.chart.total()) + " €"
        painter.drawText(rectangle_amount, int(Qt.AlignLeft | Qt.AlignVCenter), text)

        return rectangle_amount

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
