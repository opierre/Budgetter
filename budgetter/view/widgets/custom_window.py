from PySide6.QtCore import Signal, QSettings
from PySide6.QtWidgets import QMainWindow


class CustomWindow(QMainWindow):
    """
    Custom window with signals
    """

    # Resize event signal - Window's height (int) / Window's width (int)
    resizeEventSignal = Signal(int, int)

    def show(self):
        """
        Override show() to load settings

        :return: None
        """

        self.read_settings()
        super().show()

    def resizeEvent(self, event):
        """
        Override resize event

        :param event: resize event
        :return: None
        """

        self.resizeEventSignal.emit(self.height(), self.width())
        super().resizeEvent(event)

    def closeEvent(self, event):
        """
        Override closeEvent to save settings

        :param event: event
        :return: None
        """

        self.save_settings()

    def save_settings(self):
        """
        Save settings for main window

        :return: None
        """

        # Initialize settings
        settings = QSettings("opierre", "budgetter")
        settings.beginGroup("main_window")

        # Save geometry and position
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("state", self.saveState())
        settings.setValue("maximized", self.isMaximized())
        if self.isMaximized() is False:
            settings.setValue("position", self.pos())
            settings.setValue("size", self.size())

        settings.endGroup()

    def read_settings(self):
        """
        Read settings for main window

        :return: None
        """

        # Initialize settings
        settings = QSettings("opierre", "budgetter")
        settings.beginGroup("main_window")

        # Save geometry and position
        self.restoreGeometry(settings.value("geometry", self.saveGeometry()))
        self.restoreState(settings.value("state", self.saveState()))
        self.move(settings.value("position", self.pos()))
        self.resize(settings.value("size", self.size()))
        if settings.value("maximized", "false") == "true":
            self.showMaximized()

        settings.endGroup()
