from PySide2.QtCore import QObject, QCoreApplication, Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QListView, QWidget, QHBoxLayout


class Expenses(QObject):
    """
    Expenses
    """

    def __init__(self, gui):
        super(Expenses, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ Configure layout """
        self.configure_layout()

        """ Configure title bar """
        self.configure_title_bar()

        """ Configure widgets inside panel """
        self.configure_panel()

        """ Connect Account groupBox """
        # self.connectAccounts()

    def configure_title_bar(self):
        """
        Configure TitleBar with icon

        :return: None
        """

        """ Set title """
        self.ui_setup.expenses.set_title(QCoreApplication.translate("graphs", "Expenses"))

        """ Hide all widgets in title bar """
        self.ui_setup.expenses.disable_title_bar_button()
        self.ui_setup.expenses.disable_search_bar()

    def configure_layout(self):
        """
        Configure layout inside of Container

        :return: None
        """

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setSpacing(30)
        layout.setContentsMargins(20, 10, 10, 10)

        # self.ui_setup.accounts.setWidget(widget)

    def configure_panel(self):
        """
        Configure widgets' panel

        :return: None
        """

        self.ui_setup.expenses_choice.setView(QListView())
        self.ui_setup.expenses_choice.setFont(QFont("Roboto", 11))
        # self.ui_setup.expenses_choice.view().setSpacing(2)
        self.ui_setup.expenses_choice.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.ui_setup.expenses_choice.view().window().setAttribute(Qt.WA_TranslucentBackground)
