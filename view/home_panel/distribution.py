from PySide2.QtCore import QObject, Qt, QDate
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QStatusBar, QWidget, QPushButton, QListView, QSpacerItem, QSizePolicy

from models.distribution_model import DistributionModel
from widgets.distribution_delegate import DistributionDelegate
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
        self.custom_status_bar = StatusBar()
        self.status_bar = QStatusBar()

        """ Current Month button """
        self.current_month = QPushButton("September")

        """ Previous Month button """
        self.previous_month = QPushButton("August")

        """ Store item delegate """
        self.distribution_delegate = DistributionDelegate()

        """ ListView to display all categories """
        self.categories_listview = QListView()

        """ Model to handle data in distribution list """
        self.categories_model = DistributionModel([["Restaurants",
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

        self.categories_listview.setModel(self.categories_model)
        self.categories_listview.setItemDelegate(self.distribution_delegate)

        """ Configure status bar """
        self.configure_status_bar()

        """ Configure layout """
        self.configure_layout()

        """ Configure TitleBar """
        self.configure_title_bar()

    def configure_layout(self):
        """
        Configure layout inside of Container
        :return: void
        """

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.categories_listview)
        layout.addWidget(self.status_bar)
        layout.setContentsMargins(0, 10, 0, 0)

        self.uiSetup.monthlyExpenses.setWidget(widget)

    def configure_status_bar(self):
        """
        Configure status bar
        :return: void
        """

        """ Set month content """
        self.set_current_and_previous_month()

        """ Set states for activation """
        self.current_month.setProperty("activated", "true")
        self.current_month.update()
        self.previous_month.setProperty("activated", "false")
        self.previous_month.update()

        """ Set cursor for left buttons """
        self.current_month.setCursor(Qt.PointingHandCursor)
        self.previous_month.setCursor(Qt.PointingHandCursor)

        """ Add custom status bar to classic one """
        self.status_bar.addPermanentWidget(self.custom_status_bar)

        """ Add buttons on left corner """
        self.status_bar.addWidget(self.current_month)
        self.status_bar.addWidget(self.previous_month)

        """ Disable size grip """
        self.status_bar.setSizeGripEnabled(False)

        """ Hide settings """
        self.custom_status_bar.hideSettings()

    def configure_title_bar(self):
        """
        Configure TitleBar with icon
        :return: void
        """

        """ Hide all widgets in title bar """
        self.uiSetup.monthlyExpenses.disable_title_bar_button()
        self.uiSetup.monthlyExpenses.disable_search_bar()

    def set_current_and_previous_month(self):
        """
        Get current/previous month from locale and update display
        :return: void
        """

        current_month_nb = QDate.currentDate().month()
        current_month = QDate.currentDate().longMonthName(current_month_nb)
        self.current_month.setText(current_month.capitalize())

        if current_month_nb == 1:
            current_month_nb = 13
        previous_month = QDate.currentDate().longMonthName(current_month_nb - 1)
        self.previous_month.setText(previous_month.capitalize())
