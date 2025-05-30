# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddBank.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

from budgetter.view.widgets.material_outlined_line_edit import MaterialOutlinedLineEdit
from budgetter.view.resources import resources_rc

class Ui_AddBank(object):
    def setupUi(self, AddBank):
        if not AddBank.objectName():
            AddBank.setObjectName("AddBank")
        AddBank.resize(401, 183)
        AddBank.setStyleSheet("QWidget#bank \n"
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
"	color: #8ec6f4;\n"
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
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	background-color: rgba(255, 255, 255, 25);\n"
"	border-radius: 2px;\n"
"	outline: none;\n"
"}\n"
"\n"
"\n"
"QLineEdit\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	padding-left: 0px;\n"
"	/*border-bottom: 1px solid rgba(255, 255, 255, 180);*/\n"
"	outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"	/*border-bottom: 2px solid rgba(255, 255, 255, 230);*/\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"	/*bo"
                        "rder-bottom: 2px solid rgba(255, 255, 255, 230);*/\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	padding-left: 0px;\n"
"	/*border-bottom: 1px solid rgba(255, 255, 255, 180);*/\n"
"	outline: none;\n"
"}")
        self.gridLayout = QGridLayout(AddBank)
        self.gridLayout.setObjectName("gridLayout")
        self.bank = QWidget(AddBank)
        self.bank.setObjectName("bank")
        self.bank.setMinimumSize(QSize(0, 165))
        self.gridLayout_2 = QGridLayout(self.bank)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(10)
        self.label = QLabel(self.bank)
        self.label.setObjectName("label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgba(255, 255, 255, 180);")
        self.label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.widget = QWidget(self.bank)
        self.widget.setObjectName("widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bank_name = MaterialOutlinedLineEdit(self.widget)
        self.bank_name.setObjectName("bank_name")
        self.bank_name.setMinimumSize(QSize(260, 67))
        self.bank_name.setMaximumSize(QSize(16777215, 67))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.bank_name.setFont(font1)

        self.horizontalLayout.addWidget(self.bank_name)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 24)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.bank_logo = QToolButton(self.widget)
        self.bank_logo.setObjectName("bank_logo")
        self.bank_logo.setMinimumSize(QSize(50, 50))
        self.bank_logo.setMaximumSize(QSize(50, 50))
        self.bank_logo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(":/images/images/image_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bank_logo.setIcon(icon)
        self.bank_logo.setIconSize(QSize(28, 28))

        self.verticalLayout.addWidget(self.bank_logo)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.bank, 0, 0, 1, 1)


        self.retranslateUi(AddBank)

        QMetaObject.connectSlotsByName(AddBank)
    # setupUi

    def retranslateUi(self, AddBank):
        AddBank.setWindowTitle(QCoreApplication.translate("AddBank", "Form", None))
        self.label.setText(QCoreApplication.translate("AddBank", "<html><head/><body><p>It seems like you are adding an account to a new bank.</p></body></html>", None))
        self.bank_logo.setText("")
    # retranslateUi

