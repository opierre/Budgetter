from PySide6.QtCore import QObject, QCoreApplication
from PySide6.QtWidgets import QWidget, QHBoxLayout

from budgetter.view.widgets.spending_widgets.chart_dashboard_widget import ChartDashboard


class Spending(QObject):
    """
    Spending
    """

    def __init__(self, gui):
        super().__init__()

        # Store gui
        self.ui_setup = gui

        # Chart widget
        self.chart_widget = ChartDashboard(self.ui_setup.spending)

        # Configure layout
        self.configure_layout()

        # Configure title bar
        self.configure_title_bar()

    def configure_title_bar(self):
        """
        Configure TitleBar with icon

        :return: None
        """

        # Set title
        self.ui_setup.spending.set_title(QCoreApplication.translate("spending", "Spending"))

        # Hide all widgets in title bar
        self.ui_setup.spending.disable_title_bar_button()
        self.ui_setup.spending.disable_search_bar()

    def configure_layout(self):
        """
        Configure layout inside of Container

        :return: None
        """

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setSpacing(0)
        layout.addWidget(self.chart_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.ui_setup.spending.setWidget(widget)

    def update_spending(self, spending: dict):
        """
        Update spending details

        :param spending: spending info
        :return: None
        """

        spending_sorted = []
        for month, amount in spending.items():
            spending_sorted.append(amount)
        self.chart_widget.update_values(spending_sorted)
