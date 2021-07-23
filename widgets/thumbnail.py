from PySide2.QtCore import QSize
from PySide2.QtGui import QFont, QPixmap, QIcon, Qt
from PySide2.QtWidgets import QGroupBox, QGridLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QSpacerItem, \
    QSizePolicy, QStatusBar, QVBoxLayout


class Thumbnail(QGroupBox):

    def __init__(self, category="", amout=0, parent=None):
        super().__init__(parent)

        """ Set height """
        self.setMinimumHeight(180)
        self.setMaximumHeight(180)

        """ Set width """
        self.setMinimumWidth(130)
        self.setMaximumWidth(130)

        """ Category """
        self._category = QLabel("")
        self._category.setObjectName(u"categoryExpense")

        """ Amount """
        self._amount = QLabel("")
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

        """ Apply parameters """
        self.setCategory(category)
        self.setAmount(amout)

        """ Connect all widgets """
        self.connectWidgets()

    def configureWidgets(self):
        """
        Configure widgets inside thumbnail
        :return: None
        """

        """ Set alignments """
        self._category.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self._amount.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self._month.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        """ Set button icon and pointing hand and checkable """
        self._logo.setIconSize(QSize(52, 52))
        self._logo.setCursor(Qt.PointingHandCursor)
        self._logo.setCheckable(True)

        """ Set thumbnail style """
        self.setProperty("checked", "false")
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

    def connectWidgets(self):
        """
        Connect widgets inside thumbnail
        :return: None
        """

        """ Connect button to click """
        self._logo.clicked.connect(self.updateStyle)

    def configureLayout(self):
        """
        Set elements in layout
        :return: None
        """

        """ Set margins """
        self.layout.setContentsMargins(0, 0, 0, 15)
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
        :return: None
        """

        state = self._logo.isChecked()

        if state is True:
            self.setStyleSheet("Thumbnail { background-color: #2d4057;}")
        else:
            self.setStyleSheet("Thumbnail { background-color: transparent;}")
        self.updateLogoState(state)

    def updateLogoState(self, state):
        """
        Update logo state according to click on thumbnail
        :param state: thumbnail state (checked or not)
        :return: None
        """

        category = self._category.text().lower()
        if state is True:
            self._logo.setIcon(QIcon(":/images/images/" + category + "-checked-36dp.svg"))
        else:
            self._logo.setIcon(QIcon(":/images/images/" + category + "-white-36dp.svg"))

    def setCategory(self, category):
        """
        Set Thumbnail category and according logo
        :param category: expense category
        :return: None
        """

        self._category.setText(category)

        category = self._category.text().lower()
        self._logo.setIcon(QIcon(":/images/images/" + category + "-white-36dp.svg"))

    def getCategory(self):
        """
        Return thumbnail category
        :return: category
        """

        return self._category.text()

    def setAmount(self, amount):
        """
        Set thumnail amount
        :param amount: amount
        :return: None
        """

        """ Set card amount """
        self._amount.setText("€ " + "{:,.0f}".format(amount).replace(",", " "))

        if amount > 999:
            self._amount.setContentsMargins(17, 0, 0, 0)
        else:
            self._amount.setContentsMargins(0, 0, 0, 0)

    def getAmount(self):
        """
        Return thumnail amount
        :return: amount
        """

        return float(self._amount.text()[2:].replace(" ", ""))
