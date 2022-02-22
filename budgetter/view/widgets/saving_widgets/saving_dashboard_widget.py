from datetime import datetime

from PySide2.QtCore import QDate
from PySide2.QtWidgets import QWidget, QGridLayout

from budgetter.view.widgets.saving_widgets.callout_widget import CalloutChartView


class SavingDashboard(QWidget):
    """
    Saving Dashboard
    """

    def __init__(self, parent=None):
        super(SavingDashboard, self).__init__(parent)

        """ Store values for months """
        self.values = dict()
        self.current_year_values = dict()
        self.previous_year_values = dict()

        """ Store chart view """
        self.chart_view = CalloutChartView()

        """ Store layout for dashboard widget """
        self._layout = QGridLayout(self)

        """ Configure widgets """
        self.configure_widgets()

    def configure_widgets(self):
        """
        Configure child widgets

        :return: None
        """

        """ Configure layout """
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self.chart_view)

    def set_values(self, values: dict):
        """
        Set values from DB

        :param values: (dict) values to set
        :return: None
        """

        ''' Clear previous data '''
        self.current_year_values.clear()
        self.previous_year_values.clear()

        ''' Order data by date '''
        self.values = sorted(values.items(), key=lambda x: datetime.strptime(x[0], '%m-%Y'), reverse=False)

        ''' Retrieve current year for parsing '''
        current_year = str(QDate.currentDate().year())

        for item in self.values:
            if current_year in item[0]:
                self.current_year_values[item[0]] = item[1]
            else:
                self.previous_year_values[item[0]] = item[1]

        ''' Set 12 last months '''
        self.set_last_months()

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

        values = dict()
        index = 0

        if len(self.current_year_values) < 12:
            ''' Reconstruct values '''
            for item in reversed(self.values):
                if index >= 12:
                    break

                values[item[0]] = item[1]
                index += 1
        else:
            values = self.current_year_values

        ''' Order values '''
        ordered_values = sorted(values.items(), key=lambda x: datetime.strptime(x[0], '%m-%Y'), reverse=False)

        ''' Display last 12 months values '''
        self.chart_view.set_values(dict(ordered_values))
