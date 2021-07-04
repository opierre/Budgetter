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

        """ Set x axis """
        self.axis_x = QtCharts.QDateTimeAxis()
        self.axis_x.setFormat("MMM-yy")
        self.axis_x.setVisible(False)

        """ Set y axis """
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setMin(0)
        self.axis_y.setVisible(False)

        """ Store series """
        self.area_series = None
        self.series_lower = QtCharts.QLineSeries()
        self.series_upper = QtCharts.QLineSeries()
        self.series_finale = QtCharts.QLineSeries()

        """ Customize stylesheet """
        self.setBackgroundBrush(QBrush(QColor("transparent")))

        self.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

    def set_values(self, values: dict):
        """
        Set values to display
        :param values: list of values
        :return: void
        """

        """ Configure pen """
        pen = QPen(QColor("#6dd230"))
        pen.setWidthF(3.0)
        pen.setCapStyle(Qt.RoundCap)

        """ Fulfill series """
        max_value = 0
        for key, value in values.items():
            if value > max_value:
                max_value = value
            self.series_upper.append(float(QDateTime.fromString(key, "MMMM-yyyy").toMSecsSinceEpoch()), value)
            self.series_finale.append(float(QDateTime.fromString(key, "MMMM-yyyy").toMSecsSinceEpoch()), value)
            self.series_lower.append(float(QDateTime.fromString(key, "MMMM-yyyy").toMSecsSinceEpoch()), 0)

        """ Create Area series """
        self.area_series = QtCharts.QAreaSeries(self.series_upper, self.series_lower)

        """ Creat gradient to fulfill area zone """
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        gradient.setColorAt(0.0, QColor("#35536D"))
        gradient.setColorAt(1.0, QColor("transparent"))
        gradient.setCoordinateMode(QGradient.ObjectMode)

        """ Set brush and pen for series """
        self.area_series.setBrush(gradient)
        self.series_finale.setPen(pen)

        """ Remove border from area zone """
        self.area_series.setPen(pen)
        self.area_series.setBorderColor(QColor('transparent'))

        """ Add series to graph """
        self.addSeries(self.area_series)
        self.addSeries(self.series_finale)

        """ Set axes """
        self.addAxis(self.axis_x, Qt.AlignBottom)
        self.addAxis(self.axis_y, Qt.AlignLeft)

        """ Attach axes to series """
        self.series_finale.attachAxis(self.axis_x)
        self.series_finale.attachAxis(self.axis_y)
        self.area_series.attachAxis(self.axis_x)
        self.area_series.attachAxis(self.axis_y)

        """ Configure y axis """
        self.axis_y.setRange(0, max_value * 12/10)

