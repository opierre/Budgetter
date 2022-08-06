# Python transcode and adaptation from component FlatButton from repo https://github.com/laserpants/qt-material-widgets
# Here is the licence for original code in C++:
#
# #####################################################################################################################
# Copyright Johannes Hilden (c) 2017
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#
#     * Neither the name of Author name here nor the names of other
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# #####################################################################################################################

import sys
from PySide2.QtWidgets import QPushButton, QWidget, QApplication, QHBoxLayout, QLineEdit, QLabel
from PySide2.QtGui import QPainter, QColor, QBrush, QPen, QPaintEvent, QFont, QKeyEvent, QKeySequence, QFontMetrics
from PySide2.QtCore import Qt, QEvent, QPropertyAnimation, \
    QEasingCurve, Property, QStateMachine, QPointF, QState, QEventTransition, QCoreApplication, QLineF


STYLESHEET = "QLineEdit {{" \
             "  background: transparent;" \
             "  border: 1px solid rgba(224, 224, 224, 150);" \
             "  border-radius: 5px;" \
             "  padding-top: 12px;" \
             "  padding-bottom: 10px;" \
             "  padding-left: {padding}px;" \
             "}}" \
             "QLineEdit:hover {{" \
             "  background: transparent;" \
             "  border: 1px solid rgba(255, 255, 255, 255);" \
             "}}" \
             "QLineEdit:focus {{" \
             "  background: transparent;" \
             "  border: 2px solid #199DE5;" \
             "  padding-left: {padding_minus}px;" \
             "}}"


class MaterialOutlinedLineEdit(QLineEdit):
    """
    Declaration to avoid conflicts
    """
    ...


class MaterialLineEditLabel:
    """
    Declaration to avoid conflicts
    """
    ...


