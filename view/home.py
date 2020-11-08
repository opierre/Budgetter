from PySide2.QtCore import QObject
from PySide2.QtGui import QIcon

from view.home_panel.accounts import Accounts


class Home(QObject):
    """
    Home Panel to handle Accounts/Distribution/Transactions
    """

    def __init__(self, parent, gui):
        super(Home, self).__init__()

        """ Store windows and gui """
        self.uiSetup = gui
        self.mainWindow = parent

        """ Accounts groupBox """
        self._accounts = Accounts(gui)

        """ Connect slots and signals """
        self.connectHomeSlotsAndSignals()

    def connectHomeSlotsAndSignals(self):
        """
        Connect all slots and signals
        :return: void
        """

        print('coucou')
