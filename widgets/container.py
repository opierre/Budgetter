from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QGroupBox, QGridLayout, QLabel, QPushButton, QDockWidget, QLineEdit, QSpacerItem, \
    QSizePolicy, QStatusBar, QWidget, QVBoxLayout, QTextEdit

from widgets.statusbar import StatusBar
from widgets.titlebar import TitleBar


class Container(QDockWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Container title """
        self._title = ''

        """ Title bar with title and add button """
        self.titleBar = TitleBar(self)

        """ Configure widgets """
        self.configureWidgets()

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
