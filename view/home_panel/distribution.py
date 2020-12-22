from PySide2.QtCore import QObject, Qt
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter, QBrush, QColor, QCursor, QFont
from PySide2.QtWidgets import QGridLayout, QSizePolicy, QTextEdit, QVBoxLayout, QStatusBar, QWidget, QPushButton

from random import randrange
from functools import partial

from widgets.statusbar import StatusBar
from widgets.thumbnail import Thumbnail


class Distribution(QObject):
    """
    Distribution
    """

    def __init__(self, gui):
        super(Distribution, self).__init__()

        """ Store gui """
        self.uiSetup = gui

        """ Store custom/classic status bar """
        self.customStatusBar = StatusBar()
        self.statusBar = QStatusBar()

        """ Current Month button """
        self.currentMonth = QPushButton("September")
        self.currentMonth.setObjectName(u"monthDistribution")

        """ Previous Month button """
        self.previousMonth = QPushButton("August")
        self.previousMonth.setObjectName(u"monthDistribution")

        self.textEdit = QTextEdit("Hello")
        self.textEdit.setStyleSheet("background-color: transparent; border: none;")

        """ Configure layout """
        self.configureLayout()

        """ Configure status bar """
        self.configureStatusBar()

    def configureLayout(self):
        """
        Configure layout inside of Container
        :return: void
        """

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.textEdit)
        # layout.addStretch()
        layout.addWidget(self.statusBar)
        layout.setContentsMargins(0, 0, 0, 0)

        self.uiSetup.monthlyExpenses.setWidget(widget)

    def configureStatusBar(self):
        """
        Configure status bar
        :return: void
        """

        """ Set states for activation """
        self.currentMonth.setProperty("activated", "true")
        style = self.currentMonth.style()
        style.update()
        self.previousMonth.setProperty("activated", "false")
        style = self.previousMonth.style()
        style.update()

        """ Set cursor for left buttons """
        self.currentMonth.setCursor(Qt.PointingHandCursor)
        self.previousMonth.setCursor(Qt.PointingHandCursor)

        """ Add custom status bar to classic one """
        self.statusBar.addPermanentWidget(self.customStatusBar)

        """ Add buttons on left corner """
        self.statusBar.addWidget(self.currentMonth)

        """ Disable size grip """
        self.statusBar.setSizeGripEnabled(False)
