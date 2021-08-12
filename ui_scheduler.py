# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scheduler.ui'
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


class Ui_Scheduler(object):
    def setupUi(self, Scheduler):
        if Scheduler.objectName():
            Scheduler.setObjectName(u"Scheduler")
        Scheduler.resize(900, 600)
        Scheduler.setMinimumSize(QSize(900, 600))
        Scheduler.setMaximumSize(QSize(900, 600))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        Scheduler.setFont(font)
        Scheduler.setAcceptDrops(True)
        self.centralwidget = QWidget(Scheduler)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_background = QLabel(self.centralwidget)
        self.lb_background.setObjectName(u"lb_background")
        self.lb_background.setGeometry(QRect(0, 0, 900, 600))
        self.lb_background.setMaximumSize(QSize(1080, 720))
        self.lb_trushbox = QLabel(self.centralwidget)
        self.lb_trushbox.setObjectName(u"lb_trushbox")
        self.lb_trushbox.setGeometry(QRect(-1000, 440, 101, 81))
        font1 = QFont()
        font1.setPointSize(9)
        self.lb_trushbox.setFont(font1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 20, 811, 551))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Left = QVBoxLayout()
        self.Left.setObjectName(u"Left")
        self.lb_title = QLabel(self.layoutWidget)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setMaximumSize(QSize(160, 80))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.lb_title.setFont(font2)

        self.Left.addWidget(self.lb_title)

        self.pbtn_plan = QPushButton(self.layoutWidget)
        self.pbtn_plan.setObjectName(u"pbtn_plan")
        self.pbtn_plan.setMaximumSize(QSize(160, 80))

        self.Left.addWidget(self.pbtn_plan)

        self.pbtn_clear = QPushButton(self.layoutWidget)
        self.pbtn_clear.setObjectName(u"pbtn_clear")
        self.pbtn_clear.setMaximumSize(QSize(160, 80))

        self.Left.addWidget(self.pbtn_clear)

        self.lb_note = QLabel(self.layoutWidget)
        self.lb_note.setObjectName(u"lb_note")
        self.lb_note.setMaximumSize(QSize(160, 200))
        font3 = QFont()
        font3.setFamily(u"\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53")
        font3.setPointSize(13)
        font3.setKerning(True)
        self.lb_note.setFont(font3)
        self.lb_note.setFocusPolicy(Qt.NoFocus)
        self.lb_note.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.lb_note.setLayoutDirection(Qt.LeftToRight)
        self.lb_note.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.Left.addWidget(self.lb_note)


        self.horizontalLayout.addLayout(self.Left)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Right_top = QHBoxLayout()
        self.Right_top.setObjectName(u"Right_top")
        self.pbtn_charts = QPushButton(self.layoutWidget)
        self.pbtn_charts.setObjectName(u"pbtn_charts")
        self.pbtn_charts.setMaximumSize(QSize(160, 80))

        self.Right_top.addWidget(self.pbtn_charts)

        self.pbtn_settings = QPushButton(self.layoutWidget)
        self.pbtn_settings.setObjectName(u"pbtn_settings")
        self.pbtn_settings.setMaximumSize(QSize(160, 80))

        self.Right_top.addWidget(self.pbtn_settings)

        self.pbtn_personal = QPushButton(self.layoutWidget)
        self.pbtn_personal.setObjectName(u"pbtn_personal")
        self.pbtn_personal.setMaximumSize(QSize(160, 80))

        self.Right_top.addWidget(self.pbtn_personal)


        self.verticalLayout.addLayout(self.Right_top)

        self.lb_plate = QLabel(self.layoutWidget)
        self.lb_plate.setObjectName(u"lb_plate")
        self.lb_plate.setMinimumSize(QSize(550, 400))
        self.lb_plate.setMaximumSize(QSize(550, 400))
        self.lb_plate.setAcceptDrops(True)
        self.lb_plate.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.lb_plate)


        self.horizontalLayout.addLayout(self.verticalLayout)

        Scheduler.setCentralWidget(self.centralwidget)
        self.lb_background.raise_()
        self.layoutWidget.raise_()
        self.lb_trushbox.raise_()
        self.menuBar = QMenuBar(Scheduler)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 900, 17))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        Scheduler.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(Scheduler)

        QMetaObject.connectSlotsByName(Scheduler)
    # setupUi

    def retranslateUi(self, Scheduler):
        Scheduler.setWindowTitle(QCoreApplication.translate("Scheduler", u"\u65f6\u95f4\u7ba1\u7406\u5de5\u5177", None))
        self.lb_background.setText("")
        self.lb_trushbox.setText("")
        self.lb_title.setText(QCoreApplication.translate("Scheduler", u"LogoArea", None))
        self.pbtn_plan.setText("")
        self.pbtn_clear.setText("")
        self.lb_note.setText("")
        self.pbtn_charts.setText("")
        self.pbtn_settings.setText("")
        self.pbtn_personal.setText("")
        self.lb_plate.setText("")
        self.menu.setTitle(QCoreApplication.translate("Scheduler", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("Scheduler", u"\u4fdd\u5b58", None))
    # retranslateUi

