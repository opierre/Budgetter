import enum

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from budgetter.view.skeletons.Toaster import Ui_Notification


class ToasterType(enum.Enum):
    INFO = 0
    SUCCESS = enum.auto()
    ERROR = enum.auto()
    WARNING = enum.auto()


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

        # Configure toaster
        self.configure(message, toaster_type)

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
        self.toast.content.setProperty("state", ToasterType.INFO.name.lower())
        self.toast.content.style().unpolish(self.toast.content)
        self.toast.content.style().polish(self.toast.content)

        # Set icon
        icon = QIcon()
        icon.addFile("success", QSize(32, 32), QIcon.Disabled, QIcon.Off)
        self.toast.icon.setIcon(icon)
