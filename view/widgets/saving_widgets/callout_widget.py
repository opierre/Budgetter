from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QPointF, QRectF, QRect, Qt, QSizeF, QMargins, QDateTime, QLocale
from PySide2.QtGui import QFontMetrics, QFont, QPainterPath, QPainter, QColor, QResizeEvent
from PySide2.QtWidgets import QGraphicsView, QGraphicsItem, QGraphicsScene, QStyleOptionGraphicsItem

from utils.tools import convert_amount_to_str
from view.widgets.saving_widgets.saving_chart_widget import SavingChart


class Callout(QGraphicsItem):
    """
    Callout displayed as tooltip
    """

    def __init__(self, parent: QtCharts.QChart):
        super().__init__()

        """ Store parent chart """
        self.chart: QtCharts.QChart = parent

        """ Store text to display """
        self.month: str = ''
        self.amount: str = ''

        """ Store anchor to pin Callout """
        self.anchor: QPointF = QPointF()

        """ Store rectangles """
        self.text_rect_up: QRectF = QRectF()
        self.text_rect_down: QRectF = QRectF()
        self.complete_rect: QRectF = QRectF()

        """ Store font """
        self.font_top = QFont("Roboto", 11, QFont.Normal)
        self.font_bottom = QFont("Roboto Medium", 11, QFont.Normal)

    def set_text(self, month: str, amount: str):
        """
        Set text on callout

        :param month: month to set
        :param amount: amount to set
        :return: None
        """

        """ Update text variable """
        self.month = month
        self.amount = amount

        """ Compute font metrics to adjust rect size """
        metrics_top = QFontMetrics(self.font_top)
        metrics_bottom = QFontMetrics(self.font_bottom)
        self.text_rect_up = QRectF(metrics_top.boundingRect(QRect(0, 0, 150, 150), Qt.AlignLeft, self.month))
        self.text_rect_down = QRectF(metrics_bottom.boundingRect(QRect(0, 0, 150, 150), Qt.AlignCenter, self.amount))

        """ Center bottom rect according to top rect """
        self.text_rect_down.moveCenter(QPointF(self.text_rect_up.center().x(), self.text_rect_up.height() +
                                               self.text_rect_down.height()/2 + 5))

        """ Change geometry """
        self.prepareGeometryChange()

        if self.text_rect_up.width() >= self.text_rect_down.width():
            self.complete_rect = QRectF(self.text_rect_up.x() - 10,
                                        self.text_rect_up.y() - 10,
                                        self.text_rect_up.width() + 20,
                                        self.text_rect_up.height() + self.text_rect_down.height() + 25)
        else:
            self.complete_rect = QRectF(self.text_rect_down.x() - 10,
                                        self.text_rect_up.y() - 10,
                                        self.text_rect_down.width() + 20,

                                        self.text_rect_up.height() + self.text_rect_down.height() + 25)

        self.update_geometry()

    def update_geometry(self, alignment: Qt.AlignmentFlag = Qt.AlignLeft):
        """
        Update geometry to shift from anchor

        :param alignment: (Qt.AlignmentFlag) alignment of callout
        :return: None
        """

        self.prepareGeometryChange()

        if alignment == Qt.AlignLeft:
            """ Check that callout is not outside chart """
            x_temp = self.chart.mapToPosition(self.anchor) + QPointF(15, -60)
            self.setPos(x_temp)
        else:
            x_temp = self.chart.mapToPosition(self.anchor) + QPointF(-self.complete_rect.width() + 5, -60)

            """ Change from top to bottom anchor in case of high point """
            if x_temp.y() < 10:
                x_temp = self.chart.mapToPosition(self.anchor) + QPointF(-self.complete_rect.width() + 5, 18)

            self.setPos(x_temp)

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

        """ Configure background rect path """
        path = QPainterPath()
        complete_rect = self.complete_rect
        path.addRoundedRect(complete_rect, 2, 2)

        """ Configure background style """
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(25, 157, 229, 230))

        """ Draw background """
        painter.drawPath(path)

        """ Draw text """
        painter.setFont(self.font_top)
        painter.setPen(QColor("#26374C"))
        painter.drawText(self.text_rect_up, self.month)

        painter.setFont(self.font_bottom)
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(self.text_rect_down, self.amount)


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
        self.tooltip.set_text(f"{x_value}", f"{y_value} €")

        """ Anchor callout """
        self.tooltip.anchor = point

        """ Update display settings """
        self.tooltip.setZValue(11)
        self.tooltip.update_geometry(alignment)
        self.tooltip.show()
