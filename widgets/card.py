from PySide2.QtGui import QFont, QPixmap, QIcon, Qt
from PySide2.QtWidgets import QGroupBox, QHBoxLayout, QLabel, QPushButton


class Card(QGroupBox):

    def __init__(self, parent):
        super().__init__(parent)

        ''' Set maximum height '''
        self.setMinimumHeight(100)
        self.setMaximumHeight(100)

        ''' Card name '''
        self._name = ''

        ''' Card amount '''
        self._amount = QLabel("0")
        self._amount.setObjectName(u"amount")

        ''' Card description '''
        self._description = QPushButton("")
        self._description.setObjectName(u"description")

        ''' Layout '''
        self.layout = QHBoxLayout()

        ''' Configure widgets '''
        self.configureWidgets()

        ''' Configure layout '''
        self.configureLayout()

    def configureWidgets(self):
        """
        Configure widgets inside card
        :return: void
        """

        ''' Set font '''
        self.setFont(QFont("Roboto", 13, QFont.Normal))
        self._description.setFont(QFont("Roboto Light", 10, QFont.Normal))

        ''' Set description button hand cursor '''
        self._description.setCursor(Qt.PointingHandCursor)

    def configureLayout(self):
        """
        Set elements in layout
        :return: void
        """

        ''' Set margins '''
        self.layout.setContentsMargins(14, 0, 0, 0)

        ''' Add widgets '''
        self.layout.addWidget(self._description)
        self.layout.addWidget(self._amount)

        ''' Apply layout on Card '''
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
        Set card amount
        :param amount: card amount
        :return: void
        """

        self._amount.setText(str(amount))

    def getAmount(self):
        """
        Return card amount
        :return: card amount
        """

        return self._amount.text()

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
