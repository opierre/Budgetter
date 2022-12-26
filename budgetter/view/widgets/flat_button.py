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
from typing import List

from PySide6.QtCore import Qt, QEvent, QObject, QParallelAnimationGroup, QPropertyAnimation, QRect, QPoint, \
    QEasingCurve, Property
from PySide6.QtGui import QPainter, QColor, QBrush, QPainterPath, QPaintEvent, QMouseEvent, QResizeEvent
from PySide6.QtWidgets import QPushButton, QWidget, QApplication, QHBoxLayout


class WaveOverlay:
    """
    Declaration to avoid conflicts
    """


class OverlayWidget(QWidget):
    """
    Overlay to apply on widget
    """

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        if parent:
            parent.installEventFilter(self)

    def event(self, event: QEvent) -> bool:
        """
        Override event() to handle geometry resize

        :param event: event
        :return: True/False
        """

        if not self.parent():
            return QWidget.event(self, event)

        event_type = event.type()

        if event_type == QEvent.ParentChange:
            # Install event filter on new parent
            self.parent().installEventFilter(self)

            # Resize according to new parent size
            self.setGeometry(self.overlay_geometry())

        elif event_type == QEvent.ParentAboutToChange:
            # Remove current event filter on existing parent
            self.parent().removeEventFilter(self)

        return QWidget.event(self, event)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        """
        Override eventFilter()

        :param watched: watched object
        :param event: event to filter
        :return: True/False to accept/reject event action
        """

        event_type = event.type()

        if event_type in {QEvent.Move, QEvent.Resize}:
            # Resize according to resize
            self.setGeometry(self.overlay_geometry())

        return QWidget.eventFilter(self, watched, event)

    def overlay_geometry(self) -> QRect:
        """
        Return overlay geometry according to parent geometry

        :return: overlay geometry
        """

        parent_widget: QWidget = self.parentWidget()

        if not parent_widget:
            return QRect()

        return parent_widget.rect()


class Wave(QParallelAnimationGroup):
    """
    Wave animation
    """

    def __init__(self, center: QPoint, overlay: WaveOverlay = None, parent: QObject = None):
        super().__init__(parent)

        # Store attributes for animation
        self.overlay = overlay
        self.private_radius = 0.0
        self.private_opacity = 0.0
        self._center = QPoint(center)
        self._brush = QBrush()

        # Store animation on radius expand and opacity
        self.radius_animation = self.animate(b"_radius")
        self.opacity_animation = self.animate(b"_opacity")

        # Configure animations
        self.set_opacity_values(0.5, 0)
        self.set_radius_values(0, 300)

        # Configure brush style
        self._brush.setColor(Qt.black)
        self._brush.setStyle(Qt.SolidPattern)

        # Connect animation finished to destroy
        self.finished.connect(self.destroy)  # pylint: disable=no-member

    def set_overlay(self, overlay: WaveOverlay) -> None:
        """
        Apply overlay on animation

        :param overlay: overlay to set
        :return: None
        """

        self.overlay = overlay

    def set_radius(self, radius: float) -> None:
        """
        Set radius on wave animation

        :param radius: radius
        :return: None
        """

        if self.private_radius == radius:
            # Do not update overlay
            return
        self.private_radius = radius
        self.overlay.update()

    def radius(self) -> float:
        """
        Getter for radius wave

        :return: radius
        """

        return self.private_radius

    def set_opacity(self, opacity: float) -> None:
        """
        Update opacity

        :param opacity: opacity to set
        :return: None
        """

        if self.private_opacity == opacity:
            # Do not update overlay
            return
        self.private_opacity = opacity
        self.overlay.update()

    def opacity(self) -> float:
        """
        Getter for opacity wave

        :return: radius
        """

        return self.private_opacity

    def brush(self) -> QBrush:
        """
        Getter for brush wave

        :return: brush
        """

        return self._brush

    def set_color(self, color: QColor) -> None:
        """
        Update color

        :param color: color to set
        :return: None
        """

        if self._brush.color() == color:
            # Do not update overlay
            return
        self._brush.setColor(color)

        if self.overlay:
            self.overlay.update()

    def color(self) -> QColor:
        """
        Return current color

        :return: current color
        """

        return self._brush.color()

    def center(self) -> QPoint:
        """
        Return center point on wave (== click pos)

        :return: center point
        """

        return self._center

    def set_radius_animation_duration(self, duration: float) -> None:
        """
        Update radius duration animation

        :return: None
        """

        self.radius_animation.setDuration(duration)

    def set_opacity_animation_duration(self, duration: float) -> None:
        """
        Update opacity duration animation

        :return: None
        """

        self.opacity_animation.setDuration(duration)

    def set_opacity_values(self, start_value: float, end_value: float) -> None:
        """
        Set opacity start/end value for animation

        :param start_value: start value to set
        :param end_value: end value to set
        :return: None
        """

        self.opacity_animation.setStartValue(start_value)
        self.opacity_animation.setEndValue(end_value)

    def set_radius_values(self, start_value: float, end_value: float) -> None:
        """
        Set radius start/end value for animation

        :param start_value: start value to set
        :param end_value: end value to set
        :return: None
        """

        self.radius_animation.setStartValue(start_value)
        self.radius_animation.setEndValue(end_value)

    def destroy(self) -> None:
        """
        Destroy animation beahvior: remove wave

        :return: None
        """

        self.overlay.remove_wave(self)

    def animate(self, _property: bytes, easing: QEasingCurve = QEasingCurve.OutQuad,
                duration: int = 800) -> QPropertyAnimation:
        """
        Create animation on property with default values

        :param _property: property to animate
        :param easing: wave form
        :param duration: duration
        :return: animation created
        """

        # Create animation and set properties
        animation = QPropertyAnimation()
        animation.setTargetObject(self)
        animation.setPropertyName(_property)
        animation.setEasingCurve(easing)
        animation.setDuration(duration)
        self.addAnimation(animation)

        return animation

    # Define properties to animate
    _radius = Property(float, fset=set_radius, fget=radius)
    _opacity = Property(float, fset=set_opacity, fget=opacity)


