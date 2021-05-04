import datetime

from PySide2 import QtCore
from PySide2.QtCore import QSize, Qt, QRect, QRectF, QPointF, Signal, QModelIndex, QEvent
from PySide2.QtGui import QPen, QColor, QPainter, QFont, QFontMetrics, QIcon, QKeySequence
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QStyledItemDelegate, QPushButton, QStyleOptionButton, QStyle, \
    QApplication


class TransactionDelegate(QStyledItemDelegate):
    """
    Transaction Delegate
    """

    """ Signal emitted on Edit button click """
    transactionEditPressed = Signal(QModelIndex, QRect, QRect, QRect, QRect, QRectF, QRectF, QRectF, QRect, QRect)

    """ Signal emitted on Delete button click """
    transactionDeletePressed = Signal(QModelIndex)

    """ Signal emitted on Apply button click """
    transactionModified = Signal(QModelIndex)

    """ Signal emitted on Cancel button click """
    transactionModifCanceled = Signal(QModelIndex)

    """ Signal emitted when hovering comment button - Rectangle with comment (QRect) / Data index (QModelIndex) """
    commentHovered = Signal(QRect, QModelIndex)

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

        """ Hover on Edit/Delete QPushButtons """
        self.edit_hover = False
        self.delete_hover = False

        """ Show comment QPushButton """
        self.comment = QPushButton()
        self.comment.setCursor(Qt.PointingHandCursor)

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
        self.rect_mean = None
        self.rect_comment = None

        """ Store buttons rectangle for first row on add """
        self.rect_category_first_row = None
        self.rect_category_name_first_row = None
        self.rect_name_first_row = None
        self.rect_amount_first_row = None
        self.rect_date_first_row = None
        self.rect_account_first_row = None
        self.rect_exp_or_inc_first_row = None
        self.rect_edit_first_row = None
        self.rect_delete_first_row = None

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
        self.comment.setIcon(QIcon(":/images/images/notes_white_24dp.svg"))

        """ Set background color """
        self.edit.setStyleSheet("background-color: transparent;\n")
        self.delete.setStyleSheet("background-color: transparent;\n")
        self.comment.setStyleSheet("background-color: transparent;\n")

    def set_editable(self, index):
        """
        Change value of editable index
        :param index: index of editable item
        :return: void
        """

        self.editable = index
        self.selected = index

    def get_first_row_rects(self):
        """
        Retrieve first row rectangles
        :return: first row rectangles
        """

        return [self.rect_name_first_row,
                self.rect_amount_first_row,
                self.rect_date_first_row,
                self.rect_account_first_row,
                self.rect_exp_or_inc_first_row,
                self.rect_category_first_row,
                self.rect_category_name_first_row,
                self.rect_edit_first_row,
                self.rect_delete_first_row]

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
                                                 self.rect_category_name, self.rect_edit, self.rect_delete)

                """ Set transaction editable to paint different """
                self.set_editable(index)

                return True
            elif self.rect_delete.contains(cursorPosition) and index != self.editable:
                """ Emit pressed signal with model's index """
                self.transactionDeletePressed.emit(index)
                return True
            else:
                return False

        elif event.type() == QtCore.QEvent.MouseMove:
            """ Store position on click """
            cursorPosition = event.pos()

            if self.rect_edit.contains(cursorPosition) and self.selected == index:
                """ Change cursor to pointing hand """
                QApplication.setOverrideCursor(Qt.PointingHandCursor)

                """ Ask for color background """
                self.edit_hover = True
                self.delete_hover = False

                return True
            elif self.rect_delete.contains(cursorPosition) and self.selected == index:
                """ Change cursor to pointing hand """
                QApplication.setOverrideCursor(Qt.PointingHandCursor)

                """ Ask for color background """
                self.delete_hover = True
                self.edit_hover = False

                return True
            elif self.rect_comment.contains(cursorPosition):
                """ Emit hovered signal """
                self.commentHovered.emit(self.rect_comment, index)

                """ Ask for color background """
                self.edit_hover = False
                self.delete_hover = False

                return True
            else:
                """ Reset cursor shape """
                QApplication.restoreOverrideCursor()

                """ Ask for color background """
                self.edit_hover = False
                self.delete_hover = False

                return True

        # TODO: remove shortcut
        # elif event.type() == QtCore.QEvent.KeyPress:
        #     if event.matches(QKeySequence.Copy) and self.selected == index and self.editable != index:
        #         """ Emit pressed signal with model's index """
        #         self.transactionDeletePressed.emit(index)
        #         return True
        #     elif event.key() == Qt.Key_E and self.selected == index and self.editable != index:
        #         """ Emit pressed signal with model's index and rect position """
        #         self.transactionEditPressed.emit(index, self.rect_name, self.rect_amount, self.rect_date,
        #                                          self.rect_account, self.rect_exp_or_inc, self.rect_category,
        #                                          self.rect_category_name, self.rect_edit, self.rect_delete)
        #
        #         """ Set transaction editable to paint different """
        #         self.set_editable(index)
        #
        #         return True
        #     else:
        #         print(event.key())
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
        name = str(value["name"])
        category = str(value["category"])
        amount = value["amount"]
        amount = "{:,.2f}".format(amount).replace(",", " ") + " €"
        date = str(value["date"])
        date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%d %b %Y')
        account = str(value["account"])
        expOrInc = str(value["type"])
        means = str(value["means"])
        comment = str(value["comment"])

        """ Draw separator """
        self.draw_separator(painter, option)

        """ Draw item background """
        rect_background = QRect(option.rect.x() + option.rect.width() * 1 / 60, option.rect.y() + option.rect.height() * 1 / 5,
                                option.rect.width() - option.rect.width() * 2 / 60, option.rect.height() - option.rect.height() * 2 / 5)
        self.draw_item_background(painter, option, index, rect_background)

        """ Draw left icon background """
        self.rect_category = QRect(rect_background.x() + option.rect.width() * 1 / 35, rect_background.y() - option.rect.height() * 1 / 30,
                                   rect_background.height() + option.rect.height() * 2 / 30, rect_background.height() + option.rect.height() * 2 / 30)
        self.draw_left_icon(painter, index, category)

        """ Draw name """
        self.draw_name(painter, option, name, index)

        """ Draw category """
        self.draw_category(painter, option, index, category)

        """ Draw amount """
        self.draw_amount(painter, rect_background, index, amount)

        """ Draw amount label """
        self.draw_label(painter, rect_background, "Amount", 1/4)

        """ Draw date """
        self.draw_date(painter, rect_background, index, date)

        """ Draw date label """
        self.draw_label(painter, rect_background, "Date", 1.8/4)

        """ Draw account """
        self.draw_account(painter, rect_background, index, account)

        """ Draw account label """
        self.draw_label(painter, rect_background, "Account", 2.6/4)

        """ Draw mean icon """
        self.draw_means(painter, rect_background, means)

        """ Draw comment icon """
        self.draw_comment(painter, rect_background, index, comment)

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
        self.rect_exp_or_inc = QRectF(rect_background.x() + option.rect.width() * 1 / 140,
                                      self.rect_category.y() + (self.rect_category.width() - pixelsHeight - 8) / 2.0,
                                      pixelsWidth + (pixelsHeight + 8) / 2.5 + (pixelsHeight+8) / 0.9, pixelsHeight + 8)

        rect_ellipse = QRectF(self.rect_exp_or_inc.x(), self.rect_exp_or_inc.y() + (pixelsHeight + 8) / 3.5,
                              (pixelsHeight + 8) / 2.5, (pixelsHeight + 8) / 2.5)

        if self.editable != index:
            painter.setPen(Qt.NoPen)
            if expOrInc == "Income":
                painter.setBrush(QColor("#6DD230"))
            elif expOrInc == "Expenses":
                painter.setBrush(QColor("#FE4D97"))
            else:
                painter.setBrush(QColor("#FACA00"))

            """ Draw ellipse """
            painter.drawEllipse(rect_ellipse)
        else:
            """ Set income/expense pen color """
            pen = QPen(QColor("#26374C"))
            pen.setWidthF(1)
            painter.setPen(pen)

            self.rect_exp_or_inc = QRectF(rect_ellipse.x() - 2,
                                          rect_ellipse.y() - rect_ellipse.height() - 5,
                                          rect_ellipse.width() + 4,
                                          rect_ellipse.height() * 3.0 + 10)

            painter.drawRoundedRect(self.rect_exp_or_inc, 4.0, 4.0)

        pen = QPen(QColor("#1B5179"))
        pen.setWidthF(1)
        painter.setPen(pen)
        painter.setBrush(QColor("transparent"))

        """ Button edit """
        self.rect_edit = QRect(rect_background.width() + rect_background.x() - 35,
                               self.rect_name.y() - 2, 25, 25)

        optionMore = QStyleOptionButton()

        if self.editable != index and option.state & QStyle.State_Selected:
            optionMore.initFrom(self.edit)
            optionMore.rect = self.rect_edit
            optionMore.icon = self.edit.icon()
            optionMore.iconSize = QtCore.QSize(18, 18)
            optionMore.state = optionMore.state or QStyle.State_MouseOver

            self.edit.style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.edit)

        if self.edit_hover is True:
            """ Configure brush """
            painter.setBrush(QColor(255, 255, 255, 50))

            """ Draw hover effect """
            painter.drawEllipse(self.rect_edit)

        """ Buttons delete """
        self.rect_delete = QRect(rect_background.width() + rect_background.x() - 35,
                                 self.rect_category_name.y() - 2, 25, 25)

        if self.editable != index and option.state & QStyle.State_Selected:
            optionMore = QStyleOptionButton()
            optionMore.initFrom(self.delete)
            optionMore.rect = self.rect_delete
            optionMore.icon = self.delete.icon()
            optionMore.iconSize = QtCore.QSize(18, 18)
            optionMore.state = optionMore.state or QStyle.State_MouseOver

            self.delete.style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.delete)

        if self.delete_hover is True:
            """ Configure brush """
            painter.setBrush(QColor(255, 255, 255, 50))

            """ Draw hover effect """
            painter.drawEllipse(self.rect_delete)

        painter.restore()

        if index.row() == 0:
            self.rect_category_first_row = self.rect_category
            self.rect_category_name_first_row = self.rect_category_name
            self.rect_name_first_row = self.rect_name
            self.rect_amount_first_row = self.rect_amount
            self.rect_date_first_row = self.rect_date
            self.rect_account_first_row = self.rect_account
            self.rect_exp_or_inc_first_row = self.rect_exp_or_inc
            self.rect_edit_first_row = self.rect_edit
            self.rect_delete_first_row = self.rect_delete

    @staticmethod
    def draw_separator(painter, option):
        """
        Draw bottom line
        :param painter: painter
        :param option: option
        :return: void
        """

        """ Draw bottom border """
        painter.setPen(QPen(QColor("#344457")))
        painter.setBrush(Qt.NoBrush)
        painter.drawLine(option.rect.x()+option.rect.width()*1/60, option.rect.y()+option.rect.height()-1,
                         option.rect.width()-option.rect.width()*1/60, option.rect.y()+option.rect.height()-1)

        painter.setRenderHint(QPainter.Antialiasing)

    def draw_means(self, painter, rect_background, means):
        """
        Draw mean icon
        :param painter: painter
        :param rect_background: background rectangle
        :param means: payment means
        :return: void
        """

        self.rect_mean = QRectF(rect_background.width() * 3.5 / 4 - 24,
                                rect_background.y() + (rect_background.height() - 24) / 2.0,
                                24, 24)

        svgRender = QSvgRenderer(":/images/images/credit_card_white_24dp.svg")
        if means == "Espèces":
            svgRender = QSvgRenderer(":/images/images/local_atm_white_24dp.svg")
        elif means == "Virement":
            svgRender = QSvgRenderer(":/images/images/swap_horiz_white_24dp.svg")
        svgRender.setAspectRatioMode(Qt.KeepAspectRatio)
        svgRender.render(painter, self.rect_mean)

    def draw_comment(self, painter, rect_background, index, comment):
        """
        Draw mean icon
        :param painter: painter
        :param rect_background: background rectangle
        :param index: index
        :param comment: comment
        :return: void
        """

        self.rect_comment = QRect(rect_background.width() * 3.85 / 4 - 24,
                                  rect_background.y() + (rect_background.height() - 24) / 2.0,
                                  24, 24)
        optionMore = QStyleOptionButton()

        if self.editable != index and comment != '':
            """ Set tooltip """
            self.comment.setToolTip(comment)

            optionMore.initFrom(self.comment)
            optionMore.rect = self.rect_comment
            optionMore.icon = self.comment.icon()
            optionMore.iconSize = QtCore.QSize(24, 24)
            optionMore.state = optionMore.state or QStyle.State_MouseOver

            self.comment.style().drawControl(QStyle.CE_PushButton, optionMore, painter, self.comment)

    def draw_item_background(self, painter, option, index, rect_background):
        """
        Draw item background
        :param painter: painter
        :param option: option
        :param index: index
        :param rect_background: rect
        :return: void
        """
        painter.setPen(QPen(QColor("#26374C")))
        if self.editable != index and not (option.state & QStyle.State_Selected):
            painter.setBrush(QColor("transparent"))
            painter.drawRect(rect_background)
        elif self.editable != index and option.state & QStyle.State_Selected:
            self.selected = index
            painter.setBrush(QColor("#19344D"))
            painter.drawRect(rect_background.x(), rect_background.y() - option.rect.height() * 1 / 6,
                             rect_background.width(), rect_background.height() + option.rect.height() * 2 / 6)
        else:
            painter.setBrush(QColor("#1C293B"))
            painter.setOpacity(0.5)
            painter.drawRect(rect_background.x(), rect_background.y() - option.rect.height() * 1 / 6,
                             rect_background.width() + 2, option.rect.height() - 2)
            painter.setBrush(QColor("#1A537D"))
            painter.setOpacity(1)
            painter.drawRect(rect_background.x(), rect_background.y() - option.rect.height() * 1 / 6,
                             rect_background.width(), rect_background.height() + option.rect.height() * 2 / 6)

    def draw_left_icon(self, painter, index, category):
        """
        Draw left icon
        :param painter: painter
        :param index: index
        :param category: category
        :return: void
        """

        painter.setPen(QPen(QColor("#21405D")))
        painter.setBrush(QColor("#21405D"))
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
            elif category == "Transfer":
                svgRender = QSvgRenderer(":/images/images/swap_horiz_white_18dp_outlined.svg")
            svgRender.setAspectRatioMode(Qt.KeepAspectRatio)
            svgRender.render(painter, rectSvg)

    def draw_name(self, painter, option, name, index):
        """
        Draw name
        :param painter: painter
        :param option: option
        :param name: name
        :param index: index
        :return: void
        """

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
        self.rect_name = QRect(self.rect_category.x() + self.rect_category.width() + option.rect.width() * 1 / 140,
                               self.rect_category.y() + option.rect.height() * 1 / 30,
                               pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rect_name, Qt.AlignLeft | Qt.AlignVCenter, name)

    def draw_category(self, painter, option, index, category):
        """
        Draw category
        :param painter: painter
        :param option: option
        :param index: index
        :param category: category
        :return: void
        """

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

    def draw_amount(self, painter, rect_background, index, amount):
        """
        Draw amount
        :param painter: painter
        :param rect_background: rect
        :param index: index
        :param amount: amount
        :return: void
        """

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
        self.rect_amount = QRect(rect_background.width() * 1 / 4, self.rect_name.y(),
                                 pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rect_amount, Qt.AlignLeft | Qt.AlignVCenter, amount)

    def draw_label(self, painter, rect_background, label, x):
        """
        Draw label
        :param painter: painter
        :param rect_background: rect
        :param label: label to write
        :param x: x position
        :return: void
        """

        """ Set font on painter for percentage """
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        """ Set percentage pen color """
        painter.setPen(QPen(QColor("#75879B")))

        """ Get font metrics """
        fontMetrics = QFontMetrics(self.font)
        pixelsWidth = fontMetrics.width(label)
        pixelsHeight = fontMetrics.height()

        """ Set percentage beside amount """
        rectAmountLabel = QRect(rect_background.width() * x, self.rect_category_name.y(),
                                pixelsWidth, pixelsHeight)
        painter.drawText(rectAmountLabel, Qt.AlignLeft | Qt.AlignVCenter, label)

    def draw_date(self, painter, rect_background, index, date):
        """
        Draw date
        :param painter: painter
        :param rect_background: rect
        :param index: index
        :param date: date
        :return: void
        """

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
        self.rect_date = QRect(rect_background.width() * 1.8 / 4, self.rect_name.y(),
                               pixelsWidth, pixelsHeight)
        if self.editable != index:
            painter.drawText(self.rect_date, Qt.AlignLeft | Qt.AlignVCenter, date)

    def draw_account(self, painter, rect_background, index, account):
        """
        Draw account
        :param painter: painter
        :param rect_background: rect
        :param index: index
        :param account: account
        :return: void
        """

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
        self.rect_account = QRect(rect_background.width() * 2.6 / 4, self.rect_name.y(),
                                  pixelsWidth, pixelsHeight)

        if self.editable != index:
            painter.drawText(self.rect_account, Qt.AlignLeft | Qt.AlignVCenter, account)

