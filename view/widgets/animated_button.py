from PySide2.QtCore import QTimer
from PySide2.QtGui import QMouseEvent
from PySide2.QtSvg import QSvgWidget
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout


class AnimatedButton(QWidget):
    """
    Button with animated icon
    """

    def __init__(self, parent=None):
        super(AnimatedButton, self).__init__(parent)

        ''' Store animation name '''
        self.animation_name = ''

        ''' Store timer '''
        self.timer = QTimer()

        ''' Store frame counter '''
        self.frame_counter = 0

        ''' Widget to display '''
        self.svg = QSvgWidget()

        ''' Configure widget '''
        self.configure()

        ''' Connect slots and signals '''
        self.connect_slots_and_signals()

    def set_animation_type(self, animation_name: str):
        """
        Update animation type

        :param animation_name: animation name (folder name in qrc)
        :return: None
        """

        self.animation_name = animation_name

        ''' Set default frame '''
        self.svg.load(":/animated/animated/" + self.animation_name + "/frame00.svg")

    def configure(self):
        """
        Configure default state

        :return: None
        """

        ''' Add svg widget to layout '''
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(6, 6, 6, 6)
        self.layout().addWidget(self.svg)

    def connect_slots_and_signals(self):
        """
        Connect slots and signals

        :return: None
        """

        ''' Connect timer finished to update frame '''
        self.timer.timeout.connect(self.update_frame)

    def update_frame(self):
        """
        Update displayed frame

        :return: None
        """

        ''' Load frame '''
        self.svg.load(":/animated/animated/" + self.animation_name + "/frame" + f"{self.frame_counter:02}" + ".svg")
        QApplication.processEvents()

        ''' Update frame count '''
        self.frame_counter += 1
        if self.frame_counter > 60:
            ''' Stop animation '''
            self.stop()

    # def rewind_animation(self):
    #     for index in range(60, -1, -1):
    #         time.sleep(0.016)
    #         # self.button.load(r"C:\Users\Pierre\Downloads\frames_vector_refresh\60fps\frame" + f"{index:02}" + ".svg")
    #         self.button.load(":/animated/animated/refresh_to_bars/frame" + f"{index:02}" + ".svg")
    #         QApplication.processEvents()

    def start(self):
        """
        Start animation

        :return: None
        """

        self.timer.start(16)

    def stop(self):
        """
        Stop animation and reset counter

        :return: None
        """

        self.timer.stop()
        self.frame_counter = 0

    def mousePressEvent(self, event: QMouseEvent):
        """
        Override parent function

        :param event: event
        :return: None
        """

        if not self.timer.isActive():
            self.start()
