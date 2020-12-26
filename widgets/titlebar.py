from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy


class TitleBar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        """ Title """
        self._title = QLabel("Expenses Distribution")
        self._title.setObjectName(u"titleBarTitle")

        """ Empty widget with spacer item """
        self.emptyWidget = QWidget()
        self.emptyWidget.setObjectName(u"titleBarEmptyWidget")
        self.emptyLayout = QHBoxLayout(self.emptyWidget)

        """ Spacer item """
        self.spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        """ Add button on top right corner """
        self._add = QPushButton()
        self._add.setObjectName(u"titleBarAdd")

        """ Set Widget to occupy all region """
        self._addWidget = QWidget()
        self._addWidget.setObjectName(u"leftAddWidget")
        self._addLayout = QHBoxLayout(self._addWidget)
        self._leftSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        """ Layout for title bar """
        self.layout = QHBoxLayout(self)

        """ Configure widgets """
        self.configureWidgets()

        """ Configure layout """
        self.configureLayout()

    def configureWidgets(self):
        """
        Configure widgets inside container
        :return: void
        """

        """ Configure Add button on top right corner """
        self._add.setIcon(QIcon(":/images/images/add_circle_outline-white-24dp.svg"))
        self._add.setIconSize(QSize(22, 22))
        self._add.setCursor(Qt.PointingHandCursor)

    def configureLayout(self):
        """
        Set elements in layout
        :return: void
        """

        """ Configure empty widget """
        self.emptyLayout.addSpacerItem(self.spacer)

        """ Configure widget with add button """
        self._addLayout.addSpacerItem(self._leftSpacer)
        self._addLayout.addWidget(self._add)
        # self._addLayout.addSpacerItem(self._downSpacer)

        """ Set margins """
        self.layout.setContentsMargins(0, 0, 0, 0)

        """ Set horizontal spacing to 0 """
        self.layout.setSpacing(0)

        """ Add widgets to layout """
        self.layout.addWidget(self._title)
        self.layout.addWidget(self.emptyWidget)
        self.layout.addWidget(self._addWidget)

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
