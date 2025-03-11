# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Toaster.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QSizePolicy, QToolButton, QWidget)
from budgetter.view.resources import resources_rc

class Ui_Notification(object):
    def setupUi(self, Notification):
        if not Notification.objectName():
            Notification.setObjectName("Notification")
        Notification.resize(319, 82)
        Notification.setMinimumSize(QSize(0, 0))
        Notification.setMaximumSize(QSize(16777215, 16777215))
        Notification.setStyleSheet("QWidget#content\n"
"{\n"
"	background: #1e95d6;\n"
"	border: none;\n"
"	border-radius: 4px;\n"
"	outline: none;\n"
"}\n"
"\n"
"QWidget#content[state=\"warning\"]\n"
"{\n"
"	background: #d84646;\n"
"}\n"
"\n"
"QWidget#content[state=\"error\"]\n"
"{\n"
"	background: #d84646;\n"
"}\n"
"\n"
"QWidget#content[state=\"success\"]\n"
"{\n"
"	background: #43a047;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	font-family: \"Roboto\";\n"
"	font-style: normal;\n"
"	font-weight: 500;\n"
"	font-size: 16px;\n"
"	color: #F7F7F7;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Notification)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.content = QWidget(Notification)
        self.content.setObjectName("content")
        self.content.setMinimumSize(QSize(0, 70))
        self.content.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 40, 10)
        self.icon = QToolButton(self.content)
        self.icon.setObjectName("icon")
        self.icon.setEnabled(False)
        self.icon.setMinimumSize(QSize(50, 50))
        self.icon.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(":/images/success", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.icon.setIcon(icon1)
        self.icon.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.icon)

        self.message = QLabel(self.content)
        self.message.setObjectName("message")
        self.message.setMinimumSize(QSize(0, 50))
        self.message.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_2.addWidget(self.message)


        self.horizontalLayout.addWidget(self.content)


        self.retranslateUi(Notification)

        QMetaObject.connectSlotsByName(Notification)
    # setupUi

    def retranslateUi(self, Notification):
        Notification.setWindowTitle(QCoreApplication.translate("Notification", "Form", None))
        self.icon.setText("")
        self.message.setText(QCoreApplication.translate("Notification", "This is a success message!", None))
    # retranslateUi

