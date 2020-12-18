from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import QSize
from PySide2.QtGui import QFont, QPixmap, QIcon, Qt
from PySide2.QtWidgets import QGroupBox, QGridLayout, QLabel, QPushButton, QDockWidget, QLineEdit, QSpacerItem, \
    QSizePolicy, QStatusBar

from widgets.titlebar import TitleBar


class Container(QDockWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Container title """
        self._title = ''

        """ Add button on top right corner """
        self._add = QPushButton()

        self.titleBar = TitleBar(self)
        self.titleBar.setObjectName(u"test")

        """ Status Bar """
        self._statusBar = QStatusBar()

        """ Three dots button on bottom right corner """
        self._settings = QPushButton()

        """ Layout """
        self.layout = QGridLayout()

        """ Configure widgets """
        self.configureWidgets()

        """ Configure layout """
        self.configureLayout()

    def configureWidgets(self):
        """
        Configure widgets inside container
        :return: void
        """

        """ Add button to title """
        self.setTitleBarWidget(self.titleBar)
        print(self.style().pixelMetric(QtWidgets.QStyle.PM_TitleBarHeight))
        print(self.style().pixelMetric(QtWidgets.QStyle.PM_DockWidgetTitleBarButtonMargin))
        print(self.style().pixelMetric(QtWidgets.QStyle.PM_DockWidgetTitleMargin))
        print(self.style().pixelMetric(QtWidgets.QStyle.PM_DockWidgetHandleExtent))


    def configureLayout(self):
        """
        Set elements in layout
        :return: void
        """

        """ Set margins """
        self.layout.setContentsMargins(14, 0, 14, 0)

        """ Apply layout on Card """
        self.setLayout(self.layout)
