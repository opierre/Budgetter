import enum

from PySide6.QtCore import (
    QSize,
    QRect,
    QPropertyAnimation,
    QEasingCurve,
    QTimer,
    QAbstractAnimation,
)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from budgetter.view.skeletons.Toaster import Ui_Notification


class ToasterType(enum.Enum):
    INFO = 0
    SUCCESS = enum.auto()
    ERROR = enum.auto()
    WARNING = enum.auto()


class ToasterStack(QWidget):
    """
    Stack to store toaster
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store number of notifications
        self._current_toasters = []

        # Store positions
        self._bottom_position = QRect(0, 0, 400, 50)
        self._bottom_position.moveBottomRight(self.parent().geometry().bottomRight())

    def add_toast(self, toast):
        """
        Add toast to stack

        :param toast: toaster
        :return: None
        """

        self._current_toasters.append(toast)


# TOASTER_STACK = ToasterStack()


class Toaster(QWidget):
    """
    Toaster class
    """

    def __init__(self, message: str, toaster_type: ToasterType, parent=None):
        """
        Constructor

        :param message: message to set
        :param toaster_type: toaster type for styling
        """

        super().__init__(parent)

        # Create toaster
        self.toast = Ui_Notification()
        self.toast.setupUi(self)

        # Store animation
        self._animation = QPropertyAnimation(self, b"geometry")

        # Configure toaster
        self.configure(message, toaster_type)

        # Add to toaster stack
        # TOASTER_STACK.add_toast(self)

        # Show toaster
        self.show()

    def configure(self, message: str, toaster_type: ToasterType):
        """
        Configure toaster look and message

        :param message: message to set
        :param toaster_type: toaster type for styling
        :return: None
        """

        # Set message
        self.toast.message.setText(message)

        # Set style
        self.toast.content.setProperty("state", toaster_type.name.lower())
        self.toast.content.style().unpolish(self.toast.content)
        self.toast.content.style().polish(self.toast.content)

        # Set icon
        icon = QIcon()
        icon.addFile(
            ":/images/success", QSize(32, 32), QIcon.Mode.Disabled, QIcon.State.Off
        )
        self.toast.icon.setIcon(icon)

        # Configure animation
        self._animation.setDuration(500)
        self._animation.setEasingCurve(QEasingCurve.Type.OutCubic)

        # Raise dialog widget on top of all window
        self.raise_()

        # Resize toaster
        self.adjustSize()

        # Set dialog on center of main window
        end_rect = self.geometry()
        end_rect.moveBottomRight(self.parent().rect().bottomRight())

        # Update geometry animation coordinates for y
        start_animation_rect = QRect(
            self.parent().rect().bottomRight().x(),
            end_rect.y(),
            end_rect.width(),
            end_rect.height(),
        )

        self._animation.setStartValue(start_animation_rect)
        self._animation.setEndValue(end_rect)

    def show(self) -> None:
        """
        Override show for animation

        :return: None
        """

        # Show popup
        super().show()

        # Start animation
        self._animation.start()

        # Execute rollback on timer timeout
        QTimer.singleShot(3500, self.rollback_toast)

    def rollback_toast(self):
        """
        Rollback animation to hide toaster

        :return: None
        """

        # Change direction of animation and start
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
