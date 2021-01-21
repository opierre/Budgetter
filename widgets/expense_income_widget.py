import sys

from PySide2.QtCore import Qt, QRectF, QPointF
from PySide2.QtGui import QPainter, QColor
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication, \
    QStyleOptionButton, QStyle


class ExpOrIncRadio(QPushButton):
    """
    Expenses or Income Radio Button
    """

    def __init__(self, parent=None, expOrInc=None):
        super(ExpOrIncRadio, self).__init__(parent)

        """ Store type """
        self.expOrInc = expOrInc

        self.setAutoExclusive(True)
        self.setCheckable(True)

        self.setContentsMargins(0, 0, 0, 0)

    def setType(self, typeToSet):
        """
        Change type of radio button
        :param typeToSet: 'Income'/'Expenses'
        :return: void
        """

        self.expOrInc = typeToSet

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

        """ Set color according to type """
        if self.expOrInc == 'Income' and opt.state & QStyle.State_On:
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(109, 210, 48, 255))
        elif self.expOrInc == 'Income' and not(opt.state & QStyle.State_Selected):
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(109, 210, 48, 128))
        elif self.expOrInc == 'Expenses' and opt.state & QStyle.State_On:
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(254, 77, 151, 255))
        elif self.expOrInc == 'Expenses' and not(opt.state & QStyle.State_Selected):
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(254, 77, 151, 128))

        """ Draw circle """
        rectEllipse = QRectF(self.rect().x(), self.rect().y(),
                             min(self.rect().width(), self.rect().height()) * 1.8 / 3,
                             min(self.rect().width(), self.rect().height()) * 1.8 / 3)
        # rectEllipse = QRectF(self.rect().x(), self.rect().y(),
        #                      2,
        #                      2)
        rectEllipse.moveCenter(self.rect().center())
        # painter.drawEllipse(rectEllipse)

        self.resize(20, 20)
        painter.setPen(QColor("red"))
        painter.drawRect(self.rect())


class ExpensesOrIncome(QWidget):
    """
    Widget to pick Expenses or Income option in transaction item
    """

    def __init__(self, parent=None):
        super(ExpensesOrIncome, self).__init__(parent)

        """ Store layout """
        self.layout = QHBoxLayout(self)

        """ Store left button """
        self.incomeButton = ExpOrIncRadio(self)

        """ Store right button """
        self.expensesButton = ExpOrIncRadio(self)

        """ Configure widgets """
        self.configureWidgets()

        """ Configure layout """
        self.configureLayout()

    def configureWidgets(self):
        """
        Configure both push buttons
        :return: void
        """

        """ Set type """
        self.incomeButton.setType("Income")
        self.expensesButton.setType("Expenses")

    def configureLayout(self):
        """
        Configure layout
        :return: void
        """

        """ Set contents margin """
        self.layout.setContentsMargins(0, 0, 0, 0)

        """ Set Spacing """
        self.layout.setSpacing(0)

        """ Add widgets to layout """
        self.layout.addWidget(self.incomeButton)
        self.layout.addWidget(self.expensesButton)


if __name__ == "__main__":
    app = QApplication([])
    widget = ExpensesOrIncome()
    widget.setStyleSheet("background-color: #1A537D;")
    # widget.setFixedWidth(20)
    widget.show()
    sys.exit(app.exec_())
