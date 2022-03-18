# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Account.ui'
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


class Ui_Account(object):
    def setupUi(self, Account):
        if not Account.objectName():
            Account.setObjectName("Account")
        Account.resize(565, 504)
        self.gridLayout = QGridLayout(Account)
        self.gridLayout.setObjectName("gridLayout")
        self.account = QWidget(Account)
        self.account.setObjectName("account")

        self.gridLayout.addWidget(self.account, 0, 0, 1, 1)


        self.retranslateUi(Account)

        QMetaObject.connectSlotsByName(Account)
    # setupUi

    def retranslateUi(self, Account):
        Account.setWindowTitle(QCoreApplication.translate("Account", "Form", None))
    # retranslateUi

