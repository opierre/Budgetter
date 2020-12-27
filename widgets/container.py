from PySide2.QtCore import Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDockWidget

from widgets.titlebar import TitleBar


class Container(QDockWidget):
    """
    Container
    """

    """ Signal emitted when button in title bar has been clicked """
    titleBarClicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Container title """
        self._title = ''

        """ Title bar with title and add button """
        self.titleBar = TitleBar(self)

        """ Configure widgets """
        self.configureWidgets()

        """ Connect all slots and signals """
        self.connectWidgets()

    def connectWidgets(self):
        """
        Connect all slots and signals
        :return: void
        """

        """ Emit signal when button in title bar has been clicked """
        self.titleBar.clicked.connect(self.titleBarClicked.emit)

    def configureWidgets(self):
        """
        Configure widgets inside container
        :return: void
        """

        """ Add button to title """
        self.setTitleBarWidget(self.titleBar)

    def setIcon(self, icon: QIcon):
        """
        Replace QIcon with icon
        :param icon: QIcon to set
        :return: void
        """

        self.titleBar.setIcon(icon)
