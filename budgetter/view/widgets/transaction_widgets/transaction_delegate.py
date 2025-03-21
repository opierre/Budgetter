import datetime
from typing import Union

from PySide6.QtCore import (
    QSize,
    Qt,
    QRect,
    QRectF,
    Signal,
    QModelIndex,
    QPersistentModelIndex,
)
from PySide6.QtGui import QPen, QColor, QPainter, QFont, QFontMetrics, QIcon
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import (
    QStyledItemDelegate,
    QPushButton,
    QStyle,
    QApplication,
)

from budgetter.utils.defines import TransactionMean, TransactionType


class TransactionDelegate(QStyledItemDelegate):
    """
    Transaction Delegate
    """

    # Signal emitted when hovering comment button - Rectangle with comment (QRect) / Data index (QModelIndex)
    commentHovered = Signal(QRect, QModelIndex)

    def __init__(self, *args, parent=None):
        super().__init__()

        # Store selected state
        self.selected = QModelIndex()

        # Store font for values
        self.font = QFont()

        # Store all rects
        self.rect_account = None
        self.rect_amount = None
        self.rect_category = None
        self.rect_category_name = None
        self.rect_comment = None
        self.rect_date = None
        self.rect_exp_or_inc = None
        self.rect_mean = None
        self.rect_name = None

        # Show comment QPushButton
        self.comment = QPushButton()
        self.comment.setCursor(Qt.CursorShape.PointingHandCursor)

        # Configure Widgets
        self.configure_widgets()

    def configure_widgets(self):
        """
        Configure widgets on delegate item

        :return: None
        """

        # Set icon
        self.comment.setIcon(QIcon(":/images/images/notes_white_24dp.svg"))

        # Set background color
        self.comment.setStyleSheet("background-color: transparent;\n")

    def createEditor(
            self, parent, option, index: Union[QModelIndex, QPersistentModelIndex]
    ):
        """
        Override createEditor

        :param parent: parent
        :param option: option
        :param index: index
        :return: None
        """

        pass

    def sizeHint(self, _option_qstyle_option_view_item, _index):
        """
        Override sizeHint

        :param _option_qstyle_option_view_item: optionQStyleOptionViewItem
        :param _index: index
        :return: QSize(10, 70)
        """

        return QSize(10, 70)

    def paint(
            self,
            painter: QPainter,
            option,
            index: Union[QModelIndex, QPersistentModelIndex],
    ):
        """
        Override paint

        :param painter: (QPainter) painter
        :param option: option
        :param index: (QModelIndex) index
        :return: None
        """

        painter.save()

        # Get values
        value = index.data(Qt.ItemDataRole.DisplayRole)

        name = str(value.get("name"))
        category = str(value.get("category"))
        amount = value.get("amount") + " €"
        date = str(value.get("date"))
        date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d %b %Y")
        account = str(value.get("account"))
        exp_or_inc = str(value.get("transaction_type"))
        means = str(value.get("mean"))
        _ = str(value.get("comment"))

        # Draw separator
        self.draw_separator(painter, option)

        # Draw item background
        rect_background = QRect(
            option.rect.x() + option.rect.width() * 1 / 60,
            option.rect.y() + option.rect.height() * 1 / 5,
            option.rect.width() - option.rect.width() * 2 / 60,
            option.rect.height() - option.rect.height() * 2 / 5,
        )
        self.draw_item_background(painter, option, rect_background)

        # Draw left icon background
        self.rect_category = QRect(
            rect_background.x() + option.rect.width() * 1 / 35,
            rect_background.y() - option.rect.height() * 1 / 30,
            rect_background.height() + option.rect.height() * 2 / 30,
            rect_background.height() + option.rect.height() * 2 / 30,
        )
        self.draw_left_icon(painter, category)

        # Draw name
        self.draw_name(painter, option, name, rect_background)

        # Draw category
        self.draw_category(painter, option, category)

        # Draw amount
        self.draw_amount(painter, rect_background, amount)

        # Draw amount label
        self.draw_label(
            painter,
            rect_background,
            QApplication.translate("transaction_delegate", "Amount"),
            1.9 / 4,
        )

        # Draw date
        self.draw_date(painter, rect_background, date)

        # Draw date label
        self.draw_label(
            painter,
            rect_background,
            QApplication.translate("transaction_delegate", "Date"),
            3.2 / 4,
        )

        # Draw account
        self.draw_account(painter, rect_background, account)

        # Draw account label
        self.draw_label(
            painter,
            rect_background,
            QApplication.translate("transaction_delegate", "Account"),
            2.5 / 4,
        )

        # Draw mean icon
        self.draw_means(painter, rect_background, means)

        # Set font on painter for income/expense
        self.font.setFamily("Roboto")
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
        rect_ellipse = QRectF(
            rect_background.x() + option.rect.width() * 1 / 140,
            self.rect_category.y()
            + (self.rect_category.width() - pixels_height - 8) / 2.0
            + (pixels_height + 8) / 3.5,
            (pixels_height + 8) / 2.5,
            (pixels_height + 8) / 2.5,
        )

        self.rect_exp_or_inc = rect_ellipse

        painter.setPen(Qt.PenStyle.NoPen)
        if exp_or_inc.lower() == TransactionType.INCOME.value.lower():
            painter.setBrush(QColor("#6DD230"))
        elif exp_or_inc.lower() == TransactionType.EXPENSES.value.lower():
            painter.setBrush(QColor("#FE4D97"))
        else:
            painter.setBrush(QColor("#FACA00"))

        # Draw ellipse
        painter.drawEllipse(rect_ellipse)

        painter.restore()

    def draw_separator(self, painter: QPainter, option):
        """
        Draw bottom line

        :param painter: (QPainter) painter
        :param option: option
        :return: None
        """

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw bottom border
        painter.setPen(QPen(QColor("#344457")))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawLine(
            option.rect.x() + option.rect.width() * 1 / 60,
            option.rect.y() + option.rect.height() - 1,
            option.rect.width() - option.rect.width() * 1 / 60,
            option.rect.y() + option.rect.height() - 1,
        )

    def draw_means(self, painter: QPainter, rect_background, means):
        """
        Draw mean icon

        :param painter: (QPainter) painter
        :param rect_background: background rectangle
        :param means: payment means
        :return: None
        """

        self.rect_mean = QRectF(
            rect_background.width() * 3.9 / 4 - 24,
            rect_background.y() + (rect_background.height() - 24) / 2.0,
            24,
            24,
        )

        svg_render = QSvgRenderer(":/images/images/credit_card_white_24dp.svg")
        if means == TransactionMean.CASH.value:
            svg_render = QSvgRenderer(":/images/images/local_atm_white_24dp.svg")
        elif means == TransactionMean.TRANSFER.value:
            svg_render = QSvgRenderer(":/images/images/swap_horiz_white_24dp.svg")
        svg_render.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        svg_render.render(painter, self.rect_mean)

    def draw_item_background(self, painter: QPainter, option, rect_background: QRect):
        """
        Draw item background

        :param painter: (QPainter) painter
        :param option: option
        :param index: (QModelIndex) index
        :return: None
        """

        # Set pen
        painter.setPen(QPen(QColor("#26374C")))

        if option.state & QStyle.StateFlag.State_Selected:
            # Item selected and editable
            painter.setBrush(QColor("#1C293B"))
            painter.setOpacity(0.17)

            # Draw shadow
            painter.drawRoundedRect(
                rect_background.x(),
                rect_background.y() - option.rect.height() * 1 / 6,
                rect_background.width() + 2,
                rect_background.height() + option.rect.height() * 2 / 6 + 2,
                7,
                7,
            )

            # Draw background
            painter.setBrush(QColor(1, 84, 200, 200))
            painter.setOpacity(1)
            painter.drawRoundedRect(
                rect_background.x(),
                option.rect.y(),
                rect_background.width(),
                rect_background.height() + option.rect.height() * 2 / 6,
                7,
                7,
            )

    def draw_left_icon(self, painter: QPainter, category):
        """
        Draw left icon

        :param painter: (QPainter) painter
        :param category: category
        :return: None
        """

        painter.setPen(QPen(QColor("#21405D")))
        painter.setBrush(QColor("#21405D"))
        painter.drawRoundedRect(self.rect_category, 1.0, 1.0)

        # Draw icon and render svg
        painter.setPen(QPen(Qt.GlobalColor.transparent))
        painter.setBrush(QColor("transparent"))
        rect_svg = QRect(
            self.rect_category.x() + 10,
            self.rect_category.y() + 10,
            self.rect_category.width() - 20,
            self.rect_category.height() - 20,
        )
        painter.drawRect(rect_svg)

        svg_render = QSvgRenderer(":/images/images/restaurant-white-18dp_outlined.svg")
        if category == "Restaurants":
            svg_render = QSvgRenderer(
                ":/images/images/restaurant-white-18dp_outlined.svg"
            )
        elif category == "Transport":
            svg_render = QSvgRenderer(
                ":/images/images/directions_car-white-18dp_outlined.svg"
            )
        elif category == "Groceries":
            svg_render = QSvgRenderer(
                ":/images/images/local_grocery_store-white-18dp_outlined.svg"
            )
        elif category == "Transfer":
            svg_render = QSvgRenderer(
                ":/images/images/swap_horiz_white_18dp_outlined.svg"
            )
        svg_render.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        svg_render.render(painter, rect_svg)

    def draw_name(self, painter: QPainter, option, name, rect_background):
        """
        Draw name

        :param painter: (QPainter) painter
        :param option: option
        :param name: name
        :param rect_background: background rectangle
        :return: None
        """

        # Set font on painter for name
        self.font.setFamily("Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set category painter color
        painter.setPen(QPen(Qt.GlobalColor.white))
        painter.setBrush(QColor(Qt.GlobalColor.transparent))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.horizontalAdvance(name)
        pixels_height = font_metrics.height()

        # Set name on top
        x = (
                self.rect_category.x()
                + self.rect_category.width()
                + option.rect.width() * 1 / 140
        )
        self.rect_name = QRect(
            x,
            self.rect_category.y() + option.rect.height() * 1 / 30,
            min(pixels_width, rect_background.width() * 1.6 / 4 - x - 30),
            pixels_height,
        )

        painter.drawText(
            self.rect_name,
            int(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter),
            name,
        )

    def draw_category(self, painter: QPainter, option, category):
        """
        Draw category

        :param painter: (QPainter) painter
        :param option: option
        :param category: category
        :return: None
        """

        # Set font on painter for category
        self.font.setFamily("Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        # Set category pen color
        painter.setPen(QPen(QColor("#75879B")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.horizontalAdvance(category)
        pixels_height = font_metrics.height()

        # Set category beside name
        self.rect_category_name = QRect(
            self.rect_name.x(),
            self.rect_name.y()
            + self.rect_name.height()
            + option.rect.height() * 1 / 10,
            pixels_width,
            pixels_height,
        )

        painter.drawText(
            self.rect_category_name,
            int(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter),
            category,
        )

    def draw_amount(self, painter: QPainter, rect_background, amount):
        """
        Draw amount

        :param painter: (QPainter) painter
        :param rect_background: rect
        :param amount: amount
        :return: None
        """

        # Set font on painter for amount
        self.font.setFamily("Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set amount pen color
        painter.setPen(QPen(QColor("white")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_height = font_metrics.height()
        pixels_width = font_metrics.horizontalAdvance(amount)

        # Set amount on right corner
        self.rect_amount = QRect(
            rect_background.width() * 1.9 / 4,
            self.rect_name.y(),
            pixels_width,
            pixels_height,
        )

        painter.drawText(
            self.rect_amount,
            int(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter),
            amount,
        )

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
        self.font.setFamily("Roboto")
        self.font.setPointSize(10)
        painter.setFont(self.font)

        # Set percentage pen color
        painter.setPen(QPen(QColor("#75879B")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_width = font_metrics.horizontalAdvance(label)
        pixels_height = font_metrics.height()

        # Set percentage beside amount
        rect_amount_label = QRect(
            rect_background.width() * x_position,
            self.rect_category_name.y(),
            pixels_width,
            pixels_height,
        )
        painter.drawText(
            rect_amount_label,
            int(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter),
            label,
        )

    def draw_date(self, painter: QPainter, rect_background, date):
        """
        Draw date

        :param painter: (QPainter) painter
        :param rect_background: rect
        :param date: date
        :return: None
        """

        # Set font on painter for date
        self.font.setFamily("Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set date pen color
        painter.setPen(QPen(QColor("white")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_height = font_metrics.height()
        pixels_width = font_metrics.horizontalAdvance(date)

        # Set date on right corner
        self.rect_date = QRect(
            rect_background.width() * 3.2 / 4,
            self.rect_name.y(),
            pixels_width,
            pixels_height,
        )
        painter.drawText(
            self.rect_date,
            int(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter),
            date,
        )

    def draw_account(self, painter: QPainter, rect_background, account):
        """
        Draw account

        :param painter: (QPainter) painter
        :param rect_background: rect
        :param account: account
        :return: None
        """

        # Set font on painter for date
        self.font.setFamily("Roboto")
        self.font.setPointSize(11)
        painter.setFont(self.font)

        # Set date pen color
        painter.setPen(QPen(QColor("white")))

        # Get font metrics
        font_metrics = QFontMetrics(self.font)
        pixels_height = font_metrics.height()
        pixels_width = font_metrics.horizontalAdvance(account)

        # Set account on right corner
        self.rect_account = QRect(
            rect_background.width() * 2.5 / 4,
            self.rect_name.y(),
            pixels_width,
            pixels_height,
        )
        painter.drawText(
            self.rect_account,
            int(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter),
            account,
        )
