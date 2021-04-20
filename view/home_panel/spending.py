from PySide2.QtCore import QObject, Qt
from PySide2.QtGui import QPainter, QFont
from PySide2.QtWidgets import QSpacerItem, QSizePolicy, QListView, QWidget, QVBoxLayout, QHBoxLayout

from models.accounts_model import AccountsModel
from widgets.balance_widgets.account_delegate import AccountDelegate
from widgets.balance_widgets.donut_chat_widget import DonutChart
from widgets.spending_widgets.chart_dashboard_widget import ChartDashboard


class Spending(QObject):
    """
    AccSpendingounts
    """

    def __init__(self, gui):
        super(Spending, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ Chart widget """
        self.chart_widget = ChartDashboard()

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
        self.ui_setup.spending.set_title("Spending")

        """ Hide all widgets in title bar """
        self.ui_setup.spending.disable_title_bar_button()
        self.ui_setup.spending.disable_search_bar()

    def configure_layout(self):
        """
        Configure layout inside of Container
        :return: void
        """

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setSpacing(0)
        layout.addWidget(self.chart_widget)
        layout.setContentsMargins(20, 20, 20, 20)

        self.ui_setup.spending.setWidget(widget)
