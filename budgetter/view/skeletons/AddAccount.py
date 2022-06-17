# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddAccount.ui'
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

from budgetter.view.widgets.material_outlined_line_edit import MaterialOutlinedLineEdit
from budgetter.view.widgets.material_outlined_date_edit import MaterialOutlinedDateEdit
from budgetter.view.widgets.material_outlined_autocomplete import MaterialAutoComplete

import resources_rc

class Ui_AddAccount(object):
    def setupUi(self, AddAccount):
        if not AddAccount.objectName():
            AddAccount.setObjectName("AddAccount")
        AddAccount.resize(377, 278)
        AddAccount.setStyleSheet("QWidget#account \n"
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
"	/*border-bottom: 2px solid rgba(255, 255, 255, 230);*/\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"	background-color: transparent;\n"
"	border: non"
                        "e;\n"
"	border-radius: 0px;\n"
"	padding-left: 0px;\n"
"	/*border-bottom: 1px solid rgba(255, 255, 255, 180);*/\n"
"	outline: none;\n"
"}")
        self.gridLayout = QGridLayout(AddAccount)
        self.gridLayout.setObjectName("gridLayout")
        self.account = QWidget(AddAccount)
        self.account.setObjectName("account")
        self.verticalLayout = QVBoxLayout(self.account)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 15, 0)
        self.label = QLabel(self.account)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(270, 0))
        font = QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgba(255, 255, 255, 180);")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.account_name = MaterialOutlinedLineEdit(self.account)
        self.account_name.setObjectName("account_name")
        font1 = QFont()
        font1.setFamily("Roboto")
        font1.setPointSize(11)
        self.account_name.setFont(font1)

        self.verticalLayout_2.addWidget(self.account_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.account_amount = MaterialOutlinedLineEdit(self.account)
        self.account_amount.setObjectName("account_amount")
        self.account_amount.setMinimumSize(QSize(170, 0))
        self.account_amount.setMaximumSize(QSize(170, 16777215))
        self.account_amount.setFont(font1)

        self.horizontalLayout.addWidget(self.account_amount)

        self.account_amount_date = MaterialOutlinedDateEdit(self.account)
        self.account_amount_date.setObjectName("account_amount_date")
        self.account_amount_date.setMinimumSize(QSize(150, 0))
        self.account_amount_date.setMaximumSize(QSize(150, 16777215))
        self.account_amount_date.setFont(font1)

        self.horizontalLayout.addWidget(self.account_amount_date)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.bank_auto_complete = MaterialAutoComplete(self.account)
        self.bank_auto_complete.setObjectName("bank_auto_complete")
        self.bank_auto_complete.setFont(font1)
        self.bank_auto_complete.setEditable(True)

        self.verticalLayout_2.addWidget(self.bank_auto_complete)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.account, 0, 0, 1, 1)


        self.retranslateUi(AddAccount)

        QMetaObject.connectSlotsByName(AddAccount)
    # setupUi

    def retranslateUi(self, AddAccount):
        AddAccount.setWindowTitle(QCoreApplication.translate("AddAccount", "Form", None))
        self.label.setText(QCoreApplication.translate("AddAccount", "Please enter account information.", None))
        self.account_amount_date.setInputMask("")
    # retranslateUi

