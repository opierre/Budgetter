from PySide2.QtCore import QObject, Qt, QDate, QRect
from PySide2.QtGui import QIcon, QFont, QFontMetrics
from PySide2.QtWidgets import QVBoxLayout, QStatusBar, QWidget, QPushButton, QListView, QMenu, QFrame, QLineEdit, \
    QInputDialog, QDoubleSpinBox, QDateEdit, QAbstractItemView, QComboBox

from models.transactions_model import TransactionsModel, TransactionsFilterModel
from widgets.calendar_widget import CalendarWidget
from widgets.expense_income_widget import ExpensesOrIncome
from widgets.statusbar import StatusBar
from widgets.transaction_delegate import TransactionDelegate


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

        """ Store LineEdit for name edition on transaction """
        self.editName = QLineEdit(self.transactionsListView)

        """ Store DoubleSpinBox for amount edition on transaction """
        self.editAmount = QDoubleSpinBox(self.transactionsListView)

        """ Store DateEdit for date edition on transaction """
        self.editDate = QDateEdit(self.transactionsListView)

        """ Store Combobox for account selection on transaction """
        self.editAccount = QComboBox(self.transactionsListView)

        """ Store Combobox for type expense selection on transaction """
        self.editExpOrInc = ExpensesOrIncome(self.transactionsListView)

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

        """ Configure edit widgets """
        self.configureEditWidgets()

        """ Configure status bar """
        self.configureStatusBar()

        """ Configure layout """
        self.configureLayout()

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

        """ Connect signal from Edit button in list view to edit menu """
        self.transactionDelegate.transactionEditPressed.connect(self.editTransaction)

        """ Connect signal from Delete button in list view to delete item """
        self.transactionDelegate.transactionDeletePressed.connect(self.deleteTransaction)

        """ Connect signal from Apply button in list view to modify item """
        self.transactionDelegate.transactionModified.connect(self.modifyTransaction)

        """ Update filtering when click on button in status bar """
        self.expenses.clicked.connect(self.updateCurrentFiltering)
        self.income.clicked.connect(self.updateCurrentFiltering)
        self.all.clicked.connect(self.updateCurrentFiltering)

        """ Update filtering when click on button in status bar """
        self.allAccount.clicked.connect(self.addFilter)
        self.account1.clicked.connect(self.addFilter)
        self.account2.clicked.connect(self.addFilter)
        self.account3.clicked.connect(self.addFilter)

    def openContextMenu(self, index, position, rectName):
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
            self.transactionDelegate.setEditable(index)

        if action == deleteAction:
            """ Remove transaction from model """
            self.transactionsFilterModel.deleteTransaction(index)

    def configureEditWidgets(self):
        """
        Configure all edit widgets in transaction item
        :return: void
        """

        """ Configure Name widget """
        self.editName.setFont(QFont("Roboto", 11))
        self.editName.textChanged.connect(self.resizeEditWidget)
        self.editName.setVisible(False)

        """ Configure Amount widget """
        self.editAmount.setMinimum(0.0)
        self.editAmount.setMaximum(100000.0)
        self.editAmount.setFont(QFont("Roboto", 11))
        self.editAmount.valueChanged.connect(self.resizeEditWidget)
        self.editAmount.setVisible(False)

        """ Configure DateEdit widget """
        self.editDate.setFont(QFont("Roboto", 11))
        self.editDate.setCalendarPopup(True)
        self.editDate.setCalendarWidget(CalendarWidget())
        self.editDate.dateChanged.connect(self.resizeEditWidget)
        self.editDate.setVisible(False)

        """ Configure ComboBox widget """
        self.editAccount.setFont(QFont("Roboto", 11))
        self.editAccount.view().setSpacing(2)
        self.editAccount.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.editAccount.addItems(["Livret A", "Compte Chèque", "Livret Jeune"])
        self.editAccount.setCursor(Qt.PointingHandCursor)
        self.editAccount.setVisible(False)

        """ Configure custom widget """
        self.editExpOrInc.setVisible(False)

    def editTransaction(self, index, rectName, rectAmount, rectDate, rectAccount, rectExpOrInc):
        """
        Edit transaction on Edit click
        :param index: item's index
        :param rectName: rect where to put LineEdit
        :param rectAmount: rect where to put DoubleSpinBox
        :param rectDate: rect where to put DateEdit
        :param rectAccount: rect where to put Combobox
        :param rectExpOrInc: rect where to put ExpOrInc
        :return: void
        """

        """ Set transaction editable to paint different """
        self.transactionDelegate.setEditable(index)

        """ Configure Name widget """
        self.editName.setText(self.transactionsModel.data(index, Qt.DisplayRole)[0])
        fontMetrics = QFontMetrics(self.editName.font())
        pixelsWidth = fontMetrics.width(self.editName.text())
        pixelsHeight = fontMetrics.height()
        self.editName.setGeometry(rectName.x(), rectName.y()-3, pixelsWidth+10, pixelsHeight+6)
        self.editName.setVisible(True)

        """ Configure Amount widget """
        amount = self.transactionsModel.data(index, Qt.DisplayRole)[2]
        self.editAmount.setValue(amount)
        fontMetrics = QFontMetrics(self.editAmount.font())
        pixelsWidth = fontMetrics.width(str(self.editAmount.value()))
        pixelsHeight = fontMetrics.height()
        self.editAmount.setGeometry(rectAmount.x(), rectAmount.y()-3, pixelsWidth+38, pixelsHeight+6)
        self.editAmount.setVisible(True)

        """ Configure DateEdit widget """
        dateStr = self.transactionsModel.data(index, Qt.DisplayRole)[3]
        self.editDate.setDate(QDate.fromString(dateStr, 'dd/MM/yyyy'))
        fontMetrics = QFontMetrics(self.editDate.font())
        pixelsWidth = fontMetrics.width(self.editDate.date().toString('dd/MM/yyyy'))
        pixelsHeight = fontMetrics.height()
        self.editDate.setGeometry(rectDate.x(), rectDate.y() - 3, pixelsWidth + 30, pixelsHeight + 6)
        self.editDate.setVisible(True)

        """ Configure ComboBox widget """
        selectedAccount = self.transactionsModel.data(index, Qt.DisplayRole)[4]
        self.editAccount.setCurrentText(selectedAccount)
        self.editAccount.move(rectAccount.x(), rectAccount.y() - 3)
        self.editAccount.setVisible(True)

        """ Configure ComboBox widget """
        selectedExpOrInc = self.transactionsModel.data(index, Qt.DisplayRole)[5]
        rectExpOrIncResized = QRect(round(rectExpOrInc.x()), round(rectExpOrInc.y()),
                                    round(rectExpOrInc.width()*2/3), round(rectExpOrInc.height()))
        self.editExpOrInc.setGeometry(rectExpOrIncResized)
        self.editExpOrInc.setActiveType(selectedExpOrInc)
        self.editExpOrInc.setVisible(True)

    def resizeEditWidget(self):
        """
        Resize sender object (width especially) according to typed content
        :return: void
        """

        sender = self.sender()
        fontMetrics = QFontMetrics(sender.font())

        if isinstance(sender, QLineEdit):
            value = sender.text()
            pixelsWidth = fontMetrics.width(value)
            sender.setFixedWidth(pixelsWidth + 12)
        elif isinstance(sender, QDoubleSpinBox):
            value = str(sender.value())
            pixelsWidth = fontMetrics.width(value)
            sender.setFixedWidth(pixelsWidth+38)
        elif isinstance(sender, QDateEdit):
            value = str(sender.date().toString('dd/MM/yyyy'))
            pixelsWidth = fontMetrics.width(value)
            sender.setFixedWidth(pixelsWidth+30)
        else:
            value = 'coucou'

    def deleteTransaction(self, index):
        """
        Edit transaction on Edit click
        :param index: index in model
        :return: void
        """

        """ Remove transaction from model """
        self.transactionsFilterModel.deleteTransaction(index)

    def modifyTransaction(self, index):
        """
        Modify transaction content on Apply click
        :param index: index in model
        :return: void
        """

        value = [self.editName.text(), "Transport", self.editAmount.value(), self.editDate.date().toString("dd/MM/yyyy"),
                 self.editAccount.currentText(), self.editExpOrInc.activeType()]

        """ Remove transaction from model - [Name, Category, Amount, Date, Account, ExpenseOrIncome] """
        self.transactionsFilterModel.modifyTransaction(index, value)

        """ Hide all widgets """
        self.editName.setVisible(False)
        self.editAmount.setVisible(False)
        self.editDate.setVisible(False)
        self.editAccount.setVisible(False)
        self.editExpOrInc.setVisible(False)

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

        """ Set selection mode """
        # self.transactionsListView.setSelectionMode(QAbstractItemView.SingleSelection)

        """ Hide widgets for edition """
        self.editName.setVisible(False)
        self.editAmount.setVisible(False)
        self.editDate.setVisible(False)

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
