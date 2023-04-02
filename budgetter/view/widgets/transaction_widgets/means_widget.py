from PySide6.QtCore import Qt, QFile, QTextStream
from PySide6.QtGui import QPainter, QColor
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QStyleOptionButton,
    QStyle,
)


class MeanCheckbox(QPushButton):
    """
    Mean Button
    """

    def __init__(self, parent=None, _type=None):
        super().__init__(parent)

        # Store type
        self._type = _type

        # Set checkable
        self.setCheckable(True)

        # Set margins
        self.setContentsMargins(0, 0, 0, 0)

        # Set cursors
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def set_type(self, _type: str):
        """
        Change type of radio button

        :param _type: (str) 'Espèces'/'Virement'/'Carte'
        :return: None
        """

        self._type = _type

    def paintEvent(self, _event):
        """
        Override paintEvent()

        :param _event: paint event
        :return: None
        """

        # Define new painter
        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Define opt to retrieve states
        opt = QStyleOptionButton()
        self.initStyleOption(opt)

        # Set selected circle color
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(Qt.PenStyle.NoPen)

        # Load SVG content
        svg_string_file = QFile(":/images/images/credit_card_white_24dp.svg")
        if self._type == "Espèces":
            svg_string_file = QFile(":/images/images/local_atm_white_24dp.svg")
        elif self._type == "Virement":
            svg_string_file = QFile(":/images/images/swap_horiz_white_24dp.svg")

        # Replace fill color in SVG
        svg_string = ""
        if svg_string_file.open(QFile.ReadOnly | QFile.Text):
            text_stream = QTextStream(svg_string_file)
            svg_string = text_stream.readAll()
            svg_string_file.close()

        if not opt.state & QStyle.StateFlag.State_Selected:
            svg_string = svg_string.replace(
                'fill="#0190EA"', 'fill="white" fill-opacity="0.65"'
            )

        svg_bytes = bytearray(svg_string, encoding="utf-8")

        # Load SVG as bytes
        svg_render = QSvgRenderer(svg_bytes)
        svg_render.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        svg_render.render(painter, self.rect())


class Mean(QWidget):
    """
    Widget to pick mean of payment in transaction item
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store active type
        self._active_type = None

        # Store layout
        self.layout = QHBoxLayout(self)

        # Store first button
        self.left_button = MeanCheckbox(self)

        # Store second button
        self.center_button = MeanCheckbox(self)

        # Store third button
        self.right_button = MeanCheckbox(self)

        # Configure widgets
        self.configure_widgets()

        # Configure layout
        self.configure_layout()

        # Connect all slots and signals
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect all typeCliked from buttons
        self.left_button.clicked.connect(self.handle_click)  # pylint: disable=no-member
        self.center_button.clicked.connect(
            self.handle_click
        )  # pylint: disable=no-member
        self.right_button.clicked.connect(
            self.handle_click
        )  # pylint: disable=no-member

    def handle_click(self):
        """
        Handle click on one button to deselect others

        :return: None
        """

        sender = self.sender()

        if sender == self.left_button:
            self.left_button.setChecked(True)
            self.center_button.setChecked(False)
            self.right_button.setChecked(False)
        elif sender == self.center_button:
            self.center_button.setChecked(True)
            self.left_button.setChecked(False)
            self.right_button.setChecked(False)
        elif sender == self.right_button:
            self.right_button.setChecked(True)
            self.left_button.setChecked(False)
            self.center_button.setChecked(False)

    def configure_widgets(self):
        """
        Configure both push buttons

        :return: None
        """

        # Set type
        self.left_button.set_type("Virement")
        self.center_button.set_type("Espèces")
        self.right_button.set_type("Carte")

        # Set height
        self.left_button.setFixedHeight(self.rect().height())
        self.center_button.setFixedHeight(self.rect().height())
        self.right_button.setFixedHeight(self.rect().height())

    def active_type(self):
        """
        Return active type

        :return: (str) active type
        """

        return self._active_type

    def set_active_type(self, active_type: str):
        """
        Select one button according to active type parameter

        :param active_type: (str) "Virement"/"Espèces"/"Carte"
        :return: None
        """

        # Check only middle button
        self.left_button.setChecked(False)
        self.center_button.setChecked(True)
        self.right_button.setChecked(False)

        if active_type == "Virement":
            self.center_button.set_type("Virement")
            self.left_button.set_type("Espèces")
            self.right_button.set_type("Carte")
        elif active_type == "Espèces":
            self.center_button.set_type("Espèces")
            self.left_button.set_type("Virement")
            self.right_button.set_type("Carte")
        else:
            self.center_button.set_type("Carte")
            self.left_button.set_type("Espèces")
            self.right_button.set_type("Virement")

        self._active_type = active_type

    def configure_layout(self):
        """
        Configure layout

        :return: None
        """

        # Set contents margin
        self.layout.setContentsMargins(4, 0, 4, 0)

        # Set Spacing
        self.layout.setSpacing(5)

        # Add widgets to layout
        self.layout.addWidget(self.left_button)
        self.layout.addWidget(self.center_button)
        self.layout.addWidget(self.right_button)

    def paintEvent(self, _event):
        """
        Override paintEvent()

        :param _event: event
        :return: None
        """

        painter = QPainter(self)

        # Configure pen and brush
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(28, 41, 59, 128))

        # Paint background
        painter.drawRoundedRect(self.rect(), 2, 2)
