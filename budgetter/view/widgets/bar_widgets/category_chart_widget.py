from PySide6.QtCharts import QBarCategoryAxis, QValueAxis, QBarSeries, QSplineSeries, QAbstractBarSeries, \
    QChart, QBarSet
from PySide6.QtCore import Qt, QDateTime, QPointF, QLocale
from PySide6.QtGui import QPen, QColor, QBrush, QLinearGradient, QGradient, QFont


class CategoryChart(QChart):
    """
    Category chart
    """

    def __init__(self, chart_type: str, parent=None):
        super().__init__(parent)

        # Hide legend
        self.legend().hide()

        # Store chart type
        self.chart_type = chart_type

        # Store current clicked point
        self.current_point = None

        # Set x axis
        self.axis_x = QBarCategoryAxis()

        # Set y axis
        self.axis_y = QValueAxis()

        # Store series
        self.series = QBarSeries(self)
        self.average_series = QSplineSeries(self)
        self.set = None

        # Store average show state
        self._show_average = False

        # Store limits
        self.local_max_x = None
        self.local_min_x = None

        # Configure chart
        self.configure_chart()

    def configure_chart(self):
        """
        Configure all chart aspects

        :return: None
        """

        # Configure locale for number display
        locale = QLocale(QLocale.French)
        self.setLocalizeNumbers(True)
        self.setLocale(locale)

        # Configure labels
        self.series.setLabelsFormat("@value €")
        self.series.setLabelsPrecision(6)
        self.series.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)
        self.series.setLabelsVisible(True)

        # Configure X axis
        self.axis_x.setVisible(True)
        self.axis_x.setGridLineVisible(False)
        self.axis_x.setLabelsColor(QColor("#9298a8"))
        self.axis_x.setLabelsFont(QFont("Roboto", 10, QFont.Normal))
        pen = QPen(QColor(66, 96, 135, 200))
        pen.setWidthF(2.0)
        self.axis_x.setLinePen(pen)

        # Configure Y axis
        self.axis_y.setMin(0)
        self.axis_y.setVisible(False)
        self.axis_y.setLabelsColor(QColor("white"))

        # Customize stylesheet
        self.setBackgroundBrush(QBrush(QColor("transparent")))

        # Configure gradient to fulfill bars
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))

        if self.chart_type == 'Income':
            gradient.setColorAt(0.0, QColor("#23D0FE"))
            gradient.setColorAt(1.0, QColor("#1A68FA"))
        else:
            gradient.setColorAt(0.0, QColor("#D821FE"))
            gradient.setColorAt(1.0, QColor("#8118F9"))
        gradient.setCoordinateMode(QGradient.ObjectMode)
        self.series.setBarWidth(0.5)

        # Set animation
        self.setAnimationOptions(QChart.SeriesAnimations)

        # Remove margins
        self.layout().setContentsMargins(0, 0, 0, 0)

        # Configure average series
        if self.chart_type == 'Income':
            pen = QPen(QColor("#1a68fa"))
        else:
            pen = QPen(QColor("#8118F9"))
        pen.setWidthF(1.0)
        pen.setCapStyle(Qt.RoundCap)
        pen.setStyle(Qt.DashLine)
        self.average_series.setPen(pen)
        self.average_series.setOpacity(0.8)

    def configure_barset(self):
        """
        Configure bar set after eache series cleared

        :return: None
        """

        self.set = QBarSet("Category")
        self.set.setLabelFont(QFont("Roboto", 10, QFont.Normal))
        self.set.setLabelColor(QColor("#9298a8"))

        # Configure gradient to fulfill bars
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        if self.chart_type == 'Income':
            gradient.setColorAt(0.0, QColor("#23D0FE"))
            gradient.setColorAt(1.0, QColor("#1A68FA"))
        else:
            gradient.setColorAt(0.0, QColor("#D821FE"))
            gradient.setColorAt(1.0, QColor("#8118F9"))
        gradient.setCoordinateMode(QGradient.ObjectMode)
        self.set.setBrush(gradient)

        # Create pen to draw borders
        pen = QPen()
        pen.setWidthF(5.0)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        pen.setBrush(gradient)
        self.set.setPen(pen)

    def show_average(self, value: bool):
        """
        Show/hide average line

        :param value: True/False
        :return: None
        """

        self._show_average = value
        self.average_series.setVisible(value)

    def total(self) -> float:
        """
        Return total for current period

        :return: total amount
        """

        return self.set.sum()

    def average(self) -> float:
        """
        Return average for current period

        :return: average amount
        """

        return self.set.sum() / self.set.count()

    def set_values(self, values: dict):
        """
        Set values to display

        :param values: list of values
        :return: None
        """

        # Store previous state to avoid flash
        previous_state = self.series.isLabelsVisible()
        self.series.setLabelsVisible(False)

        # Clear previous values
        self.series.clear()
        self.average_series.clear()
        self.removeAxis(self.axis_x)
        self.removeAxis(self.axis_y)

        # Configure barset
        self.configure_barset()

        # Configure pen
        pen = QPen(QColor("#6dd230"))
        pen.setWidthF(3.0)
        pen.setCapStyle(Qt.RoundCap)

        # Fulfill series
        y_max_value = 0
        x_values = []
        for key, value in values.items():
            # Update Y-Axis range
            if value > y_max_value:
                y_max_value = value

            # Update X-Axis range
            x_value = QDateTime.toString(QDateTime.fromString(key, "MM-yyyy"), "MMM-yy")

            x_values.append(x_value)
            self.set.append(value)

        # Compute average
        average_value = self.set.sum() / self.set.count()
        for index in range(0, self.set.count()):
            self.average_series.append(index, average_value)

        # Update local max and min
        self.local_max_x = x_values[-1]
        self.local_min_x = x_values[0]

        # Set brush and pen for series
        self.axis_x.setCategories(x_values)
        self.series.append(self.set)

        # Add series to graph
        self.addSeries(self.average_series)
        self.addSeries(self.series)
        self.average_series.setVisible(self._show_average)

        # Set axes
        self.addAxis(self.axis_x, Qt.AlignBottom)
        self.addAxis(self.axis_y, Qt.AlignLeft)

        # Attach axes to series
        self.series.attachAxis(self.axis_x)
        self.average_series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)
        self.average_series.attachAxis(self.axis_y)

        # Configure y axis
        self.axis_y.setRange(0, y_max_value * 12 / 10)

        # Restore previous state
        self.series.setLabelsVisible(previous_state)

    def show_labels(self, value: bool):
        """
        Display labels on bars

        :param value: True/False
        :return: None
        """

        self.series.setLabelsVisible(value)
