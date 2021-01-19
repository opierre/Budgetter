from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget


class CustomWindow(QWidget):
    """
    Custom window with signals
    """

    """ Resize event signal - Window's height (int) / Window's width (int) """
    resizeEventSignal = Signal(int, int)

    def __init__(self):
        super().__init__()

    def resizeEvent(self, event):
        """
        Override resize event
        :param event: resize event
        :return: void
        """

        self.resizeEventSignal.emit(self.height(), self.width())
        super(CustomWindow, self).resizeEvent(event)
