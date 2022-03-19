# Copyright (c) 2021 Pierre OLIVIER
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from PySide2.QtWidgets import QWidget, QGraphicsDropShadowEffect, QGraphicsOpacityEffect
from PySide2.QtCore import QParallelAnimationGroup, QPropertyAnimation, QRect, QObject, QEvent
from PySide2.QtGui import QColor

from budgetter.view.skeletons.Dialog import Ui_Dialog


class Dialog(QWidget):
    """
    Dialog with animation
    """

    def __init__(self, dialog_title: str, central_widget: QWidget, parent=None):
        super().__init__(parent)

        # Store dialog UI
        self._dialog = Ui_Dialog()

        # Setup UI on current widget
        self._dialog.setupUi(self)

        # Store effects: drop shadow + opacity effect
        self.drop_shadow = QGraphicsDropShadowEffect()
        self.opacity = QGraphicsOpacityEffect(opacity=0)

        # Store animation group for parallel effects
        self.parallel_animation_group = QParallelAnimationGroup(self)

        # Configure widgets
        self.configure_widgets(dialog_title, central_widget)

        # Show dialog
        self.show()

    def configure_widgets(self, dialog_title: str, central_widget: QWidget):
        """
        Configure title, central widget and animations

        :param dialog_title: dialog main title
        :param central_widget: central widget
        :return: None
        """

        # Configure title
        self._dialog.title.setText(dialog_title)

        # Configure animations - Geometry and opacity
        geometry_animation = QPropertyAnimation(self, b'geometry')
        geometry_animation.setDuration(200)
        self.parallel_animation_group.addAnimation(geometry_animation)

        opacity_animation = QPropertyAnimation(self, b'opacity')
        opacity_animation.setStartValue(0)
        opacity_animation.setEndValue(1)
        opacity_animation.setDuration(200)
        self.parallel_animation_group.addAnimation(opacity_animation)

        # Set initial opacity effect
        self.setGraphicsEffect(self.opacity)

        # Set central widget
        self._dialog.central_widget.layout().setContentsMargins(0, 0, 0, 0)
        self._dialog.central_widget.layout().addWidget(central_widget)

        # Install event filter on parent in order to replace dialog on center after resize/move
        self.parent().installEventFilter(self)

    def show(self):
        """
        Override show method

        :return: None
        """

        # Raise dialog widget on top of all window
        self.raise_()

        # Resize dialog to minimum space
        self.adjustSize()

        # Set dialog on center of main window
        self.geometry().moveCenter(self.parent().rect().center())

        # Update geometry animation coordinates for y
        geometry = self.geometry()
        start_animation_rect = QRect(geometry.x(),
                                     geometry.y() - geometry.height() / 3.0,
                                     geometry.width(),
                                     geometry.height())
        self.parallel_animation_group.animationAt(0).setStartValue(start_animation_rect)
        self.parallel_animation_group.animationAt(0).setEndValue(geometry)

        # Show dialog
        super().show()

        # Start parallel animation
        self.parallel_animation_group.finished.connect(self.show_drop_shadow)
        self.parallel_animation_group.start()

    def show_drop_shadow(self):
        """
        Show drop shadow when animation completed and start new animation to appear

        :return: None
        """

        # Configure drop shadow effect
        self.drop_shadow.setBlurRadius(64)
        self.drop_shadow.setOffset(0, 13)

        # Configure animation on color for drop shadow to get smooth
        drop_shadow_animation = QPropertyAnimation(self.drop_shadow, b'color')
        drop_shadow_animation.setKeyValueAt(0, QColor(0, 0, 0, 0))
        drop_shadow_animation.setKeyValueAt(1, QColor(19, 32, 43, 200))
        drop_shadow_animation.setDuration(100)

        # Set drop shadow effect on dialog
        self.setGraphicsEffect(self.drop_shadow)

        # Add new animation to parallel group after clearing
        self.parallel_animation_group.clear()
        self.parallel_animation_group.addAnimation(drop_shadow_animation)
        self.parallel_animation_group.finished.disconnect(self.show_drop_shadow)
        self.parallel_animation_group.start()

    def close(self) -> bool:
        """
        Override close()

        :return: boolean
        """

        # Hide overlay
        self.overlay.hide()

        return super().close()

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        """
        Override eventFilter()

        :param watched: watched
        :param event: event
        :return: True/False to accept/reject event
        """

        if watched == self.parent() and event.type() == QEvent.Resize:
            # Stop animations
            self.animation_group.stop()

            # Call reset to update animations and opacity
            self.reset()

        return super().eventFilter(watched, event)

    def reset(self):
        """
        Define reset behavior: stop animations and reset opacity and geometry

        :return: None
        """

        # Stop timer and animations
        self.parallel_animation_group.stop()

        # Reset opacity to full and drop shadow visible
        self.opacity = QGraphicsOpacityEffect(opacity=1)
        self.setGraphicsEffect(self.opacity)
        self.drop_shadow = QGraphicsDropShadowEffect()
        self.drop_shadow.setColor(QColor(19, 32, 43, 200))
        self.drop_shadow.setBlurRadius(64)
        self.drop_shadow.setOffset(0, 13)
        self.setGraphicsEffect(self.drop_shadow)

        # Update geometry
        dialog_geometry = self.geometry()
        dialog_geometry.moveCenter(self.parent().rect().center())
        self.setGeometry(dialog_geometry)

    def adjust_size(self):
        """
        Adjust size on expand

        :return: None
        """

        # Resize to minimum space
        self.adjustSize()

        # Move dialog on center
        dialog_geometry = self.geometry()
        dialog_geometry.moveCenter(self.parent().rect().center())
        self.setGeometry(dialog_geometry)
