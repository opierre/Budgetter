from PySide2.QtWidgets import QWidget

from budgetter.view.skeletons.AddAccount import Ui_AddAccount


class AddAccountDialog(QWidget):
    """
    Add account dialgo content
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store dialog content
        self.content = Ui_AddAccount()
        self.content.setupUi(self)

