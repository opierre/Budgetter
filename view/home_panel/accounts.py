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
        self.uiSetup.card1.setDescription("Caisse d'Epargne")
        self.uiSetup.card1.setAmount(2107.56)

    def setAccounts(self, accountList):
        """
        Set accounts list to display in groupBox
        :param accountList: accounts list
        :return: void
        """

        for account in accountList:
            print('alors')
