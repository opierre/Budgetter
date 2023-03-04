from PySide6.QtCore import Qt, QRect, QPoint, QSize
from PySide6.QtGui import QColor, QPen, QPainter
from PySide6.QtWidgets import QCalendarWidget


class CalendarWidget(QCalendarWidget):
    """
    Calendar Widget without red weekends labels and with rounded selection
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Hide week number
        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        # Set days on top as one letter only
        self.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)

        # Change red color on weekends
        for day in (Qt.Saturday, Qt.Sunday,):
            fmt = self.weekdayTextFormat(day)
            fmt.setForeground(QColor("white"))
            self.setWeekdayTextFormat(day, fmt)

    def paintCell(self, painter, rect, date):
        """
        Override paintCell to display rounded selection

        :param painter: painter
        :param rect: rect
        :param date: date
        :return: None
        """

        if date == self.selectedDate():
            painter.save()

            # Improve rendering
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            # Fill background selection
            painter.fillRect(rect, QColor("transparent"))

            # Set no border
            painter.setPen(Qt.PenStyle.NoPen)

            # Set circle color
            painter.setBrush(QColor("#0190EA"))

            # Configure rect for ellipse
            rect_selection = QRect(QPoint(), rect.height() * QSize(1, 1))
            rect_selection.moveCenter(rect.center())
            painter.drawEllipse(rect_selection)

            # Draw day number
            painter.setPen(QPen(QColor("white")))
            painter.drawText(rect_selection, Qt.AlignmentFlag.AlignCenter, str(date.day()))

            painter.restore()
        else:
            super().paintCell(painter, rect, date)
