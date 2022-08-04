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
from PySide2.QtWidgets import QPushButton, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QComboBox, QLabel, \
    QGraphicsOpacityEffect, QGraphicsDropShadowEffect
from PySide2.QtGui import QPainter, QColor, QBrush, QPen, QPaintEvent, QFont, QKeyEvent, QKeySequence, QFontMetrics
from PySide2.QtCore import Qt, QEvent, QPropertyAnimation, Signal, QObject, \
    QEasingCurve, Property, QStateMachine, QPointF, QPoint, QState, QSignalTransition, QCoreApplication, QLineF

from budgetter.view.widgets.material_outlined_line_edit import MaterialOutlinedLineEdit, MaterialLineEditPrivate
from budgetter.view.widgets.flat_button import FlatButton

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


class MaterialAutoCompleteStateMachine(QStateMachine):
    """
    Material line edit state machine to handle animations
    """

    open = Signal()
    close = Signal()
    fade = Signal()

    def __init__(self, menu: QWidget):
        super().__init__(menu)

        self.menu = QWidget(menu)

        # Store states for animation
        self.closed_state = QState()
        self.open_state = QState()
        self.closing_state = QState()

        # Configure animation and states
        self.configure(menu)

    def configure(self, parent: QWidget):
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


class MaterialAutoComplete:
    """
    Declaration to avoid conflicts
    """
    ...


class MaterialAutoCompletePrivate(MaterialLineEditPrivate):
    """
    Private widget with attributes and init method to be configured
    """

    def __init__(self, autocomplete: MaterialAutoComplete):
        self.autocomplete: MaterialAutoComplete = autocomplete
        self.menu: QWidget = QWidget()
        self.frame: QWidget = QWidget()
        self.state_machine: MaterialAutoCompleteStateMachine = None
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
        self.state_machine = MaterialAutoCompleteStateMachine(self.menu)

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
        self.menu.setStyleSheet('background:blue;')
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_layout.setSpacing(0)

        # Connect text changed to update results list
        self.autocomplete.textEdited.connect(self.autocomplete.update_results)

        # Start state machine for states
        self.state_machine.start()
        QCoreApplication.processEvents()


class MaterialAutoComplete(MaterialOutlinedLineEdit):
    """
    Material outlined autocomplete
    """

    # Signal emitted to find selected item
    selectedItem = Signal(str)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent=parent, create=False)

        # if create is True:
        self.autocomplete_private = MaterialAutoCompletePrivate(self)
        self.autocomplete_private.configure()

    def set_data(self, data: [str]) -> None:
        """
        Update data in menu

        :param data: data to set
        :return: None
        """
        self.autocomplete_private.data = data
        self.update()

    def update_results(self, text: str) -> None:
        """
        Update results to display in menu

        :param text: text
        :return: None
        """

        results = []
        trimmed = text.strip()

        if trimmed:
            lookup = trimmed.lower()
            for result in self.autocomplete_private.data:
                if lookup in result:
                    results.append(result)

        diff: int = len(results) - self.autocomplete_private.menu_layout.count()

        font = QFont("Roboto", 12, QFont.Normal)

        if diff > 0:
            for c in range(diff):
                item = FlatButton()
                item.setFont(font)
                # item.setTextAlignment(Qt.AlignLeft)
                # item.setCornerRadius(0)
                # item.setHaloVisible(False)
                item.setFixedHeight(50)
                # item.setOverlayStyle(Material.TintedOverlay)
                self.autocomplete_private.menu_layout.addWidget(item)
                item.installEventFilter(self)

        elif diff < 0:
            for c in range(-diff):
                widget_in_menu: QWidget = self.autocomplete_private.menu_layout.itemAt(0).widget()
                if widget_in_menu:
                    self.autocomplete_private.menu_layout.removeWidget(widget)
                    del widget_in_menu

        fm = QFontMetrics(font)
        self.autocomplete_private.max_width = 0

        for index, text in enumerate(results):
            item = self.autocomplete_private.menu_layout.itemAt(index).widget()
            if isinstance(item, FlatButton):
                rect: QRect = fm.boundingRect(text)
                self.autocomplete_private.max_width = max(self.autocomplete_private.max_width, rect.width())
                item.setText(text)

        if not len(results):
            self.autocomplete_private.state_machine.close.emit()
        else:
            self.autocomplete_private.state_machine.open.emit()

        self.autocomplete_private.menu.setFixedHeight(len(results) * 50)
        self.autocomplete_private.menu.setFixedWidth(max(self.autocomplete_private.max_width + 24, self.width()))
        self.autocomplete_private.menu.update()
        self.autocomplete_private.menu.setVisible(True)

    def event(self, event: QEvent) -> bool:
        """
        Override handle of event

        :param event: event to handle
        :return: True/False to accept/reject event
        """

        # Handle Resize and Move event to update geometry
        if event.type() in [QEvent.Resize, QEvent.Move]:
            self.autocomplete_private.menu.move(self.pos() + QPoint(0, self.height() + 6))
        elif event.type() == QEvent.ParentChange:
            # Get parent
            parent = self.parent()

            if parent:
                self.autocomplete_private.menu.setParent(parent)
                self.autocomplete_private.frame.setParent(parent)

        return super().event(event)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        """
        Override eventFilter()

        :param watched: watched object
        :param event: event
        :return: True to accept event, False otherwise
        """

        if self.autocomplete_private.frame == watched:
            if event.type() == QEvent.Paint:
                # Paint frame
                painter = QPainter(self.autocomplete_private.frame)
                painter.fillRect(self.autocomplete_private.frame.rect(), Qt.white)

        elif self.autocomplete_private.menu == watched:
            if event.type() in [QEvent.Resize, QEvent.Move]:
                # Resize frame
                self.autocomplete_private.frame.setGeometry(self.autocomplete_private.menu.geometry())
            elif event.type() == QEvent.Show:
                # Show frame and menu
                self.autocomplete_private.frame.show()
                self.autocomplete_private.menu.raise_()
            elif event.type() == QEvent.Hide:
                # Hide frame
                self.autocomplete_private.frame.hide()
        else:
            if event.type() == QEvent.MouseButtonPress:
                # Fade emit
                self.autocomplete_private.state_machine.fade.emit()

                if type(watched) == FlatButton:
                    text: QString = watched.text()
                    self.setText(text)
                    self.selectedItem.emit(text)

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication([])
    widget = QWidget()
    button = MaterialAutoComplete()
    # button.setStyleSheet("background: transparent;")
    test = QPushButton('alors')
    # button.set_label('Coucou')
    button.set_data(["donc", "voila", "alors"])
    layout = QHBoxLayout()
    widget.setLayout(layout)
    layout.addWidget(test)
    layout.addWidget(button)
    layout.setContentsMargins(20, 20, 20, 20)
    button.setFixedWidth(300)
    # button.setFixedHeight(100)
    widget.show()
    button.setFixedHeight(50)
    sys.exit(app.exec_())
