# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel,
                               QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
                               QWidget)

from budgetter.view.widgets.flat_button import FlatButton


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(628, 533)
        Dialog.setStyleSheet("QWidget#dialog \n"
                             "{\n"
                             "	background-color: #1C293B;\n"
                             "	border: none;\n"
                             "	border-radius: 4px;\n"
                             "	outline: none;\n"
                             "}\n"
                             "\n"
                             "QPushButton\n"
                             "{\n"
                             "	background-color: transparent;\n"
                             "	color: rgba(25, 157, 229, 210);\n"
                             "	outline: none;\n"
                             "	padding-left: 8px;\n"
                             "	padding-right: 8px;\n"
                             "	padding-top: 8px;\n"
                             "	padding-bottom: 8px;\n"
                             "	border-radius: 4px;\n"
                             "}\n"
                             "\n"
                             "QPushButton:hover\n"
                             "{\n"
                             "	background-color: rgba(140, 195, 240, 30);\n"
                             "}\n"
                             "\n"
                             "QToolButton\n"
                             "{\n"
                             "	background-color: transparent;\n"
                             "	outline: none;\n"
                             "}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.dialog = QWidget(Dialog)
        self.dialog.setObjectName("dialog")
        self.verticalLayout = QVBoxLayout(self.dialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(25, 25, 10, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 15, -1)
        self.header_icon = QToolButton(self.dialog)
        self.header_icon.setObjectName("header_icon")
        self.header_icon.setEnabled(False)
        self.header_icon.setMinimumSize(QSize(28, 28))
        self.header_icon.setMaximumSize(QSize(28, 28))
        self.header_icon.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.header_icon)

        self.title = QLabel(self.dialog)
        self.title.setObjectName("title")
        font = QFont()
        font.setFamilies([u"Roboto Medium"])
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgba(255, 255, 255, 230);")

        self.horizontalLayout_2.addWidget(self.title)

        self.close = QToolButton(self.dialog)
        self.close.setObjectName("close")
        self.close.setMinimumSize(QSize(28, 28))
        self.close.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(":/images/images/close_white_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close.setIcon(icon)
        self.close.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.close)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.central_widget = QWidget(self.dialog)
        self.central_widget.setObjectName("central_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.central_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)

        self.verticalLayout.addWidget(self.central_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.confirm = FlatButton(self.dialog)
        self.confirm.setObjectName("confirm")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(11)
        self.confirm.setFont(font1)
        self.confirm.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.confirm)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout.addWidget(self.dialog, 0, 0, 1, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate(b"Dialog", "Form", None))
        self.header_icon.setText("")
        self.title.setText(QCoreApplication.translate(b"Dialog", "Header", None))
        self.close.setText("")
        self.confirm.setText(QCoreApplication.translate(b"Dialog", "CONFIRM", None))
    # retranslateUi
