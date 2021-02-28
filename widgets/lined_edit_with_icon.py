from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QLineEdit


class LineEditWithIcon(QLineEdit):
    """
    Line edit with icon
    """

    def __init__(self, icon, parent):
        super(LineEditWithIcon, self).__init__(parent)
        
        """ Store icon """
        self.icon = icon

        """ Update icon """
        self.setIcon(icon)

    def setIcon(self, icon):
        """
        Set icon on left
        :param icon: icon
        :return: void
        """

        """ Update variable """
        self.icon = icon

        if self.icon:
            self.setTextMargins(1, 1, 1, 1)
        else:
            self.setTextMargins(20, 1, 1, 1)

    def paintEvent(self, event):
        """
        Override paintEvent
        :param event: event
        :return: void
        """

        super(LineEditWithIcon, self).paintEvent(event)

        """ Draw icon on left """
        if self.icon:
            painter = QPainter(self)
            pixmap = self.icon.pixmap(self.height() - 6, self.height() - 6)
            painter.drawPixmap(2, 3, pixmap)
