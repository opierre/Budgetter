import time

from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QObject, QCoreApplication, QDate, Qt, QUrl, QTimer
from PySide2.QtGui import QPainter
from PySide2.QtSvg import QSvgWidget
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QListView, QWidget, QVBoxLayout, QApplication

from view.widgets.bar_widgets.category_chart_widget import CategoryChart


class Income(QObject):
    """
    Income
    """

    def __init__(self, gui):
        super(Income, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ Store chart view """
        self.chart = CategoryChart("Income")
        self.chart_view = QtCharts.QChartView(self.chart)

        """ Configure title bar """
        self.configure_title_bar()

        """ Configure panel """
        self.configure_panel()

        """ Configure parameters """
        self.configure_parameters()

        """ Configure layout """
        self.configure_layout()

        self.set_values({})

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

        """ Configure chart view """
        self.chart_view.setRenderHint(QPainter.Antialiasing)

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

        """ Set webview to display animated icon """
        self.button = QSvgWidget()
        # self.button.page().setBackgroundColor(Qt.transparent)
        # self.button.setStyleSheet("background-color: transparent;")
        self.button.load(r"C:\Users\Pierre\Downloads\frames_searchtoclose\60fps\frame00.svg")
        self.ui_setup.refresh_income.layout().addWidget(self.button)
        QTimer.singleShot(3000, self.update_animation)
        QTimer.singleShot(6000, self.update_animation)

    def update_animation(self):
        for index in range(0, 61):
            time.sleep(0.016)
            self.button.load(r"C:\Users\Pierre\Downloads\frames_searchtoclose\60fps\frame" + f"{index:02}" + ".svg")
            QApplication.processEvents()


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
        layout = QVBoxLayout(widget)
        layout.setSpacing(0)
        layout.addWidget(self.chart_view)
        layout.setContentsMargins(0, 0, 0, 0)

        self.ui_setup.widget_income_graph.setLayout(QVBoxLayout())
        self.ui_setup.widget_income_graph.layout().setContentsMargins(0, 0, 0, 0)
        self.ui_setup.widget_income_graph.layout().addWidget(widget)

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

    def set_values(self, values: dict):
        """
        Set values on series

        :param values: values to set as dict
        :return: None
        """

        values = {"01-2020": 4235.23,
                  "02-2020": 4565.23,
                  "03-2020": 5454.34,
                  "04-2020": 5674.76,
                  "05-2020": 7345.87,
                  "06-2020": 8340.89,
                  "07-2020": 8957.54,
                  "08-2020": 11100.34,
                  "09-2020": 11550.12,
                  "10-2020": 11567.87,
                  "11-2020": 11978.78,
                  "12-2020": 12010.98,
                  "01-2021": 12056,
                  "02-2021": 13450.12,
                  "03-2021": 15469.35,
                  "04-2021": 14356.00,
                  "05-2021": 25098.63,
                  "06-2021": 26098.57,
                  "07-2021": 22054.00,
                  "08-2021": 22000.45}

        """ Set values on chat """
        self.chart.set_values(values)
