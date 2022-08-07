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

from PySide2.QtCore import Qt, QEvent, QPropertyAnimation, Signal, QObject, \
    QPoint, QState, QSignalTransition, QCoreApplication, QRect
from PySide2.QtGui import QPainter, QColor, QFont, QFontMetrics
from PySide2.QtWidgets import QPushButton, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QGraphicsOpacityEffect, \
    QGraphicsDropShadowEffect

from budgetter.view.widgets.flat_button import FlatButton
from budgetter.view.widgets.material_outlined_line_edit import MaterialOutlinedLineEdit, MaterialLineEditStateMachine, \
    MaterialLineEditPrivate


class MaterialAutocompleteStateMachine(MaterialLineEditStateMachine):
    """
    Material line edit state machine to handle animations
    """

    open = Signal()
    close = Signal()
    fade = Signal()

    def __init__(self, menu: QWidget, parent: MaterialOutlinedLineEdit):
        super().__init__(parent)

        self.menu = QWidget(menu)
        self.parent = parent

        # Store states for animation
        self.closed_state = QState()
        self.open_state = QState()
        self.closing_state = QState()

        super().configure(self.parent)

        # Configure animation and states
        self.configure(menu)

    def configure_auto(self, parent: QWidget):
        """
        Configure animations and states

        :parent: parent widget
        :return: None
        """

        # Add states to state machine
        self.addState(self.closed_state)
        self.addState(self.open_state)
        self.addState(self.closing_state)

        # Set initial state to closed
        self.setInitialState(self.closed_state)

        # Add transition from close to open
        transition = QSignalTransition(self, self.open)
        transition.setTargetState(self.open_state)
        self.closed_state.addTransition(transition)

        # Add transition from open to close
        transition = QSignalTransition(self, self.close)
        transition.setTargetState(self.closed_state)
        self.open_state.addTransition(transition)

        # Add transition from open to fading
        transition = QSignalTransition(self, self.fade)
        transition.setTargetState(self.closing_state)
        self.open_state.addTransition(transition)

        # Set visible values for states
        self.closed_state.assignProperty(self, "_visible", False)
        self.open_state.assignProperty(self, "_visible", True)

        # Configure effect
        effect = QGraphicsOpacityEffect()
        parent.setGraphicsEffect(effect)

        # Assign properties
        self.open_state.assignProperty(effect, "opacity", 1)
        self.closing_state.assignProperty(effect, "opacity", 0)
        self.closed_state.assignProperty(effect, "opacity", 0)

        # Add animation on transition to update opacity
        animation = QPropertyAnimation(effect, b"opacity", self)
        animation.setDuration(240)
        self.addDefaultAnimation(animation)

        # Add transition from closing to finished
        transition = QSignalTransition(self, self.finished)
        transition.setTargetState(self.closed_state)
        self.closing_state.addTransition(transition)


class MaterialAutocomplete:
    """
    Declaration to avoid conflicts
    """
    ...


class MaterialAutocompletePrivate(MaterialLineEditPrivate):
    """
    Private widget with attributes and init method to be configured
    """

    def __init__(self, autocomplete: MaterialAutocomplete):
        self.autocomplete: MaterialAutocomplete = autocomplete
        self.menu: QWidget = QWidget()
        self.frame: QWidget = QWidget()
        self.state_machine: MaterialAutocompleteStateMachine = None
        self.menu_layout: QVBoxLayout = QVBoxLayout()
        self.data = []
        self.max_width = 0
        super().__init__(autocomplete)

    def configure(self):
        """
        Configure properties

        :return: None
        """

        # Set state machine
        self.state_machine = MaterialAutocompleteStateMachine(self.menu, self.autocomplete)

        # Set parents widget for menu & frame
        self.menu.setParent(self.autocomplete.parentWidget())
        self.frame.setParent(self.autocomplete.parentWidget())

        # Install event filter for signals
        self.menu.installEventFilter(self.autocomplete)
        self.frame.installEventFilter(self.autocomplete)

        # Configure effect
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(11)
        effect.setColor(QColor(0, 0, 0, 50))
        effect.setOffset(0, 3)

        # Apply effect on frame
        self.frame.setGraphicsEffect(effect)
        self.frame.setVisible(False)

        # Configure menu (layout, style, margins)
        self.menu.setLayout(self.menu_layout)
        self.menu.setVisible(False)
        self.menu.setStyleSheet('background:transparent;')
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_layout.setSpacing(0)

        # Connect text changed to update results list
        self.autocomplete.textEdited.connect(self.autocomplete.update_results)

        # Start state machine for states
        self.state_machine.start()
        QCoreApplication.processEvents()


