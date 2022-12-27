from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDockWidget

from budgetter.view.widgets.title_bar import TitleBar


class Container(QDockWidget):
    """
    Container
    """

    # Signal emitted when search bar in title bar is edited - Content typed: str/Search field name: str
    titleBarSearched = Signal(str, str)

    # Signal emitted when button in title bar has been clicked - Checked state: bool
    titleBarClicked = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Container title
        self._title = ''

        # Title bar with title and add button
        self.title_bar = TitleBar(self)

        # Configure widgets
        self.configure_widgets()

        # Connect all slots and signals
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Emit signal when button in title bar has been clicked
        self.title_bar.clicked.connect(self.titleBarClicked.emit)

        # Emit signal when text typed in search bar
        self.title_bar.searched.connect(self.titleBarSearched.emit)

    def configure_widgets(self):
        """
        Configure widgets inside container

        :return: None
        """

        # Add button to title
        self.setTitleBarWidget(self.title_bar)

    def set_icon(self, icon: QIcon):
        """
        Replace QIcon with icon

        :param icon: QIcon to set
        :return: None
        """

        self.title_bar.set_icon(icon)

    def disable_title_bar_button(self):
        """
        Hide button on top right corner in title bar if useless

        :return: None
        """

        self.title_bar.disable_button()

    def disable_search_bar(self):
        """
        Hide search bar on top right corner in title bar if useless

        :return: None
        """

        self.title_bar.disable_search()

    def set_info(self, info: str):
        """
        Set info on Container title bar

        :param info: info to set
        :return: None
        """

        self.title_bar.set_info(info)

    def set_title(self, title: str):
        """
        Set title on Container title bar

        :param title: title to set
        :return: None
        """

        self.title_bar.set_title(title)

    def set_button_tooltip(self, tooltip: str):
        """
        Set tooltip on right button in title bar

        :param tooltip: tooltip
        :return: None
        """

        self.title_bar.set_button_tooltip(tooltip)
