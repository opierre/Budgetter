import sys

from PySide2.QtCore import Qt, QRectF, Signal, QRect
from PySide2.QtGui import QPainter, QColor, QPen
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, \
    QStyleOptionButton, QStyle


class CircleCheckbox(QPushButton):
    """
    Circle Button
    """

    def __init__(self, parent=None, _type=None):
        super(CircleCheckbox, self).__init__(parent)

        """ Store type """
        self._type = _type

        """ Set checkable """
        self.setCheckable(True)

        """ Set margins """
        self.setContentsMargins(0, 0, 0, 0)

        """ Set cursors """
        self.setCursor(Qt.PointingHandCursor)

    def set_type(self, _type):
        """
        Change type of radio button
        :param _type: 'Income'/'Expenses'/'Transfer'
        :return: void
        """

        self._type = _type

    def paintEvent(self, event):
        """
        Override paintEvent()
        :param event: paint event
        :return: void
        """

        """ Define new painter """
        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        """ Define opt to retrieve states """
        opt = QStyleOptionButton()
        self.initStyleOption(opt)

        """ Set selected circle color """
        painter.setBrush(Qt.NoBrush)
        if opt.state & QStyle.State_On:
            pen = QPen()
            pen.setWidthF(1.5)
            pen.setColor(QColor("#0190EA"))
            painter.setPen(pen)
        else:
            pen = QPen()
            pen.setWidthF(1.5)
            pen.setColor(QColor("transparent"))
            painter.setPen(pen)

        """ Draw circle """
        rectEllipse = QRectF(self.rect().x(), self.rect().y(),
                             min(self.rect().width(), self.rect().height()) * 2.6 / 3,
                             min(self.rect().width(), self.rect().height()) * 2.6 / 3)

        rectEllipse.moveCenter(self.rect().center())
        painter.drawEllipse(rectEllipse)

        """ Set color according to type """
        painter.setPen(Qt.NoPen)
        if self._type == 'Income' and opt.state & QStyle.State_On:
            painter.setBrush(QColor(109, 210, 48, 255))
        elif self._type == 'Income' and not(opt.state & QStyle.State_Selected):
            painter.setBrush(QColor(109, 210, 48, 128))
        elif self._type == 'Expenses' and opt.state & QStyle.State_On:
            painter.setBrush(QColor(254, 77, 151, 255))
        elif self._type == 'Expenses' and not(opt.state & QStyle.State_Selected):
            painter.setBrush(QColor(254, 77, 151, 128))
        elif self._type == 'Transfer' and opt.state & QStyle.State_On:
            painter.setBrush(QColor(250, 202, 0, 255))
        elif self._type == 'Transfer' and not(opt.state & QStyle.State_Selected):
            painter.setBrush(QColor(250, 202, 0, 128))

        """ Draw circle """
        rectEllipse = QRectF(self.rect().x(), self.rect().y(),
                             min(self.rect().width(), self.rect().height()) * 1.8 / 3,
                             min(self.rect().width(), self.rect().height()) * 1.8 / 3)

        rectEllipse.moveCenter(self.rect().center())
        painter.drawEllipse(rectEllipse)


class ExpensesIncomeTransfer(QWidget):
    """
    Widget to pick Expenses or Income or Transfer option in transaction item
    """

    def __init__(self, parent=None):
        super(ExpensesIncomeTransfer, self).__init__(parent)

        """ Store active type """
        self._active_type = None

        """ Store layout """
        self.layout = QVBoxLayout(self)

        """ Store first button """
        self.top_button = CircleCheckbox(self)

        """ Store second button """
        self.middle_button = CircleCheckbox(self)

        """ Store third button """
        self.bottom_button = CircleCheckbox(self)

        """ Configure widgets """
        self.configure_widgets()

        """ Configure layout """
        self.configure_layout()

        """ Connect all slots and signals """
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals
        :return: void
        """

        """ Connect all typeCliked from buttons """
        self.top_button.clicked.connect(self.handle_click)
        self.middle_button.clicked.connect(self.handle_click)
        self.bottom_button.clicked.connect(self.handle_click)

    def handle_click(self):
        """
        Handle click on one button to deselect others
        :return: void
        """

        sender = self.sender()

        if sender == self.top_button:
            self.top_button.setChecked(True)
            self.middle_button.setChecked(False)
            self.bottom_button.setChecked(False)
        elif sender == self.middle_button:
            self.middle_button.setChecked(True)
            self.top_button.setChecked(False)
            self.bottom_button.setChecked(False)
        elif sender == self.bottom_button:
            self.bottom_button.setChecked(True)
            self.top_button.setChecked(False)
            self.middle_button.setChecked(False)

    def configure_widgets(self):
        """
        Configure both push buttons
        :return: void
        """

        """ Set type """
        self.top_button.set_type("Income")
        self.middle_button.set_type("Expenses")
        self.bottom_button.set_type("Transfer")

    def set_active_type(self, active_type):
        """
        Select one button according to active type parameter
        :param active_type: "Expenses"/"Income"/"Transfer"
        :return: void
        """

        """ Check only middle button """
        self.top_button.setChecked(False)
        self.middle_button.setChecked(True)
        self.bottom_button.setChecked(False)

        if active_type == "Expenses":
            self.middle_button.set_type("Expenses")
            self.top_button.set_type("Income")
            self.bottom_button.set_type("Transfer")
        elif active_type == "Income":
            self.middle_button.set_type("Income")
            self.top_button.set_type("Expenses")
            self.bottom_button.set_type("Transfer")
        else:
            self.middle_button.set_type("Transfer")
            self.top_button.set_type("Income")
            self.bottom_button.set_type("Expenses")

    def configure_layout(self):
        """
        Configure layout
        :return: void
        """

        """ Set contents margin """
        self.layout.setContentsMargins(0, 0, 0, 0)

        """ Set Spacing """
        self.layout.setSpacing(0)

        """ Add widgets to layout """
        self.layout.addWidget(self.top_button)
        self.layout.addWidget(self.middle_button)
        self.layout.addWidget(self.bottom_button)

    def paintEvent(self, event):
        """
        Override paintEvent()
        :param event: event
        :return: void
        """

        painter = QPainter(self)

        """ Configure pen and brush """
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(44, 64, 90, 255))

        """ Paint background """
        painter.drawRoundedRect(self.rect(), 2, 2)


if __name__ == "__main__":
    app = QApplication([])
    widget = ExpensesIncomeTransfer()
    widget.setStyleSheet("background-color: rgba(44, 64, 90, 255);")
    # widget.setFixedWidth(20)
    widget.show()
    sys.exit(app.exec_())
