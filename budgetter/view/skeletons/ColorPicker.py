# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ColorPicker.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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

class Ui_ColorPicker(object):
    def setupUi(self, ColorPicker):
        if not ColorPicker.objectName():
            ColorPicker.setObjectName("ColorPicker")
        ColorPicker.resize(308, 179)
        ColorPicker.setStyleSheet("QWidget#picker \n"
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
"	/*borde"
                        "r-bottom: 2px solid rgba(255, 255, 255, 230);*/\n"
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
        self.gridLayout = QGridLayout(ColorPicker)
        self.gridLayout.setObjectName("gridLayout")
        self.picker = QWidget(ColorPicker)
        self.picker.setObjectName("picker")
        self.gridLayout_3 = QGridLayout(self.picker)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(30)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.color_2 = QToolButton(self.picker)
        self.color_2.setObjectName("color_2")
        self.color_2.setMinimumSize(QSize(30, 30))
        self.color_2.setMaximumSize(QSize(30, 30))
        self.color_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_2.setStyleSheet("QToolButton\n"
"{\n"
"	background-radius: 2px;\n"
"	background-color: #6658ca;\n"
"	border: 2px solid #2b405b;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton::checked\n"
"{\n"
"	padding: 2px;\n"
"	border: 2px solid #0190EA;\n"
"}")
        self.color_2.setCheckable(True)
        self.color_2.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.color_2, 1, 1, 1, 1)

        self.label = QLabel(self.picker)
        self.label.setObjectName("label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgba(255, 255, 255, 180);")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4)

        self.color_3 = QToolButton(self.picker)
        self.color_3.setObjectName("color_3")
        self.color_3.setMinimumSize(QSize(30, 30))
        self.color_3.setMaximumSize(QSize(30, 30))
        self.color_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_3.setStyleSheet("QToolButton\n"
"{\n"
"	background-radius: 2px;\n"
"	background-color: #0054c7;\n"
"	border: 2px solid #2b405b;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton::checked\n"
"{\n"
"	padding: 2px;\n"
"	border: 2px solid #0190EA;\n"
"}")
        self.color_3.setCheckable(True)
        self.color_3.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.color_3, 1, 2, 1, 1)

        self.color_4 = QToolButton(self.picker)
        self.color_4.setObjectName("color_4")
        self.color_4.setMinimumSize(QSize(30, 30))
        self.color_4.setMaximumSize(QSize(30, 30))
        self.color_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_4.setStyleSheet("QToolButton\n"
"{\n"
"	background-radius: 2px;\n"
"	background-color: #26c1ca;\n"
"	border: 2px solid #2b405b;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton::checked\n"
"{\n"
"	padding: 2px;\n"
"	border: 2px solid #0190EA;\n"
"}")
        self.color_4.setCheckable(True)
        self.color_4.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.color_4, 2, 0, 1, 1)

        self.color_1 = QToolButton(self.picker)
        self.color_1.setObjectName("color_1")
        self.color_1.setMinimumSize(QSize(30, 30))
        self.color_1.setMaximumSize(QSize(30, 30))
        self.color_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_1.setStyleSheet("QToolButton\n"
"{\n"
"	background-radius: 2px;\n"
"	background-color: #1ba9e9;\n"
"	border: 2px solid #2b405b;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton::checked\n"
"{\n"
"	padding: 2px;\n"
"	border: 2px solid #0190EA;\n"
"}")
        self.color_1.setCheckable(True)
        self.color_1.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.color_1, 1, 0, 1, 1)

        self.color_5 = QToolButton(self.picker)
        self.color_5.setObjectName("color_5")
        self.color_5.setMinimumSize(QSize(30, 30))
        self.color_5.setMaximumSize(QSize(30, 30))
        self.color_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_5.setStyleSheet("QToolButton\n"
"{\n"
"	background-radius: 2px;\n"
"	background-color: #fccb01;\n"
"	border: 2px solid #2b405b;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton::checked\n"
"{\n"
"	padding: 2px;\n"
"	border: 2px solid #0190EA;\n"
"}")
        self.color_5.setCheckable(True)
        self.color_5.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.color_5, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 4)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.color_edit = MaterialOutlinedLineEdit(self.picker)
        self.color_edit.setObjectName("color_edit")
        self.color_edit.setMinimumSize(QSize(100, 67))
        self.color_edit.setMaximumSize(QSize(16777215, 67))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.color_edit.setFont(font1)

        self.verticalLayout.addWidget(self.color_edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.color_choice = QLabel(self.picker)
        self.color_choice.setObjectName("color_choice")
        self.color_choice.setMinimumSize(QSize(60, 60))
        self.color_choice.setMaximumSize(QSize(60, 60))
        self.color_choice.setStyleSheet("background-radius: 2px;\n"
"background-color: #26374d;\n"
"border: 2px solid #2b405b;\n"
"border-radius: 2px;")

        self.horizontalLayout.addWidget(self.color_choice)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.picker, 0, 0, 1, 1)


        self.retranslateUi(ColorPicker)

        QMetaObject.connectSlotsByName(ColorPicker)
    # setupUi

    def retranslateUi(self, ColorPicker):
        ColorPicker.setWindowTitle(QCoreApplication.translate("ColorPicker", "Form", None))
#if QT_CONFIG(tooltip)
        self.color_2.setToolTip(QCoreApplication.translate("ColorPicker", "#6658ca", None))
#endif // QT_CONFIG(tooltip)
        self.color_2.setText("")
        self.label.setText(QCoreApplication.translate("ColorPicker", "Basic Colors", None))
#if QT_CONFIG(tooltip)
        self.color_3.setToolTip(QCoreApplication.translate("ColorPicker", "#0054c7", None))
#endif // QT_CONFIG(tooltip)
        self.color_3.setText("")
#if QT_CONFIG(tooltip)
        self.color_4.setToolTip(QCoreApplication.translate("ColorPicker", "#26c1ca", None))
#endif // QT_CONFIG(tooltip)
        self.color_4.setText("")
#if QT_CONFIG(tooltip)
        self.color_1.setToolTip(QCoreApplication.translate("ColorPicker", "#1ba9e9", None))
#endif // QT_CONFIG(tooltip)
        self.color_1.setText("")
#if QT_CONFIG(tooltip)
        self.color_5.setToolTip(QCoreApplication.translate("ColorPicker", "#fccb01", None))
#endif // QT_CONFIG(tooltip)
        self.color_5.setText("")
        self.color_choice.setText("")
    # retranslateUi

