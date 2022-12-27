from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QWidget, QListView

from budgetter.view.skeletons.Options import Ui_Options


class TitleBar(QWidget):
    """
    Title Bar
    """

    # Signal emitted when search bar in title bar is edited - Content typed: str/Search field name: str
    searched = Signal(str, str)

    # Signal emitted when right corner button clicked - Checked state: bool
    clicked = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Add options title bar
        self.gui = Ui_Options()
        self.gui.setupUi(self)

        # Configure widgets
        self.configure_widgets()

        # Configure layout
        self.configure_layout()

        # Connect signals and slots
        self.connect_widgets()

    def connect_widgets(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect click on _add button to emit signal
        self.gui.add.clicked[bool].connect(self.clicked.emit)  # pylint: disable=unsubscriptable-object

        # Connect text changed on _search line edit to emit signal
        self.gui.title_bar_search.textChanged[str].connect(self.emit_search)  # pylint: disable=unsubscriptable-object

    def configure_widgets(self):
        """
        Configure widgets inside container

        :return: None
        """

        # Configure Search bar on top right corner
        self.gui.title_bar_search.setClearButtonEnabled(True)
        self.gui.title_bar_search.findChild(QAction, "_q_qlineeditclearaction").setIcon(
            QIcon(":/images/images/clear-white-18dp.svg"))

        # Configure ComboBox widget
        self.gui.search_field.setView(QListView())
        self.gui.search_field.setStyleSheet("QListView {"
                                            "font-size: 11pt;"
                                            "font-family: \"Roboto\";"
                                            "}"
                                            "QComboBox QAbstractItemView::item\n"
                                            "{\n"
                                            "	min-height: 25px;\n"
                                            "}\n")
        self.gui.search_field.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.gui.search_field.view().window().setAttribute(Qt.WA_TranslucentBackground)

    def configure_layout(self):
        """
        Set elements in layout

        :return: None
        """

        # Set search icon
        self.gui.title_bar_search.set_icon(QIcon(":/images/images/search-white-24dp.svg"))

    def set_info(self, info: str):
        """
        Update info label

        :param info: info to set
        :return: None
        """

        self.gui.info.setText(info)

    def set_title(self, title: str):
        """
        Set title

        :param title: title
        :return: None
        """

        self.gui.title_bar_title.setText(title)

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

        self.gui.add.hide()

    def set_button_tooltip(self, tooltip: str):
        """
        Set button tooltip

        :param tooltip: tooltip
        :return: None
        """

        self.gui.add.setToolTip(tooltip)

    def disable_search(self):
        """
        Hide search bar on top right corner if useless

        :return: None
        """

        self.gui.search_field.hide()
        self.gui.title_bar_search.hide()

    def emit_search(self, content: str):
        """
        Emit search signal with content typed and search field name

        :param content: content to emit
        :return: None
        """

        # Retrieve search field
        search_field = self.gui.search_field.currentText()

        # Emit signal
        self.searched.emit(content, search_field)