class MaterialLineEditStateMachine(QStateMachine):
    """
    Material line edit state machine to handle animations
    """

    def __init__(self, parent: MaterialOutlinedLineEdit):
        super().__init__(parent)

        # Store line edit to apply state machine on
        self.line_edit = parent

        # Store both state for animation: focus/normal
        self.normal_state = QState()
        self.focused_state = QState()

        # Store label to display on top of line edit
        self.label = 0

        # Store animation: offset and color and scale
        self.offset_animation = QPropertyAnimation(self)
        self.color_animation = QPropertyAnimation(self)
        self.scale_animation = QPropertyAnimation(self)

        # Store progress for animation update
        self.__progress = 0.0

        # Configure animation and states
        self.configure(parent)

    def configure(self, parent: MaterialOutlinedLineEdit):
        """
        Configure animations and states

        :parent: parent widget
        :return: None
        """

        # Add both states to state machine
        self.addState(self.normal_state)
        self.addState(self.focused_state)

        # Set initial state to normal
        self.setInitialState(self.normal_state)

        # Add transition from normal to focus
        transition = QEventTransition(parent, QEvent.FocusIn)
        transition.setTargetState(self.focused_state)
        self.normal_state.addTransition(transition)

        # Add animation on transition to update progress
        animation = QPropertyAnimation(self, b"_progress", self)
        animation.setEasingCurve(QEasingCurve.InCubic)
        animation.setDuration(310)
        transition.addAnimation(animation)

        # Add transition from focus to normal
        transition = QEventTransition(parent, QEvent.FocusOut)
        transition.setTargetState(self.normal_state)
        self.focused_state.addTransition(transition)

        # Add animation on transition to update progress
        animation = QPropertyAnimation(self, b"_progress", self)
        animation.setEasingCurve(QEasingCurve.OutCubic)
        animation.setDuration(310)
        transition.addAnimation(animation)

        # Set progress values for states
        self.normal_state.assignProperty(self, "_progress", 0)
        self.focused_state.assignProperty(self, "_progress", 1)

        # Setup label and states properties
        self.setup_properties()

        # Connect text changed signal to new setup properties
        self.line_edit.textChanged.connect(self.setup_properties)

    def set_label(self, label_to_set: MaterialLineEditLabel) -> None:
        """
        Apply label and create new animations

        :param label_to_set: label to set
        :return: None
        """

        if self.label:
            del self.label

        # Delete previous offset animation
        if self.offset_animation:
            self.removeDefaultAnimation(self.offset_animation)
            del self.offset_animation

        # Delete previous color animation
        if self.color_animation:
            self.removeDefaultAnimation(self.color_animation)
            del self.color_animation

        # Delete previous scale animation
        if self.scale_animation:
            self.removeDefaultAnimation(self.scale_animation)
            del self.scale_animation

        self.label = label_to_set

        if self.label:
            # Apply new offset animation
            self.offset_animation = QPropertyAnimation(self.label, b"_offset", self)
            self.offset_animation.setDuration(210)
            self.offset_animation.setEasingCurve(QEasingCurve.OutCubic)
            self.addDefaultAnimation(self.offset_animation)

            # Apply new color animation
            self.color_animation = QPropertyAnimation(self.label, b"_color", self)
            self.color_animation.setDuration(210)
            self.addDefaultAnimation(self.color_animation)

            # Apply new scale animation
            self.scale_animation = QPropertyAnimation(self.label, b"_scale", self)
            self.scale_animation.setDuration(180)
            self.addDefaultAnimation(self.scale_animation)

        # Setup properties
        self.setup_properties()

    def set_progress(self, progress: float) -> None:
        """
        Set progress value for animations

        :param progress: progress value
        :return: None
        """

        self.__progress = progress
        self.line_edit.update()

    def progress(self) -> float:
        """
        Getter for progress

        :return: progress value
        """
        return self.__progress

    def setup_properties(self) -> None:
        """
        Setup properties on label and apply on states

        :return: None
        """

        if self.label:
            margin_top: int = self.line_edit.textMargins().top() + 7

            # Move label on top if text in line edit is not empty
            if self.line_edit.text() == '':
                self.normal_state.assignProperty(self.label, "_offset", QPointF(0, 13))
                self.normal_state.assignProperty(self.label, "_scale", 1.0)
            else:
                self.normal_state.assignProperty(self.label, "_offset", QPointF(0, 0 - margin_top))
                self.normal_state.assignProperty(self.label, "_scale", 0.82)

            # Define properties values for label
            self.focused_state.assignProperty(self.label, "_offset", QPointF(0, 0 - margin_top))
            self.focused_state.assignProperty(self.label, "_color", QColor("#199DE5"))
            self.normal_state.assignProperty(self.label, "_color", QColor(158, 158, 158, 255))
            self.focused_state.assignProperty(self.label, "_scale", 0.82)

        self.line_edit.update()

    # Progress property to update
    _progress = Property(float, fset=set_progress, fget=progress)


class MaterialLineEditPrivate:
    """
    Private widget with attributes and init method to be configured
    """

    def __init__(self, line_edit: MaterialOutlinedLineEdit):
        self.line_edit: MaterialOutlinedLineEdit = line_edit
        self.text_color = QColor(0, 0, 0, 221)
        self.label_color = QColor(158, 158, 158)
        self.ink_color = QColor(0, 188, 212)
        self.input_line_color = QColor(224, 224, 224)
        self.label_string = ''
        self.label_font_size: float = 9.5
        self.show_label: bool = False
        self.show_input_line: bool = True
        self.use_theme_colors: bool = True
        self.label: MaterialLineEditLabel = None
        self.state_machine: MaterialLineEditStateMachine = None

    def configure(self):
        """
        Configure properties

        :return: None
        """

        # Set state machine and label
        self.label = 0
        self.state_machine = MaterialLineEditStateMachine(self.line_edit)

        # Apply style to default line edit
        self.line_edit.setFrame(False)
        self.line_edit.setAttribute(Qt.WA_Hover)
        self.line_edit.setMouseTracking(True)
        self.line_edit.setTextMargins(0, 2, 0, 4)

        # Set stylesheet
        self.line_edit.setStyleSheet(STYLESHEET.format(padding='9', padding_minus='8'))

        # Set font on line edit
        self.line_edit.setFont(QFont("Roboto", 11, QFont.Normal))

        # Start state machine for normal/focus state
        self.state_machine.start()
        QCoreApplication.processEvents()


