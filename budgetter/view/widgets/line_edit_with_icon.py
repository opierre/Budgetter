from PySide6.QtGui import QPainter, QIcon
from PySide6.QtWidgets import QLineEdit


class LineEditWithIcon(QLineEdit):
    """
    Line edit with icon
    """

    def __init__(self, icon: QIcon = QIcon(), parent=None):
        super().__init__(parent)

        # Store icon
        self.icon = icon

        # Update icon
        self.set_icon(icon)

    def set_icon(self, icon):
        """
        Set icon on left

        :param icon: icon
        :return: None
        """

        # Update variable
        self.icon = icon

        if not self.icon:
            self.setTextMargins(1, 1, 1, 1)
        else:
            self.setTextMargins(28, 1, 1, 1)

    def paintEvent(self, event):
        """
        Override paintEvent

        :param event: event
        :return: None
        """

        super().paintEvent(event)

        # Draw icon on left
        if self.icon:
            painter = QPainter(self)
            pixmap = self.icon.pixmap(24, 24)
            height = (self.rect().height() - 24) / 2.0
            painter.drawPixmap(3, self.rect().y() + height, 24, 24, pixmap)
