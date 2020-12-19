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

        """ Layout for empty widget """
        self.emptyLayout = QHBoxLayout(self.emptyWidget)

        """ Spacer item """
        self.spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        """ Add button on top right corner """
        self._add = QPushButton()
        self._add.setObjectName(u"titleBarAdd")

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
        self._add.setIcon(QIcon(":/images/images/add_circle_outline-white-18dp.svg"))
        self._add.setIconSize(QSize(24, 24))
        self._add.setCursor(Qt.PointingHandCursor)

    def configureLayout(self):
        """
        Set elements in layout
        :return: void
        """

        """ Configure empty widget """
        self.emptyLayout.addSpacerItem(self.spacer)

        """ Set margins """
        self.layout.setContentsMargins(0, 0, 0, 0)

        """ Set horizontal spacing to 0 """
        self.layout.setSpacing(0)

        """ Add widgets to layout """
        self.layout.addWidget(self._title)
        self.layout.addWidget(self.emptyWidget)
        self.layout.addWidget(self._add)

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
