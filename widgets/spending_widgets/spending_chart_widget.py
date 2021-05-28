from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt
from PySide2.QtGui import QPen, QColor


class SpendingChart(QtCharts.QChart):
    """
    Spending chart
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Hide legend """
        self.legend().hide()

        """ Set axis and hide them """
        self.axis_x = QtCharts.QValueAxis()
        self.axis_y = QtCharts.QValueAxis()
        self.axis_x.setVisible(False)
        self.axis_y.setVisible(False)

        """ Configure axis range and add them to chart """
        self.addAxis(self.axis_x, QtCore.Qt.AlignBottom)
        self.addAxis(self.axis_y, QtCore.Qt.AlignLeft)
        self.axis_x.setRange(0, 5)
        self.axis_x.setTickCount(1)

    def set_values(self, values: list):
        """
        Set values to display
        :param values: list of values
        :return: void
        """

        if len(values) != 6:
            return

        range_max = max(values)
        self.axis_y.setRange(0, range_max)

        pen = QPen(QColor("red"))
        pen.setWidthF(2.8)
        pen.setCapStyle(Qt.RoundCap)

        for index, value in enumerate(values):
            series = QtCharts.QSplineSeries()
            series.setPen(pen)
            series.append(index, value)
            self.addSeries(series)
            series.attachAxis(self.axis_x)
            series.attachAxis(self.axis_y)
