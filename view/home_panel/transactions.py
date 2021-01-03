from PySide2.QtCore import QObject, Qt, QDate
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QStatusBar, QWidget, QPushButton, QListView, QSpacerItem, QSizePolicy

from models.transactions_model import TransactionsModel
from widgets.statusbar import StatusBar
from widgets.transactionDelegate import TransactionDelegate


class Transactions(QObject):
    """
    Transactions
    """

    def __init__(self, gui):
        super(Transactions, self).__init__()

        """ Store gui """
        self.uiSetup = gui

        """ Store custom/classic status bar """
        self.customStatusBar = StatusBar()
        self.statusBar = QStatusBar()

        """ All button """
        self.all = QPushButton("All")

        """ Expenses button """
        self.expenses = QPushButton("Expenses")

        """ Incomes button """
        self.income = QPushButton("Income")

        """ Store item delegate """
        self.transactionDelegate = TransactionDelegate()

        """ ListView to display all transactions """
        self.transactionsListView = QListView()

        """ Model to handle data in transactions list """
        self.transactionsModel = TransactionsModel([["Flunch",
                                                     "Restaurants",
                                                     25.99,
                                                     "20/02/2020",
                                                     "Compte Chèque",
                                                     "Income"],
                                                    ["Gasoil",
                                                     "Transport",
                                                     40.01,
                                                     "12/05/2020",
                                                     "Livret A",
                                                     "Expenses"],
                                                    ["Computer",
                                                     "Groceries",
                                                     900.99,
                                                     "24/05/2020",
                                                     "Livret Jeune",
                                                     "Expenses"]])

        self.transactionsListView.setModel(self.transactionsModel)
        self.transactionsListView.setItemDelegate(self.transactionDelegate)
        self.transactionsListView.viewport().setAttribute(Qt.WA_Hover, False)
        self.transactionsListView.setMouseTracking(True)

        """ Configure layout """
        self.configureLayout()

        """ Configure status bar """
        self.configureStatusBar()

        """ Configure TitleBar """
        self.configureTitleBar()

    def configureLayout(self):
        """
        Configure layout inside of Container
        :return: void
        """

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.transactionsListView)
        layout.addWidget(self.statusBar)
        layout.setContentsMargins(0, 10, 0, 0)

        self.uiSetup.transactions.setWidget(widget)

    def configureStatusBar(self):
        """
        Configure status bar
        :return: void
        """

        """ Set states for activation """
        self.all.setProperty("activated", "true")
        self.all.update()
        self.expenses.setProperty("activated", "false")
        self.expenses.update()
        self.income.setProperty("activated", "false")
        self.income.update()

        """ Set cursor for left buttons """
        self.all.setCursor(Qt.PointingHandCursor)
        self.expenses.setCursor(Qt.PointingHandCursor)
        self.income.setCursor(Qt.PointingHandCursor)

        """ Add custom status bar to classic one """
        self.statusBar.addPermanentWidget(self.customStatusBar)

        """ Add buttons on left corner """
        self.statusBar.addWidget(self.all)
        self.statusBar.addWidget(self.expenses)
        self.statusBar.addWidget(self.income)

        """ Disable size grip """
        self.statusBar.setSizeGripEnabled(False)

        """ Hide settings """
        self.customStatusBar.hideSettings()

        """ Hide choices """
        self.customStatusBar.hideChoices()

    def configureTitleBar(self):
        """
        Configure TitleBar with icon
        :return: void
        """

        """ Set title """
        self.uiSetup.transactions.setTitle("Transactions")
        # self.uiSetup.monthlyExpenses.disableTitleBarButton()
