# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Angry_scan.ui'
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
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1315, 778)
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
        self.side_bar.setMinimumSize(QSize(160, 0))
        self.side_bar.setMaximumSize(QSize(160, 16777215))
        self.side_bar.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0.00568182 rgba(227, 198, 43, 255), stop:1 rgba(191, 32, 32, 255));")
        self.side_bar.setFrameShape(QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.side_bar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header = QVBoxLayout()
        self.header.setObjectName(u"header")
        self.top = QHBoxLayout()
        self.top.setObjectName(u"top")
        self.back = QPushButton(self.side_bar)
        self.back.setObjectName(u"back")
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
        self.back_2.setStyleSheet(u"font-size:18px;\n"
"background:none;\n"
"text-align:left;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../../assets/bull.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_2.setIcon(icon2)
        self.back_2.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.back_2)


        self.header.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.header)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.exports = QVBoxLayout()
        self.exports.setObjectName(u"exports")
        self.label_2 = QLabel(self.side_bar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:17px;\n"
"background:none;\n"
"\n"
"color:black;")

        self.exports.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox = QCheckBox(self.side_bar)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"background:none;font-size:13px;color:rgb(207, 207, 207);")

        self.verticalLayout.addWidget(self.checkBox)


        self.exports.addLayout(self.verticalLayout)

        self.export_2 = QPushButton(self.side_bar)
        self.export_2.setObjectName(u"export_2")
        self.export_2.setStyleSheet(u"background: rgb(85, 0, 0);\n"
"color:white;font-size:17px;\n"
"padding:5px;")
        icon3 = QIcon()
        icon3.addFile(u"../assets/export_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_2.setIcon(icon3)

        self.exports.addWidget(self.export_2)


        self.verticalLayout_5.addLayout(self.exports)


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
        self.frame.setMinimumSize(QSize(0, 400))
        self.frame.setMaximumSize(QSize(16777215, 3242342))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:orange;\n"
"font-size:22px;")

        self.verticalLayout_7.addWidget(self.label_3)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:grey;")

        self.verticalLayout_7.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background:none;\n"
"color:lightgrey;\n"
"font-size:17px;")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")

        self.verticalLayout_4.addWidget(self.lineEdit_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background:none;\n"
"color:lightgrey;\n"
"font-size:17px;")

        self.verticalLayout_14.addWidget(self.label_11)

        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")

        self.verticalLayout_14.addWidget(self.lineEdit_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background:none;\n"
"color:lightgrey;\n"
"font-size:17px;")

        self.verticalLayout_15.addWidget(self.label_12)

        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")

        self.verticalLayout_15.addWidget(self.lineEdit_7)


        self.horizontalLayout_4.addLayout(self.verticalLayout_15)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background:none;\n"
"color:lightgrey;\n"
"font-size:17px;")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        icon4 = QIcon()
        icon4.addFile(u"../../assets/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(23, 30))

        self.horizontalLayout_3.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.lineEdit_8 = QLineEdit(self.frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")

        self.verticalLayout_6.addWidget(self.lineEdit_8)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background:none;\n"
"color:grey;\n"
"font-size:15px;")

        self.verticalLayout_7.addWidget(self.label_14)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(400, 0))
        self.textEdit.setMaximumSize(QSize(1900, 16777215))
        self.textEdit.setStyleSheet(u"color:white;")
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.textEdit)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.progressBar_2 = QProgressBar(self.frame)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")
        self.progressBar_2.setValue(0)
        self.progressBar_2.setAlignment(Qt.AlignCenter)
        self.progressBar_2.setTextVisible(False)

        self.horizontalLayout_6.addWidget(self.progressBar_2)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background:white;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(23, 23, 23, 255), stop:1 rgba(46, 46, 46, 255));\n"
"border: 1px solid grey;\n"
"color:white;\n"
"padding:10px;\n"
"border-radius:2px;")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.verticalLayout_17.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout_17.addLayout(self.horizontalLayout_7)


        self.verticalLayout_7.addLayout(self.verticalLayout_17)


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
        self.back_2.setText(QCoreApplication.translate("MainWindow", u"Angry Scan", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Export scan:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Include time", None))
        self.export_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Run Angry Scan", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Here you can run the angry scan test. (PORT SCANNER GOES HERE)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Set as your local IP", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10.10.0.4", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Start Port", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"80", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"End Port", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"450", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Timeout(ms)", None))
        self.pushButton.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"It is recommend only to do small scans of 200 max ports at a time. Anymore could risk crashing the application it most cases iit will just take longer so preceed with caution", None))
        self.textEdit.setDocumentTitle(QCoreApplication.translate("MainWindow", u"Test", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Test</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Start Scan", None))
    # retranslateUi

