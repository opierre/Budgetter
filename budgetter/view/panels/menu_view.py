from PySide6.QtCore import QObject, QCoreApplication
from PySide6.QtGui import QActionGroup


class Menu(QObject):
    """
    Menu class to handle tool bar and left drawer
    """

    def __init__(self, parent, gui):
        super().__init__()

        # Store windows and gui
        self.ui_setup = gui
        self.main_window = parent

        # Create QActionGroup to enable only one panel
        self.action_group = QActionGroup(self)

        # Configure action group
        self.configure_action_group()

        # Connect slots and signals
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect click on buttons in drawer
        self.ui_setup.actionDashboard.triggered.connect(lambda: self.change_page(0))
        self.ui_setup.actionGraph.triggered.connect(lambda: self.change_page(1))
        self.ui_setup.actionInsights.triggered.connect(lambda: self.change_page(2))

    def configure_action_group(self):
        """
        Configure toolbar action group

        :return: None
        """

        # Add action to group
        self.action_group.addAction(self.ui_setup.actionDashboard)
        self.action_group.addAction(self.ui_setup.actionGraph)
        self.action_group.addAction(self.ui_setup.actionInsights)

        # Set group exclusive
        self.action_group.setExclusive(True)

    def change_page(self, page_number: int):
        """
        Change page by clicking on button in drawer

        :param page_number: page number to go to
        :return: None
        """

        self.ui_setup.stackedWidget.slideInIdx(page_number)

        if page_number == 0:
            # Update Header
            self.ui_setup.menuLabel.setText(QCoreApplication.translate(b"menu", b"Dashboard"))

        elif page_number == 1:
            # Update Header
            self.ui_setup.menuLabel.setText(QCoreApplication.translate(b"menu", b"Graph"))

        elif page_number == 2:
            # Update Header
            self.ui_setup.menuLabel.setText(QCoreApplication.translate(b"menu", b"Insights"))
