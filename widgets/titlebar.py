from PySide2.QtCore import QSize, Signal
from PySide2.QtGui import QIcon, Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy

from widgets.lined_edit_with_icon import LineEditWithIcon


class TitleBar(QWidget):
    """
    Title Bar
    """

    """ Signal emitted when right corner button clicked - Checked state: bool """
    clicked = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        """ Title """
        self._title = QLabel("Expenses Distribution")
        self._title.setObjectName(u"titleBarTitle")

        """ Empty widget with spacer item """
        self.empty_widget = QWidget()
        self.empty_widget.setObjectName(u"titleBarEmptyWidget")
        self.empty_layout = QHBoxLayout(self.empty_widget)

        """ Spacer item """
        self.spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        """ Add button on top right corner """
        self._add = QPushButton(self)
        self._add.setObjectName(u"titleBarAdd")

        """ Add button on top right corner """
        self._search = LineEditWithIcon(QIcon(":/images/images/search-white-24dp.svg"), self)
        self._search.setObjectName(u"titleBarSearch")

        """ Set Widget to occupy all region """
        self._widget = QWidget()
        self._widget.setObjectName(u"leftAddWidget")
        self._layout = QHBoxLayout(self._widget)
        self._left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        """ Layout for title bar """
        self.layout = QHBoxLayout(self)

        """ Configure widgets """
        self.configure_widgets()

        """ Configure layout """
        self.configure_layout()

        """ Connect signals and slots """
        self.connect_widgets()

    def connect_widgets(self):
        """
        Connect all slots and signals
        :return: void
        """

        """ Connect click on _add button to emit signal """
        self._add.clicked[bool].connect(self.clicked.emit)

    def configure_widgets(self):
        """
        Configure widgets inside container
        :return: void
        """

        """ Configure Add button on top right corner """
        self._add.setIcon(QIcon(":/images/images/add_circle_outline-white-24dp.svg"))
        self._add.setIconSize(QSize(22, 22))
        self._add.setCursor(Qt.PointingHandCursor)
        self._add.setCheckable(True)
        self._add.setChecked(True)

    def configure_layout(self):
        """
        Set elements in layout
        :return: void
        """

        """ Configure empty widget """
        self.empty_layout.addSpacerItem(self.spacer)

        """ Configure widget with add button """
        self._layout.addSpacerItem(self._left_spacer)
        self._layout.addWidget(self._search)
        self._layout.addWidget(self._add)
        # self._addLayout.addSpacerItem(self._downSpacer)

        """ Set margins """
        self.layout.setContentsMargins(0, 0, 0, 0)

        """ Set horizontal spacing to 0 """
        self.layout.setSpacing(0)

        """ Add widgets to layout """
        self.layout.addWidget(self._title)
        self.layout.addWidget(self.empty_widget)
        self.layout.addWidget(self._widget)

    def setTitle(self, title):
        """
        Set title
        :param title: title
        :return: void
        """

        self._title.setText(title)

    def getTitle(self):
        """
        Return title
        :return: title
        """

        return self._title.text()

    def setIcon(self, icon: QIcon):
        """
        Replace QIcon with icon
        :param icon: QIcon to set
        :return: void
        """

        self._add.setIcon(icon)
        self._add.setIconSize(QSize(22, 22))

    def disableButton(self):
        """
        Hide button on top right corner if useless
        :return: void
        """

        self._add.hide()
