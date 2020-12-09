from PySide2.QtCore import QObject


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

        """ Connect Account groupBox """
        self.connectAccounts()

    def connectAccounts(self):
        """
        Connect Accounts widgets
        :return: void
        """

        """ Connect click on groupBox to set always checked """
        self.uiSetup.accounts.clicked.connect(self.checkGroupBox)

    def setAccounts(self, accountList):
        """
        Set accounts list to display in groupBox
        :param accountList: accounts list
        :return: void
        """

        for account in accountList:
            print('alors')

    def checkGroupBox(self):
        """
        Set checkbox always enabled
        :return: void
        """

        self.uiSetup.accounts.setChecked(True)
