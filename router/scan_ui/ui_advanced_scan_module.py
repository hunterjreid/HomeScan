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
        MainWindow.resize(1199, 392)
        MainWindow.setMaximumSize(QSize(6000, 6000))
        MainWindow.setStyleSheet(u"border: unset;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));")
        self.app = QWidget(MainWindow)
        self.app.setObjectName(u"app")
        self.app.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));")
        self.horizontalLayout_4 = QHBoxLayout(self.app)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.app)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background:none;\n"
"color:lightgrey;\n"
"font-size:17px;")

        self.verticalLayout.addWidget(self.label_3)

        self.pushButton_2 = QPushButton(self.app)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background:white;\n"
"padding:2px")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.lineEdit = QLineEdit(self.app)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")

        self.verticalLayout.addWidget(self.lineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.app)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background:none;\n"
"color:lightgrey;\n"
"font-size:17px;")

        self.verticalLayout_2.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.app)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.app)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background:none;\n"
"color:lightgrey;\n"
"font-size:17px;")

        self.verticalLayout_3.addWidget(self.label_6)

        self.lineEdit_3 = QLineEdit(self.app)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")

        self.verticalLayout_3.addWidget(self.lineEdit_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.app)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background:none;\n"
"color:lightgrey;\n"
"font-size:17px;")

        self.verticalLayout_4.addWidget(self.label_8)

        self.lineEdit_4 = QLineEdit(self.app)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")

        self.verticalLayout_4.addWidget(self.lineEdit_4)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.app)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background:none;\n"
"color:grey;\n"
"font-size:15px;")

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.textEdit = QTextEdit(self.app)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(400, 0))
        self.textEdit.setMaximumSize(QSize(1900, 16777215))
        self.textEdit.setStyleSheet(u"background: white;\n"
"color: black;\n"
"padding: 20px;")
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.textEdit)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progressBar = QProgressBar(self.app)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.pushButton = QPushButton(self.app)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background:white;\n"
"padding:20px")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_14 = QPushButton(self.app)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(37, 37, 37, 255), stop:1 rgba(19, 19, 19, 255));\n"
"color:rgb(255, 255, 255);\n"
"font-size:17px;\n"
"border:none;")
        icon = QIcon()
        icon.addFile(u"../assets/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.app)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(37, 37, 37, 255), stop:1 rgba(19, 19, 19, 255));\n"
"color:rgb(255, 255, 255);\n"
"font-size:17px;\n"
"border:none;")
        icon1 = QIcon()
        icon1.addFile(u"../assets/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon1)
        self.pushButton_15.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_15)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        MainWindow.setCentralWidget(self.app)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Set as your IP", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10.10.0.4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Start Port", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"80", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"End Port", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"450", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Timeout(ms)", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"It is recommend only to do small scans of 200 max ports at a time. Anymore could risk crashing the application it most cases iit will just take longer so preceed with caution", None))
        self.textEdit.setDocumentTitle(QCoreApplication.translate("MainWindow", u"Test", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Test</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; text-decoration: underline;\">Advanced Scan Module: </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600; font-style:italic; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-blo"
                        "ck-indent:0; text-indent:0px; font-size:10pt; font-weight:600; font-style:italic; text-decoration: underline;\"><br /></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SCAN NOW", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"GO BACK TO MAIN", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

