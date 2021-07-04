from PySide2.QtCore import QMargins
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QWidget, QGridLayout
from PySide2.QtCharts import QtCharts

from widgets.saving_widgets.saving_chart_widget import SavingChart


class SavingDashboard(QWidget):
    """
    Saving Dashboard
    """

    def __init__(self, parent=None):
        super(SavingDashboard, self).__init__(parent)

        """ Store values for months """
        self.values = {"Janvier-2021": 12056,
                       "Février-2021": 13450,
                       "Mars-2021": 15469,
                       "Avril-2021": 14356,
                       "Mai-2021": 25098,
                       "Juin-2021": 26098,
                       "Juillet-2021": 22054,
                       "Août-2021": 25098,
                       "Septembre-2021": 29087}

        """ Store chart """
        self.chart = SavingChart()
        self.chart_view = QtCharts.QChartView(self.chart)
        # self.chart_view = CalloutChartView(self.chart.series_finale, parent=self.chart)
        self._layout = QGridLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self.chart_view)

        """ Configure widgets """
        self.configure_widgets()

    def configure_widgets(self):
        """
        Configure child widgets
        :return: void
        """

        """ Configure chart view """
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setVisible(True)

        """ Configure chart """
        self.chart.set_values(self.values)
        self.chart.layout().setContentsMargins(0, 0, 0, 0)
        self.chart.setBackgroundRoundness(0)
        self.chart.setMargins(QMargins(0, 0, 0, 0))

    def set_values(self, values):
        """
        Set value for each month
        :param values: values [1 --> 6]
        :return: void
        """

        self.values.clear()

        for value in enumerate(values):
            self.values.append(value)

        self.draw_values()

    def draw_values(self):
        """
        Draw points for each value
        :return: void
        """

        """ Draw chart view """
        self.chart_view.setGeometry(self.rect().x(), self.rect().y(),
                                    self.rect().width(),
                                    self.rect().height())

        self.chart_view.setVisible(True)
