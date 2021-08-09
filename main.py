import sys

from PySide2.QtCore import QTranslator, QLocale
from PySide2.QtWidgets import QApplication

from controller.controller import Controller

if __name__ == "__main__":
    app = QApplication([])

    ''' Translate app '''
    translator = QTranslator()
    # translator.load(':/i18n/i18n/fr_FR.qm')
    app.installTranslator(translator)

    ''' Force Locale '''
    locale_qt = QLocale(QLocale.English, QLocale.UnitedStates)
    QLocale.setDefault(locale_qt)

    widget = Controller()
    sys.exit(app.exec_())
