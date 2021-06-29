from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt
from PySide2.QtGui import QPen, QColor, QBrush


class SavingChart(QtCharts.QChart):
    """
    Saving chart
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Hide legend """
        self.legend().hide()

        """ Set axis and hide them """
        self.axis_x = QtCharts.QValueAxis()
        self.axis_y = QtCharts.QValueAxis()
        self.axis_x.setVisible(True)
        self.axis_y.setVisible(True)

        """ Configure axis range and add them to chart """
        self.addAxis(self.axis_x, QtCore.Qt.AlignBottom)
        self.addAxis(self.axis_y, QtCore.Qt.AlignLeft)
        self.axis_x.setRange(0, 5)
        self.axis_x.setTickCount(1)

        """ Customize stylesheet """
        self.setBackgroundBrush(QBrush(QColor("transparent")))

        self.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

    def set_values(self, values: list):
        """
        Set values to display
        :param values: list of values
        :return: void
        """

        if len(values) != 6:
            return

        range_max = max(values)
        self.axis_y.setRange(0, range_max*11/10)

        """ Configure pen """
        pen = QPen(QColor("white"))
        pen.setWidthF(6.0)
        pen.setCapStyle(Qt.RoundCap)

        """ Fulfill series """
        series = QtCharts.QSplineSeries()
        for index, value in enumerate(values):
            series.append(index, value)

        """ Draw values """
        series.setPen(pen)
        self.addSeries(series)
        series.attachAxis(self.axis_x)
        series.attachAxis(self.axis_y)
