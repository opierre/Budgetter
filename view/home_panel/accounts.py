from PySide2.QtCore import QObject
from PySide2.QtWidgets import QSpacerItem, QSizePolicy

from widgets.card import Card


class Accounts(QObject):
    """
    Accounts
    """

    def __init__(self, gui):
        super(Accounts, self).__init__()

        """ Store gui """
        self.uiSetup = gui

        self.uiSetup.card1.setName("Compte Chèque")
        self.uiSetup.card1.setBank("Caisse d'Epargne")
        self.uiSetup.card1.setBackgroundColor(1)
        self.uiSetup.card1.setAmount(2107.56)

        self.card2 = Card()
        self.card2.setName("Livret A")
        self.card2.setBank("Crédit Agricole")
        self.card2.setBackgroundColor(2)
        self.card2.setAmount(156.48)

        self.card3 = Card()
        self.card3.setName("Livret Jeune")
        self.card3.setBank("Banque Populaire")
        self.card3.setBackgroundColor(3)
        self.card3.setAmount(2000.48)

        """ Spacer item """
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        """ Connect Account groupBox """
        self.connectAccounts()

    def connectAccounts(self):
        """
        Connect Accounts widgets
        :return: void
        """

        """ Connect click on groupBox to set always checked """
        self.uiSetup.accounts.clicked.connect(self.checkGroupBox)

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

        self.uiSetup.accounts.layout().addWidget(self.card2)
        self.uiSetup.accounts.layout().addWidget(self.card3)
        self.uiSetup.accounts.layout().addItem(self.spacer)

    def checkGroupBox(self):
        """
        Set checkbox always enabled
        :return: void
        """

        self.uiSetup.accounts.setChecked(True)
