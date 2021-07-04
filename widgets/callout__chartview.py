from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QGraphicsEllipseItem


class CalloutChartView(QtCharts.QChartView):
    """
    Callout Chart view to display dots
    """

    def __init__(self, line_series, parent=None):
        super(CalloutChartView, self).__init__(parent)

        """ Store line series """
        self.line_series = line_series

        """ Ellipse item """
        self.ellipse_item = QGraphicsEllipseItem(parent)

    def keyPressEvent(self, event):
        """
        Override keyPressEvent()
        :param event: event
        :return: void
        """

        if event.key() == Qt.Key_Right:
            """ Move on to next point """
            self.move_to_next_point(Qt.Key_Left)
        elif event.key() == Qt.Key_Left:
            """ Move on to previous point """
            self.move_to_next_point(Qt.Key_Left)
        else:
            super(CalloutChartView, self).keyPressEvent(event)

    def move_to_next_point(self, key_direction):
        """
        Move on to next point
        :param key_direction: KeyLeft/KeyRight
        :return: void
        """

        point = self.line_series.at(2)

        pointPos = self.chart().mapToPosition(point)
        self.ellipse_item.setPos(pointPos)
