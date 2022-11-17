# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NetworkScan.ui'
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
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(961, 505)
        MainWindow.setMaximumSize(QSize(31321, 31232))
        MainWindow.setStyleSheet(u"border: unset;")
        self.app = QWidget(MainWindow)
        self.app.setObjectName(u"app")
        self.horizontalLayout = QHBoxLayout(self.app)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_bar = QFrame(self.app)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setMaximumSize(QSize(160, 16777215))
        self.side_bar.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0.00568182 rgba(227, 198, 43, 255), stop:1 rgba(191, 32, 32, 255));")
        self.side_bar.setFrameShape(QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.side_bar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.header = QVBoxLayout()
        self.header.setObjectName(u"header")
        self.top = QHBoxLayout()
        self.top.setObjectName(u"top")
        self.back = QPushButton(self.side_bar)
        self.back.setObjectName(u"back")
        self.back.setMinimumSize(QSize(0, 65))
        self.back.setStyleSheet(u"font-size:20px;\n"
"background:none;")
        icon = QIcon()
        icon.addFile(u"../../assets/back2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back.setIcon(icon)
        self.back.setIconSize(QSize(18, 32))

        self.top.addWidget(self.back, 0, Qt.AlignTop)

        self.help = QPushButton(self.side_bar)
        self.help.setObjectName(u"help")
        self.help.setStyleSheet(u"background:none;\n"
"padding:0px;\n"
"margin:0px;")
        icon1 = QIcon()
        icon1.addFile(u"../../assets/help3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help.setIcon(icon1)
        self.help.setIconSize(QSize(16, 16))

        self.top.addWidget(self.help, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.header.addLayout(self.top)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.side_bar)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:14px;\n"
"background:none;\n"
"color:white;")

        self.verticalLayout_3.addWidget(self.label)

        self.back_2 = QPushButton(self.side_bar)
        self.back_2.setObjectName(u"back_2")
        self.back_2.setStyleSheet(u"font-size:17px;\n"
"background:none;\n"
"text-align:left;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../../assets/quick_scan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_2.setIcon(icon2)
        self.back_2.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.back_2)


        self.header.addLayout(self.verticalLayout_3)


        self.verticalLayout_9.addLayout(self.header)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.side_bar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:17px;\n"
"background:none;\n"
"\n"
"color:black;")

        self.verticalLayout_5.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_3 = QCheckBox(self.side_bar)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setStyleSheet(u"background:none;font-size:13px;color:rgb(207, 207, 207);")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.side_bar)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"background:none;font-size:13px;color:rgb(207, 207, 207);")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.side_bar)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"background:none;font-size:13px;color:rgb(207, 207, 207);")

        self.verticalLayout.addWidget(self.checkBox)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.export_2 = QPushButton(self.side_bar)
        self.export_2.setObjectName(u"export_2")
        self.export_2.setStyleSheet(u"background: rgb(85, 0, 0);\n"
"color:white;font-size:17px;\n"
"padding:5px;")
        icon3 = QIcon()
        icon3.addFile(u"../assets/export_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_2.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.export_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)


        self.horizontalLayout.addWidget(self.side_bar)

        self.body = QFrame(self.app)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"background-color:rgb(12, 12, 12);")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.body)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 3242342))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:orange;\n"
"font-size:22px;")

        self.verticalLayout_8.addWidget(self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")
        icon4 = QIcon()
        icon4.addFile(u"../../assets/search.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: rgb(203, 0, 0);\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")
        icon5 = QIcon()
        icon5.addFile(u"../../assets/bull.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QSize(23, 23))

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color:grey;")

        self.verticalLayout_8.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color:white;\n"
"font-size:15px;\n"
"background:none;\n"
"border:none;")

        self.verticalLayout_6.addWidget(self.label_5)

        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_6.addWidget(self.listWidget)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(200, 0))
        self.label_6.setMaximumSize(QSize(200, 16777215))
        self.label_6.setStyleSheet(u"color:white;\n"
"font-size:15px;\n"
"background:none;\n"
"border:none;")

        self.verticalLayout_7.addWidget(self.label_6)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(200, 0))
        self.textEdit.setMaximumSize(QSize(200, 16777215))
        self.textEdit.setStyleSheet(u"color:white;\n"
"font-size:9px;\n"
"")

        self.verticalLayout_7.addWidget(self.textEdit)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 0))
        self.pushButton.setMaximumSize(QSize(200, 16777215))
        self.pushButton.setStyleSheet(u"background-color: black;\n"
"color:white;font-size:17px;\n"
"padding:5px;\n"
"border: 1px solid grey;")
        icon6 = QIcon()
        icon6.addFile(u"../../assets/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(33, 33))

        self.verticalLayout_8.addWidget(self.pushButton, 0, Qt.AlignRight)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:grey;")

        self.verticalLayout_8.addWidget(self.label_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:grey;\n"
"font-size:25px;\n"
"background:none;\n"
"border:none;")

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color:white;\n"
"font-size:15px;\n"
"background:none;\n"
"border:none;")

        self.verticalLayout_4.addWidget(self.label_9)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;\n"
"\n"
"\n"
"font-size:20px\n"
"")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton_15 = QPushButton(self.frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")
        self.pushButton_15.setIcon(icon4)
        self.pushButton_15.setIconSize(QSize(23, 23))

        self.horizontalLayout_2.addWidget(self.pushButton_15)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color:white;\n"
"font-size:15px;\n"
"background:none;\n"
"border:none;")

        self.verticalLayout_8.addWidget(self.label_8)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.app)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.back.setText(QCoreApplication.translate("MainWindow", u" Go back", None))
        self.help.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"You are in: ", None))
        self.back_2.setText(QCoreApplication.translate("MainWindow", u"Network Scan", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Export scan:", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Include time", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Include Port Search", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Include History", None))
        self.export_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Run Network Scan", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Search about  IP", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Find IP Origin", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Block Port", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Scan Init : 2022-11-15 11:41:07.954143", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Action History", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Run Scan", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Search port meaning :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Port Protocol Search", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"After clicking on this search button scroll down to service name", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"443", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Search Port Meaning", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ports can be used for other features too. Stay alert. Click here to learn more.", None))
    # retranslateUi

