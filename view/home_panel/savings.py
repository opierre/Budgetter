from PySide2.QtCore import QObject, Qt, QDate
from PySide2.QtWidgets import QWidget, QVBoxLayout, QStatusBar, \
    QPushButton

from widgets.saving_widgets.saving_dashboard_widget import SavingDashboard
from widgets.statusbar import StatusBar


class Savings(QObject):
    """
    Savings
    """

    def __init__(self, gui):
        super(Savings, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ Store custom/classic status bar """
        self.custom_status_bar = StatusBar()
        self.status_bar = QStatusBar()

        """ Current Year button """
        self.current_year = QPushButton("")

        """ Previous Year button """
        self.previous_year = QPushButton("")

        """ Chart widget """
        self.chart_widget = SavingDashboard(self.ui_setup.savings)

        """ Configure layout """
        self.configure_layout()

        """ Configure title bar """
        self.configure_title_bar()

        """ Configure status bar """
        self.configure_status_bar()

        """ Connect Account groupBox """
        # self.connectAccounts()

    def configure_title_bar(self):
        """
        Configure TitleBar with icon
        :return: void
        """

        """ Set title """
        self.ui_setup.savings.set_title("Savings")

        """ Hide all widgets in title bar """
        self.ui_setup.savings.disable_title_bar_button()
        self.ui_setup.savings.disable_search_bar()

    def configure_status_bar(self):
        """
        Configure status bar
        :return: void
        """

        """ Set month content """
        self.set_current_and_previous_year()

        """ Set states for activation """
        self.current_year.setProperty("activated", "true")
        self.current_year.update()
        self.previous_year.setProperty("activated", "false")
        self.previous_year.update()

        """ Set cursor for left buttons """
        self.current_year.setCursor(Qt.PointingHandCursor)
        self.previous_year.setCursor(Qt.PointingHandCursor)

        """ Add custom status bar to classic one """
        self.status_bar.addPermanentWidget(self.custom_status_bar)

        """ Add buttons on left corner """
        self.status_bar.addWidget(self.current_year)
        self.status_bar.addWidget(self.previous_year)

        """ Disable size grip """
        self.status_bar.setSizeGripEnabled(False)

        """ Hide settings """
        self.custom_status_bar.hideSettings()

    def set_current_and_previous_year(self):
        """
        Get current/previous year from locale and update display
        :return: void
        """

        current_year = QDate.currentDate().year()
        self.current_year.setText(str(current_year))
        self.previous_year.setText(str(current_year - 1))

    def configure_layout(self):
        """
        Configure layout inside of Container
        :return: void
        """

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(0)
        layout.addWidget(self.chart_widget)
        layout.addWidget(self.status_bar)
        layout.setContentsMargins(0, 20, 0, 0)

        self.ui_setup.savings.setWidget(widget)

