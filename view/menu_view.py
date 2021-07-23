from PySide2.QtCore import QObject
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QActionGroup


class Menu(QObject):
    """
    Menu class to handle tool bar and left drawer
    """

    def __init__(self, parent, gui):
        super(Menu, self).__init__()

        """ Store windows and gui """
        self.uiSetup = gui
        self.mainWindow = parent

        """ Create QActionGroup to enable only one panel """
        self.action_group = QActionGroup(self)

        """ Configure action group """
        self.configure_action_group()

        """ Connect slots and signals """
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals
        :return: None
        """

        """ Connect click on buttons in drawer """
        self.uiSetup.actionDashboard.triggered.connect(lambda: self.change_page(0))
        self.uiSetup.actionGraph.triggered.connect(lambda: self.change_page(1))
        self.uiSetup.actionInsights.triggered.connect(lambda: self.change_page(2))

    def configure_action_group(self):
        """
        Configure toolbar action group
        :return: None
        """

        """ Add action to group """
        self.action_group.addAction(self.uiSetup.actionDashboard)
        self.action_group.addAction(self.uiSetup.actionGraph)
        self.action_group.addAction(self.uiSetup.actionInsights)

        """ Set group exclusive """
        self.action_group.setExclusive(True)

    def change_page(self, pageNumber):
        """
        Change page by clicking on button in drawer
        :param pageNumber: page number to go to
        :return: None
        """

        self.uiSetup.stackedWidget.slideInIdx(pageNumber)

        if pageNumber == 0:
            """ Update Header """
            self.uiSetup.menuLabel.setText("Dashboard")

        elif pageNumber == 1:
            """ Update Header """
            self.uiSetup.menuLabel.setText("Graph")

        elif pageNumber == 2:
            """ Update Header """
            self.uiSetup.menuLabel.setText("Insights")
