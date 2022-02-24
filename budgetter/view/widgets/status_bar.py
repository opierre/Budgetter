from PySide2.QtCore import QSize, Signal
from PySide2.QtGui import QIcon, Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton


class StatusBar(QWidget):
    """
    Custom Status Bar
    """

    # Signal emitted when click on Previous
    previousClicked = Signal()

    # Signal emitted when click on Next
    nextClicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        # Add buttons on bottom right corner
        self._settings = QPushButton()
        self._settings.setObjectName(u"statusBarSettings")
        self._previous = QPushButton()
        self._previous.setObjectName(u"statusBarPrevious")
        self._next = QPushButton()
        self._next.setObjectName(u"statusBarNext")

        # Layout for status bar
        self.layout = QHBoxLayout(self)

        # Configure widgets
        self.configure_widgets()

        # Configure layout
        self.configure_layout()

        # Connect all slots and signals
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect click on previous/next buttons to emit signal
        self._previous.clicked.connect(self.previousClicked.emit)
        self._next.clicked.connect(self.nextClicked.emit)

    def configure_widgets(self):
        """
        Configure widgets inside container

        :return: None
        """

        # Configure Add button on bottom right corner
        self._settings.setIcon(QIcon(":/images/images/more_horiz-white-24dp.svg"))
        self._settings.setIconSize(QSize(22, 22))
        self._settings.setCursor(Qt.PointingHandCursor)

        # Configure Previous button on bottom right corner
        self._previous.setIcon(QIcon(":/images/images/navigate_before_black_24dp.svg"))
        self._previous.setIconSize(QSize(22, 22))
        self._previous.setCursor(Qt.PointingHandCursor)
        self._previous.setVisible(False)

        # Configure Add button on bottom right corner
        self._next.setIcon(QIcon(":/images/images/navigate_next_black_24dp.svg"))
        self._next.setIconSize(QSize(22, 22))
        self._next.setCursor(Qt.PointingHandCursor)
        self._next.setVisible(False)

    def configure_layout(self):
        """
        Set elements in layout

        :return: None
        """

        # Set margins
        self.layout.setContentsMargins(0, 12, 14, 12)

        # Add widgets to layout
        self.layout.addWidget(self._settings)
        self.layout.addWidget(self._previous)
        self.layout.addWidget(self._next)

    def show_settings(self, _bool: bool):
        """
        Show settings button with three dots

        :param _bool: True/False
        :return: None
        """

        if _bool:
            self._settings.show()
        else:
            self._settings.hide()

    def hide_settings(self):
        """
        Hide settings button

        :return: None
        """

        self._settings.setIcon(QIcon(":/images/images/more_horiz-white-24dp_hidden.svg"))
        self._settings.setCursor(Qt.ArrowCursor)

    def show_previous_next(self):
        """
        Show previous/next arrows in place of settings

        :return: None
        """

        self._settings.hide()
        self._next.show()
        self._previous.show()
