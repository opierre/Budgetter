import ctypes
import os
import sys

from PySide6.QtCore import QTranslator, QLocale
from PySide6.QtWidgets import QApplication

from budgetter.controller.controller import Controller


def start_app():
    """
    Start application with icon in task bar

    :return: None
    """

    if os.name == 'nt':
        # Enable icon in task bar
        app_unique_id = 'budgetter'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_unique_id)

    app = QApplication(sys.argv)

    # Translate app
    translator = QTranslator()
    # translator.load(':/i18n/i18n/fr_FR.qm')
    app.installTranslator(translator)

    # Force Locale
    locale_qt = QLocale(QLocale.English, QLocale.UnitedStates)
    QLocale.setDefault(locale_qt)

    _ = Controller()
    return app.exec_()


if __name__ == "__main__":
    result = start_app()
    sys.exit(result)
