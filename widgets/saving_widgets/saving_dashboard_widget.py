from PySide2.QtCore import QDate
from PySide2.QtWidgets import QWidget, QGridLayout

from widgets.saving_widgets.callout_widget import CalloutChartView


class SavingDashboard(QWidget):
    """
    Saving Dashboard
    """

    def __init__(self, parent=None):
        super(SavingDashboard, self).__init__(parent)

        """ Store values for months """
        self.values = {"Janvier-2021": 12056,
                       "Février-2021": 13450.12,
                       "Mars-2021": 15469.35,
                       "Avril-2021": 14356.00,
                       "Mai-2021": 25098.63,
                       "Juin-2021": 26098.57,
                       "Juillet-2021": 22054.00,
                       "Août-2021": 22000.45,
                       "Janvier-2020": 4235.23,
                       "Février-2020": 4565.23,
                       "Mars-2020": 5454.34,
                       "Avril-2020": 5674.76,
                       "Mai-2020": 7345.87,
                       "Juin-2020": 8340.89,
                       "Juillet-2020": 8957.54,
                       "Août-2020": 11100.34,
                       "Septembre-2020": 11550.12,
                       "Octobre-2020": 11567.87,
                       "Novembre-2020": 11978.78,
                       "Décembre-2020": 12010.98}

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

        """ Configure chart """
        self.set_current_year_values(True)

    def set_current_year_values(self, boolean):
        """
        Display current year values if True, previous year values otherwise

        :param boolean: True/False
        :return: None
        """

        values = dict()

        if boolean:
            ''' Retrieve current year for parsing '''
            year = str(QDate.currentDate().year())

        else:
            ''' Retrieve previous year for parsing '''
            year = str(QDate.currentDate().year() - 1)

        for key, item in self.values.items():
            if year in key:
                values[key] = item
        self.chart_view.set_values(values)

    def set_last_months(self):
        """
        Display values for the last 12 months

        :return: None
        """

        values = dict()

        ''' Reconstrcut values '''
        for key, item in self.values.items():
            if len(values) != 12:
                values[key] = item
            else:
                break

        self.chart_view.set_values(values)
