from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QPointF, QRectF, QRect, Qt, QSizeF, QMargins, QDateTime, QLocale
from PySide2.QtGui import QFontMetrics, QFont, QPainterPath, QPainter, QColor, QResizeEvent
from PySide2.QtWidgets import QGraphicsView, QGraphicsItem, QGraphicsScene, QStyleOptionGraphicsItem

from utils.tools import convert_amount_to_str
from widgets.saving_widgets.saving_chart_widget import SavingChart


class Callout(QGraphicsItem):
    """
    Callout displayed as tooltip
    """

    def __init__(self, parent: QtCharts.QChart):
        super().__init__()

        """ Store parent chart """
        self.chart: QtCharts.QChart = parent

        """ Store text to display """
        self.text: str = ''

        """ Store anchor to pin Callout """
        self.anchor: QPointF = QPointF()

        """ Store rectangles """
        self.text_rect: QRectF = QRectF()
        self.complete_rect: QRectF = QRectF()

        """ Store font """
        self.font = QFont("Roboto", 11, QFont.Normal)

    def set_text(self, text: str):
        """
        Set text on callout

        :param text: text to set
        :return: None
        """

        """ Update text variable """
        self.text = text

        """ Compute font metrics to adjust rect size """
        metrics = QFontMetrics(self.font)
        self.text_rect = QRectF(metrics.boundingRect(QRect(0, 0, 150, 150), Qt.AlignLeft, self.text))

        """ Translate text rect """
        self.text_rect.translate(0, 0)

        """ Change geometry """
        self.prepareGeometryChange()
        self.complete_rect = QRectF(self.text_rect.adjusted(-5, -5, 5, 5))
        self.update_geometry()

    def update_geometry(self, alignment: Qt.AlignmentFlag = Qt.AlignLeft):
        """
        Update geometry to shift from anchor

        :param alignment: (Qt.AlignmentFlag) alignment of callout
        :return: None
        """

        self.prepareGeometryChange()

        if alignment == Qt.AlignLeft:
            self.setPos(self.chart.mapToPosition(self.anchor) + QPointF(10, -50))
        else:
            self.setPos(self.chart.mapToPosition(self.anchor) + QPointF(-self.complete_rect.width() - 5, -50))

    def boundingRect(self) -> QRectF:
        """
        Override boundingRect() from QGraphicsItem

        :return: (QRectF) bounding rect
        """

        """ Retrieve position from chart """
        from_parent = self.mapFromParent(self.chart.mapToPosition(self.anchor))

        """ Define anchor from parent """
        anchor = QPointF(from_parent)

        rect = QRectF()
        rect.setLeft(min(self.complete_rect.left(), anchor.x()))
        rect.setRight(max(self.complete_rect.right(), anchor.x()))
        rect.setTop(min(self.complete_rect.top(), anchor.y()))
        rect.setBottom(max(self.complete_rect.bottom(), anchor.y()))

        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget):
        """
        Override paint() from QGraphicsItem

        :param painter: (QPainter) painter
        :param option: (QStyleOptionGraphicsItem)
        :param widget: widget
        :return: None
        """

        """ Configure background shadow rect path """
        path_shadow = QPainterPath()
        complete_rect_shadow = QRectF(self.complete_rect.x(), self.complete_rect.y(),
                                      self.complete_rect.width() + 3, self.complete_rect.height() + 3)
        path_shadow.addRoundedRect(complete_rect_shadow, 5, 5)

        """ Configure shadow style """
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#1C293B"))

        """ Draw shadow """
        painter.drawPath(path_shadow)

        """ Configure background rect path """
        path = QPainterPath()
        complete_rect = self.complete_rect
        path.addRoundedRect(complete_rect, 5, 5)

        """ Configure background style """
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#015185"))

        """ Draw background """
        painter.drawPath(path)

        """ Draw text """
        painter.setFont(self.font)
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(self.text_rect, self.text)


class CalloutChartView(QGraphicsView):
    """
    Callout ChartView
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Store chart """
        self.chart = SavingChart()

        """ Store callout """
        self.tooltip = Callout(self.chart)

        """ Configure widget """
        self.configure_widgets()

        """ Connect all slots and signals """
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        """ Connect click on series to display callout """
        self.chart.pointClicked.connect(self.display_callout)

    def configure_widgets(self):
        """
        Configure all widgets

        :return: None
        """

        """ Configure chart view appearance """
        self.setStyleSheet("background-color: transparent; border: none;")
        self.setRenderHint(QPainter.Antialiasing)

        """ Configure chart view scene """
        self.setScene(QGraphicsScene())
        self.scene().addItem(self.chart)
        self.scene().addItem(self.tooltip)

        """ Configure chart """
        self.chart.layout().setContentsMargins(0, 0, 0, 0)
        self.chart.setBackgroundRoundness(0)
        self.chart.setMargins(QMargins(0, 0, 0, 0))

    def set_values(self, values: dict):
        """
        Set values on series for callout display

        :param values: values to set as dict
        :return: None
        """

        """ Set values on chat """
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

    def display_callout(self, point: QPointF, alignment: Qt.AlignmentFlag):
        """
        Display callout

        :param point: (QPointF) Point to display legend on
        :param alignment: (Qt.AlignmentFlag) alignment to display callout on left or right
        :return: None
        """

        """ Set text """
        x_value = QLocale().toString(QDateTime.fromMSecsSinceEpoch(point.x()), "MMMM yyyy").capitalize()
        y_value = convert_amount_to_str(point.y())
        self.tooltip.set_text(f"{x_value}\n{y_value} €")

        """ Anchor callout """
        self.tooltip.anchor = point

        """ Update display settings """
        self.tooltip.setZValue(11)
        self.tooltip.update_geometry(alignment)
        self.tooltip.show()
