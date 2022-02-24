from PySide2.QtWidgets import QWidget


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
        self.drop_shadow = QGraphicsDropShadow()
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

    def show(self):
        """
        Override show method

        :return: None
        """

        # Raise dialog widget on top of all window
        self._raise()

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
        drop_shadow_animation.setKeyValue(0, QColor(0, 0, 0, 0, 0))
        drop_shadow_animation.setKeyValue(1, QColor(19, 32, 43, 200))
        drop_shadow_animation.setDuration(100)

        # Set drop shadow effect on dialog
        self.setGraphicsEffect(self.drop_shadow)

        # Add new animation to parallel group after clearing
        self.parallel_animation_group.clear()
        self.parallel_animation_group.addAnimation(drop_shadow_animation)
        self.parallel_animation_group.finished.disconnect(self.show_drop_shadow)
        self.parallel_animation_group.start()
