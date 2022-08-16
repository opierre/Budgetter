from PySide6 import QtCore
from PySide6.QtCharts import QChart, QValueAxis, QSplineSeries
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor, QBrush


class SpendingChart(QChart):
    """
    Spending chart
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Hide legend
        self.legend().hide()

        # Set axis and hide them
        self.axis_x = QValueAxis()
        self.axis_y = QValueAxis()
        self.axis_x.setVisible(False)
        self.axis_y.setVisible(False)

        # Configure axis range and add them to chart
        self.addAxis(self.axis_x, QtCore.Qt.AlignBottom)
        self.addAxis(self.axis_y, QtCore.Qt.AlignLeft)
        self.axis_x.setRange(0, 5)
        self.axis_x.setTickCount(1)

        # Customize stylesheet
        self.setBackgroundBrush(QBrush(QColor("transparent")))

        # Set animation on series
        self.setAnimationOptions(QChart.SeriesAnimations)

    def set_values(self, values: list):
        """
        Set values to display

        :param values: list of values
        :return: None
        """

        if len(values) != 6:
            return

        range_max = max(values)
        self.axis_y.setRange(0, range_max * 11 / 10)

        # Configure pen
        pen = QPen(QColor("white"))
        pen.setWidthF(6.0)
        pen.setCapStyle(Qt.RoundCap)

        # Fulfill series
        series = QSplineSeries()
        for index, value in enumerate(values):
            series.append(index, value)

        # Draw values
        series.setPen(pen)
        self.addSeries(series)
        series.attachAxis(self.axis_x)
        series.attachAxis(self.axis_y)
