from PySide6.QtCore import QObject, Qt, QDate, QCoreApplication
from PySide6.QtWidgets import QWidget, QVBoxLayout, QStatusBar, \
    QPushButton

from budgetter.view.widgets.saving_widgets.saving_dashboard_widget import SavingDashboard
from budgetter.view.widgets.status_bar import StatusBar


class Savings(QObject):
    """
    Savings
    """

    def __init__(self, gui):
        super().__init__()

        # Store gui
        self.ui_setup = gui

        # Store custom/classic status bar
        self.custom_status_bar = StatusBar()
        self.status_bar = QStatusBar()

        # Last 12 months button
        self.last_twelve_months = QPushButton(QCoreApplication.translate("savings", "Last 12 months"))

        # Current Year button
        self.current_year = QPushButton("")

        # Previous Year button
        self.previous_year = QPushButton("")

        # Chart widget
        self.chart_widget = SavingDashboard(self.ui_setup.savings)

        # Configure layout
        self.configure_layout()

        # Connect all slots and signals
        self.connect_slots_and_signals()

        # Configure title bar
        self.configure_title_bar()

        # Configure status bar
        self.configure_status_bar()

        # Configure chart
        self.configure_chart()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect click on buttons to display new values
        self.last_twelve_months.clicked.connect(self.display_values)  # pylint: disable=no-member
        self.current_year.clicked.connect(self.display_values)  # pylint: disable=no-member
        self.previous_year.clicked.connect(self.display_values)  # pylint: disable=no-member

        # Connect click on previous/next from status bar to move point
        self.custom_status_bar.nextClicked.connect(self.chart_widget.chart_view.chart.show_next)
        self.custom_status_bar.previousClicked.connect(self.chart_widget.chart_view.chart.show_previous)

        # Connect legend signal to display legend
        self.chart_widget.legendSaving.connect(self.update_legend)

    def configure_chart(self):
        """
        Initialize data for chart

        :return: None
        """

        values = {"01-2020": 4235.23,
                  "02-2020": 4565.23,
                  "03-2020": 5454.34,
                  "04-2020": 5674.76,
                  "05-2020": 7345.87,
                  "06-2020": 8340.89,
                  "07-2020": 8957.54,
                  "08-2020": 11100.34,
                  "09-2020": 11550.12,
                  "10-2020": 11567.87,
                  "11-2020": 11978.78,
                  "12-2020": 12010.98,
                  "01-2021": 12056,
                  "02-2021": 13450.12,
                  "03-2021": 15469.35,
                  "04-2021": 14356.00,
                  "05-2021": 25098.63,
                  "06-2021": 26098.57,
                  "07-2021": 22054.00,
                  "08-2021": 22000.45}

        self.chart_widget.set_values(values)

    def display_values(self):
        """
        Display values according to clicked button

        :return: None
        """

        sender = self.sender()

        if sender == self.current_year:
            # Update stylesheet
            self.current_year.setProperty("activated", "true")
            self.last_twelve_months.setProperty("activated", "false")
            self.previous_year.setProperty("activated", "false")

            # Update values to display
            self.chart_widget.set_current_year_values(True)
        elif sender == self.last_twelve_months:
            # Update stylesheet
            self.current_year.setProperty("activated", "false")
            self.last_twelve_months.setProperty("activated", "true")
            self.previous_year.setProperty("activated", "false")

            # Update values to display
            self.chart_widget.set_last_months()
        else:
            # Update stylesheet
            self.current_year.setProperty("activated", "false")
            self.last_twelve_months.setProperty("activated", "false")
            self.previous_year.setProperty("activated", "true")

            # Update values to display
            self.chart_widget.set_current_year_values(False)

        # Update display style
        self.current_year.style().unpolish(self.current_year)
        self.current_year.style().polish(self.current_year)
        self.previous_year.style().unpolish(self.previous_year)
        self.previous_year.style().polish(self.previous_year)
        self.last_twelve_months.style().unpolish(self.last_twelve_months)
        self.last_twelve_months.style().polish(self.last_twelve_months)

    def configure_title_bar(self):
        """
        Configure TitleBar with icon

        :return: None
        """

        # Set title
        self.ui_setup.savings.set_title(QCoreApplication.translate("savings", "Savings"))

        # Hide all widgets in title bar
        self.ui_setup.savings.disable_title_bar_button()
        self.ui_setup.savings.disable_search_bar()

    def configure_status_bar(self):
        """
        Configure status bar

        :return: None
        """

        # Set month content
        self.set_current_and_previous_year()

        # Set states for activation
        self.current_year.setProperty("activated", "false")
        self.current_year.update()
        self.previous_year.setProperty("activated", "false")
        self.previous_year.update()
        self.last_twelve_months.setProperty("activated", "true")
        self.last_twelve_months.update()

        # Set cursor for left buttons
        self.current_year.setCursor(Qt.CursorShape.PointingHandCursor)
        self.previous_year.setCursor(Qt.CursorShape.PointingHandCursor)
        self.last_twelve_months.setCursor(Qt.CursorShape.PointingHandCursor)

        # Show next and previous arrows
        self.custom_status_bar.show_previous_next()

        # Add custom status bar to classic one
        self.status_bar.addPermanentWidget(self.custom_status_bar)

        # Add buttons on left corner
        self.status_bar.addWidget(self.last_twelve_months)
        self.status_bar.addWidget(self.current_year)
        self.status_bar.addWidget(self.previous_year)

        # Disable size grip
        self.status_bar.setSizeGripEnabled(False)

        # Hide settings
        self.custom_status_bar.hide_settings()

    def set_current_and_previous_year(self):
        """
        Get current/previous year from locale and update display

        :return: None
        """

        current_year = QDate.currentDate().year()
        self.current_year.setText(str(current_year))
        self.previous_year.setText(str(current_year - 1))

    def configure_layout(self):
        """
        Configure layout inside of Container

        :return: None
        """

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(0)
        layout.addWidget(self.chart_widget)
        layout.addWidget(self.status_bar)
        layout.setContentsMargins(0, 0, 0, 0)

        self.ui_setup.savings.setWidget(widget)

    def update_legend(self, month: str, amount: str):
        """
        Update saving legend

        :param month: month
        :param amount: amount
        :return: None
        """

        # Update title bar info
        self.ui_setup.savings.set_info(f"{month} / {amount}")
