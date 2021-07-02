from PySide2.QtCore import QObject, Qt, QMargins
from PySide2.QtGui import QPainter, QFont
from PySide2.QtWidgets import QSpacerItem, QSizePolicy, QListView, QWidget, QVBoxLayout, QHBoxLayout

from models.accounts_model import AccountsModel
from widgets.balance_widgets.account_delegate import AccountDelegate
from widgets.balance_widgets.donut_chat_widget import DonutChart
from widgets.saving_widgets.saving_dashboard_widget import SavingDashboard
from widgets.spending_widgets.chart_dashboard_widget import ChartDashboard


class Savings(QObject):
    """
    Savings
    """

    def __init__(self, gui):
        super(Savings, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ Chart widget """
        self.chart_widget = SavingDashboard(self.ui_setup.savings)

        """ Configure layout """
        self.configure_layout()

        """ Configure title bar """
        self.configure_title_bar()

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

    def configure_layout(self):
        """
        Configure layout inside of Container
        :return: void
        """

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setSpacing(0)
        layout.addWidget(self.chart_widget)
        layout.setContentsMargins(0, 20, 0, 0)

        self.ui_setup.savings.setWidget(widget)

