import math

from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt, QDateTime, QPointF, Signal
from PySide2.QtGui import QPen, QColor, QBrush, QLinearGradient, QGradient


class SavingChart(QtCharts.QChart):
    """
    Saving chart
    """

    """ Signal emmitted when click on chart - Point clicked / Alignment of Callout """
    pointClicked = Signal(QPointF, Qt.Alignment)

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
        self.area_series = QtCharts.QAreaSeries()
        self.series_lower = QtCharts.QLineSeries()
        self.series_upper = QtCharts.QLineSeries()
        self.series_finale = QtCharts.QLineSeries()
        self.series_scatter = QtCharts.QScatterSeries()

        """ Customize stylesheet """
        self.setBackgroundBrush(QBrush(QColor("transparent")))

        """ Set animation """
        self.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        """ Connect all slots and signals """
        self.connect_slots_and_signals()

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
        self.area_series.setLowerSeries(self.series_lower)
        self.area_series.setUpperSeries(self.series_upper)

        """ Creat gradient to fulfill area zone """
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        gradient.setColorAt(0.0, QColor("#35536D"))
        gradient.setColorAt(1.0, QColor("transparent"))
        gradient.setCoordinateMode(QGradient.ObjectMode)

        """ Set brush and pen for series """
        self.area_series.setBrush(gradient)
        self.series_finale.setPen(pen)

        """ Configure scatter series pen and brush """
        self.series_scatter.setPen(pen)
        self.series_scatter.setBrush(QColor("#26374C"))

        """ Remove border from area zone """
        self.area_series.setPen(pen)
        self.area_series.setBorderColor(QColor('transparent'))

        """ Add series to graph """
        self.addSeries(self.area_series)
        self.addSeries(self.series_finale)
        self.addSeries(self.series_scatter)

        """ Set axes """
        self.addAxis(self.axis_x, Qt.AlignBottom)
        self.addAxis(self.axis_y, Qt.AlignLeft)

        """ Attach axes to series """
        self.series_finale.attachAxis(self.axis_x)
        self.series_finale.attachAxis(self.axis_y)
        self.area_series.attachAxis(self.axis_x)
        self.area_series.attachAxis(self.axis_y)
        self.series_scatter.attachAxis(self.axis_x)
        self.series_scatter.attachAxis(self.axis_y)

        """ Configure y axis """
        self.axis_y.setRange(0, max_value * 12/10)

        """ Display middle point """
        self.show_point(self.get_middle_value())

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals from within chart

        :return: void
        """

        """ Connect click on series finale to display scatter """
        self.series_finale.clicked[QPointF].connect(self.show_point)
        self.area_series.clicked[QPointF].connect(self.show_point)

    def show_point(self, clicked_point):
        """
        Display point on click

        :param clicked_point: QPointF
        :return: void
        """

        """ Random max distance """
        distance = 2147483647

        """ Find closest point in series finale """
        for current_point in self.series_finale.points():
            current_distance = math.sqrt((current_point.x() - clicked_point.x()) *
                                         (current_point.x() - clicked_point.x())
                                         + (current_point.y() - clicked_point.y())
                                         * (current_point.y() - clicked_point.y()))

            if current_distance < distance:
                distance = current_distance
                closest = current_point

        """ Remove previous point and append closest to click """
        self.series_scatter.clear()
        self.series_scatter.append(closest)

        """ Retrieve position in list """
        points = self.series_finale.points()
        index = points.index(closest)

        """ Emit signal to display callout """
        if index >= len(points) / 2:
            self.pointClicked.emit(closest, Qt.AlignRight)
        else:
            self.pointClicked.emit(closest, Qt.AlignLeft)

    def get_middle_value(self):
        """
        Retrieve center value for initial display

        :return: middle value as QPointF
        """

        middle_index = int(len(self.series_finale.points()) / 2)
        return self.series_finale.points()[middle_index]
