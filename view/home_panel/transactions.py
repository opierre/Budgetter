from PySide2.QtCore import QObject, Qt, QDate, QFile, QRect, QSize
from PySide2.QtGui import QIcon, QRegion, QPixmap, QPainter, QBrush
from PySide2.QtWidgets import QVBoxLayout, QStatusBar, QWidget, QPushButton, QListView, QSpacerItem, QSizePolicy, QMenu, \
    QApplication

from models.transactions_model import TransactionsModel
from widgets.statusbar import StatusBar
from widgets.transactionDelegate import TransactionDelegate


class Transactions(QObject):
    """
    Transactions
    """

    def __init__(self, gui, parent):
        super(Transactions, self).__init__()

        """ Store gui and main window """
        self.uiSetup = gui
        self.mainWindow = parent

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

        """ Configure layout """
        self.configureLayout()

        """ Configure status bar """
        self.configureStatusBar()

        """ Configure List view """
        self.configureListView()

        """ Configure TitleBar """
        self.configureTitleBar()

        """ Connect all widgets """
        self.connectWidgets()

    def connectWidgets(self):
        """
        Connect all slots and signals
        :return: void
        """

        """ Connect signal from More button in list view to opening context menu """
        self.transactionDelegate.transactionMorePressed.connect(self.openContextMenu)

    def openContextMenu(self, index, position):
        """
        Open context menu on More click
        :param index: index in model
        :param position: position to open context menu
        :return: void
        """

        """ Add actions to QMenu """
        menu = QMenu(self.mainWindow)
        editAction = menu.addAction("Edit  ")
        editAction.setIcon(QIcon(":/images/images/edit-white-18dp.svg"))
        deleteAction = menu.addAction("Delete  ")
        deleteAction.setIcon(QIcon(":/images/images/delete-white-18dp.svg"))

        """ Set translucent background """
        menu.setWindowFlags(menu.windowFlags() | Qt.FramelessWindowHint)
        menu.setAttribute(Qt.WA_TranslucentBackground)

        """ Show menu with hand pointing cursor """
        menu.setCursor(Qt.PointingHandCursor)
        action = menu.exec_(self.transactionsListView.mapToGlobal(position))

        """ Deal with click """
        if action == editAction:
            print('edit')
        if action == deleteAction:
            """ Remove transaction from model """
            self.transactionsModel.deleteTransaction(index)

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

    def configureListView(self):
        """
        Configure transactions list view to handle events/model
        :return: void
        """

        """ Set model """
        self.transactionsListView.setModel(self.transactionsModel)

        """ Set mouse tracking """
        self.transactionsListView.setMouseTracking(True)

        """ Set item delegate"""
        self.transactionsListView.setItemDelegate(self.transactionDelegate)

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
