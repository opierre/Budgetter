from PySide2.QtCore import QSize
from PySide2.QtGui import QFont, QPixmap, QIcon, Qt
from PySide2.QtWidgets import QGroupBox, QHBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QSpacerItem, \
    QSizePolicy


class Card(QGroupBox):

    def __init__(self, parent):
        super().__init__(parent)

        """ Set maximum height """
        self.setMinimumHeight(100)
        self.setMaximumHeight(100)

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

        """ Card description """
        self._description = QPushButton("")
        self._description.setObjectName(u"description")

        """ Layout """
        self.layout = QHBoxLayout()

        """ Configure widgets """
        self.configureWidgets()

        """ Configure layout """
        self.configureLayout()

    def configureWidgets(self):
        """
        Configure widgets inside card
        :return: void
        """

        """ Set font """
        self.setFont(QFont("Roboto", 13, QFont.Normal))

        """ Set description properties """
        # self._description.setCursor(Qt.PointingHandCursor)

        """ Set amount properties """
        # self._amount.setFixedSize(QSize())

    def configureLayout(self):
        """
        Set elements in layout
        :return: void
        """

        """ Set margins """
        self.layout.setContentsMargins(14, 0, 14, 0)

        """ Set spacing """
        self.layout.setSpacing(50)

        """ Add widgets """
        self.layout.addWidget(self._description)
        self.layout.addSpacerItem(self.spacer)
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
        self._amount.setText("{:,.2f}".format(amount).replace(",", " ") + " €")

        """ Refresh month trend """
        self.refreshMonthTrend()

    def getAmount(self):
        """
        Return card amount
        :return: card amount
        """

        return float(self._amount.text()[:-1].replace(" ", ""))

    def setDescription(self, description):
        """
        Set card description
        :param description: card description
        :return: void
        """

        self._description.setText(description)

        if "Caisse d'Epargne" in description:
            self._description.setIcon(QIcon(":/logo/images/caissedepargne.png"))

    def getDescription(self):
        """
        Return card description
        :return: card description
        """

        return self._description.text()

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
