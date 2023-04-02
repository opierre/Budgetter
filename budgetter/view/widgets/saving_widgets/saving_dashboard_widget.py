from datetime import datetime

from PySide6.QtCore import QDate, Signal
from PySide6.QtWidgets import QWidget, QGridLayout

from budgetter.view.widgets.saving_widgets.chart_view import ChartView


class SavingDashboard(QWidget):
    """
    Saving Dashboard
    """

    # Signals
    legendSaving = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store values for months
        self.values = {}
        self.current_year_values = {}
        self.previous_year_values = {}

        # Store chart view """
        self.chart_view = ChartView()

        # Store layout for dashboard widget """
        self._layout = QGridLayout(self)

        # Configure widgets """
        self.configure_widgets()

        # Connect signal
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals from chart widget

        :return: None
        """

        # Connect legend signal to update legend in title bar
        self.chart_view.legend.connect(self.legendSaving.emit)

    def configure_widgets(self):
        """
        Configure child widgets

        :return: None
        """

        # Configure layout """
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self.chart_view)

    def set_values(self, values: dict):
        """
        Set values from DB

        :param values: (dict) values to set
        :return: None
        """

        # Clear previous data
        self.current_year_values.clear()
        self.previous_year_values.clear()

        # Order data by date
        self.values = sorted(
            values.items(),
            key=lambda x: datetime.strptime(x[0], "%m-%Y"),
            reverse=False,
        )

        # Retrieve current year for parsing
        current_year = str(QDate.currentDate().year())

        for item in self.values:
            if current_year in item[0]:
                self.current_year_values[item[0]] = item[1]
            else:
                self.previous_year_values[item[0]] = item[1]

        # Set 12 last months
        self.set_last_months()

        # Set legend
        self.chart_view.show_legend(self.chart_view.chart.get_middle_value())

    def set_current_year_values(self, boolean: bool):
        """
        Display current year values if True, previous year values otherwise

        :param boolean: (bool)
        :return: None
        """

        if boolean:
            self.chart_view.set_values(self.current_year_values)
        else:
            self.chart_view.set_values(self.previous_year_values)

    def set_last_months(self):
        """
        Display values for the last 12 months

        :return: None
        """

        values = {}
        index = 0

        if len(self.current_year_values) < 12:
            # Reconstruct values
            for item in reversed(self.values):
                if index >= 12:
                    break

                values[item[0]] = item[1]
                index += 1
        else:
            values = self.current_year_values

        # Order values
        ordered_values = sorted(
            values.items(),
            key=lambda x: datetime.strptime(x[0], "%m-%Y"),
            reverse=False,
        )

        # Display last 12 months values
        self.chart_view.set_values(dict(ordered_values))
