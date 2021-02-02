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
    transactionEditPressed = Signal(QModelIndex, QRect, QRect, QRect, QRect, QRectF, QRectF, QRectF)

    """ Signal emitted on Delete button click """
    transactionDeletePressed = Signal(QModelIndex)

    """ Signal emitted on Apply button click """
    transactionModified = Signal(QModelIndex)

    """ Signal emitted on Cancel button click """
    transactionModifCanceled = Signal(QModelIndex)

    def __init__(self, parent=None, *args):
        QStyledItemDelegate.__init__(self, parent, *args)

        """ Store editable state """
        self.editable = False

        """ Store selected state """
        self.selected = False

        """ Store font for values """
        self.font = QFont()

        """ Edit/Delete QPushButtons """
        self.edit = QPushButton()
        self.delete = QPushButton()

        """ Apply/Cancel QPushButtons """
        self.apply = QPushButton()
        self.cancel = QPushButton()

        """ Store buttons rectangle """
        self.rect_edit = None
        self.rect_delete = None
        self.rect_category = None
        self.rect_category_name = None
        self.rect_name = None
        self.rect_amount = None
        self.rect_date = None
        self.rect_account = None
        self.rect_exp_or_inc = None

        """ Configure Widgets """
        self.configure_widgets()

    def configure_widgets(self):
        """
        Configure widgets on delegate item
        :return: void
        """

        """ Set icon """
        self.edit.setIcon(QIcon(":/images/images/edit-white-18dp.svg"))
        self.delete.setIcon(QIcon(":/images/images/delete-white-18dp.svg"))
        self.apply.setIcon(QIcon(":/images/images/check-white-18dp.svg"))
        self.cancel.setIcon(QIcon(":/images/images/close-white-18dp.svg"))

        """ Set background color """
        self.edit.setStyleSheet("background-color: transparent;\n")
        self.delete.setStyleSheet("background-color: transparent;\n")
        self.apply.setStyleSheet("background-color: transparent;\n")
        self.cancel.setStyleSheet("background-color: transparent;\n")

    def set_editable(self, index):
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

            if self.rect_edit.contains(cursorPosition) and index != self.editable:
                """ Emit pressed signal with model's index and rect position """
                self.transactionEditPressed.emit(index, self.rect_name, self.rect_amount, self.rect_date,
                                                 self.rect_account, self.rect_exp_or_inc, self.rect_category,
                                                 self.rect_category_name)
                return True
            elif self.rect_delete.contains(cursorPosition) and index != self.editable:
                """ Emit pressed signal with model's index """
                self.transactionDeletePressed.emit(index)
                return True
            elif self.rect_edit.contains(cursorPosition) and index == self.editable:
                """ Emit signal to update data from external widgets """
                self.transactionModified.emit(index)

                """ Update editable item """
                self.editable = False

                return True
            elif self.rect_delete.contains(cursorPosition) and index == self.editable:
                """ Emit signal to cancel data update from external widgets """
                self.transactionModifCanceled.emit(index)

                """ Update editable item """
                self.editable = False

                return True
            else:
                return False

        elif event.type() == QtCore.QEvent.MouseMove:
            """ Store position on click """
            cursorPosition = event.pos()

            if self.rect_edit.contains(cursorPosition) and self.selected == index:
                """ Change cursor to pointing hand """
                QApplication.setOverrideCursor(Qt.PointingHandCursor)
                return True
            elif self.rect_delete.contains(cursorPosition) and self.selected == index:
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
        if self.editable != index and not(option.state & QStyle.State_Selected):
            painter.setBrush(QColor("transparent"))
            painter.drawRect(rectBackground)
        elif self.editable != index and option.state & QStyle.State_Selected:
            self.selected = index
            painter.setBrush(QColor("#19344D"))
            painter.drawRect(rectBackground.x(), rectBackground.y()-option.rect.height()*1/6,
                             rectBackground.width(), rectBackground.height()+option.rect.height()*2/6)
        else:
            painter.setBrush(QColor("#1A537D"))
            painter.drawRect(rectBackground.x(), rectBackground.y()-option.rect.height()*1/6,
                             rectBackground.width(), rectBackground.height()+option.rect.height()*2/6)

        """ Draw left icon background """
        painter.setPen(QPen(QColor("#21405D")))
        painter.setBrush(QColor("#21405D"))
        self.rect_category = QRect(rectBackground.x() + option.rect.width() * 1 / 120, rectBackground.y() - option.rect.height() * 1 / 30,
                                   rectBackground.height() + option.rect.height() * 2 / 30, rectBackground.height() + option.rect.height() * 2 / 30)
        painter.drawRoundedRect(self.rect_category, 1.0, 1.0)

        if self.editable != index:
            """ Draw icon and render svg """
            painter.setPen(QPen(Qt.transparent))
            painter.setBrush(QColor("transparent"))
            rectSvg = QRect(self.rect_category.x() + 10, self.rect_category.y() + 10,
                            self.rect_category.width() - 20, self.rect_category.height() - 20)
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
        self.rect_name = QRect(self.rect_category.x() + self.rect_category.width() + option.rect.width() * 1 / 140, self.rect_category.y() + option.rect.height() * 1 / 30,
                               pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rect_name, Qt.AlignLeft | Qt.AlignVCenter, name)

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
        self.rect_category_name = QRect(self.rect_name.x(), self.rect_name.y() + self.rect_name.height() +
                                        option.rect.height() * 1 / 10, pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rect_category_name, Qt.AlignLeft | Qt.AlignVCenter, category)

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
        self.rect_amount = QRect(rectBackground.width() * 1 / 4, self.rect_name.y(),
                                 pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rect_amount, Qt.AlignLeft | Qt.AlignVCenter, amount)

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
        rectAmountLabel = QRect(rectBackground.width()*1/4, self.rect_category_name.y(),
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
        self.rect_date = QRect(rectBackground.width() * 1.8 / 4, self.rect_name.y(),
                               pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rect_date, Qt.AlignLeft | Qt.AlignVCenter, date)

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
        rectDateLabel = QRect(rectBackground.width()*1.8/4, self.rect_category_name.y(),
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
        self.rect_account = QRect(rectBackground.width() * 2.6 / 4, self.rect_name.y(),
                                  pixelsWidth, pixelsHeight)

        if self.editable != index:
            painter.drawText(self.rect_account, Qt.AlignLeft | Qt.AlignVCenter, account)

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
        rectAccountLabel = QRect(rectBackground.width()*2.6/4, self.rect_category_name.y(),
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
        self.rect_exp_or_inc = QRectF(rectBackground.width() * 3.7 / 4 - pixelsWidth - (pixelsHeight + 8) / 2.5,
                                      self.rect_category.y() + (self.rect_category.width() - pixelsHeight - 8) / 2.0,
                                      pixelsWidth + (pixelsHeight + 8) / 2.5 + (pixelsHeight+8) / 0.9, pixelsHeight + 8)

        if self.editable != index:
            painter.drawRoundedRect(self.rect_exp_or_inc, 4.0, 4.0)

            painter.setPen(QPen(QColor("white")))
            painter.drawText(self.rect_exp_or_inc.x() + (pixelsHeight + 8) / 0.9, self.rect_exp_or_inc.y() + 5.0,
                             pixelsWidth, pixelsHeight,
                             Qt.AlignLeft | Qt.AlignVCenter, expOrInc)

            painter.setPen(Qt.NoPen)
            if expOrInc == "Income":
                painter.setBrush(QColor("#6DD230"))
            else:
                painter.setBrush(QColor("#FE4D97"))
            rectEllipse = QRectF(self.rect_exp_or_inc.x() + (pixelsHeight + 8) / 2.5, self.rect_exp_or_inc.y() + (pixelsHeight + 8) / 3.5,
                                 (pixelsHeight + 8) / 2.5, (pixelsHeight + 8) / 2.5)
            painter.drawEllipse(rectEllipse)
        else:
            """ Set income/expense pen color """
            pen = QPen(QColor("#26374C"))
            pen.setWidthF(1)
            painter.setPen(pen)

            self.rect_exp_or_inc = QRectF(rectBackground.width() * 3.7 / 4 - pixelsWidth - (pixelsHeight + 8) / 2.5,
                                          self.rect_category.y() + (self.rect_category.width() - pixelsHeight - 8) / 2.0,
                                          (pixelsWidth + (pixelsHeight + 8) / 2.5 + (pixelsHeight + 8) / 0.9) * 2 / 3,
                                          pixelsHeight + 8)

            painter.drawRoundedRect(self.rect_exp_or_inc, 4.0, 4.0)

        pen = QPen(QColor("#1B5179"))
        pen.setWidthF(1)
        painter.setPen(pen)
        painter.setBrush(QColor("transparent"))

        """ Button edit """
        self.rect_edit = QRect(rectBackground.width() + rectBackground.x() - self.rect_category.x() / 1.3, self.rect_name.y(),
                               25, self.rect_name.height())

        optionMore = QStyleOptionButton()

        if self.editable != index and option.state & QStyle.State_Selected:
            optionMore.initFrom(self.edit)
            optionMore.rect = self.rect_edit
            optionMore.icon = self.edit.icon()
            optionMore.iconSize = QtCore.QSize(18, 18)
            optionMore.state = optionMore.state or QStyle.State_MouseOver

            self.edit.style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.edit)
        elif self.editable == index:
            optionMore.initFrom(self.apply)
            optionMore.rect = self.rect_edit
            optionMore.icon = self.apply.icon()
            optionMore.iconSize = QtCore.QSize(18, 18)
            optionMore.state = optionMore.state or QStyle.State_MouseOver

            self.apply.style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.apply)

        """ Buttons rects """
        self.rect_delete = QRect(rectBackground.width() + rectBackground.x() - self.rect_category.x() / 1.3, self.rect_category_name.y(),
                                 25, self.rect_name.height())

        if self.editable != index and option.state & QStyle.State_Selected:
            optionMore = QStyleOptionButton()
            optionMore.initFrom(self.delete)
            optionMore.rect = self.rect_delete
            optionMore.icon = self.delete.icon()
            optionMore.iconSize = QtCore.QSize(18, 18)
            optionMore.state = optionMore.state or QStyle.State_MouseOver

            self.delete.style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.delete)
        elif self.editable == index:
            optionMore.initFrom(self.cancel)
            optionMore.rect = self.rect_delete
            optionMore.icon = self.cancel.icon()
            optionMore.iconSize = QtCore.QSize(18, 18)
            optionMore.state = optionMore.state or QStyle.State_MouseOver

            self.cancel.style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.cancel)

        painter.restore()
