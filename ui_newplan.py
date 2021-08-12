# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newplan.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Newplan(object):
    def setupUi(self, Newplan):
        if Newplan.objectName():
            Newplan.setObjectName(u"Newplan")
        Newplan.resize(720, 480)
        Newplan.setMinimumSize(QSize(720, 480))
        Newplan.setMaximumSize(QSize(720, 480))
        self.centralwidget = QWidget(Newplan)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_background = QLabel(self.centralwidget)
        self.lb_background.setObjectName(u"lb_background")
        self.lb_background.setGeometry(QRect(0, 0, 720, 480))
        self.lb_background.setMinimumSize(QSize(720, 480))
        self.lb_background.setMaximumSize(QSize(720, 480))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 701, 371))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_newplan = QLabel(self.layoutWidget)
        self.lb_newplan.setObjectName(u"lb_newplan")
        self.lb_newplan.setMaximumSize(QSize(160, 80))

        self.verticalLayout.addWidget(self.lb_newplan)

        self.lb_nr = QLabel(self.layoutWidget)
        self.lb_nr.setObjectName(u"lb_nr")
        self.lb_nr.setMinimumSize(QSize(160, 80))
        self.lb_nr.setMaximumSize(QSize(160, 80))
        font = QFont()
        font.setFamily(u"\u7b49\u7ebf Light")
        font.setPointSize(12)
        self.lb_nr.setFont(font)

        self.verticalLayout.addWidget(self.lb_nr)

        self.lb_sj = QLabel(self.layoutWidget)
        self.lb_sj.setObjectName(u"lb_sj")
        self.lb_sj.setMaximumSize(QSize(160, 80))
        self.lb_sj.setFont(font)

        self.verticalLayout.addWidget(self.lb_sj)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(500, 80))

        self.verticalLayout_2.addWidget(self.textEdit)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dte1 = QDateTimeEdit(self.layoutWidget)
        self.dte1.setObjectName(u"dte1")
        self.dte1.setMinimumSize(QSize(160, 60))
        self.dte1.setMaximumSize(QSize(240, 60))
        self.dte1.setFont(font)

        self.horizontalLayout.addWidget(self.dte1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(20, 80))
        font1 = QFont()
        font1.setFamily(u"\u7b49\u7ebf Light")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.dte2 = QDateTimeEdit(self.layoutWidget)
        self.dte2.setObjectName(u"dte2")
        self.dte2.setMinimumSize(QSize(160, 60))
        self.dte2.setMaximumSize(QSize(240, 60))
        self.dte2.setFont(font)

        self.horizontalLayout.addWidget(self.dte2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_2.addWidget(self.label_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.pbtn_yes = QPushButton(self.centralwidget)
        self.pbtn_yes.setObjectName(u"pbtn_yes")
        self.pbtn_yes.setGeometry(QRect(560, 440, 141, 21))
        font2 = QFont()
        font2.setFamily(u"\u7b49\u7ebf Light")
        font2.setPointSize(9)
        self.pbtn_yes.setFont(font2)
        Newplan.setCentralWidget(self.centralwidget)

        self.retranslateUi(Newplan)

        QMetaObject.connectSlotsByName(Newplan)
    # setupUi

    def retranslateUi(self, Newplan):
        Newplan.setWindowTitle(QCoreApplication.translate("Newplan", u"MainWindow", None))
        self.lb_background.setText("")
        self.lb_newplan.setText(QCoreApplication.translate("Newplan", u"child_newplan", None))
        self.lb_nr.setText(QCoreApplication.translate("Newplan", u"- \u8ba1\u5212\u5185\u5bb9", None))
        self.lb_sj.setText(QCoreApplication.translate("Newplan", u"- \u8ba1\u5212\u8d77\u6b62\u65f6\u95f4", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("Newplan", u"\u81f3", None))
        self.label_4.setText("")
        self.pbtn_yes.setText(QCoreApplication.translate("Newplan", u"OK", None))
    # retranslateUi

