from PySide2.QtCore import Qt, QRect, QPoint, QSize
from PySide2.QtGui import QColor, QPen, QPainter
from PySide2.QtWidgets import QCalendarWidget


class CalendarWidget(QCalendarWidget):
    """
    Calendar Widget without red weekends labels and with rounded selection
    """

    def __init__(self, parent=None):
        super(CalendarWidget, self).__init__(parent)

        """ Hide week number """
        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        """ Set days on top as one letter only """
        self.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)

        """ Change red color on weekends """
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

            """ Improve rendering """
            painter.setRenderHint(QPainter.Antialiasing)

            """ Fill background selection """
            painter.fillRect(rect, QColor("transparent"))

            """ Set no border """
            painter.setPen(Qt.NoPen)

            """ Set circle color """
            painter.setBrush(QColor("#0190EA"))

            """ Configure rect for ellipse """
            rectSelection = QRect(QPoint(), rect.height()*QSize(1, 1))
            rectSelection.moveCenter(rect.center())
            painter.drawEllipse(rectSelection)

            """ Draw day number """
            painter.setPen(QPen(QColor("white")))
            painter.drawText(rectSelection, Qt.AlignCenter, str(date.day()))

            painter.restore()
        else:
            super(CalendarWidget, self).paintCell(painter, rect, date)
