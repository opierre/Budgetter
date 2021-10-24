from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt, QDateTime
from PySide2.QtGui import QPen, QColor, QBrush


class CategoryChart(QtCharts.QChart):
    """
    Category chart
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Hide legend """
        self.legend().hide()

        """ Store current clicked point """
        self.current_point = None

        """ Set x axis """
        self.axis_x = QtCharts.QBarCategoryAxis()
        self.axis_x.setVisible(True)
        self.axis_x.setGridLineVisible(False)

        """ Set y axis """
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setMin(0)
        self.axis_y.setVisible(True)

        """ Store series """
        self.series = QtCharts.QBarSeries(self)
        self.set = QtCharts.QBarSet("Category")

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
            # x_value = QDateTime.fromString(key, "MM-yyyy").toMSecsSinceEpoch()
            x_value = QDateTime.toString(QDateTime.fromString(key, "MM-yyyy"), "MMM-yyyy")

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
        # self.setAxisX(self.axis_x, self.series)
        # self.setAxisY(self.axis_y, self.series)

        # self.axis_x.setRange(QDateTime.fromMSecsSinceEpoch(self.series.points()[0].x()),
        #                      QDateTime.fromMSecsSinceEpoch(self.series.points()[-1].x()))

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
