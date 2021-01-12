# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transactiontIgSzu.ui'
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


class Ui_transaction(object):
    def setupUi(self, transaction):
        if not transaction.objectName():
            transaction.setObjectName(u"transaction")
        transaction.resize(1085, 129)
        self.gridLayout = QGridLayout(transaction)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_2 = QPushButton(transaction)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 5, 2, 1)

        self.label_2 = QLabel(transaction)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)

        self.comboBox_2 = QComboBox(transaction)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 0, 4, 1, 1)

        self.lineEdit = QLineEdit(transaction)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.comboBox = QComboBox(transaction)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(transaction)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 2, 1, 1)

        self.dateEdit = QDateEdit(transaction)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 0, 3, 1, 1)

        self.pushButton = QPushButton(transaction)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 2, 1)

        self.label = QLabel(transaction)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.label_3 = QLabel(transaction)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 4, 1, 1)

        self.label_4 = QLabel(transaction)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 6, 2, 1)


        self.retranslateUi(transaction)

        QMetaObject.connectSlotsByName(transaction)
    # setupUi

    def retranslateUi(self, transaction):
        transaction.setWindowTitle(QCoreApplication.translate("transaction", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("transaction", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("transaction", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("transaction", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("transaction", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("transaction", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("transaction", u"TextLabel", None))
    # retranslateUi

