from PySide2.QtCore import QSize
from PySide2.QtGui import QFont, QPixmap, QIcon, Qt
from PySide2.QtWidgets import QGroupBox, QGridLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QSpacerItem, \
    QSizePolicy, QStatusBar, QVBoxLayout


class Thumbnail(QGroupBox):

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Set height """
        self.setMinimumHeight(180)
        self.setMaximumHeight(180)

        """ Set width """
        self.setMinimumWidth(130)
        self.setMaximumWidth(130)

        """ Category """
        self._category = QLabel("Shopping")
        self._category.setObjectName(u"categoryExpense")

        """ Amount """
        self._amount = QLabel("€ 524")
        self._amount.setObjectName(u"amountExpense")

        """ Per month """
        self._month = QLabel(" /mo")
        self._month.setObjectName(u"monthExpense")

        """ Logo """
        self._logo = QPushButton()
        self._logo.setObjectName(u"logoExpense")

        """ Layout """
        self.layout = QGridLayout()

        """ Configure widgets """
        self.configureWidgets()

        """ Configure layout """
        self.configureLayout()

    def configureWidgets(self):
        """
        Configure widgets inside thumbnail
        :return: void
        """

        """ Set alignments """
        self._category.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self._amount.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self._month.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        """ Set button icon and pointing hand and checkable """
        self._logo.setIcon(QIcon(":/images/images/shopping_cart-white-36dp.svg"))
        self._logo.setIconSize(QSize(52, 52))
        self._logo.setCursor(Qt.PointingHandCursor)
        self._logo.setCheckable(True)

        """ Set thumbnail style """
        self.setProperty("checked", "false")
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

        """ Connect button to click """
        self._logo.clicked.connect(self.updateStyle)

    def configureLayout(self):
        """
        Set elements in layout
        :return: void
        """

        """ Set margins """
        self.layout.setContentsMargins(0, 0, 0, 25)
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(5)

        """ Add widgets """
        self.layout.addWidget(self._logo, 0, 0, 1, 0)
        self.layout.addWidget(self._category, 1, 0, 1, 0)
        self.layout.addWidget(self._amount, 2, 0)
        self.layout.addWidget(self._month, 2, 1)

        """ Apply layout on Card """
        self.setLayout(self.layout)

    def updateStyle(self):
        """
        Update style on checked button
        :return: void
        """

        state = self._logo.isChecked()

        if state is True:
            self.setStyleSheet(self.styleSheet() + "background-color: #32344C;")
        else:
            self.setStyleSheet(self.styleSheet() + "background-color: transparent;")
        # self.style().unpolish(self)
        # self.style().polish(self)
        # self.update()

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
