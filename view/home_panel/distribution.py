from PySide2.QtCore import QObject, Qt, QDate
from PySide2.QtWidgets import QTextEdit, QVBoxLayout, QStatusBar, QWidget, QPushButton, QListView

from widgets.statusbar import StatusBar


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

        """ Previous Month button """
        self.previousMonth = QPushButton("August")

        """ ListView to display all categories """
        self.categoriesListView = QListView()

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
        layout.addWidget(self.categoriesListView)
        layout.addWidget(self.statusBar)
        layout.setContentsMargins(0, 0, 0, 0)

        self.uiSetup.monthlyExpenses.setWidget(widget)

    def configureStatusBar(self):
        """
        Configure status bar
        :return: void
        """

        """ Set month content """
        self.setCurrentAndPreviousMonth()

        """ Set states for activation """
        self.currentMonth.setProperty("activated", "true")
        self.currentMonth.update()
        self.previousMonth.setProperty("activated", "false")
        self.previousMonth.update()

        """ Set cursor for left buttons """
        self.currentMonth.setCursor(Qt.PointingHandCursor)
        self.previousMonth.setCursor(Qt.PointingHandCursor)

        """ Add custom status bar to classic one """
        self.statusBar.addPermanentWidget(self.customStatusBar)

        """ Add buttons on left corner """
        self.statusBar.addWidget(self.currentMonth)
        self.statusBar.addWidget(self.previousMonth)

        """ Disable size grip """
        self.statusBar.setSizeGripEnabled(False)

    def setCurrentAndPreviousMonth(self):
        """
        Get current/previous month from locale and update display
        :return: void
        """

        currentMonthNb = QDate.currentDate().month()
        currentMonth = QDate.currentDate().longMonthName(currentMonthNb)
        self.currentMonth.setText(currentMonth.capitalize())

        previousMonth = QDate.currentDate().longMonthName(currentMonthNb - 1)
        self.previousMonth.setText(previousMonth.capitalize())
