from PySide2.QtWidgets import QStyledItemDelegate, QStyle


class CategoryComboBox(QStyledItemDelegate):
    """
    Category combobox with icons
    """

    def __init__(self, parent=None):
        super(CategoryComboBox, self).__init__(parent)

    def paint(self, painter, option, index):
        """
        Override paint()
        :param painter: painter
        :param option: option
        :param index: index
        :return: void
        """

        """ Init options """
        opt = option
        self.initStyleOption(opt, index)

        """ Set icon in center """
        opt.decorationSize.setWidth(opt.rect.width()-1)

        """ Draw item """
        opt.widget.style().drawControl(QStyle.CE_ItemViewItem, opt, painter, opt.widget)
