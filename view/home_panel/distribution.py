from PySide2.QtCore import QObject, Qt
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter, QBrush, QColor, QCursor, QFont
from PySide2.QtWidgets import QGridLayout, QSizePolicy

from random import randrange
from functools import partial

from widgets.thumbnail import Thumbnail


class Distribution(QObject):
    """
    Distribution
    """

    def __init__(self, gui):
        super(Distribution, self).__init__()

        """ Store gui """
        self.uiSetup = gui

        """ Store line/column/page """
        self.row = 0
        self.col = 0
        self.page = 0

        """ Layout """
        self.layout = QGridLayout()

        self.expense1 = Thumbnail()
        self.expense1.setCategory("Shopping")
        self.expense1.setAmount(524)

        self.expense2 = Thumbnail()
        self.expense2.setCategory("Fuel")
        self.expense2.setAmount(126)

        self.expense3 = Thumbnail()
        self.expense3.setCategory("Travel")
        self.expense3.setAmount(1002)

        """ Connect Distribution groupBox """
        self.connectDistribution()

        """ Configure widgets """
        self.configureWidgets()

        """ Configure layout """
        self.configureLayout()

        self.addExpense(self.expense1)
        self.addExpense(self.expense2)
        self.addExpense(self.expense3)

    def connectDistribution(self):
        """
        Connect Accounts widgets
        :return: void
        """

        """ Connect click left/right chevron """
        self.uiSetup.rightPageMonthlyExpenses.clicked.connect(lambda: self.changePage(1))
        self.uiSetup.leftPageMonthlyExpenses.clicked.connect(lambda: self.changePage(0))

    def configureLayout(self):
        """
        Set elements in layout
        :return: void
        """

        """ Set margins """
        self.layout.setContentsMargins(0, 0, 0, 0)

        """ Apply layout on Card """
        self.uiSetup.page1MonthlyExpenses.setLayout(self.layout)

    def configureWidgets(self):
        """
        Configure widgets inside distribution panel
        :return: void
        """

        """ Set sliding animation """
        self.uiSetup.monthlyExpensesThumb.setDirection(Qt.Horizontal)

    def changePage(self, pageNumber):
        """
        Change page number and hide/show chevron
        :param pageNumber: page number
        :return: void
        """

        """ Hide chevrons """
        self.uiSetup.rightPageMonthlyExpenses.hide()
        self.uiSetup.leftPageMonthlyExpenses.hide()

        """ Change current index """
        self.uiSetup.monthlyExpensesThumb.slideInIdx(pageNumber)

        """ Hide chevrons """
        # self.uiSetup.rightPageMonthlyExpenses.show()
        # self.uiSetup.leftPageMonthlyExpenses.show()

    def addExpense(self, thumbnail):
        """
        Add monthly expense to groupbox (max: 6/page)
        :param thumbnail: thumbanil expense to add
        :return: void
        """

        if self.row < 2:
            if self.col < 3:
                if self.page < 2:
                    self.uiSetup.page1MonthlyExpenses.layout().addWidget(thumbnail, self.row, self.col)
                    self.col += 1
                else:
                    return
            else:
                self.col = 0
                self.row += 1
                self.addExpense(thumbnail)
        else:
            self.page += 1
            self.row = 0
            self.addExpense(thumbnail)
