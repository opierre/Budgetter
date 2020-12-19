from PySide2.QtGui import QIcon, Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton


class StatusBar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        """ Add button on bottom right corner """
        self._settings = QPushButton()
        self._settings.setObjectName(u"statusBarSettings")

        """ Layout for status bar """
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
        self._settings.setIcon(QIcon(":/images/images/more_horiz-white-24dp.svg"))
        # self._settings.setFixedHeight(self.parent.style().pixelMetric(QtWidgets.QStyle.PM_TitleBarHeight)+12*2)
        self._settings.setCursor(Qt.PointingHandCursor)

    def configureLayout(self):
        """
        Set elements in layout
        :return: void
        """

        """ Set margins """
        self.layout.setContentsMargins(0, 12, 1, 12)

        """ Add widgets to layout """
        self.layout.addWidget(self._settings)
