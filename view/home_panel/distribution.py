from PySide2.QtCore import QObject, Qt, QDate, QCoreApplication, QLocale
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QStatusBar, QWidget, QPushButton, QListView, QSpacerItem, QSizePolicy

from models.distribution_model import DistributionModel
from widgets.distribution_delegate import DistributionDelegate
from widgets.status_bar import StatusBar


class Distribution(QObject):
    """
    Distribution
    """

    def __init__(self, gui):
        super(Distribution, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ Store custom/classic status bar """
        self.custom_status_bar = StatusBar()
        self.status_bar = QStatusBar()

        """ Current Month button """
        self.current_month = QPushButton(QCoreApplication.translate("distribution", "September"))

        """ Previous Month button """
        self.previous_month = QPushButton(QCoreApplication.translate("distribution", "August"))

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

        :return: None
        """

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.categories_listview)
        layout.addWidget(self.status_bar)
        layout.setContentsMargins(0, 10, 0, 0)

        self.ui_setup.monthlyExpenses.setWidget(widget)

    def configure_status_bar(self):
        """
        Configure status bar

        :return: None
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
        self.custom_status_bar.hide_settings()

    def configure_title_bar(self):
        """
        Configure TitleBar with icon

        :return: None
        """

        """ Set title """
        self.ui_setup.monthlyExpenses.set_title(QCoreApplication.translate("savings", "Expenses Distribution"))

        """ Hide all widgets in title bar """
        self.ui_setup.monthlyExpenses.disable_title_bar_button()
        self.ui_setup.monthlyExpenses.disable_search_bar()

    def set_current_and_previous_month(self):
        """
        Get current/previous month from locale and update display

        :return: None
        """

        current_month = QLocale().toString(QDate.currentDate(), 'MMMM')
        self.current_month.setText(current_month.capitalize())

        if current_month_nb == 1:
            current_month_nb = 13
        previous_month = QDate.currentDate().longMonthName(current_month_nb - 1)
        self.previous_month.setText(previous_month.capitalize())
