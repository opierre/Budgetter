from PySide6.QtCore import QPointF, QRectF, QSizeF, QMargins, QDateTime, QLocale, Signal
from PySide6.QtGui import QPainter, QResizeEvent
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

from budgetter.utils.tools import convert_amount_to_str
from budgetter.view.widgets.saving_widgets.saving_chart_widget import SavingChart


class ChartView(QGraphicsView):
    """
    ChartView
    """

    # Signal emitted when clicked on chat to display legend - Month (str) / Amount (str)
    legend = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store chart
        self.chart = SavingChart()

        # Configure widget
        self.configure_widgets()

        # Connect all slots and signals
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect click on series to display legend in title bar
        self.chart.pointClicked.connect(self.show_legend)

    def configure_widgets(self):
        """
        Configure all widgets

        :return: None
        """

        # Configure chart view appearance
        self.setStyleSheet("background-color: transparent; border: none;")
        self.setRenderHint(QPainter.Antialiasing)

        # Configure chart view scene
        self.setScene(QGraphicsScene())
        self.scene().addItem(self.chart)

        # Configure chart
        self.chart.layout().setContentsMargins(0, 0, 0, 0)
        self.chart.setBackgroundRoundness(0)
        self.chart.setMargins(QMargins(0, 0, 0, 0))

    def set_values(self, values: dict):
        """
        Set values on series

        :param values: values to set as dict
        :return: None
        """

        # Set values on chat
        self.chart.set_values(values)

    def resizeEvent(self, event: QResizeEvent):
        """
        Override resizeEvent()

        :param event: QResizeEvent
        :return: None
        """
        if scene := self.scene():
            scene.setSceneRect(QRectF(QPointF(0, 0), QSizeF(event.size())))
            self.chart.resize(QSizeF(event.size()))

        super().resizeEvent(event)

    def show_legend(self, point: QPointF):
        """
        Display legend by emitting signal

        :param point: (QPointF) Point to display legend on
        :return: None
        """

        # Set text
        x_value = QLocale().toString(QDateTime.fromMSecsSinceEpoch(int(point.x())), "MMMM yyyy").capitalize()
        y_value = convert_amount_to_str(point.y())
        self.legend.emit(f"{x_value}", f"{y_value} €")
