from PySide2.QtCore import QObject, QCoreApplication
from PySide2.QtWidgets import QWidget, QHBoxLayout

from budgetter.view.widgets.spending_widgets.chart_dashboard_widget import ChartDashboard


class Spending(QObject):
    """
    Spending
    """

    def __init__(self, gui):
        super(Spending, self).__init__()

        """ Store gui """
        self.ui_setup = gui

        """ Chart widget """
        self.chart_widget = ChartDashboard(self.ui_setup.spending)

        """ Configure layout """
        self.configure_layout()

        """ Configure title bar """
        self.configure_title_bar()

    def configure_title_bar(self):
        """
        Configure TitleBar with icon

        :return: None
        """

        """ Set title """
        self.ui_setup.spending.set_title(QCoreApplication.translate("spending", "Spending"))

        """ Hide all widgets in title bar """
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
        layout.setContentsMargins(2, 2, 2, 2)

        self.ui_setup.spending.setWidget(widget)
