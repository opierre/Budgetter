from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt, QDateTime, QPointF
from PySide2.QtGui import QPen, QColor, QBrush, QLinearGradient, QGradient, QFont
from PySide2.QtWidgets import QGraphicsBlurEffect


class CategoryChart(QtCharts.QChart):
    """
    Category chart
    """

    def __init__(self, chart_type: str, parent=None):
        super().__init__(parent)

        """ Hide legend """
        self.legend().hide()

        """ Store chart type """
        self.chart_type = chart_type

        """ Store current clicked point """
        self.current_point = None

        """ Set x axis """
        self.axis_x = QtCharts.QBarCategoryAxis()

        """ Set y axis """
        self.axis_y = QtCharts.QValueAxis()

        """ Store series """
        self.series = QtCharts.QBarSeries(self)
        self.set = QtCharts.QBarSet("Category")

        """ Configure chart """
        self.configure_chart()

        """ Connect all slots and signals """
        self.connect_slots_and_signals()

    def configure_chart(self):
        """
        Configure all chart aspects

        :return: None
        """

        """ Configure X axis """
        self.axis_x.setVisible(True)
        self.axis_x.setGridLineVisible(False)
        self.axis_x.setLabelsColor(QColor("#9298a8"))
        self.axis_x.setLabelsFont(QFont("Roboto", 10, QFont.Normal))
        pen = QPen(QColor(66, 96, 135, 200))
        pen.setWidthF(2.0)
        self.axis_x.setLinePen(pen)

        """ Configure Y axis """
        self.axis_y.setMin(0)
        self.axis_y.setVisible(False)
        self.axis_y.setLabelsColor(QColor("white"))

        """ Customize stylesheet """
        self.setBackgroundBrush(QBrush(QColor("transparent")))

        """ Configure gradient to fulfill bars """
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))

        if self.chart_type == 'Income':
            gradient.setColorAt(0.0, QColor("#23D0FE"))
            gradient.setColorAt(1.0, QColor("#1A68FA"))
        else:
            gradient.setColorAt(0.0, QColor("#D821FE"))
            gradient.setColorAt(1.0, QColor("#8118F9"))
        gradient.setCoordinateMode(QGradient.ObjectMode)
        self.set.setBrush(gradient)

        """ Create pen to draw borders """
        pen = QPen()
        pen.setWidthF(5.0)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        pen.setBrush(gradient)
        self.set.setPen(pen)
        self.series.setBarWidth(0.5)

        """ Set animation """
        self.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        """ Remove margins """
        self.layout().setContentsMargins(0, 0, 0, 0)

    def set_values(self, values: dict):
        """
        Set values to display

        :param values: list of values
        :return: None
        """

        """ Clear previous values """
        self.series.clear()

        """ Configure pen """
        pen = QPen(QColor("#6dd230"))
        pen.setWidthF(3.0)
        pen.setCapStyle(Qt.RoundCap)

        """ Fulfill series """
        y_max_value = 0
        x_values = []
        for key, value in values.items():
            """ Update Y-Axis range """
            if value > y_max_value:
                y_max_value = value

            """ Update X-Axis range """
            x_value = QDateTime.toString(QDateTime.fromString(key, "MM-yyyy"), "MMM-yy")

            x_values.append(x_value)
            self.set.append(value)

        """ Set brush and pen for series """
        self.axis_x.append(x_values)
        self.series.append(self.set)

        """ Add series to graph """
        self.addSeries(self.series)

        """ Set axes """
        self.addAxis(self.axis_x, Qt.AlignBottom)
        self.addAxis(self.axis_y, Qt.AlignLeft)

        """ Attach axes to series """
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)

        """ Configure y axis """
        self.axis_y.setRange(0, y_max_value * 12/10)

        """ Display middle point """
        # self.show_point(self.get_middle_value())

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals from within chart

        :return: None
        """

        """ Connect click on series finale to display scatter """
        # self.series_finale.clicked[QPointF].connect(self.show_point)
        # self.area_series.clicked[QPointF].connect(self.show_point)