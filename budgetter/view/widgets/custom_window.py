from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow


class CustomWindow(QMainWindow):
    """
    Custom window with signals
    """

    # Resize event signal - Window's height (int) / Window's width (int)
    resizeEventSignal = Signal(int, int)

    def resizeEvent(self, event):
        """
        Override resize event
        :param event: resize event
        :return: None
        """

        self.resizeEventSignal.emit(self.height(), self.width())
        super().resizeEvent(event)
