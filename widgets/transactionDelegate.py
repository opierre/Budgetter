import datetime

from PySide2 import QtCore
from PySide2.QtCore import QSize, Qt, QRect, QRectF, QPointF, QPoint, Signal, QModelIndex
from PySide2.QtGui import QPen, QColor, QPainter, QFont, QFontMetrics, QIcon, QRegion
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QStyledItemDelegate, QPushButton, QStyleOptionButton, QStyle, \
    QApplication, QLineEdit, QWidget, QSpinBox, QStyleOptionFrame

from skeletons.transaction import Ui_transaction


class TransactionDelegate(QStyledItemDelegate):
    """
    Transaction Delegate
    """

    """ Signal emitted on More button click """
    transactionMorePressed = Signal(QModelIndex, QPoint, QRect)

    def __init__(self, parent=None, *args):
        QStyledItemDelegate.__init__(self, parent, *args)

        """ Store editable state """
        self.editable = False

        """ Store font for values """
        self.font = QFont()

        """ More QPushButton """
        self.more = QPushButton()

        """ Store more button rectangle """
        self.rectMore = None
        self.rectName = None

        """ Configure Widgets """
        self.configureWidgets()

    def configureWidgets(self):
        """
        Configure widgets on delegate item
        :return: void
        """

        """ Set names """
        self.more.setObjectName(u"moreTransaction")

        """ Set icon """
        self.more.setIcon(QIcon(":/images/images/more_vert-white-18dp.svg"))

        """ Set background color """
        self.more.setStyleSheet("background-color: transparent;\n")

    def setEditable(self, index):
        """
        Change value of editable index
        :param index: index of editable item
        :return: void
        """

        self.editable = index

    def createEditor(self, parent, option, index):
        """
        Override createEditor
        :param parent: parent
        :param option: option
        :param index: index
        :return: void
        """

        pass

    def setEditorData(self, editor, index):
        """
        Override setEditorData()
        :param editor: editor
        :param index: index
        :return: void
        """

        transaction = index.model().data(index, Qt.DisplayRole)

        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)

        editor.setFont(self.font)

        editor.setText(transaction[0])

    def setModelData(self, editor, model, index):
        """
        Override setModelData()
        :param editor: editor
        :param model: model
        :param index: index
        :return: void
        """

        text = editor.text()

        model.setData(index, [text, "Restaurants", 25.99, "20/02/2020", "Compte Chèque", "Income", False],
                      Qt.DisplayRole)

    def updateEditorGeometry(self, editor, option, index):
        """
        Override updateEditorGeometry()
        :param editor: editor
        :param option: option
        :param index: index
        :return: void
        """

        editor.setGeometry(option.rect.x()+0, option.rect.y()-0,
                           option.rect.width(), option.rect.height())

    def editorEvent(self, event, model, option, index):
        """
        Override editorEvent to handle events
        :param event: event
        :param model: model
        :param option: option
        :param index: index
        :return: bool
        """

        """ Reset cursor shape """
        QApplication.restoreOverrideCursor()

        if event.type() == QtCore.QEvent.MouseButtonRelease:
            """ Store position on click """
            cursorPosition = event.pos()

            if self.rectMore.contains(cursorPosition):
                """ Emit pressed signal with model's index and cursor position """
                print(self.rectName)
                self.transactionMorePressed.emit(index, cursorPosition, self.rectName)
                return True
            else:
                return False

        elif event.type() == QtCore.QEvent.MouseMove:
            """ Store position on click """
            cursorPosition = event.pos()

            if self.rectMore.contains(cursorPosition):
                """ Change cursor to pointing hand """
                QApplication.setOverrideCursor(Qt.PointingHandCursor)
                return True
            elif self.rectName.contains(cursorPosition) and self.editable == index:
                """ Change cursor to pointing hand """
                QApplication.setOverrideCursor(Qt.PointingHandCursor)
                return True
            else:
                """ Reset cursor shape """
                QApplication.restoreOverrideCursor()
                return True

        elif event.type() == QtCore.QEvent.KeyPress:
            return True
        else:
            return False

    def sizeHint(self, optionQStyleOptionViewItem, index):
        """
        Override sizeHint
        :param optionQStyleOptionViewItem: optionQStyleOptionViewItem
        :param index: index
        :return: QSize(10, 70)
        """

        return QSize(10, 70)

    def paint(self, painter, option, index):
        """
        Override paint
        :param painter: painter
        :param option: option
        :param index: index
        :return: void
        """

        painter.save()

        """ Get values """
        value = index.data(Qt.DisplayRole)
        name = str(value[0])
        category = str(value[1])
        amount = value[2]
        amount = "{:,.2f}".format(amount).replace(",", " ") + " €"
        date = str(value[3])
        date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%d %b %Y')
        account = str(value[4])
        expOrInc = str(value[5])

        """ Draw bottom border """
        painter.setPen(QPen(QColor("#344457")))
        painter.setBrush(Qt.NoBrush)
        painter.drawLine(option.rect.x()+20, option.rect.y()+option.rect.height()-1,
                         option.rect.width()-20, option.rect.y()+option.rect.height()-1)

        painter.setRenderHint(QPainter.Antialiasing)

        """ Draw item background """
        painter.setPen(QPen(QColor("#26374C")))
        rectBackground = QRect(option.rect.x()+20, option.rect.y()+12,
                               option.rect.width()-40, option.rect.height()-25)
        if self.editable != index:
            painter.setBrush(QColor("transparent"))
            painter.drawRect(rectBackground)
        else:
            painter.setBrush(QColor("#1A537D"))
            painter.drawRect(rectBackground.x()-10, rectBackground.y()-10,
                             rectBackground.width()+20, rectBackground.height()+20)

        """ Draw left icon background """
        painter.setPen(QPen(QColor("#21405D")))
        painter.setBrush(QColor("#21405D"))
        rectIcon = QRect(option.rect.x()+20, option.rect.y()+12,
                         option.rect.x()+45, option.rect.height()-25)
        painter.drawRoundedRect(rectIcon, 1.0, 1.0)

        """ Draw icon and render svg """
        painter.setPen(QPen(Qt.transparent))
        painter.setBrush(QColor("transparent"))
        rectSvg = QRect(rectIcon.x()+10, rectIcon.y()+10,
                        rectIcon.width()-20, rectIcon.height()-20)
        painter.drawRect(rectSvg)

        if category == "Restaurants":
            svgRender = QSvgRenderer(":/images/images/restaurant-white-18dp_outlined.svg")
        elif category == "Transport":
            svgRender = QSvgRenderer(":/images/images/directions_car-white-18dp_outlined.svg")
        elif category == "Groceries":
            svgRender = QSvgRenderer(":/images/images/local_grocery_store-white-18dp_outlined.svg")
        svgRender.setAspectRatioMode(Qt.KeepAspectRatio)
        svgRender.render(painter, rectSvg)

        """ Set font on painter for name """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        """ Set category painter color """
        painter.setPen(QPen(Qt.white))
        painter.setBrush(QColor(Qt.transparent))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width(name)
        pixelsHeight = fontMetrics.height()

        """ Set name on top """
        self.rectName = QRect(rectIcon.width()+35, rectIcon.y(),
                              pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rectName, Qt.AlignLeft | Qt.AlignVCenter | Qt.AlignVCenter, name)

        #     optionMore = QStyleOptionFrame()
        #     optionMore.initFrom(self.name)
        #     optionMore.rect = self.rectName
        #     optionMore.state = optionMore.state or QStyle.State_Sunken
        #
        #     self.name.style().drawPrimitive(QStyle.PE_PanelLineEdit, optionMore, painter, self.name)
            # self.name.setReadOnly(False)
            # self.name.resize(self.rectName.size())
            # self.name.setText("Test")
            # painter.translate(self.rectName.topLeft())
            # self.name.render(painter, QPoint(), QRegion(), QWidget.DrawChildren)

        """ Set font on painter for category """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set category pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width(category)
        pixelsHeight = fontMetrics.height()

        """ Set category beside name """
        painter.drawText(rectIcon.width() + 35, rectIcon.y()+25,
                         pixelsWidth, pixelsHeight,
                         Qt.AlignLeft | Qt.AlignVCenter, category)

        """ Set font on painter for amount """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        """ Set amount pen color """
        painter.setPen(QPen(QColor("white")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsHeight = fontMetrics.height()
        pixelsWidth = fontMetrics.width(amount)

        """ Set amount on right corner """
        rectAmount = QRect(rectIcon.x()+rectIcon.width()+230, rectIcon.y()+2,
                           pixelsWidth, pixelsHeight)
        painter.drawText(rectAmount, Qt.AlignLeft | Qt.AlignVCenter, amount)

        """ Set font on painter for percentage """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set percentage pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsHeight = fontMetrics.height()

        """ Set percentage beside amount """
        rectAmountLabel = QRect(rectIcon.x()+rectIcon.width()+230, rectIcon.y()+27,
                                60, pixelsHeight)
        painter.drawText(rectAmountLabel, Qt.AlignLeft | Qt.AlignVCenter, "Amount")

        """ Set font on painter for date """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        """ Set date pen color """
        painter.setPen(QPen(QColor("white")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsHeight = fontMetrics.height()
        pixelsWidth = fontMetrics.width(date)

        """ Set date on right corner """
        rectDate = QRect(rectIcon.x() + rectIcon.width() + 2*230, rectIcon.y() + 2,
                         pixelsWidth, pixelsHeight)
        painter.drawText(rectDate, Qt.AlignLeft | Qt.AlignVCenter, date)

        """ Set font on painter for date """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set date pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsHeight = fontMetrics.height()

        """ Set date beside amount """
        rectDateLabel = QRect(rectIcon.x() + rectIcon.width() + 2*230, rectIcon.y() + 27,
                              60, pixelsHeight)
        painter.drawText(rectDateLabel, Qt.AlignLeft | Qt.AlignVCenter, "Date")

        """ Set font on painter for date """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        """ Set date pen color """
        painter.setPen(QPen(QColor("white")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsHeight = fontMetrics.height()
        pixelsWidth = fontMetrics.width(account)

        """ Set account on right corner """
        rectAccount = QRect(rectIcon.x() + rectIcon.width() + 3*230+20, rectIcon.y() + 2,
                            pixelsWidth, pixelsHeight)
        painter.drawText(rectAccount, Qt.AlignLeft | Qt.AlignVCenter, account)

        """ Set font on painter for date """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set date pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsHeight = fontMetrics.height()

        """ Set account label beside account """
        rectAccountLabel = QRect(rectIcon.x() + rectIcon.width() + 3*230+20, rectIcon.y() + 27,
                                 70, pixelsHeight)
        painter.drawText(rectAccountLabel, Qt.AlignLeft | Qt.AlignVCenter, "Account")

        """ Set font on painter for income/expense """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        """ Set income/expense pen color """
        pen = QPen(QColor("#1B5179"))
        pen.setWidthF(1)
        painter.setPen(pen)

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsHeight = fontMetrics.height()
        pixelsWidth = fontMetrics.width(expOrInc)

        """ Set income/expense on right corner """
        rectInOrOut = QRectF(rectBackground.width()+rectBackground.x()-55.5-pixelsWidth-45,
                             rectIcon.y()+(rectIcon.width()-pixelsHeight-8)/2.0,
                             pixelsWidth+45, pixelsHeight+8)

        painter.drawRoundedRect(rectInOrOut, 4.0, 4.0)

        painter.setPen(QPen(QColor("white")))
        painter.drawText(rectInOrOut.x()+35, rectInOrOut.y()+5.0,
                         pixelsWidth, pixelsHeight,
                         Qt.AlignLeft | Qt.AlignVCenter, expOrInc)

        painter.setPen(Qt.NoPen)
        if expOrInc == "Income":
            painter.setBrush(QColor("#6DD230"))
        else:
            painter.setBrush(QColor("#FE4D97"))
        painter.drawEllipse(QPointF(rectInOrOut.x()+17.5, rectInOrOut.y()+4.5+pixelsHeight/2.0),
                            (pixelsHeight+8)/5.0,
                            (pixelsHeight+8)/5.0)

        pen = QPen(QColor("#1B5179"))
        pen.setWidthF(1)
        painter.setPen(pen)
        painter.setBrush(QColor("transparent"))

        """ Buttons rects """
        self.rectMore = QRect(rectBackground.width()+rectBackground.x()-26, rectInOrOut.y(),
                              25, rectInOrOut.height())

        optionMore = QStyleOptionButton()
        optionMore.initFrom(self.more)
        optionMore.rect = self.rectMore
        optionMore.icon = self.more.icon()
        optionMore.iconSize = QtCore.QSize(22, 22)
        optionMore.state = optionMore.state or QStyle.State_MouseOver

        self.more.style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.more)

        painter.restore()

