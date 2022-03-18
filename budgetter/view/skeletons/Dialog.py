# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(628, 533)
        Dialog.setStyleSheet(u"QWidget#dialog \n"
"{\n"
"	background-color: #1C293B;\n"
"	border: none;\n"
"	border-radius: 2px;\n"
"	outline: none;\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dialog = QWidget(Dialog)
        self.dialog.setObjectName(u"dialog")
        self.verticalLayout = QVBoxLayout(self.dialog)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 25, 25, 25)
        self.title = QLabel(self.dialog)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"Roboto Medium")
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgba(255, 255, 255, 230);")

        self.verticalLayout.addWidget(self.title)

        self.central_widget = QWidget(self.dialog)
        self.central_widget.setObjectName(u"central_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.central_widget)


        self.gridLayout.addWidget(self.dialog, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Form", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Header", None))
    # retranslateUi

