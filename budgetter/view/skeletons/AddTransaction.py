# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddTransaction.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
    QRadioButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

from budgetter.view.widgets.material_outlined_date_edit import MaterialOutlinedDateEdit
from budgetter.view.widgets.material_outlined_line_edit import MaterialOutlinedLineEdit
import resources_rc

class Ui_AddTransaction(object):
    def setupUi(self, AddTransaction):
        if not AddTransaction.objectName():
            AddTransaction.setObjectName("AddTransaction")
        AddTransaction.resize(457, 409)
        AddTransaction.setStyleSheet("QWidget#transaction \n"
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
"	border:"
                        " none;\n"
"	border-radius: 0px;\n"
"	padding-left: 0px;\n"
"	/*border-bottom: 1px solid rgba(255, 255, 255, 180);*/\n"
"	outline: none;\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"	outline: none;\n"
"}\n"
"\n"
"QRadioButton::indicator \n"
"{\n"
"    width: 22px;\n"
"    height: 22px;\n"
"}\n"
"\n"
"QRadioButton#expenses::indicator::checked \n"
"{\n"
"	image: url(:/images/images/radio_button_checked_FILL0_wght400_GRAD0_opsz48_expenses.svg);\n"
"}\n"
"\n"
"QRadioButton#expenses::indicator::unchecked \n"
"{\n"
"	image: url(:/images/images/radio_button_unchecked_FILL0_wght400_GRAD0_opsz48_expenses.svg);\n"
"}\n"
"\n"
"QRadioButton#income::indicator::checked \n"
"{\n"
"	image: url(:/images/images/radio_button_checked_FILL0_wght400_GRAD0_opsz48_income.svg);\n"
"}\n"
"\n"
"QRadioButton#income::indicator::unchecked \n"
"{\n"
"	image: url(:/images/images/radio_button_unchecked_FILL0_wght400_GRAD0_opsz48_income.svg);\n"
"}\n"
"\n"
"QRadioButton#transfer::indicator::checked \n"
"{\n"
"	image: url(:/images/images/radio_button_c"
                        "hecked_FILL0_wght400_GRAD0_opsz48_transfer.svg);\n"
"}\n"
"\n"
"QRadioButton#transfer::indicator::unchecked \n"
"{\n"
"	image: url(:/images/images/radio_button_unchecked_FILL0_wght400_GRAD0_opsz48_transfer.svg);\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"	border: none;\n"
"	border-radius: 3px;\n"
"	outline: none;\n"
"}")
        self.gridLayout = QGridLayout(AddTransaction)
        self.gridLayout.setObjectName("gridLayout")
        self.transaction = QWidget(AddTransaction)
        self.transaction.setObjectName("transaction")
        self.verticalLayout = QVBoxLayout(self.transaction)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 15, 0)
        self.label = QLabel(self.transaction)
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
        self.radio_buttons = QHBoxLayout()
        self.radio_buttons.setSpacing(30)
        self.radio_buttons.setObjectName("radio_buttons")
        self.radio_buttons.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.radio_buttons.addItem(self.horizontalSpacer)

        self.expenses = QRadioButton(self.transaction)
        self.expenses.setObjectName("expenses")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.expenses.setFont(font1)
        self.expenses.setCursor(QCursor(Qt.PointingHandCursor))
        self.expenses.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.expenses.setChecked(True)

        self.radio_buttons.addWidget(self.expenses)

        self.income = QRadioButton(self.transaction)
        self.income.setObjectName("income")
        self.income.setFont(font1)
        self.income.setCursor(QCursor(Qt.PointingHandCursor))
        self.income.setStyleSheet("color: rgba(255, 255, 255, 210);")

        self.radio_buttons.addWidget(self.income)

        self.transfer = QRadioButton(self.transaction)
        self.transfer.setObjectName("transfer")
        self.transfer.setFont(font1)
        self.transfer.setCursor(QCursor(Qt.PointingHandCursor))
        self.transfer.setStyleSheet("color: rgba(255, 255, 255, 210);")

        self.radio_buttons.addWidget(self.transfer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.radio_buttons.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.radio_buttons)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 17, -1, -1)
        self.category_icon = QToolButton(self.transaction)
        self.category_icon.setObjectName("category_icon")
        self.category_icon.setEnabled(False)
        self.category_icon.setMinimumSize(QSize(52, 52))
        self.category_icon.setMaximumSize(QSize(52, 52))
        self.category_icon.setFocusPolicy(Qt.NoFocus)
        self.category_icon.setStyleSheet("background-color: #21405D;")
        icon = QIcon()
        icon.addFile(":/images/images/category_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.category_icon.setIcon(icon)
        self.category_icon.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.category_icon)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.category = MaterialOutlinedLineEdit(self.transaction)
        self.category.setObjectName("category")
        self.category.setMinimumSize(QSize(200, 67))
        self.category.setMaximumSize(QSize(16777215, 67))
        self.category.setFont(font1)

        self.horizontalLayout.addWidget(self.category)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name = MaterialOutlinedLineEdit(self.transaction)
        self.name.setObjectName("name")
        self.name.setMinimumSize(QSize(200, 67))
        self.name.setMaximumSize(QSize(16777215, 67))
        self.name.setFont(font1)

        self.horizontalLayout_2.addWidget(self.name)

        self.amount = MaterialOutlinedLineEdit(self.transaction)
        self.amount.setObjectName("amount")
        self.amount.setMinimumSize(QSize(170, 67))
        self.amount.setMaximumSize(QSize(170, 67))
        self.amount.setFont(font1)

        self.horizontalLayout_2.addWidget(self.amount)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.date = MaterialOutlinedDateEdit(self.transaction)
        self.date.setObjectName("date")
        self.date.setMinimumSize(QSize(0, 67))
        self.date.setMaximumSize(QSize(16777215, 67))
        self.date.setFont(font1)

        self.horizontalLayout_4.addWidget(self.date)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.card = QRadioButton(self.transaction)
        self.card.setObjectName("card")
        self.card.setFont(font1)
        self.card.setCursor(QCursor(Qt.PointingHandCursor))
        self.card.setStyleSheet("color: rgba(255, 255, 255, 210);")

        self.horizontalLayout_5.addWidget(self.card)

        self.cash = QRadioButton(self.transaction)
        self.cash.setObjectName("cash")
        self.cash.setFont(font1)
        self.cash.setCursor(QCursor(Qt.PointingHandCursor))
        self.cash.setStyleSheet("color: rgba(255, 255, 255, 210);")

        self.horizontalLayout_5.addWidget(self.cash)

        self.money_transfer = QRadioButton(self.transaction)
        self.money_transfer.setObjectName("money_transfer")
        self.money_transfer.setFont(font1)
        self.money_transfer.setCursor(QCursor(Qt.PointingHandCursor))
        self.money_transfer.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.money_transfer.setIconSize(QSize(22, 22))

        self.horizontalLayout_5.addWidget(self.money_transfer)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.notes = MaterialOutlinedLineEdit(self.transaction)
        self.notes.setObjectName("notes")
        self.notes.setMinimumSize(QSize(0, 67))
        self.notes.setMaximumSize(QSize(16777215, 67))
        self.notes.setFont(font1)

        self.verticalLayout_2.addWidget(self.notes)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.transaction, 0, 0, 1, 1)


        self.retranslateUi(AddTransaction)

        QMetaObject.connectSlotsByName(AddTransaction)
    # setupUi

    def retranslateUi(self, AddTransaction):
        AddTransaction.setWindowTitle(QCoreApplication.translate("AddTransaction", "Form", None))
        self.label.setText(QCoreApplication.translate("AddTransaction", "Please enter transaction information.", None))
        self.expenses.setText(QCoreApplication.translate("AddTransaction", "Expenses", None))
        self.income.setText(QCoreApplication.translate("AddTransaction", "Income", None))
        self.transfer.setText(QCoreApplication.translate("AddTransaction", "Transfer", None))
        self.category_icon.setText("")
        self.card.setText(QCoreApplication.translate("AddTransaction", "Credit Card", None))
        self.cash.setText(QCoreApplication.translate("AddTransaction", "Cash", None))
        self.money_transfer.setText(QCoreApplication.translate("AddTransaction", "Money Transfer", None))
    # retranslateUi

