from PySide2.QtCore import Signal, QPropertyAnimation, QAbstractAnimation, Property
from PySide2.QtWidgets import QWidget


class Drawer(QWidget):
    """
    Drawer Widget
    """

    """ Signal emitted when animation is finished """
    animationFinished = Signal()

    """ Signal emitted when animation is started """
    animationStarted = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Store parent widget """
        self.parent = parent

        """ Set width parameter """
        self._width = 0

        """ Define animation for moving drawer """
        self.animation = QPropertyAnimation(self, b"width")

        """ Drawer expanded state """
        self.expanded = False

        """ Configure animation properties """
        self.configureAnimation()

        """ Display all labels for extended drawer """
        self.animation.finished.connect(self.animationFinished.emit)

    def configureAnimation(self):
        """
        Set animation properties
        :return: void
        """

        """ Define width starting value and animation duration for reaching max width """
        self.animation.setStartValue(65)
        self.animation.setDuration(300)

        """ Set maximum width """
        self.setMaximumWidth(150)

        """ Connect animation to set width value """
        self.animation.valueChanged.connect(self.setFixedWidth)

    def getMaximumWidth(self):
        """
        Return maximum width for drawer
        :return: maximum width
        """

        return self._width

    def setMaximumWidth(self, width):
        """
        Set maximum width for drawer
        :return: void
        """

        self._width = width
        self.animation.setEndValue(self._width)

    """ Width property to animate with getter/setter """
    width = Property(float, getMaximumWidth, setMaximumWidth)

    def expand(self):
        """
        Expand drawer to display labels
        :return: void
        """

        """ Set animation drawer direction: forward from minWidth to maxWidth """
        self.animation.setDirection(QAbstractAnimation.Forward)

        """ Update state """
        self.expanded = True

        """ Start animation """
        self.animation.start()

    def collapse(self):
        """
        Collapse drawer to hide labels
        :return: void
        """

        """ Set animation drawer direction: forward from minWidth to maxWidth """
        self.animation.setDirection(QAbstractAnimation.Backward)

        """ Update state """
        self.expanded = False

        """ Hide all labels for collapsed drawer """
        self.animationStarted.emit()

        """ Start animation """
        self.animation.start()

    def getExpanded(self):
        """
        Return drawer expanded state
        :return: drawer state - True:Expanded/False:Collapsed
        """

        return self.expanded