class WaveOverlay(OverlayWidget):
    """
    Override default wave overlay
    """

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        # Store attributes
        self.waves: List[Wave] = []
        self.clip_path = QPainterPath()
        self.use_clip = False

        # Set attributes on overlay to hide background and set transparent
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_NoSystemBackground)

    def add_wave(self, wave: Wave = None, position: QPoint = None, radius: float = 300) -> None:
        """
        Add wave in overlay

        :param wave: wave to add
        :param position: position to center on
        :param radius: radius end value for animation
        :return: None
        """

        if not wave:
            # Create default wave
            wave = Wave(center=position)
            wave.setRadiusEndValue(radius)
            self.add_wave(wave=wave)

        # Set overlay on wave
        wave.set_overlay(self)
        self.waves.append(wave)

        # Start animation
        wave.start()

        # On destroyed signal stop animation and remove object
        self.destroyed.connect(wave.stop)  # pylint: disable=no-member
        self.destroyed.connect(wave.deleteLater)  # pylint: disable=no-member

    def remove_wave(self, wave: Wave) -> None:
        """
        Remove existing wave

        :param wave: wave to remove
        :return: None
        """

        if self.waves.remove(wave):
            del self.ripple
            self.update()

    def set_clipping(self, enable: bool) -> None:
        """
        Update clipping flag

        :param enable: value to set
        :return: None
        """

        self.use_clip = enable
        self.update()

    def set_clip_path(self, path: QPainterPath) -> None:
        """
        Update clip path for wave to follow

        :param path: clipping path
        :return: None
        """

        self.clip_path = path
        self.update()

    def paintEvent(self, _event: QPaintEvent) -> None:
        """
        Override paintEvent()

        :param _event: paint event
        :return: None
        """

        # Define painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # Use clip path
        if self.use_clip:
            painter.setClipPath(self.clip_path)

        # Paint each wave
        for wave in self.waves:
            self.paint_wave(painter, wave)

    @staticmethod
    def paint_wave(painter: QPainter, wave: Wave) -> None:
        """
        Paint each wave with wave properties

        :param painter: painter
        :param wave: wave
        :return: None
        """

        radius: float = wave.radius()
        center = wave.center()
        painter.setOpacity(wave.opacity())
        painter.setBrush(wave.brush())
        painter.drawEllipse(center, radius, radius)


class FlatButton(QPushButton):
    """
    Flat Button with animation
    """

    def __init__(self, text: str = '', parent=None):
        super().__init__(text, parent)

        # Store corner radius
        self.corner_radius = 4.0

        # Store and configure wave overlay
        self.wave_overlay = WaveOverlay(self)

        # Set clipping path overlay on button
        path = QPainterPath()
        path.addRoundedRect(self.rect(), 4, 4)
        self.wave_overlay.set_clip_path(path)
        self.wave_overlay.set_clipping(True)

    def resizeEvent(self, event: QResizeEvent) -> None:
        """
        Override resizeEvent() to handle resize of animation and clipping path

        :param event: resize event
        :return: None
        """

        super().resizeEvent(event)
        self.update_clip_path()

    def set_corner_radius(self, radius: float):
        """
        Update corner radius

        :param radius: radius to set
        :return: None
        """

    def update_clip_path(self) -> None:
        """
        Update clipping path to fit with button

        :return: None
        """

        # Set radius
        radius = self.corner_radius

        # Update path
        path = QPainterPath()
        path.addRoundedRect(self.rect(), radius, radius)
        self.wave_overlay.set_clip_path(path)

    def mousePressEvent(self, event: QMouseEvent):
        """
        Override mousePressEvent() to start animation

        :param event: event
        :return: None
        """

        # Get position on click
        pos = event.pos()
        radius_end_value = self.width()

        # Define and configure wave
        wave = Wave(pos)
        wave.set_radius_values(0, radius_end_value)
        wave.set_opacity_values(0.35, 1)
        wave.set_color(QColor(142, 198, 244, 100))
        wave.set_opacity_animation_duration(1200)
        wave.set_radius_animation_duration(600)
        self.wave_overlay.add_wave(wave)

        # Call super method to handle event
        super().mousePressEvent(event)


if __name__ == '__main__':
    app = QApplication([])
    widget = QWidget()
    button = FlatButton("I'm flat")
    button.setStyleSheet("	background-color: rgba(128, 128, 128, 128); "
                         "color: #8ec6f4; "
                         "outline: none; "
                         "padding-left: 8px; "
                         "padding-right: 8px; "
                         "padding-top: 8px; "
                         "padding-bottom: 8px;"
                         "border-radius: 14px;")
    layout = QHBoxLayout()
    widget.setLayout(layout)
    layout.addWidget(button)
    layout.setContentsMargins(20, 20, 20, 20)
    button.setFixedWidth(300)
    button.setFixedHeight(100)
    widget.show()
    sys.exit(app.exec_())
