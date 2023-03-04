# Copyright 2018 by Edwin Christian Yllanes Cucho, @eyllanesc (Github/Stack Overflow).
# All rights reserved.
# This file is released under the Attribution-ShareAlike 4.0 International
# (CC BY-SA 4.0 - https://creativecommons.org/licenses/by-sa/4.0/legalcode)
# Link to the material : https://stackoverflow.com/questions/52596386/slide-qstackedwidget-page
# Compatible license : GPLv3 \
# https://creativecommons.org/share-your-work/licensing-considerations/compatible-licenses
#################################################################################################
# Changes :
# - Change of default direction from Horizontal to Vertical
# - Add signal when animation finished

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Signal


class SlidingStackedWidget(QtWidgets.QStackedWidget):
    """
    Sligin Stacked Widget
    """

    # Signal emitted when animation finished
    animationFinished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_direction = QtCore.Qt.Vertical
        self.m_speed = 500
        self.m_animationtype = QtCore.QEasingCurve.Type.OutCubic
        self.m_now = 0
        self.m_next = 0
        self.m_wrap = False
        self.m_pnow = QtCore.QPoint(0, 0)
        self.m_active = False

    def setDirection(self, direction):
        self.m_direction = direction

    def setSpeed(self, speed):
        self.m_speed = speed

    def setAnimation(self, animationtype):
        self.m_animationtype = animationtype

    def setWrap(self, wrap):
        self.m_wrap = wrap

    def slideInPrev(self):
        now = self.currentIndex()
        if self.m_wrap or now > 0:
            self.slideInIdx(now - 1)

    def slideInNext(self):
        now = self.currentIndex()
        if self.m_wrap or now < (self.count() - 1):
            self.slideInIdx(now + 1)

    def slideInIdx(self, idx):
        if idx > (self.count() - 1):
            idx = idx % self.count()
        elif idx < 0:
            idx = (idx + self.count()) % self.count()
        self.slideInWgt(self.widget(idx))

    def slideInWgt(self, newwidget):
        if self.m_active:
            return

        self.m_active = True

        _now = self.currentIndex()
        _next = self.indexOf(newwidget)

        if _now == _next:
            self.m_active = False
            return

        offset_x, offset_y = self.frameRect().width(), self.frameRect().height()
        self.widget(_next).setGeometry(self.frameRect())

        if self.m_direction != QtCore.Qt.Horizontal:
            if _now < _next:
                offset_x, offset_y = 0, -offset_y
            else:
                offset_x = 0
        else:
            if _now < _next:
                offset_x, offset_y = -offset_x, 0
            else:
                offset_y = 0

        pnext = self.widget(_next).pos()
        pnow = self.widget(_now).pos()
        self.m_pnow = pnow

        offset = QtCore.QPoint(offset_x, offset_y)
        self.widget(_next).move(pnext - offset)
        self.widget(_next).show()
        self.widget(_next).raise_()

        anim_group = QtCore.QParallelAnimationGroup(
            self, finished=self.animationDoneSlot
        )

        for index, start, end in zip(
                (_now, _next), (pnow, pnext - offset), (pnow + offset, pnext)
        ):
            animation = QtCore.QPropertyAnimation(
                self.widget(index),
                b"pos",
                duration=self.m_speed,
                easingCurve=self.m_animationtype,
                startValue=start,
                endValue=end
            )
            anim_group.addAnimation(animation)

        self.m_next = _next
        self.m_now = _now
        self.m_active = True
        anim_group.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

    def animationDoneSlot(self):
        self.setCurrentIndex(self.m_next)
        self.widget(self.m_now).hide()
        self.widget(self.m_now).move(self.m_pnow)
        self.m_active = False
        self.animationFinished.emit()
