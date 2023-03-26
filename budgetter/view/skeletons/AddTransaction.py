# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddTransaction.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel,
                               QRadioButton, QSizePolicy, QSpacerItem, QToolButton,
                               QVBoxLayout, QWidget)

from budgetter.view.widgets.material_outlined_date_edit import MaterialOutlinedDateEdit
from budgetter.view.widgets.material_outlined_line_edit import MaterialOutlinedLineEdit


class Ui_AddTransaction(object):
    def setupUi(self, AddTransaction):
        if not AddTransaction.objectName():
            AddTransaction.setObjectName("AddTransaction")
        AddTransaction.resize(427, 431)
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
                                     "}\n"
                                     "\n"
                                     "QRadioButton#card::indicator::checked \n"
                                     "{\n"
                                     "	image: url(:/images/images/credit_card_FILL1_wght400_GRAD0_opsz48.svg);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton#card::indicator::unchecked \n"
                                     "{\n"
                                     "	image: url(:/images/images/credit_card_FILL0_wght400_GRAD0_opsz48.svg);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton#cash::indicator::checked \n"
                                     "{\n"
                                     "	image: url(:/images/images/local_atm_FILL1_wght400_GRAD0_opsz48.svg);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton#cash::indicator::unchecked \n"
                                     "{\n"
                                     "	image: url(:/images/images/local_atm_FILL0_wght400_GRAD0_opsz48.svg);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton#money_transfer::indicator::checked \n"
                                     "{\n"
                                     "	image: url(:/images/images/swap_horizontal_circle_FILL1_wght400_GRAD0_opsz48.svg);\n"
                                     "}\n"
                                     ""
                                     "\n"
                                     "QRadioButton#money_transfer::indicator::unchecked \n"
                                     "{\n"
                                     "	image: url(:/images/images/swap_horizontal_circle_FILL0_wght400_GRAD0_opsz48.svg);\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton#cash::indicator, QRadioButton#card::indicator, QRadioButton#money_transfer::indicator \n"
                                     "{\n"
                                     "    width: 26px;\n"
                                     "    height: 26px;\n"
                                     "}\n"
                                     "")
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
        self.widget = QWidget(self.transaction)
        self.widget.setObjectName("widget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(336, 32))
        self.widget.setMaximumSize(QSize(16777215, 32))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.expenses = QRadioButton(self.widget)
        self.expenses.setObjectName("expenses")
        self.expenses.setMinimumSize(QSize(92, 0))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.expenses.setFont(font1)
        self.expenses.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.expenses.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.expenses.setChecked(True)

        self.horizontalLayout_3.addWidget(self.expenses)

        self.income = QRadioButton(self.widget)
        self.income.setObjectName("income")
        self.income.setMinimumSize(QSize(92, 0))
        self.income.setFont(font1)
        self.income.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.income.setStyleSheet("color: rgba(255, 255, 255, 210);")

        self.horizontalLayout_3.addWidget(self.income)

        self.transfer = QRadioButton(self.widget)
        self.transfer.setObjectName("transfer")
        self.transfer.setMinimumSize(QSize(92, 0))
        self.transfer.setFont(font1)
        self.transfer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.transfer.setStyleSheet("color: rgba(255, 255, 255, 210);")

        self.horizontalLayout_3.addWidget(self.transfer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addWidget(self.widget)

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
        icon.addFile(":/images/images/category_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal,
                     QIcon.State.Off)
        self.category_icon.setIcon(icon)
        self.category_icon.setIconSize(QSize(30, 30))

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

        self.account = MaterialOutlinedLineEdit(self.transaction)
        self.account.setObjectName("account")
        self.account.setMinimumSize(QSize(170, 67))
        self.account.setMaximumSize(QSize(16777215, 67))

        self.horizontalLayout_2.addWidget(self.account)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.date = MaterialOutlinedDateEdit(self.transaction)
        self.date.setObjectName("date")
        self.date.setMinimumSize(QSize(0, 67))
        self.date.setMaximumSize(QSize(16777215, 67))
        self.date.setFont(font1)

        self.horizontalLayout_4.addWidget(self.date)

        self.amount = MaterialOutlinedLineEdit(self.transaction)
        self.amount.setObjectName("amount")
        self.amount.setMinimumSize(QSize(170, 67))
        self.amount.setMaximumSize(QSize(16777215, 67))
        self.amount.setFont(font1)

        self.horizontalLayout_4.addWidget(self.amount)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(30)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, 10, -1, 0)
        self.notes = MaterialOutlinedLineEdit(self.transaction)
        self.notes.setObjectName("notes")
        self.notes.setMinimumSize(QSize(0, 67))
        self.notes.setMaximumSize(QSize(16777215, 67))
        self.notes.setFont(font1)

        self.gridLayout_2.addWidget(self.notes, 1, 0, 1, 3)

        self.widget_2 = QWidget(self.transaction)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setMinimumSize(QSize(20, 32))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 2, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.card = QRadioButton(self.widget_2)
        self.card.setObjectName("card")
        self.card.setMinimumSize(QSize(92, 0))
        self.card.setFont(font1)
        self.card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.card.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.card.setChecked(True)

        self.horizontalLayout_6.addWidget(self.card)

        self.cash = QRadioButton(self.widget_2)
        self.cash.setObjectName("cash")
        self.cash.setMinimumSize(QSize(92, 0))
        self.cash.setFont(font1)
        self.cash.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cash.setStyleSheet("color: rgba(255, 255, 255, 210);")

        self.horizontalLayout_6.addWidget(self.cash)

        self.money_transfer = QRadioButton(self.widget_2)
        self.money_transfer.setObjectName("money_transfer")
        self.money_transfer.setMinimumSize(QSize(92, 0))
        self.money_transfer.setFont(font1)
        self.money_transfer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.money_transfer.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.money_transfer.setIconSize(QSize(22, 22))

        self.horizontalLayout_6.addWidget(self.money_transfer)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 3)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout.addWidget(self.transaction, 0, 0, 1, 1)

        QWidget.setTabOrder(self.expenses, self.income)
        QWidget.setTabOrder(self.income, self.transfer)
        QWidget.setTabOrder(self.transfer, self.category)
        QWidget.setTabOrder(self.category, self.name)
        QWidget.setTabOrder(self.name, self.account)
        QWidget.setTabOrder(self.account, self.date)
        QWidget.setTabOrder(self.date, self.amount)
        QWidget.setTabOrder(self.amount, self.card)
        QWidget.setTabOrder(self.card, self.cash)
        QWidget.setTabOrder(self.cash, self.money_transfer)
        QWidget.setTabOrder(self.money_transfer, self.notes)

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
        self.card.setText(QCoreApplication.translate("AddTransaction", "Card", None))
        self.cash.setText(QCoreApplication.translate("AddTransaction", "Cash", None))
        self.money_transfer.setText(QCoreApplication.translate("AddTransaction", "Transfer", None))
    # retranslateUi