class MaterialOutlinedLineEdit(QLineEdit):
    """
    Material outlined line edit
    """

    def __init__(self, parent: QWidget = None, create: bool = True):
        super().__init__(parent)

        # Store trailing symbol
        self.trailing_symbol = None

        if create is True:
            self.line_edit_private = MaterialLineEditPrivate(self)
            self.line_edit_private.configure()

    def set_label_background_color(self, color: QColor):
        """
        Set label background color

        :param color: color to set
        :return: None
        """

        self.line_edit_private.label.set_background_color(color)

    def set_trailing_symbol(self, symbol: str):
        """
        Set trailing symbol on left

        :param symbol: symbol to set
        :return: None
        """

        self.trailing_symbol = QLabel(symbol + " ", parent=self)
        self.trailing_symbol.setFont(QFont("Roboto", 11, QFont.Normal))
        self.trailing_symbol.setStyleSheet("color: " + self.text_color().name() + "; padding: 0px;")
        self.trailing_symbol.setWordWrap(True)
        self.trailing_symbol.setVisible(False)

    def set_show_label(self, value: bool) -> None:
        """
        Create new label if not created

        :param value: True/False
        :return: None
        """

        # Do not update if value is already up-to-date
        if self.line_edit_private.show_label == value:
            return

        self.line_edit_private.show_label = value

        # If no label already exist and showing is asked, create new label
        if not self.line_edit_private.label and value:
            self.line_edit_private.label = MaterialLineEditLabel(self)
            self.line_edit_private.state_machine.set_label(self.line_edit_private.label)

        # Set margin on top
        if value:
            self.setContentsMargins(0, 17, 0, 0)
        else:
            self.setContentsMargins(0, 0, 0, 0)

    def has_label(self) -> bool:
        """
        Check if line edit alreayd has label

        :return: True/False
        """
        return self.line_edit_private.show_label

    def set_label_font_size(self, size: float) -> None:
        """
        Update label font size

        :param size: size to set
        :return:
        """
        self.line_edit_private.label_font_size = size

        # Set font on label and size
        if self.line_edit_private.label:
            font = QFont(self.line_edit_private.label.font())
            font.setPointSizeF(size)
            self.line_edit_private.label.setFont(font)
            self.line_edit_private.label.update()

    def label_font_size(self) -> float:
        """
        Return label font size

        :return: label font size
        """
        return self.line_edit_private.label_font_size

    def set_label(self, label: str) -> None:
        """
        Set label text on top of line edit

        :param label: label content
        :return: None
        """

        self.line_edit_private.label_string = label
        self.set_show_label(True)
        self.line_edit_private.label.update()

    def label(self) -> str:
        """
        Return label content

        :return: label content
        """

        return self.line_edit_private.label_string

    def set_text_color(self, color: QColor) -> None:
        """
        Apply new color on text

        :param color: new color
        :return: None
        """

        self.line_edit_private.text_color = color
        # self.setStyleSheet(f"QLineEdit {{ color: {color.name()} }}")
        self.line_edit_private.state_machine.setup_properties()

    def text_color(self) -> QColor:
        """
        Return text color

        :return: text color
        """
        return self.line_edit_private.text_color

    def set_label_color(self, color: QColor) -> None:
        """
        Set new label color

        :param color: color to set
        :return: None
        """

        self.line_edit_private.label_color = color
        self.line_edit_private.state_machine.setup_properties()

    def label_color(self) -> QColor:
        """
        Return label color

        :return: label color
        """
        return self.line_edit_private.label_color

    def event(self, event: QEvent) -> bool:
        """
        Override handle of event

        :param event: event to handle
        :return: True/False to accept/reject event
        """

        # Handle Resize and Move event to update geometry
        if event.type() in [QEvent.Resize, QEvent.Move]:
            if self.line_edit_private.label:
                self.line_edit_private.label.setGeometry(self.rect())

        return super().event(event)

    def paintEvent(self, event: QPaintEvent) -> None:
        """
        Override paintEvent()

        :param event: paint event
        :return: None
        """

        if self.trailing_symbol is not None and self.text() != '':
            self.setStyleSheet(STYLESHEET.format(padding='24', padding_minus='23'))
        else:
            self.setStyleSheet(STYLESHEET.format(padding='9', padding_minus='8'))

        super().paintEvent(event)

        if self.text() != '' and self.trailing_symbol is not None:
            self.trailing_symbol.move(self.rect().left() + 15, self.rect().center().y())
            self.trailing_symbol.setVisible(True)
        else:
            if self.trailing_symbol is not None:
                self.trailing_symbol.setVisible(False)

    # Properties to animate or modify
    _textColor = Property(QColor, fset=set_text_color, fget=text_color)


