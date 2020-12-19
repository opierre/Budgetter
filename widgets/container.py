from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import QSize
from PySide2.QtGui import QFont, QPixmap, QIcon, Qt
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

        """ Status bar """
        self.customStatusBar = StatusBar()
        self.statusBar = QStatusBar()

        """ Configure widgets """
        self.configureWidgets()

    def configureWidgets(self):
        """
        Configure widgets inside container
        :return: void
        """

        """ Add button to title """
        self.setTitleBarWidget(self.titleBar)
