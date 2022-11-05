# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conn_list.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

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
        self.name_and_tabs = QFrame(self.main)
        self.name_and_tabs.setObjectName(u"name_and_tabs")
        self.name_and_tabs.setEnabled(True)
        self.name_and_tabs.setGeometry(QRect(0, 0, 279, 23))
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

        self.color_bar = QFrame(self.main)
        self.color_bar.setObjectName(u"color_bar")
        self.color_bar.setGeometry(QRect(0, 23, 924, 20))
        self.color_bar.setMinimumSize(QSize(0, 20))
        self.color_bar.setMaximumSize(QSize(16777215, 20))
        self.color_bar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0.00568182 rgba(227, 198, 43, 255), stop:1 rgba(191, 32, 32, 255))")
        self.color_bar.setFrameShape(QFrame.StyledPanel)
        self.color_bar.setFrameShadow(QFrame.Raised)
        self.pushButton_14 = QPushButton(self.main)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(200, 900, 311, 71))
        self.pushButton_14.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(37, 37, 37, 255), stop:1 rgba(19, 19, 19, 255));\n"
"color:rgb(255, 255, 255);\n"
"font-size:17px;\n"
"border:none;")
        icon3 = QIcon()
        icon3.addFile(u"../assets/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon3)
        self.label_7 = QLabel(self.main)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 102, 16, 23))
        self.label_7.setStyleSheet(u"color: white;\n"
"border: 20px;\n"
"top:0;\n"
"border: none;\n"
"background: none;\n"
"font-size: 19px;")
        self.label_7.setPixmap(QPixmap(u"assets/qt.png"))
        self.label_5 = QLabel(self.main)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 351, 111))
        self.label_5.setStyleSheet(u"color:white;\n"
"font-size:25px;\n"
"background:none;\n"
"border:none;")
        self.listWidget = QListWidget(self.main)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 110, 701, 491))
        self.listWidget.setStyleSheet(u"background: black;\n"
"color: white;\n"
"padding: 20px;\n"
"font-size:20px;\n"
"border: 1.4px dashed orange;")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit = QTextEdit(self.main)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 680, 700, 201))
        self.textEdit.setMinimumSize(QSize(400, 0))
        self.textEdit.setMaximumSize(QSize(700, 16777215))
        self.textEdit.setStyleSheet(u"background: white;\n"
"color: black;\n"
"padding: 20px;")
        self.label_2 = QLabel(self.main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 610, 341, 41))
        self.label_2.setStyleSheet(u"color:orange;\n"
"font-size:25px;\n"
"background:none;\n"
"border:none;")
        self.lineEdit = QLineEdit(self.main)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(300, 610, 211, 41))
        self.lineEdit.setStyleSheet(u"background: white;\n"
"color: black;\n"
"font-size:20px\n"
"")
        self.pushButton_15 = QPushButton(self.main)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(530, 610, 201, 51))
        self.pushButton_15.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(37, 37, 37, 255), stop:1 rgba(19, 19, 19, 255));\n"
"color:rgb(255, 255, 255);\n"
"font-size:17px;\n"
"border:none;")
        icon4 = QIcon()
        icon4.addFile(u"../assets/search.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon4)
        self.pushButton_15.setIconSize(QSize(23, 23))
        self.lineEdit_2 = QLineEdit(self.main)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(300, 60, 431, 41))
        self.lineEdit_2.setStyleSheet(u"background: white;\n"
"color: black;\n"
"margin:2px;")

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
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"RETURN", None))
        self.label_7.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Connection List:", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; text-decoration: underline;\">Click List Item for Details:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600; font-style:italic; text-decoration: underline;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600; f"
                        "ont-style:italic; text-decoration: underline;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port Protocol Search", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"443", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Search Port Meaning", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"ewq", None))
    # retranslateUi
