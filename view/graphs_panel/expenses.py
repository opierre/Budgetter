from PySide2.QtCore import QObject, QCoreApplication
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
