# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Account.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QLineEdit, QSizePolicy, QWidget)

class Ui_Account(object):
    def setupUi(self, Account):
        if not Account.objectName():
            Account.setObjectName("Account")
        Account.resize(565, 504)
        Account.setStyleSheet("QWidget#account\n"
"{\n"
"	background-color: #1C293B;\n"
"	border: none;\n"
"	border-radius: 2px;\n"
"	outline: none;\n"
"}")
        self.gridLayout = QGridLayout(Account)
        self.gridLayout.setObjectName("gridLayout")
        self.account = QWidget(Account)
        self.account.setObjectName("account")
        self.comboBox = QComboBox(self.account)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(280, 160, 69, 22))
        self.lineEdit = QLineEdit(self.account)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(170, 290, 113, 20))
        self.doubleSpinBox = QDoubleSpinBox(self.account)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(220, 360, 62, 22))

        self.gridLayout.addWidget(self.account, 0, 0, 1, 1)


        self.retranslateUi(Account)

        QMetaObject.connectSlotsByName(Account)
    # setupUi

    def retranslateUi(self, Account):
        Account.setWindowTitle(QCoreApplication.translate("Account", "Form", None))
    # retranslateUi

