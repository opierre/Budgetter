from PySide2.QtCore import QObject, Qt
from PySide2.QtGui import QPainter, QFont
from PySide2.QtWidgets import QSpacerItem, QSizePolicy, QListView, QWidget, QVBoxLayout, QHBoxLayout
from PySide2.QtCharts import QtCharts

from widgets.balance_widgets.donut_chat_widget import DonutChart
from widgets.card import Card


class Accounts(QObject):
    """
    Accounts
    """

    def __init__(self, gui):
        super(Accounts, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ ListView to display all accounts """
        self.accounts_listview = QListView()

        """ DonutChart to display balance distribution """
        self.balance_chart = DonutChart()
        self.balance_chart.add_slice(23)
        self.balance_chart.add_slice(27)
        self.balance_chart.add_slice(10)
        self.balance_chart.add_slice(39)

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
        self.ui_setup.accounts.set_title("Balance")

        """ Hide all widgets in title bar """
        self.ui_setup.accounts.disable_title_bar_button()
        self.ui_setup.accounts.disable_search_bar()

    def configure_layout(self):
        """
        Configure layout inside of Container
        :return: void
        """

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(self.balance_chart)
        layout.addWidget(self.accounts_listview)
        layout.setContentsMargins(30, 0, 0, 0)

        self.ui_setup.accounts.setWidget(widget)
