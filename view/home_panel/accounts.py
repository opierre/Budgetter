from PySide2.QtCore import QObject, Qt
from PySide2.QtGui import QPainter, QFont
from PySide2.QtWidgets import QSpacerItem, QSizePolicy, QListView, QWidget, QVBoxLayout, QHBoxLayout

from models.accounts_model import AccountsModel
from widgets.balance_widgets.account_delegate import AccountDelegate
from widgets.balance_widgets.donut_chat_widget import DonutChart


class Accounts(QObject):
    """
    Accounts
    """

    def __init__(self, gui):
        super(Accounts, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ Store item delegate """
        self.account_delegate = AccountDelegate()

        """ ListView to display all accounts """
        self.accounts_list = QListView()

        """ Model to handle data in accounts list """
        self.accounts_model = AccountsModel([["Caisse d'Epargne",
                                              "Compte Chèque",
                                              1056.53,
                                              "UP",
                                              "#1CA9E9"],
                                             ["Crédit Agricole",
                                              "Livret A",
                                              12050.1,
                                              "DOWN",
                                              "#0154C8"],
                                             ["Caisse d'Epargne",
                                              "Compte Courant",
                                              47.93,
                                              "STILL",
                                              "#26C1C9"]
                                             ])

        self.accounts_list.setModel(self.accounts_model)
        self.accounts_list.setItemDelegate(self.account_delegate)

        """ DonutChart to display balance distribution """
        self.balance_chart = DonutChart()
        self.balance_chart.add_slice(39)
        self.balance_chart.add_slice(21)
        self.balance_chart.add_slice(40)
        self.balance_chart.set_total_amount(15307.8)

        """ Configure layout """
        self.configure_layout()

        """ Configure title bar """
        self.configure_title_bar()

        """ Connect Account groupBox """
        # self.connectAccounts()

    def configure_title_bar(self):
        """
        Configure TitleBar with icon
        :return: None
        """

        """ Set title """
        self.ui_setup.accounts.set_title("Balance")

        """ Hide all widgets in title bar """
        self.ui_setup.accounts.disable_title_bar_button()
        self.ui_setup.accounts.disable_search_bar()

    def configure_layout(self):
        """
        Configure layout inside of Container
        :return: None
        """

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setSpacing(30)
        layout.addWidget(self.balance_chart)
        self.accounts_list.setViewportMargins(0, 10, 0, 10)
        layout.addWidget(self.accounts_list)
        layout.setContentsMargins(20, 10, 10, 10)

        self.ui_setup.accounts.setWidget(widget)
