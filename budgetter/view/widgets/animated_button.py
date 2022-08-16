from enum import Enum

from PySide6.QtCore import QTimer, Signal
from PySide6.QtGui import QMouseEvent
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout


class DIRECTIONS(Enum):
    """
    Directions Enum
    """

    PLAY = 1
    REWIND = -1


class AnimatedButton(QWidget):
    """
    Button with animated icon
    """

    # Signal emitted on click
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store animation name
        self.animation_name = ''

        # Store timer
        self.timer = QTimer()

        # Store frame counter
        self.frame_counter = 0

        # Store number of repetitions
        self.repeat = 1000

        # Store animation direction
        self.direction = None

        # Widget to display
        self.svg = QSvgWidget()

        # Configure widget
        self.configure()

        # Connect slots and signals
        self.connect_slots_and_signals()

    def set_animation_type(self, animation_name: str):
        """
        Update animation type

        :param animation_name: animation name (folder name in qrc)
        :return: None
        """

        self.animation_name = animation_name

        # Set default frame
        self.svg.load(":/animated/animated/" + self.animation_name + "/frame00.svg")

    def configure(self):
        """
        Configure default state

        :return: None
        """

        # Add svg widget to layout
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(6, 6, 6, 6)
        self.layout().addWidget(self.svg)

    def connect_slots_and_signals(self):
        """
        Connect slots and signals

        :return: None
        """

        # Connect timer finished to update frame
        self.timer.timeout.connect(self.update_frame)

    def update_frame(self):
        """
        Update displayed frame

        :return: None
        """

        if self.direction == DIRECTIONS.PLAY:
            self.roll_frame()
        else:
            self.rewind_frame()

    def roll_frame(self):
        """
        Roll displayed frame

        :return: None
        """

        # Load frame
        self.svg.load(":/animated/animated/" + self.animation_name + "/frame" + f"{self.frame_counter:02}" + ".svg")
        QApplication.processEvents()

        # Update frame count
        self.frame_counter += 1
        if self.frame_counter > 15:
            if self.repeat != 1000:
                # Update repeat till 0
                self.repeat -= 1

                if self.repeat <= 0:
                    self.stop()
                    return

            # Rewind animation from end
            self.frame_counter = 15
            self.direction = DIRECTIONS.REWIND
            QApplication.processEvents()

    def rewind_frame(self):
        """
        Update backwards displayed frame

        :return: None
        """

        # Load frame
        self.svg.load(":/animated/animated/" + self.animation_name + "/frame" + f"{self.frame_counter:02}" + ".svg")
        QApplication.processEvents()

        # Update frame count
        self.frame_counter -= 1
        if self.frame_counter < 0:
            # Play animation from start
            self.frame_counter = 0
            self.direction = DIRECTIONS.PLAY
            QApplication.processEvents()

    def start(self, repeat: int = 1000):
        """
        Start animation

        :param repeat: number of repetitions
        :return: None
        """

        if not self.timer.isActive():
            self.direction = DIRECTIONS.PLAY
            self.repeat = repeat
            self.timer.start(20)

    def stop(self):
        """
        Stop animation and reset counter

        :return: None
        """

        if self.timer.isActive():
            self.timer.stop()
            self.frame_counter = 0

    def mousePressEvent(self, event: QMouseEvent):
        """
        Override parent function

        :param event: event
        :return: None
        """

        self.clicked.emit()
        super().mousePressEvent(event)
