from typing import List

from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QPointF, QRectF, QRect, Qt, QSizeF, QMargins
from PySide2.QtGui import QFontMetrics, QFont, QPainterPath, QPainter, QColor, QResizeEvent, QMouseEvent
from PySide2.QtWidgets import QGraphicsView, QGraphicsSceneMouseEvent, QGraphicsItem, QStyleOptionGraphicsItem, QWidget, \
    QGraphicsScene, QGraphicsSimpleTextItem

from widgets.saving_widgets.saving_chart_widget import SavingChart


class Callout(QGraphicsItem):

    def __init__(self, parent: QtCharts.QChart):
        super().__init__()
        self.m_chart: QtCharts.QChart = parent
        self.m_text: str = ''
        self.m_anchor: QPointF = QPointF()
        self.m_font: QFont = QFont()
        self.m_textRect: QRectF = QRectF()
        self.m_rect: QRectF = QRectF()

    def setText(self, text: str):
        self.m_text = text
        metrics = QFontMetrics(self.m_font)
        self.m_textRect = QRectF(metrics.boundingRect(QRect(0, 0, 150, 150), Qt.AlignLeft, self.m_text))
        self.m_textRect.translate(5, 5)
        self.prepareGeometryChange()
        self.m_rect = QRectF(self.m_textRect.adjusted(-5, -5, 5, 5))
        self.updateGeometry()

    def updateGeometry(self):
        self.prepareGeometryChange()
        self.setPos(self.m_chart.mapToPosition(self.m_anchor) + QPointF(10, -50))

    def boundingRect(self) -> QRectF:
        from_parent = self.mapFromParent(self.m_chart.mapToPosition(self.m_anchor))
        anchor = QPointF(from_parent)
        rect = QRectF()
        rect.setLeft(min(self.m_rect.left(), anchor.x()))
        rect.setRight(max(self.m_rect.right(), anchor.x()))
        rect.setTop(min(self.m_rect.top(), anchor.y()))
        rect.setBottom(max(self.m_rect.bottom(), anchor.y()))
        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget):
        path = QPainterPath()
        mr = self.m_rect
        path.addRoundedRect(mr, 5, 5)

        anchor = QPointF(self.mapFromParent(self.m_chart.mapToPosition(self.m_anchor)))
        if not mr.contains(anchor):
            point1 = QPointF()
            point2 = QPointF()

            # establish the position of the anchor point in relation to self.m_rect
            above = anchor.y() <= mr.top()
            above_center = mr.top() < anchor.y() <= mr.center().y()
            below_center = mr.center().y() < anchor.y() <= mr.bottom()
            below = anchor.y() > mr.bottom()

            on_left = anchor.x() <= mr.left()
            left_of_center = mr.left() < anchor.x() <= mr.center().x()
            right_of_center = mr.center().x() < anchor.x() <= mr.right()
            on_right = anchor.x() > mr.right()

            # get the nearest self.m_rect corner.
            x = (on_right + right_of_center) * mr.width()
            y = (below + below_center) * mr.height()
            corner_case = (above and on_left) or (above and on_right) or (below and on_left) or (below and on_right)
            vertical = abs(anchor.x() - x) > abs(anchor.y() - y)
            horizontal = bool(not vertical)

            x1 = x + left_of_center * 10 - right_of_center * 20 + corner_case * horizontal * (
                    on_left * 10 - on_right * 20)
            y1 = y + above_center * 10 - below_center * 20 + corner_case * vertical * (above * 10 - below * 20)
            point1.setX(x1)
            point1.setY(y1)

            x2 = x + left_of_center * 20 - right_of_center * 10 + corner_case * horizontal * (
                    on_left * 20 - on_right * 10)
            y2 = y + above_center * 20 - below_center * 10 + corner_case * vertical * (above * 20 - below * 10)
            point2.setX(x2)
            point2.setY(y2)

            path.moveTo(point1)
            path.lineTo(anchor)
            path.lineTo(point2)
            path = path.simplified()

        painter.setPen(QColor(30, 30, 30))
        painter.setBrush(QColor(255, 255, 255))
        painter.drawPath(path)
        painter.drawText(self.m_textRect, self.m_text)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        event.setAccepted(True)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        if event.buttons() & Qt.LeftButton:
            self.setPos(self.mapToParent(event.pos() - event.buttonDownPos(Qt.LeftButton)))
            event.setAccepted(True)
        else:
            event.setAccepted(False)


class CalloutChartView(QGraphicsView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_callouts: List[Callout] = []
        self.setDragMode(QGraphicsView.NoDrag)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # chart
        self.m_chart = SavingChart(parent)
        self.m_chart.layout().setContentsMargins(0, 0, 0, 0)
        self.m_chart.setBackgroundRoundness(0)
        self.m_chart.setMargins(QMargins(0, 0, 0, 0))

        self.setRenderHint(QPainter.Antialiasing)

        self.setScene(QGraphicsScene())
        self.scene().addItem(self.m_chart)

        self.m_coordX = QGraphicsSimpleTextItem(self.m_chart)
        self.m_coordX.setPos(self.m_chart.size().width() / 2 - 50, self.m_chart.size().height() - 20)
        self.m_coordX.setText("X: ")
        self.m_coordY = QGraphicsSimpleTextItem(self.m_chart)
        self.m_coordY.setPos(self.m_chart.size().width() / 2 + 50, self.m_chart.size().height() - 20)
        self.m_coordY.setText("Y: ")

        self.m_tooltip = Callout(self.m_chart)
        self.scene().addItem(self.m_tooltip)

        self.m_chart.series_finale.clicked.connect(self.keep_callout)
        self.m_chart.series_finale.hovered.connect(self.tooltip)

    def set_values(self, values):
        """
        Set values on series for callout display

        :param values: values to set as dict
        :return: void
        """

        """ Set values on chat """
        self.m_chart.set_values(values)

    def resizeEvent(self, event: QResizeEvent):
        if scene := self.scene():
            scene.setSceneRect(QRectF(QPointF(0, 0), QSizeF(event.size())))
            self.m_chart.resize(QSizeF(event.size()))
            self.m_coordX.setPos(self.m_chart.size().width() / 2 - 50, self.m_chart.size().height() - 20)
            self.m_coordY.setPos(self.m_chart.size().width() / 2 + 50, self.m_chart.size().height() - 20)

            for callout in self.m_callouts:
                callout.updateGeometry()

        super().resizeEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        from_chart = self.m_chart.mapToValue(event.pos())
        self.m_coordX.setText(f"X: {from_chart.x()}")
        self.m_coordX.setText(f"Y: {from_chart.y()}")
        super().mouseMoveEvent(event)

    def keep_callout(self):
        self.m_callouts.append(self.m_tooltip)
        self.m_tooltip = Callout(self.m_chart)
        self.scene().addItem(self.m_tooltip)

    def tooltip(self, point: QPointF, state: bool):
        if not self.m_tooltip:
            self.m_tooltip = Callout(self.m_chart)

        if state:
            self.m_tooltip.setText(f"X: {point.x()} \nY: {point.x()} ")
            self.m_tooltip.m_anchor = point
            self.m_tooltip.setZValue(11)
            self.m_tooltip.updateGeometry()
            self.m_tooltip.show()
        else:
            self.m_tooltip.hide()

