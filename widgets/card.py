from PySide2.QtCore import QSize
from PySide2.QtGui import QFont, QPixmap, QIcon, Qt
from PySide2.QtWidgets import QGroupBox, QGridLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QSpacerItem, \
    QSizePolicy


class Card(QGroupBox):

    def __init__(self, parent):
        super().__init__(parent)

        """ Set maximum height """
        self.setMinimumHeight(243)
        self.setMaximumHeight(243)

        """ Card name """
        self._name = ''

        """ Card amount """
        self._amount = QLabel("0")
        self._amount.setObjectName(u"amount")

        """ Card month trend """
        self._monthTrend = QPushButton("0")
        self._monthTrend.setObjectName(u"monthTrend")

        """ Spacer item """
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        """ Layout """
        self.layout = QGridLayout()

        """ Configure widgets """
        self.configureWidgets()

        """ Configure layout """
        self.configureLayout()

    def configureWidgets(self):
        """
        Configure widgets inside card
        :return: void
        """

        """ Set font for title """
        self.setFont(QFont("Roboto", 16, QFont.Normal))

    def configureLayout(self):
        """
        Set elements in layout
        :return: void
        """

        """ Set margins """
        self.layout.setContentsMargins(14, 0, 14, 0)

        """ Set spacing """
        self.layout.setSpacing(10)

        """ Add widgets """
        # self.layout.addSpacerItem(self.spacer)
        self.layout.addWidget(self._amount)
        self.layout.addWidget(self._monthTrend)

        """ Apply layout on Card """
        self.setLayout(self.layout)

    def setName(self, name):
        """
        Set Card name (title for GroupBox)
        :param name: card name
        :return: void
        """

        self._name = name
        self.setTitle(name)

    def getName(self):
        """
        Return card name
        :return: card name
        """

        return self._name

    def setAmount(self, amount):
        """
        Set card amount and refresh month trend
        :param amount: card amount
        :return: void
        """

        """ Set card amount """
        self._amount.setText("{:,.2f}".format(amount).replace(",", " ") + " EUR")

        """ Refresh month trend """
        self.refreshMonthTrend()

    def getAmount(self):
        """
        Return card amount
        :return: card amount
        """

        return float(self._amount.text()[:-3].replace(" ", ""))

    def setBank(self, bank):
        """
        Set card bank
        :param bank: card bank
        :return: void
        """

        if "Caisse d'Epargne" in bank:
            self.setStyleSheet("background-image: url(:/images/images/background_caisse_epargne.svg);")

    def setBackgroundColor(self, colorNb):
        """
        Apply new background color
        :param colorNb: color to apply
        :return: void
        """

        if colorNb == 1:
            self.setStyleSheet(self.styleSheet() + "background-color: qconicalgradient(cx:0.0, cy:0.5, angle:220,"
                    "stop:0 #322B67, stop:1 #764CFF);")
        self._amount.setStyleSheet("background-color: transparent;")
        self._monthTrend.setStyleSheet("background-color: transparent;")

    def refreshMonthTrend(self):
        """
        Refresh month trend according to current amount
        :param amount: current amount
        :return: void
        """

        """ Get previous amount from database """
        # self.getPreviousMonthAmount.emit()    # TODO: emit signal to retrieve previous month account

        self.setMonthTrend(3105.48)

    def setMonthTrend(self, previousAmount):
        """
        Set month trend
        :param previousAmount: previous amount from database
        :return: void
        """

        currentAmount = self.getAmount()
        diff = currentAmount - previousAmount

        """ Update text """
        self._monthTrend.setText("  {:,.2f}".format(diff).replace(",", " "))

        if diff > 0:
            """ Difference is positive """
            self._monthTrend.setIcon(QIcon(":/images/images/trending_up-#12A61C-36dp.svg"))
            self._monthTrend.setIconSize(QSize(36, 36))

        else:
            """ Difference is negative """
            self._monthTrend.setIcon(QIcon(":/images/images/trending_down-#F20505-36dp.svg"))
            self._monthTrend.setIconSize(QSize(36, 36))
