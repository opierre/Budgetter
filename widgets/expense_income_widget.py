import sys

from PySide2.QtCore import Qt, QRectF, QSize
from PySide2.QtGui import QPainter, QColor, QPen
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMainWindow, QApplication, QRadioButton, \
    QStyleOptionButton, QStyle, QProxyStyle


class RadioButtonStyle(QProxyStyle):
    """
    Radio Button Style - Center indicator/focus rect/click rect
    """

    def subElementRect(self, element, option, widget):
        """
        Override subElementRect()
        :param element: element
        :param option: option
        :param widget: widget
        :return: QRect
        """

        """ Get default rect """
        rect = super().subElementRect(element, option, widget)

        """ Center rect for indicator/focus rect/click rect """
        if element in (
            QStyle.SE_RadioButtonIndicator,
            QStyle.SE_RadioButtonFocusRect,
            QStyle.SE_RadioButtonClickRect,
        ):
            rect.moveCenter(option.rect.center())

        return rect


class ExpOrIncRadio(QRadioButton):
    """
    Expenses or Income Radio Button
    """

    def __init__(self, parent=None, expOrInc=None):
        super(ExpOrIncRadio, self).__init__(parent)

        """ Store type """
        self.expOrInc = expOrInc

        """ Overwrite style """
        self.setStyle(RadioButtonStyle())

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
        elif self.expOrInc == 'Income' and opt.state & QStyle.State_Off:
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(109, 210, 48, 128))
        elif self.expOrInc == 'Expenses' and opt.state & QStyle.State_On:
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(254, 77, 151, 255))
        elif self.expOrInc == 'Expenses' and opt.state & QStyle.State_Off:
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(254, 77, 151, 128))

        """ Draw circle """
        rectEllipse = QRectF(self.rect().x(), self.rect().y(),
                             min(self.rect().width(), self.rect().height()) * 1.8 / 3,
                             min(self.rect().width(), self.rect().height()) * 1.8 / 3)
        rectEllipse.moveCenter(self.rect().center())
        painter.drawEllipse(rectEllipse)


class ExpensesOrIncome(QWidget):
    """
    Widget to pick Expenses or Income option in transaction item
    """

    def __init__(self, parent=None):
        super(ExpensesOrIncome, self).__init__(parent)

        """ Store layout """
        self.layout = QHBoxLayout(self)

        """ Store left button """
        self.incomeButton = ExpOrIncRadio("a")

        """ Store right button """
        self.expensesButton = ExpOrIncRadio("b")

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

        """ Set cursor """
        self.incomeButton.setCursor(Qt.PointingHandCursor)
        self.expensesButton.setCursor(Qt.PointingHandCursor)

    def configureLayout(self):
        """
        Configure layout
        :return: void
        """

        """ Set contents margin """
        self.layout.setContentsMargins(0, 0, 0, 0)

        """ Set Spacing """
        self.layout.setSpacing(1)

        """ Add widgets to layout """
        self.layout.addWidget(self.incomeButton)
        self.layout.addWidget(self.expensesButton)


if __name__ == "__main__":
    app = QApplication([])
    widget = ExpensesOrIncome()
    widget.setStyleSheet("background-color: #1A537D;")
    # widget.setFixedSize(QSize(200, 200))
    widget.show()
    sys.exit(app.exec_())
