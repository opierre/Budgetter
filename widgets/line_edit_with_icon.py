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

        if not self.icon:
            self.setTextMargins(1, 1, 1, 1)
        else:
            self.setTextMargins(28, 1, 1, 1)

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
            pixmap = self.icon.pixmap(24, 24)
            height = (self.rect().height() - 24) / 2.0
            painter.drawPixmap(3, self.rect().y() + height, 24, 24, pixmap)
