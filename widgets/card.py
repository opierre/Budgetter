from PySide2.QtCore import QSize
from PySide2.QtGui import QFont, QPixmap, QIcon, Qt
from PySide2.QtWidgets import QGroupBox, QGridLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QSpacerItem, \
    QSizePolicy, QStatusBar


class Card(QGroupBox):

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Set height """
        self.setMinimumHeight(243)
        self.setMaximumHeight(243)

        """ Set width """
        self.setMinimumWidth(383)
        self.setMaximumWidth(383)

        """ Card name """
        self._name = ''

        """ Card amount """
        self._amount = QLabel("0")
        self._amount.setObjectName(u"amount")

        """ Card currency """
        self._currency = QLabel(" EUR")
        self._currency.setObjectName(u"currency")

        """ Card month trend """
        self._monthTrend = QPushButton("0")
        self._monthTrend.setObjectName(u"monthTrend")

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
        self.setFont(QFont("Roboto", 14, QFont.Normal))

        """ Set alignment for amout/currency """
        self._amount.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._currency.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    def configureLayout(self):
        """
        Set elements in layout
        :return: void
        """

        """ Set margins """
        self.layout.setContentsMargins(14, 0, 14, 0)

        """ Add widgets """
        self.layout.addWidget(self._amount, 0, 0)
        self.layout.addWidget(self._currency, 0, 1)
        self.layout.addWidget(self._monthTrend, 1, 0)

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
        self._amount.setText("{:,.2f}".format(amount).replace(",", " "))

        """ Refresh month trend """
        self.refreshMonthTrend()

    def getAmount(self):
        """
        Return card amount
        :return: card amount
        """

        return float(self._amount.text().replace(" ", ""))

    def setBank(self, bank):
        """
        Set card bank
        :param bank: card bank
        :return: void
        """

        if "Caisse d'Epargne" in bank:
            self.setStyleSheet("background-image: url(:/images/images/background_caisse_epargne.svg);")
        elif "Crédit Agricole" in bank:
            self.setStyleSheet("background-image: url(:/images/images/background_credit_agricole.svg);")
        elif "Banque Populaire" in bank:
            self.setStyleSheet("background-image: url(:/images/images/background_banque_populaire.svg);")

    def setBackgroundColor(self, colorNb):
        """
        Apply new background color
        :param colorNb: color to apply
        :return: void
        """

        if colorNb == 1:
            self.setStyleSheet(self.styleSheet() + "background-color: qconicalgradient(cx:0.0, cy:0.5, angle:220,"
                    "stop:0 #322B67, stop:1 #764CFF);")
        elif colorNb == 2:
            self.setStyleSheet(self.styleSheet() + "background-color: qconicalgradient(cx:0.0, cy:0.5, angle:220,"
                    "stop:0 #633c01, stop:1 #E58900);")
        elif colorNb == 3:
            self.setStyleSheet(self.styleSheet() + "background-color: qconicalgradient(cx:0.0, cy:0.5, angle:220,"
                    "stop:0 #163e4d, stop:1 #49C6F4);")
        self._amount.setStyleSheet("background-color: transparent;")
        self._monthTrend.setStyleSheet("background-color: transparent;")
        self._currency.setStyleSheet("background-color: transparent;")

    def refreshMonthTrend(self):
        """
        Refresh month trend according to current amount
        :param amount: current amount
        :return: void
        """

        """ Get previous amount from database """
        # self.getPreviousMonthAmount.emit()    # TODO: emit signal to retrieve previous month account

        self.setMonthTrend(2000.48)

    def setMonthTrend(self, previousAmount):
        """
        Set month trend
        :param previousAmount: previous amount from database
        :return: void
        """

        currentAmount = self.getAmount()
        diff = currentAmount - previousAmount

        """ Update text """
        self._monthTrend.setText("  {:,.2f}".format(diff).replace(",", " ") + " €")

        if diff > 0:
            """ Difference is positive """
            self._monthTrend.setIcon(QIcon(":/images/images/trending_up-#12A61C-36dp.svg"))
            self._monthTrend.setIconSize(QSize(36, 36))
            self._monthTrend.setProperty("positive", "true")
            self._monthTrend.style().unpolish(self._monthTrend)
            self._monthTrend.style().polish(self._monthTrend)
            self._monthTrend.update()

        elif diff < 0 :
            """ Difference is negative """
            self._monthTrend.setIcon(QIcon(":/images/images/trending_down-#F20505-36dp.svg"))
            self._monthTrend.setIconSize(QSize(36, 36))
            self._monthTrend.setProperty("positive", "false")
            self._monthTrend.style().unpolish(self._monthTrend)
            self._monthTrend.style().polish(self._monthTrend)
            self._monthTrend.update()

        else:
            """ Difference is null """
            self._monthTrend.setIcon(QIcon(":/images/images/trending_flat-white-36dp.svg"))
            self._monthTrend.setIconSize(QSize(36, 36))
            self._monthTrend.setProperty("positive", "none")
            self._monthTrend.style().unpolish(self._monthTrend)
            self._monthTrend.style().polish(self._monthTrend)
            self._monthTrend.update()
