# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImportTransactions.ui'
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
    QLayout, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)

from budgetter.view.widgets.material_outlined_line_edit import MaterialOutlinedLineEdit

class Ui_ImportTransactions(object):
    def setupUi(self, ImportTransactions):
        if not ImportTransactions.objectName():
            ImportTransactions.setObjectName("ImportTransactions")
        ImportTransactions.resize(435, 193)
        ImportTransactions.setStyleSheet("QWidget#transaction \n"
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
"\n"
"QRadioButton\n"
"{\n"
"	color: rgba(255, 255, 255, 210);\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"	background-color: #212f41;\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk \n"
"{\n"
"    background-color: #199ce5;\n"
"    border-radius: 2px;\n"
"}")
        self.gridLayout = QGridLayout(ImportTransactions)
        self.gridLayout.setObjectName("gridLayout")
        self.transaction = QWidget(ImportTransactions)
        self.transaction.setObjectName("transaction")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transaction.sizePolicy().hasHeightForWidth())
        self.transaction.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.transaction)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 15, 0)
        self.label = QLabel(self.transaction)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(270, 0))
        self.label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgba(255, 255, 255, 180);")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.import_path = MaterialOutlinedLineEdit(self.transaction)
        self.import_path.setObjectName("import_path")
        self.import_path.setMinimumSize(QSize(400, 50))
        self.import_path.setMaximumSize(QSize(400, 50))
        self.import_path.setReadOnly(True)

        self.horizontalLayout.addWidget(self.import_path)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 6, -1, 6)
        self.import_transactions_progress = QProgressBar(self.transaction)
        self.import_transactions_progress.setObjectName("import_transactions_progress")
        self.import_transactions_progress.setMaximumSize(QSize(16777215, 5))
        self.import_transactions_progress.setValue(0)
        self.import_transactions_progress.setTextVisible(False)

        self.horizontalLayout_2.addWidget(self.import_transactions_progress)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header_info = QLabel(self.transaction)
        self.header_info.setObjectName("header_info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header_info.sizePolicy().hasHeightForWidth())
        self.header_info.setSizePolicy(sizePolicy1)
        self.header_info.setMinimumSize(QSize(400, 0))
        self.header_info.setMaximumSize(QSize(400, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        font1.setItalic(True)
        self.header_info.setFont(font1)
        self.header_info.setStyleSheet("color: rgba(255, 255, 255, 100);\n"
"font-style: italic;")
        self.header_info.setTextFormat(Qt.AutoText)
        self.header_info.setScaledContents(True)
        self.header_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.header_info.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.header_info)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.transaction, 0, 0, 1, 1)


        self.retranslateUi(ImportTransactions)

        QMetaObject.connectSlotsByName(ImportTransactions)
    # setupUi

    def retranslateUi(self, ImportTransactions):
        ImportTransactions.setWindowTitle(QCoreApplication.translate("ImportTransactions", "Form", None))
        self.label.setText(QCoreApplication.translate("ImportTransactions", "Import an OFX file with transactions.", None))
        self.import_path.setText("")
        self.header_info.setText("")
    # retranslateUi

