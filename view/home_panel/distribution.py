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
        self.layout1 = QGridLayout()
        self.layout2 = QGridLayout()

    #     self.expense1 = Thumbnail("Shopping", 524)
    #     self.expense2 = Thumbnail("Fuel", 126)
    #     self.expense3 = Thumbnail("Travel", 1002)
    #     self.expense4 = Thumbnail("Car", 304)
    #     self.expense5 = Thumbnail("Grocery", 251)
    #     self.expense6 = Thumbnail("Phone", 11.99)
    #     self.expense7 = Thumbnail("Internet", 32.99)
    #     self.expense8 = Thumbnail("Water", 12)
    #     self.expense9 = Thumbnail("Electricity", 53)
    #     self.expense10 = Thumbnail("Transport", 20)
    #     self.expense11 = Thumbnail("Sports", 300)
    #     self.expense12 = Thumbnail("Electronics", 154)
    #
    #     """ Connect Distribution groupBox """
    #     self.connectDistribution()
    #
    #     """ Configure widgets """
    #     self.configureWidgets()
    #
    #     """ Configure layout """
    #     self.configureLayout()
    #
    #     self.addExpense(self.expense1)
    #     self.addExpense(self.expense2)
    #     self.addExpense(self.expense3)
    #     self.addExpense(self.expense4)
    #     self.addExpense(self.expense5)
    #     self.addExpense(self.expense6)
    #     self.addExpense(self.expense7)
    #     self.addExpense(self.expense8)
    #     self.addExpense(self.expense9)
    #     self.addExpense(self.expense10)
    #     self.addExpense(self.expense11)
    #     self.addExpense(self.expense12)
    #
    # def connectDistribution(self):
    #     """
    #     Connect Accounts widgets
    #     :return: void
    #     """
    #
    #     """ Connect click left/right chevron """
    #     self.uiSetup.rightPageMonthlyExpenses.clicked.connect(lambda: self.changePage(1))
    #     self.uiSetup.leftPageMonthlyExpenses.clicked.connect(lambda: self.changePage(0))
    #
    #     """ Connect animation finished on sliding stacked widget to show chevron """
    #     self.uiSetup.monthlyExpensesThumb.animationFinished.connect(self.showChevrons)
    #
    # def configureLayout(self):
    #     """
    #     Set elements in layout
    #     :return: void
    #     """
    #
    #     """ Set margins """
    #     self.layout1.setContentsMargins(0, 0, 0, 0)
    #     self.layout2.setContentsMargins(0, 0, 0, 0)
    #
    #     """ Apply layout on Card """
    #     self.uiSetup.page1MonthlyExpenses.setLayout(self.layout1)
    #     self.uiSetup.page2MonthlyExpenses.setLayout(self.layout2)
    #
    # def configureWidgets(self):
    #     """
    #     Configure widgets inside distribution panel
    #     :return: void
    #     """
    #
    #     """ Set sliding animation axe """
    #     self.uiSetup.monthlyExpensesThumb.setDirection(Qt.Horizontal)
    #
    # def changePage(self, pageNumber):
    #     """
    #     Change page number and hide chevron
    #     :param pageNumber: page number
    #     :return: void
    #     """
    #
    #     """ Hide chevrons """
    #     self.uiSetup.rightPageMonthlyExpenses.hide()
    #     self.uiSetup.leftPageMonthlyExpenses.hide()
    #
    #     """ Change current index """
    #     self.uiSetup.monthlyExpensesThumb.slideInIdx(pageNumber)
    #
    # def showChevrons(self):
    #     """
    #     Show chevrons for right/left page
    #     :return: void
    #     """
    #
    #     self.uiSetup.rightPageMonthlyExpenses.show()
    #     self.uiSetup.leftPageMonthlyExpenses.show()
    #
    # def addExpense(self, thumbnail):
    #     """
    #     Add monthly expense to groupbox (max: 6/page)
    #     :param thumbnail: thumbanil expense to add
    #     :return: void
    #     """
    #
    #     if self.row < 2:
    #         if self.col < 3:
    #             if self.page == 0:
    #                 self.uiSetup.page1MonthlyExpenses.layout().addWidget(thumbnail, self.row, self.col)
    #                 self.col += 1
    #             elif self.page == 1:
    #                 self.uiSetup.page2MonthlyExpenses.layout().addWidget(thumbnail, self.row, self.col)
    #                 self.col += 1
    #             else:
    #                 return
    #         else:
    #             self.col = 0
    #             self.row += 1
    #             self.addExpense(thumbnail)
    #     else:
    #         self.page += 1
    #         self.row = 0
    #         self.addExpense(thumbnail)
