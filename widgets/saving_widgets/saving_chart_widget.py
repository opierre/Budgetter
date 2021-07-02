from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt, QDateTime, QPointF
from PySide2.QtGui import QPen, QColor, QBrush, QLinearGradient, QGradient


class SavingChart(QtCharts.QChart):
    """
    Saving chart
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Hide legend """
        self.legend().hide()

        """ Set axis """
        self.axis_x = QtCharts.QDateTimeAxis()
        self.axis_x.setFormat("MMM-yy")
        # self.axis_x.setTickCount(6)
        self.axis_x.setVisible(False)

        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setVisible(False)

        """ Customize stylesheet """
        #self.setBackgroundBrush(QBrush(QColor("transparent")))

        self.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

    def set_values(self, values: dict):
        """
        Set values to display
        :param values: list of values
        :return: void
        """

        """ Configure pen """
        pen = QPen(QColor("#6dd230"))
        pen.setWidthF(6.0)
        pen.setCapStyle(Qt.RoundCap)

        """ Fulfill series """
        series = QtCharts.QSplineSeries()
        for key, value in values.items():
            series.append(float(QDateTime.fromString(key, "MMMM-yyyy").toMSecsSinceEpoch()), value)

        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        gradient.setColorAt(0.0, 0x3cc63c)
        gradient.setColorAt(1.0, 0x26f626)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        series.setBrush(gradient)

        """ Draw values """
        series.setPen(pen)
        self.addSeries(series)

        """ Set axes """
        self.addAxis(self.axis_x, Qt.AlignBottom)
        self.addAxis(self.axis_y, Qt.AlignLeft)
        series.attachAxis(self.axis_x)
        series.attachAxis(self.axis_y)

