from PySide2.QtWidgets import QWidget, QGridLayout

from widgets.saving_widgets.callout_widget import CalloutChartView


class SavingDashboard(QWidget):
    """
    Saving Dashboard
    """

    def __init__(self, parent=None):
        super(SavingDashboard, self).__init__(parent)

        """ Store values for months """
        self.values = [{"Janvier-2021": 12056,
                        "Février-2021": 13450.12,
                        "Mars-2021": 15469.35,
                        "Avril-2021": 14356.00,
                        "Mai-2021": 25098.63,
                        "Juin-2021": 26098.57,
                        "Juillet-2021": 22054.00,
                        "Août-2021": 22000.45,
                        "Septembre-2021": 29087.98,
                        "Octobre-2021": 25043.23,
                        "Novembre-2021": 25098.45,
                        "Décembre-2021": 28034.00}]

        """ Store chart view """
        self.chart_view = CalloutChartView()

        """ Store layout for dashboard widget """
        self._layout = QGridLayout(self)

        """ Configure widgets """
        self.configure_widgets()

    def configure_widgets(self):
        """
        Configure child widgets
        :return: void
        """

        """ Configure layout """
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self.chart_view)

        """ Configure chart """
        self.chart_view.set_values(self.values)

    def display_first_callout(self):
        """
        Disaply first callout after windows resized

        :return: void
        """

        self.chart_view.displ