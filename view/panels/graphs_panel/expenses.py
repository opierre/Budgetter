from PySide2.QtCore import QObject, QCoreApplication, Qt, QDate
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

        """ Set income bar graph """
        self.set_bar_graph()

        """ Configure parameters """
        self.configure_parameters()

        """ Connect income """
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals from Expenses panel

        :return: None
        """

        """ Connect date range option checked to actualize date and refresh """
        self.ui_setup.this_year_expenses.clicked.connect(self.change_date_range)
        self.ui_setup.last_12_months_expenses.clicked.connect(self.change_date_range)
        self.ui_setup.previous_year_expenses.clicked.connect(self.change_date_range)

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

        """ Configure combobox for category """
        self.ui_setup.expenses_choice.setView(QListView())
        self.ui_setup.expenses_choice.setStyleSheet("QListView {"
                                                    "font-size: 11pt;"
                                                    "font-family: \"Roboto\";"
                                                    "}"
                                                    "QComboBox QAbstractItemView::item\n"
                                                    "{\n"
                                                    "	min-height: 25px;\n"
                                                    "}\n"
                                                    )
        self.ui_setup.expenses_choice.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.ui_setup.expenses_choice.view().window().setAttribute(Qt.WA_TranslucentBackground)

    def set_bar_graph(self):
        """
        Initialize bar graph with values stored

        :return: None
        """

        pass

    def configure_parameters(self):
        """
        Configure parameters to look for

        :return: None
        """

        """ Set current date """
        self.ui_setup.dateEdit_expenses_to.setDate(QDate.currentDate())
        self.ui_setup.dateEdit_expenses_from.setDate(QDate.currentDate().addDays(-365))

    def change_date_range(self):
        """
        Change date range according to only option box checked

        :return: None
        """

        """ Get sender """
        sender = self.sender()

        if sender == self.ui_setup.this_year_expenses:
            self.ui_setup.dateEdit_expenses_to.setDate(QDate.currentDate())
            self.ui_setup.dateEdit_expenses_from.setDate(QDate.currentDate().addMonths(-QDate.currentDate().month()+1))
        elif sender == self.ui_setup.last_12_months_expenses:
            self.ui_setup.dateEdit_expenses_to.setDate(QDate.currentDate())
            self.ui_setup.dateEdit_expenses_from.setDate(QDate.currentDate().addDays(-365))
        elif sender == self.ui_setup.previous_year_expenses:
            self.ui_setup.dateEdit_expenses_to.setDate(QDate.currentDate().addMonths(-QDate.currentDate().month()))
            self.ui_setup.dateEdit_expenses_from.setDate(QDate.currentDate().addMonths(-QDate.currentDate().month()-11))
