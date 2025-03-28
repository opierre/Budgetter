# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddAccount.ui'
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

from budgetter.view.widgets.material_outlined_date_edit import MaterialOutlinedDateEdit
from budgetter.view.widgets.material_outlined_line_edit import MaterialOutlinedLineEdit
from budgetter.view.resources import resources_rc

class Ui_AddAccount(object):
    def setupUi(self, AddAccount):
        if not AddAccount.objectName():
            AddAccount.setObjectName("AddAccount")
        AddAccount.resize(377, 345)
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
"QToolButton:hover\n"
"{\n"
"	background-color: rgba(255, 255, 255, 25);\n"
"	border-radius: 2px;\n"
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
"	/*bord"
                        "er-bottom: 2px solid rgba(255, 255, 255, 230);*/\n"
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
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgba(255, 255, 255, 180);")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.account_name = MaterialOutlinedLineEdit(self.account)
        self.account_name.setObjectName("account_name")
        self.account_name.setMinimumSize(QSize(0, 67))
        self.account_name.setMaximumSize(QSize(16777215, 67))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.account_name.setFont(font1)

        self.horizontalLayout_2.addWidget(self.account_name)

        self.widget = QWidget(self.account)
        self.widget.setObjectName("widget")
        self.widget.setMinimumSize(QSize(0, 67))
        self.widget.setMaximumSize(QSize(16777215, 67))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.color_picker = QToolButton(self.widget)
        self.color_picker.setObjectName("color_picker")
        self.color_picker.setMinimumSize(QSize(50, 50))
        self.color_picker.setMaximumSize(QSize(50, 50))
        self.color_picker.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(":/images/images/palette_FILL0_wght500_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.color_picker.setIcon(icon)
        self.color_picker.setIconSize(QSize(28, 28))

        self.verticalLayout_4.addWidget(self.color_picker)


        self.horizontalLayout_2.addWidget(self.widget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.account_number = MaterialOutlinedLineEdit(self.account)
        self.account_number.setObjectName("account_number")
        self.account_number.setMinimumSize(QSize(0, 67))
        self.account_number.setMaximumSize(QSize(16777215, 67))
        self.account_number.setFont(font1)

        self.horizontalLayout_3.addWidget(self.account_number)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.account_amount = MaterialOutlinedLineEdit(self.account)
        self.account_amount.setObjectName("account_amount")
        self.account_amount.setMinimumSize(QSize(170, 67))
        self.account_amount.setMaximumSize(QSize(170, 67))
        self.account_amount.setFont(font1)

        self.horizontalLayout.addWidget(self.account_amount)

        self.account_amount_date = MaterialOutlinedDateEdit(self.account)
        self.account_amount_date.setObjectName("account_amount_date")
        self.account_amount_date.setMinimumSize(QSize(150, 67))
        self.account_amount_date.setMaximumSize(QSize(150, 67))
        self.account_amount_date.setFont(font1)

        self.horizontalLayout.addWidget(self.account_amount_date)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.account_bank = MaterialOutlinedLineEdit(self.account)
        self.account_bank.setObjectName("account_bank")
        self.account_bank.setMinimumSize(QSize(0, 67))
        self.account_bank.setMaximumSize(QSize(16777215, 67))
        self.account_bank.setFont(font1)

        self.verticalLayout_2.addWidget(self.account_bank)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.account, 0, 0, 1, 1)


        self.retranslateUi(AddAccount)

        QMetaObject.connectSlotsByName(AddAccount)
    # setupUi

    def retranslateUi(self, AddAccount):
        AddAccount.setWindowTitle(QCoreApplication.translate("AddAccount", "Form", None))
        self.label.setText(QCoreApplication.translate("AddAccount", "Please enter account information.", None))
        self.color_picker.setText("")
        self.account_amount_date.setInputMask("")
    # retranslateUi

