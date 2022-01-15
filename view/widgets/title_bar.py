from PySide2.QtCore import Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QAction

from view.skeletons.Options import Ui_Options


class TitleBar(QWidget):
    """
    Title Bar
    """

    """ Signal emitted when search bar editing finished - Content typed: str """
    searched = Signal(str)

    """ Signal emitted when right corner button clicked - Checked state: bool """
    clicked = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Add options title bar """
        self.ui = Ui_Options()
        self.ui.setupUi(self)

        """ Configure widgets """
        self.configure_widgets()

        """ Configure layout """
        self.configure_layout()

        """ Connect signals and slots """
        self.connect_widgets()

    def connect_widgets(self):
        """
        Connect all slots and signals

        :return: None
        """

        """ Connect click on _add button to emit signal """
        self.ui.add.clicked[bool].connect(self.clicked.emit)

        """ Connect text changed on _search line edit to emit signal """
        self.ui.title_bar_search.textChanged[str].connect(self.searched.emit)

    def configure_widgets(self):
        """
        Configure widgets inside container

        :return: None
        """

        """ Configure Search bar on top right corner """
        self.ui.title_bar_search.setClearButtonEnabled(True)
        self.ui.title_bar_search.findChild(QAction, "_q_qlineeditclearaction").setIcon(QIcon(":/images/images/clear-white-18dp.svg"))

    def configure_layout(self):
        """
        Set elements in layout

        :return: None
        """

        """ Set search icon """
        self.ui.title_bar_search.setIcon(QIcon(":/images/images/search-white-24dp.svg"))

    def set_title(self, title):
        """
        Set title

        :param title: title
        :return: None
        """

        self.ui.title_bar_title.setText(title)

    def get_title(self):
        """
        Return title

        :return: title
        """

        return self._title.text()

    def disable_button(self):
        """
        Hide button on top right corner if useless

        :return: None
        """

        self.ui.add.hide()

    def disable_search(self):
        """
        Hide search bar on top right corner if useless

        :return: None
        """

        self.ui.search_field.hide()
        self.ui.title_bar_search.hide()
