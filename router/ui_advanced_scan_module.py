# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advanced_scan_module.ui'
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
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 1141)
        MainWindow.setStyleSheet(u"border: unset;")
        self.app = QWidget(MainWindow)
        self.app.setObjectName(u"app")
        self.main = QFrame(self.app)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(0, 0, 771, 71))
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

        self.color_bar = QFrame(self.main)
        self.color_bar.setObjectName(u"color_bar")
        self.color_bar.setMinimumSize(QSize(0, 20))
        self.color_bar.setMaximumSize(QSize(16777215, 20))
        self.color_bar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0.00568182 rgba(227, 198, 43, 255), stop:1 rgba(191, 32, 32, 255))")
        self.color_bar.setFrameShape(QFrame.StyledPanel)
        self.color_bar.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.color_bar)

        self.footer = QFrame(self.main)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background:none;\n"
"border:none;")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.footer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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

        self.verticalLayout_6.addWidget(self.frame_9, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)

        self.label_3 = QLabel(self.app)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 97, 121, 31))
        self.label_3.setStyleSheet(u"")
        self.lineEdit = QLineEdit(self.app)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 130, 121, 41))
        self.lineEdit.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.lineEdit_2 = QLineEdit(self.app)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(180, 130, 121, 41))
        self.lineEdit_2.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.lineEdit_3 = QLineEdit(self.app)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(350, 130, 121, 41))
        self.lineEdit_3.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.lineEdit_4 = QLineEdit(self.app)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(530, 130, 121, 41))
        self.lineEdit_4.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.label_4 = QLabel(self.app)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 90, 121, 31))
        self.label_4.setStyleSheet(u"")
        self.label_6 = QLabel(self.app)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 90, 121, 31))
        self.label_6.setStyleSheet(u"")
        self.label_8 = QLabel(self.app)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(520, 80, 121, 31))
        self.label_8.setStyleSheet(u"")
        self.pushButton = QPushButton(self.app)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 200, 75, 23))
        self.pushButton.setStyleSheet(u"background:white;")
        self.textEdit = QTextEdit(self.app)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 245, 700, 561))
        self.textEdit.setMinimumSize(QSize(400, 0))
        self.textEdit.setMaximumSize(QSize(700, 16777215))
        self.textEdit.setStyleSheet(u"background: white;\n"
"color: black;\n"
"padding: 20px;")
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.pushButton_14 = QPushButton(self.app)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(20, 890, 718, 21))
        self.pushButton_14.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(37, 37, 37, 255), stop:1 rgba(19, 19, 19, 255));\n"
"color:rgb(255, 255, 255);\n"
"font-size:17px;\n"
"border:none;")
        icon3 = QIcon()
        icon3.addFile(u"../assets/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon3)
        self.progressBar = QProgressBar(self.app)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 200, 441, 23))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"192.168.0.1", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"80", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"450", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Start Port", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"End Port", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Timeout(ms)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SCAN NOW", None))
        self.textEdit.setDocumentTitle(QCoreApplication.translate("MainWindow", u"Test", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Test</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; text-decoration: underline;\">Advanced Scan Module: </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600; font-style:italic; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-blo"
                        "ck-indent:0; text-indent:0px; font-size:10pt; font-weight:600; font-style:italic; text-decoration: underline;\"><br /></p></body></html>", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"GO BACK TO MAIN", None))
    # retranslateUi

