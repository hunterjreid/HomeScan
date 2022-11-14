# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scan.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 1141)
        MainWindow.setStyleSheet(u"border: unset;")
        self.app = QWidget(MainWindow)
        self.app.setObjectName(u"app")
        self.horizontalLayout = QHBoxLayout(self.app)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(self.app)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(54, 54, 54, 255), stop:1 rgba(44, 48, 50, 255))")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.name_and_tabs = QFrame(self.main)
        self.name_and_tabs.setObjectName(u"name_and_tabs")
        self.name_and_tabs.setEnabled(True)
        self.name_and_tabs.setMaximumSize(QSize(16777215, 34))
        self.name_and_tabs.setStyleSheet(u"")
        self.name_and_tabs.setFrameShape(QFrame.StyledPanel)
        self.name_and_tabs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.name_and_tabs)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, 0)
        self.label = QLabel(self.name_and_tabs)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border:none;background: none;\n"
"color:lightgray;\n"
"font-size:17px;")

        self.horizontalLayout_3.addWidget(self.label)

        self.frame_12 = QFrame(self.name_and_tabs)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(30, 0))
        self.frame_12.setMaximumSize(QSize(112, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.min = QPushButton(self.frame_12)
        self.min.setObjectName(u"min")
        self.min.setStyleSheet(u"background-color: lightgray;\n"
"border: none;\n"
"top:0;border-radius: 0;\n"
"width:30px;")
        icon = QIcon()
        icon.addFile(u"assets/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.min)

        self.full = QPushButton(self.frame_12)
        self.full.setObjectName(u"full")
        self.full.setStyleSheet(u"background-color: lightgray;\n"
"border: none;\n"
"top:0;border-radius: 0;")
        icon1 = QIcon()
        icon1.addFile(u"assets/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.full.setIcon(icon1)

        self.horizontalLayout_9.addWidget(self.full)

        self.exit = QPushButton(self.frame_12)
        self.exit.setObjectName(u"exit")
        self.exit.setStyleSheet(u"background-color: #e15b5d;\n"
"border: none;\n"
"top:0;border-radius: 0;\n"
"margin-top:0px;")
        icon2 = QIcon()
        icon2.addFile(u"assets/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.exit)


        self.horizontalLayout_3.addWidget(self.frame_12)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.name_and_tabs)

        self.footer = QFrame(self.main)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background:none;\n"
"border:none;")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.footer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.footer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 461, 51))
        self.label_2.setStyleSheet(u"color:white;\n"
"font-size:19px;")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 150, 231, 31))
        self.pushButton.setStyleSheet(u"color:white;\n"
"background:black;")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(570, 50, 200, 37))
        self.pushButton_4.setMinimumSize(QSize(0, 37))
        self.pushButton_4.setMaximumSize(QSize(200, 16777215))
        self.pushButton_4.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(37, 37, 37, 255), stop:1 rgba(19, 19, 19, 255));\n"
"color:rgb(255, 255, 255);\n"
"font-size:17px;\n"
"border:none;")
        icon3 = QIcon()
        icon3.addFile(u"assets/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(37, 37))

        self.verticalLayout_6.addWidget(self.frame)

        self.frame_9 = QFrame(self.footer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(700, 0))
        self.frame_9.setMaximumSize(QSize(728, 16777215))
        self.frame_9.setStyleSheet(u"background: none;\n"
"border:none;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color:white;\n"
"font-size:15px;\n"
"background:none;\n"
"border:none;")

        self.verticalLayout_7.addWidget(self.label_5)

        self.frame_3 = QFrame(self.frame_9)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(400, 81))
        self.frame_3.setMaximumSize(QSize(16777215, 111))
        self.frame_3.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.0454545, y1:0.313, x2:0.550318, y2:0.489, stop:0 rgba(144, 144, 144, 125), stop:1 rgba(73, 73, 73, 55));\n"
"border-color: white;\n"
"border: 2px;\n"
"border: 1px solid rgb(34, 34, 34);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 120, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_2 = QCheckBox(self.frame_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"border:none;background: none;\n"
"color:rgb(213, 213, 213);\n"
"font-size:13px;")

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.frame_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"border:none;background: none;\n"
"color:lightgray;\n"
"\n"
"font-size:13px;")

        self.horizontalLayout_2.addWidget(self.checkBox)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border:none;background: none;\n"
"color:lightgray;\n"
"font-size:17px;")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"background-color: lightgray;\n"
"border: 20px;\n"
"top:0;\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_11.addLayout(self.verticalLayout_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout_7.addWidget(self.frame_3)


        self.verticalLayout_6.addWidget(self.frame_9, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.app)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"HomeScan Pro Edition", None))
        self.min.setText("")
        self.full.setText("")
        self.exit.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CLICK THE BUTTON BELOW TO START THE SCAN", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Back to main page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Export Result(s):", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Network Connections", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Port Results", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Export format", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Text File .txt", None))
    # retranslateUi

