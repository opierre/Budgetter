from PySide6.QtCore import QEvent, Signal
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget


class Overlay(QWidget):
    """
    Overlay
    """

    # Signal emitted when overlay is clicked
    overlayClickedSignal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set initial size
        self.setFixedSize(parent.size())

        # Install event filter on parent in order to replace dialog on center after resize/move
        self.parent().installEventFilter(self)

        # Hide overlay by default
        self.hide()

    def paintEvent(self, event):
        """
        Override paintEvent()

        :param event: paint event
        :return: None
        """

        # Set border and background color
        pen_color = QColor("#303030")
        fill_color = QColor(48, 48, 48, 80)

        # Set painter
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # Apply color to painter pen/brush
        painter.setPen(pen_color)
        painter.setBrush(fill_color)

        # Draw overlay rectangle
        painter.drawRect(self.parent().rect())

        # Close painter
        painter.end()

    def eventFilter(self, watched, event):
        """
        Override event filter

        :param watched: watched
        :param event: event
        :return: None
        """

        if watched == self.parent() and event.type() == QEvent.Resize:
            # Reset new size
            self.setFixedSize(self.parent().size())

        # Intercept click on overlay
        if event.type() == QEvent.MouseButtonRelease:
            if self.rect().contains(event.pos()):
                self.overlayClickedSignal.emit()
                result = True
            else:
                result = False
        else:
            result = False

        return result

    def show(self):
        """
        Override show() to raise overlay on top of all widgets

        :return: None
        """

        # Raise overlay
        self.raise_()

        super().show()
