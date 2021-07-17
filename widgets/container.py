from PySide2.QtCore import Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDockWidget

from widgets.title_bar import TitleBar


class Container(QDockWidget):
    """
    Container
    """

    """ Signal emitted when search bar in title bar is edited - Content typed: str """
    titleBarSearched = Signal(str)

    """ Signal emitted when button in title bar has been clicked - Checked state: bool """
    titleBarClicked = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Container title """
        self._title = ''

        """ Title bar with title and add button """
        self.titleBar = TitleBar(self)

        """ Configure widgets """
        self.configure_widgets()

        """ Connect all slots and signals """
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals
        :return: void
        """

        """ Emit signal when button in title bar has been clicked """
        self.titleBar.clicked.connect(self.titleBarClicked.emit)

        """ Emit signal when text typed in search bar """
        self.titleBar.searched.connect(self.titleBarSearched.emit)

    def configure_widgets(self):
        """
        Configure widgets inside container
        :return: void
        """

        """ Add button to title """
        self.setTitleBarWidget(self.titleBar)

    def set_icon(self, icon: QIcon):
        """
        Replace QIcon with icon
        :param icon: QIcon to set
        :return: void
        """

        self.titleBar.set_icon(icon)

    def disable_title_bar_button(self):
        """
        Hide button on top right corner in title bar if useless
        :return: void
        """

        self.titleBar.disable_button()

    def disable_search_bar(self):
        """
        Hide search bar on top right corner in title bar if useless
        :return: void
        """

        self.titleBar.disable_search()

    def set_title(self, title):
        """
        Set title on Container title bar
        :param title: title to set
        :return: void
        """

        self.titleBar.set_title(title)
