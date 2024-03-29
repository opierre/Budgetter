from PySide6.QtCore import QObject, QCoreApplication, Qt, QDate
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QListView,
    QWidget,
    QVBoxLayout,
    QApplication,
    QGraphicsDropShadowEffect,
)

from budgetter.view.widgets.bar_widgets.chart_bars_widget import ChartBars


class Expenses(QObject):
    """
    Expenses
    """

    def __init__(self, gui):
        super().__init__()

        # Store gui
        self.ui_setup = gui

        # Store chart bars widget
        self.chart_widget = ChartBars("Expenses", self.ui_setup.expenses)

        # Store drop shadow effect
        self.shadow_effect = QGraphicsDropShadowEffect(self)

        # Store range options
        self.this_year_option = {
            "to": QDate.currentDate(),
            "from": QDate.currentDate().addMonths(-QDate.currentDate().month() + 1),
        }
        self.last_12_months = {
            "to": QDate.currentDate(),
            "from": QDate.currentDate().addDays(-365),
        }
        self.previous_year = {
            "to": QDate.currentDate().addMonths(-QDate.currentDate().month()),
            "from": QDate.currentDate().addMonths(-QDate.currentDate().month() - 11),
        }

        # Configure title bar
        self.configure_title_bar()

        # Configure panel
        self.configure_panel()

        # Configure parameters
        self.configure_parameters()

        # Configure layout
        self.configure_layout()

        self.set_values({})

        # Connect income
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals from Expenses panel

        :return: None
        """

        # Connect date range option checked to actualize date and refresh
        self.ui_setup.this_year_expenses.clicked.connect(self.change_date_option)
        self.ui_setup.last_12_months_expenses.clicked.connect(self.change_date_option)
        self.ui_setup.previous_year_expenses.clicked.connect(self.change_date_option)

        # Connect manual change to deselect range options
        self.ui_setup.dateEdit_expenses_from.dateChanged.connect(
            self.update_range_option
        )
        self.ui_setup.dateEdit_expenses_to.dateChanged.connect(self.update_range_option)

        # Connect click on refresh button
        self.ui_setup.refresh_expenses.clicked.connect(self.refresh)

        # Connect show labels checked to display labels
        self.ui_setup.check_labels_expenses.clicked.connect(self.show_labels)

        # Connect show average to display line on graph
        self.ui_setup.check_average_expenses.toggled.connect(
            self.chart_widget.show_average
        )

        # Connect show total to display total amount on graph view
        self.ui_setup.check_total_expenses.toggled.connect(self.chart_widget.show_total)

    def configure_title_bar(self):
        """
        Configure TitleBar with icon

        :return: None
        """

        # Set title
        self.ui_setup.expenses.set_title(
            QCoreApplication.translate("graphs", "Expenses")
        )

        # Hide all widgets in title bar
        self.ui_setup.expenses.disable_title_bar_button()
        self.ui_setup.expenses.disable_search_bar()

    def configure_layout(self):
        """
        Configure layout inside of Container

        :return: None
        """

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(0)
        layout.addWidget(self.chart_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.ui_setup.widget_expenses_graph.setLayout(QVBoxLayout())
        self.ui_setup.widget_expenses_graph.layout().setContentsMargins(0, 0, 0, 0)
        self.ui_setup.widget_expenses_graph.layout().addWidget(widget)

    def configure_panel(self):
        """
        Configure widgets' panel

        :return: None
        """

        # Configure combobox for category
        self.ui_setup.expenses_choice.setView(QListView())
        self.ui_setup.expenses_choice.setStyleSheet(
            "QListView {"
            "font-size: 11pt;"
            'font-family: "Roboto";'
            "}"
            "QComboBox QAbstractItemView::item\n"
            "{\n"
            "	min-height: 25px;\n"
            "}\n"
        )
        self.ui_setup.expenses_choice.view().window().setWindowFlags(
            Qt.Popup | Qt.FramelessWindowHint
        )
        self.ui_setup.expenses_choice.view().window().setAttribute(
            Qt.WA_TranslucentBackground
        )

        # Set widget to display animated icon
        self.ui_setup.refresh_expenses.set_animation_type("bars_purple")

        # Configure effect
        self.shadow_effect.setBlurRadius(3)
        self.shadow_effect.setOffset(5)
        self.shadow_effect.setColor(QColor(28, 41, 59, 128))
        self.ui_setup.widget_expenses.setGraphicsEffect(self.shadow_effect)

    def configure_parameters(self):
        """
        Configure parameters to look for

        :return: None
        """

        # Set current date
        self.ui_setup.dateEdit_expenses_to.setDate(QDate.currentDate())
        self.ui_setup.dateEdit_expenses_from.setDate(QDate.currentDate().addDays(-365))

    def change_date_option(self):
        """
        Change date range according to only option box checked

        :return: None
        """

        # Get sender
        sender = self.sender()

        # Disconnect signals to avoid conflicts
        self.ui_setup.dateEdit_expenses_from.dateChanged.disconnect(
            self.update_range_option
        )
        self.ui_setup.dateEdit_expenses_to.dateChanged.disconnect(
            self.update_range_option
        )

        if sender == self.ui_setup.this_year_expenses:
            self.ui_setup.dateEdit_expenses_to.setDate(self.this_year_option["to"])
            self.ui_setup.dateEdit_expenses_from.setDate(self.this_year_option["from"])
        elif sender == self.ui_setup.last_12_months_expenses:
            self.ui_setup.dateEdit_expenses_to.setDate(self.last_12_months["to"])
            self.ui_setup.dateEdit_expenses_from.setDate(self.last_12_months["from"])
        elif sender == self.ui_setup.previous_year_expenses:
            self.ui_setup.dateEdit_expenses_to.setDate(self.previous_year["to"])
            self.ui_setup.dateEdit_expenses_from.setDate(self.previous_year["from"])

        # Refresh bars
        self.refresh()

        # Re-connect signals to avoid conflicts
        self.ui_setup.dateEdit_expenses_from.dateChanged.connect(
            self.update_range_option
        )
        self.ui_setup.dateEdit_expenses_to.dateChanged.connect(self.update_range_option)

    def update_range_option(self):
        """
        Update range option (select/deselect)

        :return: None
        """

        # Retrieve dates
        from_date = self.ui_setup.dateEdit_expenses_from.date()
        to_date = self.ui_setup.dateEdit_expenses_to.date()

        # Compare dates to each range option
        if (
                from_date == self.this_year_option["from"]
                and to_date == self.this_year_option["to"]
        ):
            self.ui_setup.this_year_expenses.setChecked(True)
        elif (
                from_date == self.last_12_months["from"]
                and to_date == self.last_12_months["to"]
        ):
            self.ui_setup.last_12_months_expenses.setChecked(True)
        elif (
                from_date == self.previous_year["from"]
                and to_date == self.previous_year["to"]
        ):
            self.ui_setup.previous_year_expenses.setChecked(True)
        else:
            self.ui_setup.this_year_expenses.setAutoExclusive(False)
            self.ui_setup.this_year_expenses.setChecked(False)
            self.ui_setup.this_year_expenses.setAutoExclusive(True)
            self.ui_setup.last_12_months_expenses.setAutoExclusive(False)
            self.ui_setup.last_12_months_expenses.setChecked(False)
            self.ui_setup.last_12_months_expenses.setAutoExclusive(True)
            self.ui_setup.previous_year_expenses.setAutoExclusive(False)
            self.ui_setup.previous_year_expenses.setChecked(False)
            self.ui_setup.previous_year_expenses.setAutoExclusive(True)

    def refresh(self):
        """
        Refresh displayed values

        :return: None
        """

        # Start animation
        self.ui_setup.refresh_expenses.start(1)
        QApplication.processEvents()

        values = {
            "01-2020": 4235.23,
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
            "09-2021": 22000.45,
            "10-2021": 20012.45,
            "11-2021": 18042.45,
        }

        final_values = {}
        for key, value in values.items():
            date = QDate.fromString(key, "MM-yyyy")
            if (
                    self.ui_setup.dateEdit_expenses_from.date()
                    <= date
                    <= self.ui_setup.dateEdit_expenses_to.date()
            ):
                final_values.update({key: value})

        # Set date range
        self.chart_widget.set_values(final_values)

    def set_values(self, values_to_set: dict):
        """
        Set values on series

        :param values_to_set: values to set as dict
        :return: None
        """

        values = {
            "01-2020": 4235.23,
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
            "08-2021": 22000.45,
        }

        # Set values on chat
        self.chart_widget.set_values(values)

    def show_labels(self, checked: bool):
        """
        Display labels on bars

        :param checked: True/False
        :return: None
        """

        self.chart_widget.show_labels(checked)
