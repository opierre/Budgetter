from PySide2.QtCore import QObject, QCoreApplication, QDate
from PySide2.QtWidgets import QListView, QWidget, QHBoxLayout


class Income(QObject):
    """
    Income
    """

    def __init__(self, gui):
        super(Income, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ Configure layout """
        self.configure_layout()

        """ Configure title bar """
        self.configure_title_bar()

        """ Configure parameters """
        self.configure_parameters()

        """ Connect Account groupBox """
        # self.connectAccounts()

    def configure_title_bar(self):
        """
        Configure TitleBar with icon

        :return: None
        """

        """ Set title """
        self.ui_setup.income.set_title(QCoreApplication.translate("graphs", "Income"))

        """ Hide all widgets in title bar """
        self.ui_setup.income.disable_title_bar_button()
        self.ui_setup.income.disable_search_bar()

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

    def configure_parameters(self):
        """
        Configure parameters to look for

        :return: None
        """

        """ Set current date """
        self.ui_setup.dateEdit_income_to.setDate(QDate.currentDate())


