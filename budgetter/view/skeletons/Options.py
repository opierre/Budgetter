# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Options.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            QSize, Qt)
from PySide2.QtGui import (QCursor, QFont,
                           QIcon)
from PySide2.QtWidgets import *

from budgetter.view.widgets.line_edit_with_icon import LineEditWithIcon


class Ui_Options(object):
    def setupUi(self, Options):
        if not Options.objectName():
            Options.setObjectName(u"Options")
        Options.resize(533, 42)
        Options.setStyleSheet(u"QWidget#content \n"
"{\n"
"	background-color: #26374C;\n"
"	border: 1px solid #344457;\n"
"	border-bottom: 1px solid transparent;\n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"}\n"
"\n"
"QLineEdit#title_bar_search\n"
"{\n"
"	border: 0px solid transparent;\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(44, 64, 90, 255);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QLineEdit::focus\n"
"{\n"
"	border: 1px solid #0190EA;\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-l"
                        "eft: 5px;\n"
"	padding-right: 3px;\n"
"	background: rgba(28, 41, 59, 128);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QLineEdit#title_bar_search::hover\n"
"{\n"
"	border: 0px solid transparent;\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	background: rgba(44, 64, 90, 255);\n"
"	color: white;\n"
"	selection-background-color: #0190EA;\n"
"}\n"
"\n"
"QComboBox \n"
"{\n"
"	border: 0px solid transparent;\n"
"	border-left: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(44, 64, 90, 255), stop:0.24 rgba(44, 64, 90, 255), stop:0.25 #75879B, stop:0.75 #75879B, stop:0.76 rgba(44, 64, 90, 255), stop:1 rgba(44, 64, 90, 255));\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px"
                        ";\n"
"	padding-left: 9px;\n"
"	padding-right: 3px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	background: rgba(44, 64, 90, 255);\n"
"	color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"QComboBox::hover\n"
"{\n"
"	border: 0px solid transparent;\n"
"	border-left: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(44, 64, 90, 255), stop:0.24 rgba(44, 64, 90, 255), stop:0.25 #75879B, stop:0.75 #75879B, stop:0.76 rgba(44, 64, 90, 255), stop:1 rgba(44, 64, 90, 255));\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	padding-left: 9px;\n"
"	padding-right: 5px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	background: rgba(44, 64, 90, 255);\n"
"	color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"QComboBox::focus\n"
"{\n"
"	border: 0px solid #0190EA;\n"
"	border-left: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(44, 64, 90, 255), stop:0.24 rgba(44, 64, 90, 2"
                        "55), stop:0.25 #75879B, stop:0.75 #75879B, stop:0.76 rgba(44, 64, 90, 255), stop:1 rgba(44, 64, 90, 255));\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	padding-left: 9px;\n"
"	padding-right: 5px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	background: rgba(44, 64, 90, 255);\n"
"	color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	border: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/images/images/expand_more-white-18dp_opacity.svg);\n"
"	width: 18px;\n"
"	height: 18px;\n"
"	padding-right: 15px;\n"
"	padding-top: 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"	image: url(:/images/images/expand_less-white-18dp_opacity.svg);\n"
"	width: 18px;\n"
"	height: 18px;\n"
"	padding-right: 15px;\n"
"	padding-top: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"	background: #212F41;\n"
"	color: white;\n"
""
                        "	border-top-style: inset;\n"
"	border-width: 0px;\n"
"	border-radius: 3px;\n"
"	border-color: #0190EA;\n"
"	selection-background-color: #0190EA;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	outline: none;\n"
"	margin-top: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item\n"
"{\n"
"	min-height: 35px;\n"
"}\n"
"\n"
"QComboBox QScollBar:vertical\n"
"{\n"
"	border: 0px;\n"
"	background: transparent;\n"
"	width: 10px;\n"
"	margin: 1px 1 1px 0;\n"
"}\n"
"\n"
"QComboBox QScollBar::handle:vertical\n"
"{\n"
"	background: #0190EA;\n"
"	min-height: 20px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"	background-color: #26374C;\n"
"	border-top: 0px solid #344457;\n"
"	border-right: 0px solid #344457;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"	padding-bottom: 0px;\n"
"	padding-left: 0px;\n"
"	pad"
                        "ding-top: 0px;\n"
"}\n"
"\n"
"QLabel#title_bar_title \n"
"{\n"
"	background-color: #26374C;\n"
"	border: 0px solid transparent;\n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"	padding-bottom: 10px;\n"
"	padding-left: 0px;\n"
"	padding-top: 10px;\n"
"	color: white;\n"
"}")
        self.gridLayout = QGridLayout(Options)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.content = QWidget(Options)
        self.content.setObjectName(u"content")
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(16, 3, 16, 3)
        self.title_bar_title = QLabel(self.content)
        self.title_bar_title.setObjectName(u"title_bar_title")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(13)
        self.title_bar_title.setFont(font)

        self.horizontalLayout.addWidget(self.title_bar_title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.title_bar_search = LineEditWithIcon(self.content)
        self.title_bar_search.setObjectName(u"title_bar_search")
        self.title_bar_search.setMinimumSize(QSize(0, 28))
        self.title_bar_search.setMaximumSize(QSize(200, 28))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(11)
        self.title_bar_search.setFont(font1)

        self.horizontalLayout_2.addWidget(self.title_bar_search)

        self.search_field = QComboBox(self.content)
        self.search_field.addItem("")
        self.search_field.addItem("")
        self.search_field.addItem("")
        self.search_field.setObjectName(u"search_field")
        self.search_field.setMinimumSize(QSize(0, 28))
        self.search_field.setMaximumSize(QSize(100, 28))
        self.search_field.setFont(font1)

        self.horizontalLayout_2.addWidget(self.search_field)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.add = QToolButton(self.content)
        self.add.setObjectName(u"add")
        self.add.setMinimumSize(QSize(28, 28))
        self.add.setMaximumSize(QSize(28, 28))
        self.add.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/images/images/add_circle_outline-white-24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add.setIcon(icon)
        self.add.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.add)


        self.gridLayout.addWidget(self.content, 0, 0, 1, 1)


        self.retranslateUi(Options)

        QMetaObject.connectSlotsByName(Options)
    # setupUi

    def retranslateUi(self, Options):
        Options.setWindowTitle(QCoreApplication.translate("Options", u"Form", None))
        self.title_bar_title.setText(QCoreApplication.translate("Options", u"Title", None))
        self.title_bar_search.setPlaceholderText(QCoreApplication.translate("Options", u"Search...", None))
        self.search_field.setItemText(0, QCoreApplication.translate("Options", u"Name", None))
        self.search_field.setItemText(1, QCoreApplication.translate("Options", u"Amount", None))
        self.search_field.setItemText(2, QCoreApplication.translate("Options", u"Date", None))

        self.add.setText("")
    # retranslateUi
