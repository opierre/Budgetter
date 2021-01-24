import datetime

from PySide2 import QtCore
from PySide2.QtCore import QSize, Qt, QRect, QRectF, QPointF, Signal, QModelIndex
from PySide2.QtGui import QPen, QColor, QPainter, QFont, QFontMetrics, QIcon
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QStyledItemDelegate, QPushButton, QStyleOptionButton, QStyle, \
    QApplication


class TransactionDelegate(QStyledItemDelegate):
    """
    Transaction Delegate
    """

    """ Signal emitted on Edit button click """
    transactionEditPressed = Signal(QModelIndex, QRect, QRect, QRect, QRect, QRectF)

    """ Signal emitted on Delete button click """
    transactionDeletePressed = Signal(QModelIndex)

    def __init__(self, parent=None, *args):
        QStyledItemDelegate.__init__(self, parent, *args)

        """ Store editable state """
        self.editable = False

        """ Store font for values """
        self.font = QFont()

        """ Edit/Delete QPushButtons """
        self.edit = QPushButton()
        self.delete = QPushButton()

        """ Store buttons rectangle """
        self.rectEdit = None
        self.rectDelete = None
        self.rectName = None
        self.rectAmount = None
        self.rectDate = None
        self.rectAccount = None
        self.rectExpOrInc = None

        """ Configure Widgets """
        self.configureWidgets()

    def configureWidgets(self):
        """
        Configure widgets on delegate item
        :return: void
        """

        """ Set names """
        self.edit.setObjectName(u"editTransaction")
        self.edit.setObjectName(u"deleteTransaction")

        """ Set icon """
        self.edit.setIcon(QIcon(":/images/images/edit-white-18dp.svg"))
        self.delete.setIcon(QIcon(":/images/images/delete-white-18dp.svg"))

        """ Set background color """
        self.edit.setStyleSheet("background-color: transparent;\n")
        self.delete.setStyleSheet("background-color: transparent;\n")

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

            if self.rectEdit.contains(cursorPosition):
                """ Emit pressed signal with model's index and rect position """
                self.transactionEditPressed.emit(index, self.rectName, self.rectAmount, self.rectDate, self.rectAccount,
                                                 self.rectExpOrInc)
                return True
            elif self.rectDelete.contains(cursorPosition):
                """ Emit pressed signal with model's index """
                self.transactionDeletePressed.emit(index)
                return True
            else:
                return False

        elif event.type() == QtCore.QEvent.MouseMove:
            """ Store position on click """
            cursorPosition = event.pos()

            if self.rectEdit.contains(cursorPosition):
                """ Change cursor to pointing hand """
                QApplication.setOverrideCursor(Qt.PointingHandCursor)
                return True
            elif self.rectDelete.contains(cursorPosition):
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
        painter.drawLine(option.rect.x()+option.rect.width()*1/60, option.rect.y()+option.rect.height()-1,
                         option.rect.width()-option.rect.width()*1/60, option.rect.y()+option.rect.height()-1)

        painter.setRenderHint(QPainter.Antialiasing)

        """ Draw item background """
        painter.setPen(QPen(QColor("#26374C")))
        rectBackground = QRect(option.rect.x()+option.rect.width()*1/60, option.rect.y()+option.rect.height()*1/5,
                               option.rect.width()-option.rect.width()*2/60, option.rect.height()-option.rect.height()*2/5)
        if self.editable != index:
            painter.setBrush(QColor("transparent"))
            painter.drawRect(rectBackground)
        else:
            painter.setBrush(QColor("#1A537D"))
            painter.drawRect(rectBackground.x(), rectBackground.y()-option.rect.height()*1/6,
                             rectBackground.width(), rectBackground.height()+option.rect.height()*2/6)

        """ Draw left icon background """
        painter.setPen(QPen(QColor("#21405D")))
        painter.setBrush(QColor("#21405D"))
        rectIcon = QRect(rectBackground.x()+option.rect.width()*1/120, rectBackground.y()-option.rect.height()*1/30,
                         rectBackground.height()+option.rect.height()*2/30, rectBackground.height()+option.rect.height()*2/30)
        painter.drawRoundedRect(rectIcon, 1.0, 1.0)

        """ Draw icon and render svg """
        painter.setPen(QPen(Qt.transparent))
        painter.setBrush(QColor("transparent"))
        rectSvg = QRect(rectIcon.x()+10, rectIcon.y()+10,
                        rectIcon.width()-20, rectIcon.height()-20)
        painter.drawRect(rectSvg)

        svgRender = QSvgRenderer(":/images/images/restaurant-white-18dp_outlined.svg")
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
        self.rectName = QRect(rectIcon.x()+rectIcon.width()+option.rect.width()*1/140, rectIcon.y()+option.rect.height()*1/30,
                              pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rectName, Qt.AlignLeft | Qt.AlignVCenter, name)

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
        rectCategory = QRect(self.rectName.x(), self.rectName.y()+self.rectName.height()+option.rect.height()*1/10,
                             pixelsWidth, pixelsHeight)
        painter.drawText(rectCategory, Qt.AlignLeft | Qt.AlignVCenter, category)

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
        self.rectAmount = QRect(rectBackground.width()*1/4, self.rectName.y(),
                                pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rectAmount, Qt.AlignLeft | Qt.AlignVCenter, amount)

        """ Set font on painter for percentage """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set percentage pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width("Amount")
        pixelsHeight = fontMetrics.height()

        """ Set percentage beside amount """
        rectAmountLabel = QRect(rectBackground.width()*1/4, rectCategory.y(),
                                pixelsWidth, pixelsHeight)
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
        self.rectDate = QRect(rectBackground.width()*1.8/4, self.rectName.y(),
                              pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rectDate, Qt.AlignLeft | Qt.AlignVCenter, date)

        """ Set font on painter for date """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set date pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width("Date")
        pixelsHeight = fontMetrics.height()

        """ Set date beside amount """
        rectDateLabel = QRect(rectBackground.width()*1.8/4, rectCategory.y(),
                              pixelsWidth, pixelsHeight)
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
        self.rectAccount = QRect(rectBackground.width()*2.6/4, self.rectName.y(),
                                 pixelsWidth, pixelsHeight)

        if self.editable != index:
            painter.drawText(self.rectAccount, Qt.AlignLeft | Qt.AlignVCenter, account)

        """ Set font on painter for date """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set date pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width("Account")
        pixelsHeight = fontMetrics.height()

        """ Set account label beside account """
        rectAccountLabel = QRect(rectBackground.width()*2.6/4, rectCategory.y(),
                                 pixelsWidth, pixelsHeight)
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
        self.rectExpOrInc = QRectF(rectBackground.width()*3.7/4-pixelsWidth-(pixelsHeight+8)/2.5,
                                   rectIcon.y()+(rectIcon.width()-pixelsHeight-8)/2.0,
                                   pixelsWidth+(pixelsHeight + 8)/2.5+(pixelsHeight+8)/0.9, pixelsHeight+8)

        if self.editable != index:
            painter.drawRoundedRect(self.rectExpOrInc, 4.0, 4.0)

            painter.setPen(QPen(QColor("white")))
            painter.drawText(self.rectExpOrInc.x()+(pixelsHeight + 8) / 0.9, self.rectExpOrInc.y()+5.0,
                             pixelsWidth, pixelsHeight,
                             Qt.AlignLeft | Qt.AlignVCenter, expOrInc)

            painter.setPen(Qt.NoPen)
            if expOrInc == "Income":
                painter.setBrush(QColor("#6DD230"))
            else:
                painter.setBrush(QColor("#FE4D97"))
            rectEllipse = QRectF(self.rectExpOrInc.x()+(pixelsHeight + 8) / 2.5, self.rectExpOrInc.y()+(pixelsHeight + 8) / 3.5,
                                 (pixelsHeight + 8) / 2.5, (pixelsHeight + 8) / 2.5)
            painter.drawEllipse(rectEllipse)
        else:
            """ Set income/expense pen color """
            pen = QPen(QColor("#26374C"))
            pen.setWidthF(1)
            painter.setPen(pen)

            self.rectExpOrInc = QRectF(rectBackground.width() * 3.7 / 4 - pixelsWidth - (pixelsHeight + 8) / 2.5,
                                       rectIcon.y() + (rectIcon.width() - pixelsHeight - 8) / 2.0,
                                       (pixelsWidth + (pixelsHeight + 8) / 2.5 + (pixelsHeight + 8) / 0.9)*2/3,
                                       pixelsHeight + 8)

            painter.drawRoundedRect(self.rectExpOrInc, 4.0, 4.0)

        pen = QPen(QColor("#1B5179"))
        pen.setWidthF(1)
        painter.setPen(pen)
        painter.setBrush(QColor("transparent"))

        """ Button edit """
        self.rectEdit = QRect(rectBackground.width()+rectBackground.x()-rectIcon.x()/1.3, self.rectName.y(),
                              25, self.rectName.height())

        optionMore = QStyleOptionButton()
        optionMore.initFrom(self.edit)
        optionMore.rect = self.rectEdit
        optionMore.icon = self.edit.icon()
        optionMore.iconSize = QtCore.QSize(18, 18)
        optionMore.state = optionMore.state or QStyle.State_MouseOver

        self.edit.style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.edit)

        """ Buttons rects """
        self.rectDelete = QRect(rectBackground.width()+rectBackground.x()-rectIcon.x()/1.3, rectCategory.y(),
                                25, self.rectName.height())

        optionMore = QStyleOptionButton()
        optionMore.initFrom(self.delete)
        optionMore.rect = self.rectDelete
        optionMore.icon = self.delete.icon()
        optionMore.iconSize = QtCore.QSize(18, 18)
        optionMore.state = optionMore.state or QStyle.State_MouseOver

        self.delete.style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.delete)

        painter.restore()
