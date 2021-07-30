import sys

from PySide2.QtCore import QTranslator
from PySide2.QtWidgets import QApplication

from controller.controller import Controller

if __name__ == "__main__":
    app = QApplication([])
    translator = QTranslator()
    translator.load(':/i18n/i18n/fr_FR.qm')
    app.installTranslator(translator)
    widget = Controller()
    sys.exit(app.exec_())