class MaterialLineEditLabel(QWidget):
    """
    Material line edit label
    """

    def __init__(self, parent: MaterialOutlinedLineEdit):
        super().__init__(parent)

        # Store attributes
        self.line_edit = parent
        self.__scale = 1.0
        self.x_position = 0.0
        self.y_position = 13
        self.color = QColor(parent.label_color())
        self.background_color = QColor("transparent")

        # Configure and apply default font
        font = QFont("Roboto", int(parent.fontInfo().pointSizeF()), QFont.Medium)
        self.setFont(font)

    def set_scale(self, scale: float) -> None:
        """
        Set new scale

        :param scale: scale to set
        :return: None
        """

        self.__scale = scale
        self.update()

    def scale(self) -> float:
        """
        Return current scale

        :return: current scale
        """
        return self.__scale

    def set_offset(self, offset: QPointF) -> None:
        """
        Update current offset

        :param offset: offset to set
        :return:
        """
        self.x_position = offset.x()
        self.y_position = offset.y()
        self.update()

    def offset(self) -> QPointF:
        """
        Return current offset

        :return: current offset
        """
        return QPointF(self.x_position, self.y_position)

    def set_background_color(self, color: QColor) -> None:
        """
        Set background color on label

        :param color: color to set
        :return: None
        """
        self.background_color = color
        self.update()

    def set_color(self, color: QColor) -> None:
        """
        Set color on label

        :param color: color to set
        :return: None
        """
        self.color = color
        self.update()

    def color(self) -> QColor:
        """
        Return current color

        :return: current color
        """
        return self.color

    def paintEvent(self, event: QPaintEvent) -> None:
        """
        Override paintEvent

        :param event: paint event
        :return: None
        """

        if not self.line_edit.has_label():
            return

        # Configure painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.scale(self.__scale, self.__scale)
        painter.setPen(self.color)
        painter.setOpacity(1)

        # Get metrics
        font_metrics = QFontMetrics(self.font())
        width = font_metrics.horizontalAdvance(self.line_edit.label())
        height = font_metrics.height()

        # Draw label with offset
        pos = QPointF(15 + self.x_position, self.height() - 32 + self.y_position)
        painter.fillRect(pos.x() - 3, pos.y() - height, width + 6, height + 4,
                         self.background_color)
        painter.drawText(pos.x(), pos.y(), self.line_edit.label())

    # Properties to animate or modify
    _scale = Property(float, fset=set_scale, fget=scale)
    _offset = Property(QPointF, fset=set_offset, fget=offset)
    _color = Property(QColor, fset=set_color, fget=color)


if __name__ == '__main__':
    app = QApplication([])
    widget = QWidget()
    button = MaterialOutlinedLineEdit()
    # button.setStyleSheet("background: transparent;")
    test = QPushButton('alors')
    button.set_label('Coucou')
    button.set_label_color(QColor(224, 224, 224, 255))
    button.set_label_background_color(QColor(255, 255, 255, 255))
    button.set_trailing_symbol('€')
    layout = QHBoxLayout()
    widget.setLayout(layout)
    layout.addWidget(test)
    layout.addWidget(button)
    layout.setContentsMargins(20, 20, 20, 20)
    button.setFixedWidth(300)
    # button.setFixedHeight(100)
    widget.show()
    sys.exit(app.exec_())
