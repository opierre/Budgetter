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

        """ Store current clicked point """
        self.current_point = None

        """ Set x axis """
        self.axis_x = QtCharts.QDateTimeAxis()
        self.axis_x.setFormat("MMMM-yyyy")
        self.axis_x.setVisible(False)

        """ Set y axis """
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setMin(0)
        self.axis_y.setVisible(False)

        """ Store series """
        self.area_series = QtCharts.QAreaSeries(self)
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
        :return: None
        """

        """ Clear previous values """
        self.series_lower.clear()
        self.series_upper.clear()
        self.series_scatter.clear()
        self.series_finale.clear()

        """ Configure pen """
        pen = QPen(QColor("#6dd230"))
        pen.setWidthF(3.0)
        pen.setCapStyle(Qt.RoundCap)

        """ Fulfill series """
        y_max_value = 0
        for key, value in values.items():
            """ Update Y-Axis range """
            if value > y_max_value:
                y_max_value = value

            """ Update X-Axis range """
            x_value = float(QDateTime.fromString(key, "MM-yyyy").toMSecsSinceEpoch())

            self.series_upper.append(x_value, value)
            self.series_finale.append(x_value, value)
            self.series_lower.append(x_value, 0)

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
        self.axis_y.setRange(0, y_max_value * 12/10)
        self.axis_x.setRange(QDateTime.fromMSecsSinceEpoch(self.series_finale.points()[0].x()),
                             QDateTime.fromMSecsSinceEpoch(self.series_finale.points()[-1].x()))

        """ Display middle point """
        self.show_point(self.get_middle_value())

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals from within chart

        :return: None
        """

        """ Connect click on series finale to display scatter """
        self.series_finale.clicked[QPointF].connect(self.show_point)
        self.area_series.clicked[QPointF].connect(self.show_point)

    def show_point(self, clicked_point):
        """
        Display point on click

        :param clicked_point: QPointF
        :return: None
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

        """ Update current point clicked """
        self.current_point = closest

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

    def show_next(self):
        """
        Show next point

        :return: None
        """

        """ Retrieve position in list """
        points = self.series_finale.points()
        index = points.index(self.current_point)

        if index < len(points) - 1:
            index += 1

        """ Show next point and callout """
        self.show_point(points[index])

    def show_previous(self):
        """
        Show next point

        :return: None
        """

        """ Retrieve position in list """
        points = self.series_finale.points()
        index = points.index(self.current_point)

        if index > 0:
            index -= 1

        """ Show previous point and callout """
        self.show_point(points[index])