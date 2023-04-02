from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QStyledItemDelegate, QStyle


class CategoryComboBox(QStyledItemDelegate):
    """
    Category combobox with icons
    """

    def paint(self, painter: QPainter, option, index: QModelIndex):
        """
        Override paint()

        :param painter: (QPainter) painter
        :param option: option
        :param index: (QModelIndex) index
        :return: None
        """

        # Init options """
        opt = option
        self.initStyleOption(opt, index)

        # Set icon in center """
        opt.decorationSize.setWidth(opt.rect.width() - 1)

        # Draw item """
        opt.widget.style().drawControl(
            QStyle.ControlElement.CE_ItemViewItem, opt, painter, opt.widget
        )
