from PySide2.QtCore import QObject, Qt
from PySide2.QtGui import QPainter, QFont
from PySide2.QtWidgets import QSpacerItem, QSizePolicy
from PySide2.QtCharts import QtCharts

from widgets.card import Card


class Accounts(QObject):
    """
    Accounts
    """

    def __init__(self, gui):
        super(Accounts, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ Spacer item """
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        """ Configure chart """
        self.configure_chart()

        """ Configure title bar """
        self.configure_title_bar()

        """ Connect Account groupBox """
        # self.connectAccounts()

    def configure_chart(self):
        """
        Configure chart
        :return: void
        """

        series = QtCharts.QPieSeries()
        series.setHoleSize(0.35)
        series.append("Protein 4.2%", 4.2)
        slice = series.append("Fat 15.6%", 15.6)
        slice.setExploded()
        slice.setLabelVisible()
        series.append("Other 23.8%", 23.8)
        series.append("Carbs 56.4%", 56.4)

        chartView = QtCharts.QChartView(self.ui_setup.widgetDonut)
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.chart().setTitle("Donut with a lemon glaze (100g)")
        chartView.chart().addSeries(series)
        chartView.chart().legend().setAlignment(Qt.AlignBottom)
        chartView.chart().setTheme(QtCharts.QChart.ChartThemeBlueCerulean)
        chartView.chart().legend().setFont(QFont("Arial", 7))

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

    def connectAccounts(self):
        """
        Connect Accounts widgets
        :return: void
        """

        """ Connect click on groupBox to set always checked """
        self.ui_setup.accounts.clicked.connect(self.checkGroupBox)

        self.addAccount()

    def setAccounts(self, accountList):
        """
        Set accounts list to display in groupBox
        :param accountList: accounts list
        :return: void
        """

        for account in accountList:
            print('alors')

    def addAccount(self):
        """
        Add account to dashboard (max: 3)
        :return: void
        """

        self.ui_setup.accounts.layout().addWidget(self.card2)
        self.ui_setup.accounts.layout().addWidget(self.card3)
        self.ui_setup.accounts.layout().addItem(self.spacer)

    def checkGroupBox(self):
        """
        Set checkbox always enabled
        :return: void
        """

        self.ui_setup.accounts.setChecked(True)
