from PySide2.QtCore import QObject, QCoreApplication, QDate, Qt
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

        """ Configure panel """
        self.configure_panel()

        """ Configure parameters """
        self.configure_parameters()

        """ Connect income """
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals from Income panel

        :return: None
        """

        """ Connect date range option checked to actualize date and refresh """
        self.ui_setup.this_year_income.clicked.connect(self.change_date_range)
        self.ui_setup.last_12_months_income.clicked.connect(self.change_date_range)
        self.ui_setup.previous_year_income.clicked.connect(self.change_date_range)

    def configure_panel(self):
        """
        Configure panel look and field

        :return: None
        """

        """ Configure combobox for category """
        self.ui_setup.income_choice.setView(QListView())
        self.ui_setup.income_choice.setStyleSheet("QListView {"
                                                    "font-size: 11pt;"
                                                    "font-family: \"Roboto\";"
                                                    "}"
                                                    "QComboBox QAbstractItemView::item\n"
                                                    "{\n"
                                                    "	min-height: 25px;\n"
                                                    "}\n")
        self.ui_setup.income_choice.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.ui_setup.income_choice.view().window().setAttribute(Qt.WA_TranslucentBackground)

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
        self.ui_setup.dateEdit_income_from.setDate(QDate.currentDate().addDays(-365))

    def change_date_range(self):
        """
        Change date range according to only option box checked

        :return: None
        """

        """ Get sender """
        sender = self.sender()

        if sender == self.ui_setup.this_year_income:
            self.ui_setup.dateEdit_income_to.setDate(QDate.currentDate())
            self.ui_setup.dateEdit_income_from.setDate(QDate.currentDate().addMonths(-QDate.currentDate().month()+1))
        elif sender == self.ui_setup.last_12_months_income:
            self.ui_setup.dateEdit_income_to.setDate(QDate.currentDate())
            self.ui_setup.dateEdit_income_from.setDate(QDate.currentDate().addDays(-365))
        elif sender == self.ui_setup.previous_year_income:
            self.ui_setup.dateEdit_income_to.setDate(QDate.currentDate().addMonths(-QDate.currentDate().month()))
            self.ui_setup.dateEdit_income_from.setDate(QDate.currentDate().addMonths(-QDate.currentDate().month()-11))
