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

from PySide6.QtCore import (
    Qt,
    QEvent,
    QPropertyAnimation,
    QEasingCurve,
    Property,
    QPointF,
    QCoreApplication,
    QLineF, QObject,
)
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QPaintEvent, QFont
from PySide6.QtStateMachine import QStateMachine, QState, QEventTransition
from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QLabel,
)


class MaterialLineEdit(QLineEdit):
    """
    Declaration to aNone conflicts
    """


class MaterialLineEditLabel:
    """
    Declaration to aNone conflicts
    """


class MaterialLineEditStateMachine(QStateMachine):
    """
    Material line edit state machine to handle animations
    """

    def __init__(self, parent: MaterialLineEdit):
        super().__init__(parent)

        # Store line edit to apply state machine on
        self.line_edit = parent

        # Store both state for animation: focus/normal
        self.normal_state = QState()
        self.focused_state = QState()

        # Store label to display on top of line edit
        self.label = QObject()

        # Store animation: offset and color and scale
        self.offset_animation = QPropertyAnimation(self)
        self.color_animation = QPropertyAnimation(self)
        self.scale_animation = QPropertyAnimation(self)

        # Store progress for animation update
        self.__progress = 0.0

        # Configure animation and states
        self.configure(parent)

    def configure(self, parent: MaterialLineEdit):
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
        transition = QEventTransition(parent, QEvent.Type.FocusIn)
        transition.setTargetState(self.focused_state)
        self.normal_state.addTransition(transition)

        # Add animation on transition to update progress
        animation = QPropertyAnimation(self, b"_progress", self)
        animation.setEasingCurve(QEasingCurve.Type.InCubic)
        animation.setDuration(310)
        transition.addAnimation(animation)

        # Add transition from focus to normal
        transition = QEventTransition(parent, QEvent.Type.FocusOut)
        transition.setTargetState(self.normal_state)
        self.focused_state.addTransition(transition)

        # Add animation on transition to update progress
        animation = QPropertyAnimation(self, b"_progress", self)
        animation.setEasingCurve(QEasingCurve.Type.OutCubic)
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
            self.offset_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
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
            margin_top: int = self.line_edit.textMargins().top()

            # Move label on top if text in line edit is not empty
            if self.line_edit.text() == "":
                self.normal_state.assignProperty(self.label, "_offset", QPointF(0, 23))
                self.normal_state.assignProperty(self.label, "_scale", 1.0)
            else:
                self.normal_state.assignProperty(
                    self.label, "_offset", QPointF(0, 0 - margin_top)
                )
                self.normal_state.assignProperty(self.label, "_scale", 0.82)

            # Define properties values for label
            self.focused_state.assignProperty(
                self.label, "_offset", QPointF(0, 0 - margin_top)
            )
            self.focused_state.assignProperty(
                self.label, "_color", self.line_edit.ink_color()
            )
            self.normal_state.assignProperty(
                self.label, "_color", self.line_edit.label_color()
            )
            self.focused_state.assignProperty(self.label, "_scale", 0.82)

        self.line_edit.update()

    # Progress property to update
    _progress = Property(float, fset=set_progress, fget=progress)


class MaterialLineEditPrivate:
    """
    Private widget with attributes and init method to be configured
    """

    def __init__(self, line_edit: MaterialLineEdit):
        self.line_edit: MaterialLineEdit = line_edit
        self.text_color = QColor(0, 0, 0, 221)
        self.label_color = QColor(158, 158, 158)
        self.ink_color = QColor(0, 188, 212)
        self.input_line_color = QColor(224, 224, 224)
        self.label_string = ""
        self.label_font_size: float = 9.5
        self.show_label: bool = False
        self.show_input_line: bool = True
        self.use_theme_colors: bool = True
        self.label = None
        self.state_machine = None

        # Configure properties
        self.configure()

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

        # Set font on line edit
        self.line_edit.setFont(QFont("Roboto", 11, QFont.Weight.Normal))

        # Start state machine for normal/focus state
        self.state_machine.start()
        QCoreApplication.processEvents()