class MaterialAutocomplete(MaterialOutlinedLineEdit):
    """
    Material outlined autocomplete
    """

    # Signal emitted to find selected item
    selectedItem = Signal(str)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent=parent, create=True)

        # if create is True:
        self.line_edit_private = MaterialAutocompletePrivate(self)
        self.line_edit_private.configure()

    def set_data(self, data: [str]) -> None:
        """
        Update data in menu

        :param data: data to set
        :return: None
        """
        self.line_edit_private.data = data
        self.update()

    def update_results(self, text: str) -> None:
        """
        Update results to display in menu

        :param text: text
        :return: None
        """

        results = []
        trimmed = text.strip()

        # Check if typed content exists in data
        if trimmed:
            lookup = trimmed.lower()
            for result in self.line_edit_private.data:
                if lookup in result.lower():
                    results.append(result)

        diff: int = len(results) - self.line_edit_private.menu_layout.count()

        font = QFont("Roboto", 12, QFont.Normal)

        if diff > 0:
            # Add item if not already present
            for _ in range(diff):
                item = FlatButton()
                item.setFont(font)
                item.set_corner_radius(0)
                # item.setHaloVisible(False)
                item.setFixedHeight(50)
                # item.setOverlayStyle(Material.TintedOverlay)
                self.line_edit_private.menu_layout.addWidget(item)
                item.installEventFilter(self)

        elif diff < 0:
            # Remove item if it does not match typed content
            for _ in range(-diff):
                widget_in_menu: QWidget = self.line_edit_private.menu_layout.itemAt(0).widget()
                if widget_in_menu:
                    self.line_edit_private.menu_layout.removeWidget(widget_in_menu)
                    del widget_in_menu

        fm = QFontMetrics(font)
        self.line_edit_private.max_width = 0

        # Set text to added button
        for index, text in enumerate(results):
            item = self.line_edit_private.menu_layout.itemAt(index).widget()
            if isinstance(item, FlatButton):
                rect: QRect = fm.boundingRect(text)
                self.line_edit_private.max_width = max(self.line_edit_private.max_width, rect.width())
                item.setText(text)

        if not len(results):
            self.line_edit_private.state_machine.close.emit()
        else:
            self.line_edit_private.state_machine.open.emit()

        # Configure menu
        self.line_edit_private.menu.setFixedHeight(len(results) * 50)
        self.line_edit_private.menu.setFixedWidth(max(self.line_edit_private.max_width + 24, self.width()))
        self.line_edit_private.menu.update()
        self.line_edit_private.menu.setVisible(True)

    def event(self, event: QEvent) -> bool:
        """
        Override handle of event

        :param event: event to handle
        :return: True/False to accept/reject event
        """

        # Handle Resize and Move event to update geometry
        if event.type() in [QEvent.Resize, QEvent.Move]:
            self.line_edit_private.menu.move(self.pos() + QPoint(0, self.height() + 6))
        elif event.type() == QEvent.ParentChange:
            # Get parent
            parent = self.parent()

            if parent:
                self.line_edit_private.menu.setParent(parent)
                self.line_edit_private.frame.setParent(parent)

        return super().event(event)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        """
        Override eventFilter()

        :param watched: watched object
        :param event: event
        :return: True to accept event, False otherwise
        """

        if self.line_edit_private.frame == watched:
            if event.type() == QEvent.Paint:
                # Paint frame
                painter = QPainter(self.line_edit_private.frame)
                painter.fillRect(self.line_edit_private.frame.rect(), Qt.white)

        elif self.line_edit_private.menu == watched:
            if event.type() in [QEvent.Resize, QEvent.Move]:
                # Resize frame
                self.line_edit_private.frame.setGeometry(self.line_edit_private.menu.geometry())
            elif event.type() == QEvent.Show:
                # Show frame and menu
                self.line_edit_private.frame.show()
                self.line_edit_private.menu.raise_()
            elif event.type() == QEvent.Hide:
                # Hide frame
                self.line_edit_private.frame.hide()
        else:
            if event.type() == QEvent.MouseButtonPress:
                # Fade emit
                self.line_edit_private.state_machine.fade.emit()

                if type(watched) == FlatButton:
                    text: str = watched.text()
                    self.setText(text)
                    self.selectedItem.emit(text)

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication([])
    widget = QWidget()
    button = MaterialAutocomplete(widget)
    # button.setStyleSheet("background: transparent;")
    test = QPushButton('alors')
    button.set_label('Coucou')
    button.set_label_color(QColor(224, 224, 224, 255))
    button.set_label_background_color(QColor(255, 255, 255, 255))
    button.setFixedHeight(67)
    button.set_data(["donc", "voila", "alors"])
    layout = QHBoxLayout()
    widget.setLayout(layout)
    layout.addWidget(test)
    layout.addWidget(button)
    layout.setContentsMargins(20, 20, 20, 20)
    button.setFixedWidth(400)
    # button.setFixedHeight(100)
    widget.show()
    sys.exit(app.exec_())
