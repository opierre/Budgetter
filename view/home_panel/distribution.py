from PySide2.QtCore import QObject, Qt, QDate
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QStatusBar, QWidget, QPushButton, QListView

from models.distribution_model import DistributionModel
from widgets.distributionDelegate import DistributionDelegate
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

        """ Store item delegate """
        self.distributionDelegate = DistributionDelegate()

        """ ListView to display all categories """
        self.categoriesListView = QListView()

        """ Model to handle data in distribution list """
        self.categoriesModel = DistributionModel([["Restaurants",
                                                  3,
                                                  22095.53,
                                                  100],
                                                  ["Transport",
                                                   120,
                                                   209.12,
                                                   42],
                                                  ["Groceries",
                                                   1,
                                                   20.43,
                                                   5]
                                                  ])

        self.categoriesListView.setModel(self.categoriesModel)
        self.categoriesListView.setItemDelegate(self.distributionDelegate)

        """ Configure layout """
        self.configureLayout()

        """ Configure status bar """
        self.configureStatusBar()

        """ Configure TitleBar """
        self.configureTitleBar()

        """ Connect all slots and signals """
        self.connectWidgets()

    def connectWidgets(self):
        """
        Connect all slots and signals
        :return: void
        """

        """ Connect click on button in title bar to change icon """
    #     self.uiSetup.monthlyExpenses.titleBarClicked.connect(self.changeSortIcon)
    #
    # def changeSortIcon(self):
    #     """
    #     Change sort icon
    #     :return: void
    #     """
    #



    def configureLayout(self):
        """
        Configure layout inside of Container
        :return: void
        """

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.categoriesListView)
        layout.addWidget(self.statusBar)
        layout.setContentsMargins(0, 10, 0, 0)

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

    def configureTitleBar(self):
        """
        Configure TitleBar with icon
        :return: void
        """

        self.uiSetup.monthlyExpenses.setIcon(QIcon(":/images/images/filter_list-white-24dp.svg"))

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