class MaterialLineEdit(QLineEdit):
    """
    Material line edit
    """

    def __init__(self, parent: QWidget = None, create: bool = True):
        super().__init__(parent)

        # Store trailing symbol
        self.trailing_symbol = QLabel()

        if create is True:
            self.line_edit_private = MaterialLineEditPrivate(self)

    def set_trailing_symbol(self, symbol: str):
        """
        Set trailing symbol on left

        :param symbol: symbol to set
        :return: None
        """

        self.trailing_symbol = QLabel(symbol + " ", parent=self)
        self.trailing_symbol.setFont(QFont("Roboto", 11, QFont.Weight.Normal))
        self.trailing_symbol.setStyleSheet(
            "color: " + self.text_color().name() + "; padding: 0px;"
        )
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
            self.setContentsMargins(0, 20, 0, 0)
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
        self.setStyleSheet(f"QLineEdit {{ color: {color.name()} }}")
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

    def set_ink_color(self, color: QColor) -> None:
        """
        Apply new ink color

        :param color: color to apply on ink
        :return: None
        """

        self.line_edit_private.ink_color = color
        self.line_edit_private.state_machine.setup_properties()

    def ink_color(self) -> QColor:
        """
        Return ink color

        :return: ink color
        """
        return self.line_edit_private.ink_color

    def set_input_line_color(self, color: QColor) -> None:
        """
        Set input line color

        :param color: color to set
        :return: None
        """

        self.line_edit_private.input_line_color = color
        self.line_edit_private.state_machine.setup_properties()

    def input_line_color(self) -> QColor:
        """
        Return input line color

        :return: input line color
        """
        return self.line_edit_private.input_line_color

    def show_input_line(self, value: bool) -> None:
        """
        Update input line display

        :param value: show/hide input line
        :return: None
        """
        if self.line_edit_private.show_input_line == value:
            return

        self.line_edit_private.show_input_line = value
        self.update()

    def has_input_line(self) -> bool:
        """
        Check that input line exists

        :return: True/False
        """
        return self.line_edit_private.show_input_line

    def event(self, event: QEvent) -> bool:
        """
        Override handle of event

        :param event: event to handle
        :return: True/False to accept/reject event
        """

        # Handle Resize and Move event to update geometry
        if event.type() in [QEvent.Type.Resize, QEvent.Type.Move]:
            if self.line_edit_private.label:
                self.line_edit_private.label.setGeometry(self.rect())

        return super().event(event)

    def paintEvent(self, event: QPaintEvent) -> None:
        """
        Override paintEvent()

        :param event: paint event
        :return: None
        """

        if self.trailing_symbol is not None and self.text() != "":
            self.setContentsMargins(
                self.trailing_symbol.rect().width(),
                self.contentsMargins().top(),
                self.contentsMargins().right(),
                self.contentsMargins().bottom(),
            )
        else:
            self.setContentsMargins(
                0,
                self.contentsMargins().top(),
                self.contentsMargins().right(),
                self.contentsMargins().bottom(),
            )

        super().paintEvent(event)

        if self.text() != "" and self.trailing_symbol is not None:
            self.trailing_symbol.move(self.rect().left(), self.rect().center().y() + 1)
            self.trailing_symbol.setVisible(True)
        else:
            if self.trailing_symbol is not None:
                self.trailing_symbol.setVisible(False)

        try:
            # Get progress
            progress: float = self.line_edit_private.state_machine.progress()
        except Exception:
            return

        painter = QPainter(self)

        # Handle no text and progress for background color
        if self.text() == "" and progress < 1:
            painter.setOpacity(1 - progress)
            painter.fillRect(self.rect(), QColor(Qt.GlobalColor.transparent))

        y_start: int = self.height() - 1
        width_start: int = self.width() - 5

        if self.line_edit_private.show_input_line:
            # Configure pen to draw bottom line
            pen = QPen()
            pen.setWidth(1)
            pen.setColor(self.input_line_color())

            if not self.isEnabled():
                pen.setStyle(Qt.PenStyle.DashLine)

            painter.setPen(pen)
            painter.setOpacity(1)
            painter.drawLine(QLineF(2.5, y_start, width_start, y_start))

            # Configure brush
            brush = QBrush()
            brush.setStyle(Qt.BrushStyle.SolidPattern)
            brush.setColor(self.ink_color())

            if progress > 0:
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(brush)
                width: int = int((1 - progress) * (width_start / 2))
                painter.drawRect(
                    int(width + 2.5), self.height() - 2, width_start - width * 2, 2
                )

    # Properties to animate or modify
    _textColor = Property(QColor, fset=set_text_color, fget=text_color)
    _inkColor = Property(QColor, fset=set_ink_color, fget=ink_color)
    _inputLineColor = Property(QColor, fset=set_input_line_color, fget=input_line_color)


class MaterialLineEditLabel(QWidget):
    """
    Material line edit label
    """

    def __init__(self, parent: MaterialLineEdit):
        super().__init__(parent)

        # Store attributes
        self.line_edit = parent
        self.__scale = 1.0
        self.x_position = 0.0
        self.y_position = 23.0
        self.private_color = QColor(parent.label_color())

        # Configure and apply default font
        font = QFont("Roboto", int(parent.fontInfo().pointSizeF()), QFont.Weight.Medium)
        # font.setLetterSpacing(QFont.PercentageSpacing, 102)
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

    def set_color(self, color: QColor) -> None:
        """
        Set color on label

        :param color: color to set
        :return: None
        """
        self.private_color = color
        self.update()

    def color(self) -> QColor:
        """
        Return current color

        :return: current color
        """
        return self.private_color

    def paintEvent(self, _event: QPaintEvent) -> None:
        """
        Override paintEvent

        :param _event: paint event
        :return: None
        """

        if not self.line_edit.has_label():
            return

        # Configure painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.scale(self.__scale, self.__scale)
        painter.setPen(self.private_color)
        painter.setOpacity(1)

        # Draw label with offset
        pos = QPointF(2 + self.x_position, self.height() - 32 + self.y_position)
        painter.drawText(int(pos.x()), int(pos.y()), self.line_edit.label())

    # Properties to animate or modify
    _scale = Property(float, fset=set_scale, fget=scale)
    _offset = Property(QPointF, fset=set_offset, fget=offset)
    _color = Property(QColor, fset=set_color, fget=color)


if __name__ == "__main__":
    app = QApplication([])
    widget = QWidget()
    button = MaterialLineEdit()
    button.setStyleSheet("background: transparent;")
    test = QPushButton("alors")
    button.set_label("Coucou")
    button.set_trailing_symbol("€")
    layout = QHBoxLayout()
    widget.setLayout(layout)
    layout.addWidget(test)
    layout.addWidget(button)
    layout.setContentsMargins(20, 20, 20, 20)
    button.setFixedWidth(300)
    # button.setFixedHeight(100)
    widget.show()
    sys.exit(app.exec_())
