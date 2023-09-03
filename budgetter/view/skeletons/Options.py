# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Options.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QSizePolicy, QSpacerItem,
    QToolButton, QWidget)

from budgetter.view.widgets.line_edit_with_icon import LineEditWithIcon
from budgetter.view.resources import resources_rc

class Ui_Options(object):
    def setupUi(self, Options):
        if not Options.objectName():
            Options.setObjectName("Options")
        Options.resize(533, 46)
        Options.setStyleSheet("QWidget#content \n"
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
"	border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;\n"
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
"	border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;\n"
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
"	border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;\n"
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
"	border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
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
"	border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
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
"	border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
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
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.content = QWidget(Options)
        self.content.setObjectName("content")
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(16, 3, 16, 3)
        self.title_bar_title = QLabel(self.content)
        self.title_bar_title.setObjectName("title_bar_title")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(13)
        self.title_bar_title.setFont(font)

        self.horizontalLayout.addWidget(self.title_bar_title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.info = QLabel(self.content)
        self.info.setObjectName("info")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        font1.setItalic(False)
        self.info.setFont(font1)
        self.info.setStyleSheet("font-family: \"Roboto\";\n"
"font-size: 11pt;\n"
"font-style: normal;\n"
"font-weight: 400px;\n"
"color: #BCBCBC;")

        self.horizontalLayout.addWidget(self.info)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_bar_search = LineEditWithIcon(self.content)
        self.title_bar_search.setObjectName("title_bar_search")
        self.title_bar_search.setMinimumSize(QSize(0, 32))
        self.title_bar_search.setMaximumSize(QSize(200, 32))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        self.title_bar_search.setFont(font2)

        self.horizontalLayout_2.addWidget(self.title_bar_search)

        self.search_field = QComboBox(self.content)
        self.search_field.addItem("")
        self.search_field.addItem("")
        self.search_field.addItem("")
        self.search_field.setObjectName("search_field")
        self.search_field.setMinimumSize(QSize(0, 32))
        self.search_field.setMaximumSize(QSize(100, 32))
        self.search_field.setFont(font2)

        self.horizontalLayout_2.addWidget(self.search_field)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.upload_file = QToolButton(self.content)
        self.upload_file.setObjectName("upload_file")
        self.upload_file.setMinimumSize(QSize(28, 28))
        self.upload_file.setMaximumSize(QSize(28, 28))
        self.upload_file.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(":/images/images/upload_file_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_file.setIcon(icon)
        self.upload_file.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.upload_file)

        self.add = QToolButton(self.content)
        self.add.setObjectName("add")
        self.add.setMinimumSize(QSize(28, 28))
        self.add.setMaximumSize(QSize(28, 28))
        self.add.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(":/images/images/add_circle_outline-white-24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add.setIcon(icon1)
        self.add.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.add)


        self.gridLayout.addWidget(self.content, 0, 0, 1, 1)


        self.retranslateUi(Options)

        QMetaObject.connectSlotsByName(Options)
    # setupUi

    def retranslateUi(self, Options):
        Options.setWindowTitle(QCoreApplication.translate("Options", "Form", None))
        self.title_bar_title.setText(QCoreApplication.translate("Options", "Title", None))
        self.info.setText("")
        self.title_bar_search.setPlaceholderText(QCoreApplication.translate("Options", "Search...", None))
        self.search_field.setItemText(0, QCoreApplication.translate("Options", "Name", None))
        self.search_field.setItemText(1, QCoreApplication.translate("Options", "Amount", None))
        self.search_field.setItemText(2, QCoreApplication.translate("Options", "Date", None))

#if QT_CONFIG(tooltip)
        self.upload_file.setToolTip(QCoreApplication.translate("Options", "Upload OFX File", None))
#endif // QT_CONFIG(tooltip)
        self.upload_file.setText("")
        self.add.setText("")
    # retranslateUi

