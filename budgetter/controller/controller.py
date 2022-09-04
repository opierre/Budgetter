from PySide6.QtCore import QThreadPool

from budgetter.view.panels.graphs import Graphs
from budgetter.view.panels.home import Home
from budgetter.view.panels.menu_view import Menu
from budgetter.view.skeletons.MainWindow import Ui_MainWindow
from budgetter.view.widgets.custom_window import CustomWindow


class Controller:
    """
    Controller class
    """

    def __init__(self):
        # Create MainWindow
        self.main_window = CustomWindow()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self.main_window)

        # Store thread pool
        self.thread_pool = QThreadPool()

        # # Store effects
        # self.effectAccounts = QGraphicsDropShadowEffect()
        # self.effectDistribution = QGraphicsDropShadowEffect()
        # self.effectTransactions = QGraphicsDropShadowEffect()

        # Configure main effect and apply
        # self.configureGraphicalEffects()

        # Left Drawer
        self.menu_drawer = Menu(self.main_window, self.gui)

        # Home Panel
        self.home_panel = Home(self.main_window, self.gui)

        # Graphs Panel
        self.graphs_panel = Graphs(self.main_window, self.gui)

        # Connect all signals/slots
        self.connect_slots_and_signals()

        # Show FullScreen
        self.main_window.showMaximized()

    # def configureGraphicalEffects(self):
    #     """
    #     Apply all grpahical effects to main widgets
    #     :return: None
    #     """
    #
    #     # Configure effect
    #     self.effectAccounts.setBlurRadius(10)
    #     self.effectAccounts.setColor(QColor(37, 55, 70, 120))
    #     self.effectAccounts.setXOffset(5)
    #     self.effectAccounts.setYOffset(8)
    #     self.effectDistribution.setBlurRadius(10)
    #     self.effectDistribution.setColor(QColor(37, 55, 70, 120))
    #     self.effectDistribution.setXOffset(5)
    #     self.effectDistribution.setYOffset(8)
    #     self.effectTransactions.setBlurRadius(10)
    #     self.effectTransactions.setColor(QColor(37, 55, 70, 120))
    #     self.effectTransactions.setXOffset(5)
    #     self.effectTransactions.setYOffset(8)
    #
    #     # Apply effect to all groupbox
    #     self.ui.accounts.setGraphicsEffect(self.effectAccounts)
    #     self.ui.transactions.setGraphicsEffect(self.effectDistribution)
    #     self.ui.distribution.setGraphicsEffect(self.effectTransactions)

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect Custom Windows resize to display callout
        self.main_window.resizeEventSignal.connect(self.home_panel.display_saving_tooltip)
