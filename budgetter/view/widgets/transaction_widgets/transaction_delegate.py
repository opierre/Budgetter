import datetime

from PySide2 import QtCore
from PySide2.QtCore import QSize, Qt, QRect, QRectF, Signal, QModelIndex, QEvent, QPoint
from PySide2.QtGui import QPen, QColor, QPainter, QFont, QFontMetrics, QIcon
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QStyledItemDelegate, QPushButton, QStyleOptionButton, QStyle, \
    QApplication


class TransactionDelegate(QStyledItemDelegate):
    """
    Transaction Delegate
    """

    # Signal emitted on Edit button click
    transactionEditPressed = Signal(QModelIndex, QRect, QRect, QRect, QRect, QRectF, QRectF, QRectF, QRectF,
                                    QRect, QRect)

    # Signal emitted on Delete button click
    transactionDeletePressed = Signal(QModelIndex)

    # Signal emitted on Apply button click
    transactionModified = Signal(QModelIndex)

    # Signal emitted on Cancel button click
    transactionModifCanceled = Signal(QModelIndex)

    # Signal emitted when hovering comment button - Rectangle with comment (QRect) / Data index (QModelIndex)
    commentHovered = Signal(QRect, QModelIndex)

    def __init__(self, *args, parent=None):
        QStyledItemDelegate.__init__(self, parent, *args)

        # Store editable state
        self.editable = QModelIndex()

        # Store selected state
        self.selected = QModelIndex()

        # Store font for values
        self.font = QFont()

        # Edit/Delete QPushButtons
        self.edit = QPushButton()
        self.delete = QPushButton()

        # Hover on Edit/Delete QPushButtons
        self.edit_hover = False
        self.delete_hover = False

        # Show comment QPushButton
        self.comment = QPushButton()
        self.comment.setCursor(Qt.PointingHandCursor)

        # Store buttons rectangle
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

        # Store buttons rectangle for first row on add
        self.rect_category_first_row = None
        self.rect_category_name_first_row = None
        self.rect_name_first_row = None
        self.rect_amount_first_row = None
        self.rect_date_first_row = None
        self.rect_account_first_row = None
        self.rect_exp_or_inc_first_row = None
        self.rect_means_first_row = None
        self.rect_edit_first_row = None
        self.rect_delete_first_row = None

        # Configure Widgets
        self.configure_widgets()

    def configure_widgets(self):
        """
        Configure widgets on delegate item

        :return: None
        """

        # Set icon
        self.edit.setIconSize(QSize(18, 18))
        self.edit.setIcon(QIcon(":/images/images/edit-white-18dp.svg"))
        self.delete.setIconSize(QSize(18, 18))
        self.delete.setIcon(QIcon(":/images/images/delete-white-18dp.svg"))
        self.comment.setIcon(QIcon(":/images/images/notes_white_24dp.svg"))

        # Set background color
        self.edit.setStyleSheet("background-color: transparent;\n")
        self.delete.setStyleSheet("background-color: transparent;\n")
        self.comment.setStyleSheet("background-color: transparent;\n")

    def set_editable(self, index):
        """
        Change value of editable index

        :param index: index of editable item
        :return: None
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
                self.rect_means_first_row,
                self.rect_edit_first_row,
                self.rect_delete_first_row]

    def createEditor(self, parent, option, index: QModelIndex):
        """
        Override createEditor

        :param parent: parent
        :param option: option
        :param index: (QModelIndex) index
        :return: None
        """

        pass

    def editorEvent(self, event: QEvent, model, option, index: QModelIndex):
        """
        Override editorEvent to handle events

        :param event: event
        :param model: model
        :param option: option
        :param index: (QModelIndex) index
        :return: bool
        """

        # Reset cursor shape
        QApplication.restoreOverrideCursor()

        if event.type() == QtCore.QEvent.MouseButtonRelease:
            # Store position on click
            cursor_position = event.pos()

            if self.rect_edit.contains(cursor_position) and index != self.editable:
                # Emit pressed signal with model's index and rect position
                self.transactionEditPressed.emit(index, self.rect_name, self.rect_amount, self.rect_date,
                                                 self.rect_account, self.rect_exp_or_inc, self.rect_category,
                                                 self.rect_category_name, self.rect_mean, self.rect_edit,
                                                 self.rect_delete)

                # Set transaction editable to paint different
                self.set_editable(index)

                # Remove hover
                self.edit_hover = False

                return True
            elif self.rect_delete.contains(cursor_position) and index != self.editable:
                # Emit pressed signal with model's index
                self.transactionDeletePressed.emit(index)

                # Remove hover
                self.delete_hover = False

                return True
            else:
                return False

        elif event.type() == QtCore.QEvent.MouseMove:
            # Store position on click
            cursor_position = event.pos()

            if self.rect_edit.contains(cursor_position) and self.selected == index:
                # Change cursor to pointing hand
                QApplication.setOverrideCursor(Qt.PointingHandCursor)

                # Ask for color background
                self.edit_hover = True
                self.delete_hover = False

                return True
            elif self.rect_delete.contains(cursor_position) and self.selected == index:
                # Change cursor to pointing hand
                QApplication.setOverrideCursor(Qt.PointingHandCursor)

                # Ask for color background
                self.delete_hover = True
                self.edit_hover = False

                return True
            elif self.rect_comment.contains(cursor_position):
                # Emit hovered signal
                self.commentHovered.emit(self.rect_comment, index)

                # Ask for color background
                self.edit_hover = False
                self.delete_hover = False

                return True
            else:
                # Reset cursor shape
                QApplication.restoreOverrideCursor()

                # Ask for color background
                self.edit_hover = False
                self.delete_hover = False

                return True

        # TODO: remove shortcut
        # elif event.type() == QtCore.QEvent.KeyPress:
        #     if event.matches(QKeySequence.Copy) and self.selected == index and self.editable != index:
        #         # Emit pressed signal with model's index
        #         self.transactionDeletePressed.emit(index)
        #         return True
        #     elif event.key() == Qt.Key_E and self.selected == index and self.editable != index:
        #         # Emit pressed signal with model's index and rect position
        #         self.transactionEditPressed.emit(index, self.rect_name, self.rect_amount, self.rect_date,
        #                                          self.rect_account, self.rect_exp_or_inc, self.rect_category,
        #                                          self.rect_category_name, self.rect_edit, self.rect_delete)
        #
        #         # Set transaction editable to paint different
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

    def paint(self, painter: QPainter, option, index: QModelIndex):
        """
        Override paint

        :param painter: (QPainter) painter
        :param option: option
        :param index: (QModelIndex) index
        :return: None
        """

        painter.save()

        # Get values
        value = index.data(Qt.DisplayRole)
        name = str(value["name"])
        category = str(value["category"])
        amount = value["amount"]
        amount = "{:,.2f}".format(amount).replace(",", " ") + " €"
        date = str(value["date"])
        date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%d %b %Y')
        account = str(value["account"])
        exp_or_inc = str(value["type"])
        means = str(value["means"])
        comment = str(value["comment"])

        # Draw separator
        self.draw_separator(painter, option, index)

        # Draw item background
        rect_background = QRect(option.rect.x() + option.rect.width() * 1 / 60,
                                option.rect.y() + option.rect.height() * 1 / 5,
                                option.rect.width() - option.rect.width() * 2 / 60,
                                option.rect.height() - option.rect.height() * 2 / 5)
        self.draw_item_background(painter, option, index, rect_background)

        # Draw left icon background
        self.rect_category = QRect(rect_background.x() + option.rect.width() * 1 / 35,
                                   rect_background.y() - option.rect.height() * 1 / 30,
                                   rect_background.height() + option.rect.height() * 2 / 30,
                                   rect_background.height() + option.rect.height() * 2 / 30)
        self.draw_left_icon(painter, index, category)

        # Draw name
        self.draw_name(painter, option, name, index)

        # Draw category
        self.draw_category(painter, option, index, category)

        # Draw amount
        self.draw_amount(painter, rect_background, index, amount)

        # Draw amount label
        self.draw_label(painter, rect_background, QApplication.translate("transaction_delegate", "Amount"), 1/4)

        # Draw date
        self.draw_date(painter, rect_background, index, date)

        # Draw date label
        self.draw_label(painter, rect_background, QApplication.translate("transaction_delegate", "Date"), 1.8/4)

        # Draw account
        self.draw_account(painter, rect_background, index, account)

        # Draw account label
        self.draw_label(painter, rect_background, QApplication.translate("transaction_delegate", "Account"), 2.6/4)

        # Draw mean icon
        self.draw_means(painter, rect_background, means, index)

        # Draw comment icon
        self.draw_comment(painter, rect_background, index, comment)

        # Set font on painter for income/expense
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set income/expense pen color
        pen = QPen(QColor("#1B5179"))
        pen.setWidthF(1)
        painter.setPen(pen)

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_height = font_metrics.height()

        # Set income/expense on left corner
        rect_ellipse = QRectF(rect_background.x() + option.rect.width() * 1 / 140,
                              self.rect_category.y() + (self.rect_category.width() - pixels_height - 8) / 2.0 +
                              (pixels_height + 8) / 3.5,
                              (pixels_height + 8) / 2.5, (pixels_height + 8) / 2.5)

        self.rect_exp_or_inc = rect_ellipse

        if self.editable != index:
            painter.setPen(Qt.NoPen)
            if exp_or_inc == "Income":
                painter.setBrush(QColor("#6DD230"))
            elif exp_or_inc == "Expenses":
                painter.setBrush(QColor("#FE4D97"))
            else:
                painter.setBrush(QColor("#FACA00"))

            # Draw ellipse
            painter.drawEllipse(rect_ellipse)

        pen = QPen(QColor("#1B5179"))
        pen.setWidthF(1)
        painter.setPen(pen)
        painter.setBrush(QColor("transparent"))

        # Button edit
        self.rect_edit = QRect(rect_background.width() + rect_background.x() - 15,
                               option.rect.y(), 25, 25)

        if self.editable != index and option.state & QStyle.State_Selected:
            # Draw background of edit as pastille
            painter.setBrush(QColor(28, 41, 59, 128))
            painter.setPen(QColor(28, 41, 59, 128))

            # Draw hover effect
            shadow_rect = QRect(self.rect_edit.x() + 3, self.rect_edit.y() + 3,
                                self.rect_edit.width(), self.rect_edit.height())
            painter.drawEllipse(shadow_rect)

            # Draw background of edit as pastille
            painter.setBrush(QColor(1, 144, 234, 150))
            painter.setPen(QColor(1, 144, 234, 150))

            # Draw hover effect
            painter.drawEllipse(self.rect_edit)

            painter.save()
            self.edit.resize(self.rect_edit.size())
            painter.translate(self.rect_edit.topLeft())
            self.edit.render(painter, QPoint(0, 0))
            painter.restore()

        # Buttons delete
        self.rect_delete = QRect(rect_background.width() + rect_background.x() - 15,
                                 option.rect.y() + option.rect.height() - 25, 25, 25)

        if self.editable != index and option.state & QStyle.State_Selected:
            # Draw background of edit as pastille
            painter.setBrush(QColor(28, 41, 59, 128))
            painter.setPen(QColor(28, 41, 59, 128))

            # Draw hover effect
            shadow_rect = QRect(self.rect_delete.x() + 3, self.rect_delete.y() + 3,
                                self.rect_delete.width(), self.rect_delete.height())
            painter.drawEllipse(shadow_rect)

            # Draw background of edit as pastille
            painter.setBrush(QColor(226, 74, 141, 150))
            painter.setPen(QColor(226, 74, 141, 150))

            # Draw hover effect
            painter.drawEllipse(self.rect_delete)

            painter.save()
            self.delete.resize(self.rect_delete.size())
            painter.translate(self.rect_delete.topLeft())
            self.delete.render(painter, QPoint(0, 0))
            painter.restore()

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
            self.rect_means_first_row = self.rect_mean

    def draw_separator(self, painter: QPainter, option, index: QModelIndex):
        """
        Draw bottom line

        :param painter: (QPainter) painter
        :param option: option
        :param index: (QModelIndex) index
        :return: None
        """

        painter.setRenderHint(QPainter.Antialiasing)

        if isinstance(self.editable, QModelIndex):
            if self.editable.row() == index.row() + 1:
                return

        if self.editable != index:
            # Draw bottom border
            painter.setPen(QPen(QColor("#344457")))
            painter.setBrush(Qt.NoBrush)
            painter.drawLine(option.rect.x()+option.rect.width()*1/60, option.rect.y()+option.rect.height()-1,
                             option.rect.width()-option.rect.width()*1/60, option.rect.y()+option.rect.height()-1)

    def draw_means(self, painter: QPainter, rect_background, means, index):
        """
        Draw mean icon

        :param painter: (QPainter) painter
        :param rect_background: background rectangle
        :param means: payment means
        :param index: current index
        :return: None
        """

        self.rect_mean = QRectF(rect_background.width() * 3.5 / 4 - 24,
                                rect_background.y() + (rect_background.height() - 24) / 2.0,
                                24, 24)
        if self.editable != index:
            svg_render = QSvgRenderer(":/images/images/credit_card_white_24dp.svg")
            if means == "Espèces":
                svg_render = QSvgRenderer(":/images/images/local_atm_white_24dp.svg")
            elif means == "Virement":
                svg_render = QSvgRenderer(":/images/images/swap_horiz_white_24dp.svg")
            svg_render.setAspectRatioMode(Qt.KeepAspectRatio)
            svg_render.render(painter, self.rect_mean)

    def draw_comment(self, painter, rect_background, index, comment: str):
        """
        Draw mean icon

        :param painter: (QPainter) painter
        :param rect_background: background rectangle
        :param index: index
        :param comment: (str) comment
        :return: None
        """

        self.rect_comment = QRect(rect_background.width() * 3.85 / 4 - 24,
                                  rect_background.y() + (rect_background.height() - 24) / 2.0,
                                  24, 24)
        option_more = QStyleOptionButton()

        if self.editable != index and comment != '':
            # Set tooltip
            self.comment.setToolTip(comment)

            option_more.initFrom(self.comment)
            option_more.rect = self.rect_comment
            option_more.icon = self.comment.icon()
            option_more.iconSize = QtCore.QSize(24, 24)
            option_more.state = option_more.state or QStyle.State_MouseOver

            self.comment.style().drawControl(QStyle.CE_PushButton, option_more, painter, self.comment)

    def draw_item_background(self, painter: QPainter, option, index: QModelIndex, rect_background: QRect):
        """
        Draw item background

        :param painter: (QPainter) painter
        :param option: option
        :param index: (QModelIndex) index
        :param rect_background: (QRect) rect
        :return: None
        """

        # Set pen
        painter.setPen(QPen(QColor("#26374C")))

        if self.editable != index and not option.state & QStyle.State_Selected:
            # Do nothing
            pass

        elif self.editable != index and option.state & QStyle.State_Selected:
            # Item selected and not editable
            self.selected = index
            painter.setBrush(QColor("#19344D"))
            painter.drawRoundedRect(rect_background.x(), rect_background.y() - option.rect.height() * 1 / 6,
                                    rect_background.width(), rect_background.height() + option.rect.height() * 2 / 6,
                                    10, 10)

        elif self.editable == index and option.state & QStyle.State_Selected:
            # Item selected and editable
            painter.setBrush(QColor("#1C293B"))
            painter.setOpacity(0.17)

            # Draw shadow
            painter.drawRoundedRect(rect_background.x(), rect_background.y() - option.rect.height() * 1 / 6,
                                    rect_background.width() + 2,
                                    rect_background.height() + option.rect.height() * 2 / 6 + 2,
                                    7, 7)

            # Draw background
            painter.setBrush(QColor(1, 84, 200, 200))
            painter.setOpacity(1)
            painter.drawRoundedRect(rect_background.x(), option.rect.y(),
                                    rect_background.width(), rect_background.height() + option.rect.height() * 2 / 6,
                                    7, 7)

    def draw_left_icon(self, painter: QPainter, index: QModelIndex, category):
        """
        Draw left icon

        :param painter: (QPainter) painter
        :param index: (QModelIndex) index
        :param category: category
        :return: None
        """

        painter.setPen(QPen(QColor("#21405D")))
        painter.setBrush(QColor("#21405D"))
        painter.drawRoundedRect(self.rect_category, 1.0, 1.0)

        if self.editable != index:
            # Draw icon and render svg
            painter.setPen(QPen(Qt.transparent))
            painter.setBrush(QColor("transparent"))
            rect_svg = QRect(self.rect_category.x() + 10, self.rect_category.y() + 10,
                             self.rect_category.width() - 20, self.rect_category.height() - 20)
            painter.drawRect(rect_svg)

            svg_render = QSvgRenderer(":/images/images/restaurant-white-18dp_outlined.svg")
            if category == "Restaurants":
                svg_render = QSvgRenderer(":/images/images/restaurant-white-18dp_outlined.svg")
            elif category == "Transport":
                svg_render = QSvgRenderer(":/images/images/directions_car-white-18dp_outlined.svg")
            elif category == "Groceries":
                svg_render = QSvgRenderer(":/images/images/local_grocery_store-white-18dp_outlined.svg")
            elif category == "Transfer":
                svg_render = QSvgRenderer(":/images/images/swap_horiz_white_18dp_outlined.svg")
            svg_render.setAspectRatioMode(Qt.KeepAspectRatio)
            svg_render.render(painter, rect_svg)

    def draw_name(self, painter: QPainter, option, name, index: QModelIndex):
        """
        Draw name

        :param painter: (QPainter) painter
        :param option: option
        :param name: name
        :param index: (QModelIndex) index
        :return: None
        """

        # Set font on painter for name
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set category painter color
        painter.setPen(QPen(Qt.white))
        painter.setBrush(QColor(Qt.transparent))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.width(name)
        pixels_height = font_metrics.height()

        # Set name on top
        self.rect_name = QRect(self.rect_category.x() + self.rect_category.width() + option.rect.width() * 1 / 140,
                               self.rect_category.y() + option.rect.height() * 1 / 30,
                               pixels_width, pixels_height)
        if self.editable != index:
            painter.drawText(self.rect_name, int(Qt.AlignLeft | Qt.AlignVCenter), name)

    def draw_category(self, painter: QPainter, option, index: QModelIndex, category):
        """
        Draw category

        :param painter: (QPainter) painter
        :param option: option
        :param index: (QModelIndex) index
        :param category: category
        :return: None
        """

        # Set font on painter for category
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        # Set category pen color
        painter.setPen(QPen(QColor("#75879B")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.width(category)
        pixels_height = font_metrics.height()

        # Set category beside name
        self.rect_category_name = QRect(self.rect_name.x(), self.rect_name.y() + self.rect_name.height() +
                                        option.rect.height() * 1 / 10, pixels_width, pixels_height)
        if self.editable != index:
            painter.drawText(self.rect_category_name, int(Qt.AlignLeft | Qt.AlignVCenter), category)

    def draw_amount(self, painter: QPainter, rect_background, index: QModelIndex, amount):
        """
        Draw amount

        :param painter: (QPainter) painter
        :param rect_background: rect
        :param index: (QModelIndex) index
        :param amount: amount
        :return: None
        """

        # Set font on painter for amount
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set amount pen color
        painter.setPen(QPen(QColor("white")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_height = font_metrics.height()
        pixels_width = font_metrics.width(amount)

        # Set amount on right corner
        self.rect_amount = QRect(rect_background.width() * 1 / 4, self.rect_name.y(),
                                 pixels_width, pixels_height)
        if self.editable != index:
            painter.drawText(self.rect_amount, int(Qt.AlignLeft | Qt.AlignVCenter), amount)

    def draw_label(self, painter: QPainter, rect_background, label, x_position):
        """
        Draw label

        :param painter: (QPainter) painter
        :param rect_background: rect
        :param label: label to write
        :param x_position: x position
        :return: None
        """

        # Set font on painter for percentage
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        # Set percentage pen color
        painter.setPen(QPen(QColor("#75879B")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.width(label)
        pixels_height = font_metrics.height()

        # Set percentage beside amount
        rect_amount_label = QRect(rect_background.width() * x_position, self.rect_category_name.y(),
                                  pixels_width, pixels_height)
        painter.drawText(rect_amount_label, int(Qt.AlignLeft | Qt.AlignVCenter), label)

    def draw_date(self, painter: QPainter, rect_background, index: QModelIndex, date):
        """
        Draw date

        :param painter: (QPainter) painter
        :param rect_background: rect
        :param index: (QModelIndex) index
        :param date: date
        :return: None
        """

        # Set font on painter for date
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set date pen color
        painter.setPen(QPen(QColor("white")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_height = font_metrics.height()
        pixels_width = font_metrics.width(date)

        # Set date on right corner
        self.rect_date = QRect(rect_background.width() * 1.8 / 4, self.rect_name.y(),
                               pixels_width, pixels_height)
        if self.editable != index:
            painter.drawText(self.rect_date, int(Qt.AlignLeft | Qt.AlignVCenter), date)

    def draw_account(self, painter: QPainter, rect_background, index: QModelIndex, account):
        """
        Draw account

        :param painter: (QPainter) painter
        :param rect_background: rect
        :param index: (QModelIndex) index
        :param account: account
        :return: None
        """

        # Set font on painter for date
        self.font.setFamily(u"Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set date pen color
        painter.setPen(QPen(QColor("white")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_height = font_metrics.height()
        pixels_width = font_metrics.width(account)

        # Set account on right corner
        self.rect_account = QRect(rect_background.width() * 2.6 / 4, self.rect_name.y(),
                                  pixels_width, pixels_height)

        if self.editable != index:
            painter.drawText(self.rect_account, int(Qt.AlignLeft | Qt.AlignVCenter), account)