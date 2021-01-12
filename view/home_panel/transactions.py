from PySide2.QtCore import QObject, Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QStatusBar, QWidget, QPushButton, QListView, QMenu, QFrame

from models.transactions_model import TransactionsModel, TransactionsFilterModel
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

        """ All button - Type """
        self.all = QPushButton("All")

        """ Expenses button - Type """
        self.expenses = QPushButton("Expenses")

        """ Incomes button - Type """
        self.income = QPushButton("Income")

        """ All button - Account """
        self.allAccount = QPushButton("All")

        """ Account 1 button - Account """
        self.account1 = QPushButton("Livret A")

        """ Account 2 button - Account """
        self.account2 = QPushButton("Compte Chèque")

        """ Account 3 button - Account """
        self.account3 = QPushButton("Livret Jeune")

        """ Store item delegate """
        self.transactionDelegate = TransactionDelegate()

        """ ListView to display all transactions """
        self.transactionsListView = QListView()

        """ Model for filtering """
        self.transactionsFilterModel = TransactionsFilterModel()

        """ Model to handle data in transactions list """
        self.transactionsModel = TransactionsModel([["Flunch",
                                                     "Restaurants",
                                                     25.99,
                                                     "20/02/2020",
                                                     "Compte Chèque",
                                                     "Income",
                                                     False],
                                                    ["Gasoil",
                                                     "Transport",
                                                     40.01,
                                                     "12/05/2020",
                                                     "Livret A",
                                                     "Expenses",
                                                     False],
                                                    ["Computer",
                                                     "Groceries",
                                                     900.99,
                                                     "24/05/2020",
                                                     "Livret Jeune",
                                                     "Expenses",
                                                     False]])

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

        """ Update filtering when click on button in status bar """
        self.expenses.clicked.connect(self.updateCurrentFiltering)
        self.income.clicked.connect(self.updateCurrentFiltering)
        self.all.clicked.connect(self.updateCurrentFiltering)

        """ Update filtering when click on button in status bar """
        self.allAccount.clicked.connect(self.addFilter)
        self.account1.clicked.connect(self.addFilter)
        self.account2.clicked.connect(self.addFilter)
        self.account3.clicked.connect(self.addFilter)

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
            self.transactionsFilterModel.editTransaction(index)
        if action == deleteAction:
            """ Remove transaction from model """
            self.transactionsFilterModel.deleteTransaction(index)

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

        """ Set proxy model """
        self.transactionsFilterModel.setSourceModel(self.transactionsModel)

        """ Date re-filtered if model changed """
        self.transactionsFilterModel.setDynamicSortFilter(True)

        """ Set model """
        self.transactionsListView.setModel(self.transactionsFilterModel)

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

        """ Set states for activation """
        self.allAccount.setProperty("activated", "true")
        self.allAccount.update()
        self.account1.setProperty("activated", "false")
        self.account1.update()
        self.account2.setProperty("activated", "false")
        self.account2.update()
        self.account3.setProperty("activated", "false")
        self.account3.update()

        """ Set cursor for left buttons """
        self.all.setCursor(Qt.PointingHandCursor)
        self.expenses.setCursor(Qt.PointingHandCursor)
        self.income.setCursor(Qt.PointingHandCursor)

        """ Set cursor for left buttons """
        self.allAccount.setCursor(Qt.PointingHandCursor)
        self.account1.setCursor(Qt.PointingHandCursor)
        self.account2.setCursor(Qt.PointingHandCursor)
        self.account3.setCursor(Qt.PointingHandCursor)

        """ Add custom status bar to classic one """
        self.statusBar.addPermanentWidget(self.customStatusBar)

        """ Add buttons on left corner """
        self.statusBar.addWidget(self.all)
        self.statusBar.addWidget(self.expenses)
        self.statusBar.addWidget(self.income)

        """ Add separator """
        vline = QFrame()
        vline.setFrameShape(vline.VLine)
        vline.setFixedHeight(self.all.sizeHint().height() * 1.2)
        vline.setStyleSheet("color: #344457;")
        self.statusBar.addWidget(vline)

        """ Add buttons on left corner """
        self.statusBar.addWidget(self.allAccount)
        self.statusBar.addWidget(self.account1)
        self.statusBar.addWidget(self.account2)
        self.statusBar.addWidget(self.account3)

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

    def updateCurrentFiltering(self):
        """
        Update current filtering after click on button
        :return: void
        """

        """ Retrieve sender """
        pyObject = self.sender()

        """ Retrieve current text """
        newFilter = pyObject.text()

        """ Update filter """
        self.transactionsFilterModel.updateFilter(newFilter)

        """ Update activated state """
        if newFilter == 'All':
            self.all.setProperty("activated", "true")
            self.expenses.setProperty("activated", "false")
            self.income.setProperty("activated", "false")
        elif newFilter == 'Expenses':
            self.all.setProperty("activated", "false")
            self.expenses.setProperty("activated", "true")
            self.income.setProperty("activated", "false")
        else:
            self.all.setProperty("activated", "false")
            self.expenses.setProperty("activated", "false")
            self.income.setProperty("activated", "true")

        """ Update style """
        self.all.style().unpolish(self.all)
        self.all.style().polish(self.all)
        self.expenses.style().unpolish(self.expenses)
        self.expenses.style().polish(self.expenses)
        self.income.style().unpolish(self.income)
        self.income.style().polish(self.income)

    def addFilter(self):
        """
        Add filter to current filtering after click on button
        :return: void
        """

        """ Retrieve sender """
        pyObject = self.sender()

        """ Retrieve current text """
        newFilter = pyObject.text()

        """ Add filter """
        self.transactionsFilterModel.addFilter(newFilter)

        """ Update activated state """
        if newFilter == 'All':
            self.allAccount.setProperty("activated", "true")
            self.account1.setProperty("activated", "false")
            self.account2.setProperty("activated", "false")
            self.account3.setProperty("activated", "false")
        elif newFilter == self.account1.text():
            self.allAccount.setProperty("activated", "false")
            self.account1.setProperty("activated", "true")
            self.account2.setProperty("activated", "false")
            self.account3.setProperty("activated", "false")
        elif newFilter == self.account2.text():
            self.allAccount.setProperty("activated", "false")
            self.account1.setProperty("activated", "false")
            self.account2.setProperty("activated", "true")
            self.account3.setProperty("activated", "false")
        elif newFilter == self.account3.text():
            self.allAccount.setProperty("activated", "false")
            self.account1.setProperty("activated", "false")
            self.account2.setProperty("activated", "false")
            self.account3.setProperty("activated", "true")

        """ Update style """
        self.allAccount.style().unpolish(self.allAccount)
        self.allAccount.style().polish(self.allAccount)
        self.account1.style().unpolish(self.account1)
        self.account1.style().polish(self.account1)
        self.account2.style().unpolish(self.account2)
        self.account2.style().polish(self.account2)
        self.account3.style().unpolish(self.account3)
        self.account3.style().polish(self.account3)
