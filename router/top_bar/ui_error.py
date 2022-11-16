# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error.ui'
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
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(914, 508)
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
        self.verticalLayout_5 = QVBoxLayout(self.side_bar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
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
        self.back_2.setStyleSheet(u"font-size:18px;\n"
"background:none;\n"
"text-align:left;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../../assets/error_pic.png", QSize(), QIcon.Normal, QIcon.Off)
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

        self.checkBox_2 = QCheckBox(self.side_bar)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"background:none;font-size:10px;color:rgb(207, 207, 207);")

        self.verticalLayout.addWidget(self.checkBox_2)


        self.exports.addLayout(self.verticalLayout)

        self.export_2 = QPushButton(self.side_bar)
        self.export_2.setObjectName(u"export_2")
        self.export_2.setStyleSheet(u"background: rgb(85, 0, 0);\n"
"color:white;font-size:17px;\n"
"padding:5px;")
        icon3 = QIcon()
        icon3.addFile(u"../../assets/export_2.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.frame.setMinimumSize(QSize(0, 490))
        self.frame.setMaximumSize(QSize(16777215, 3242342))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:orange;\n"
"font-size:22px;")

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:grey;")

        self.verticalLayout_6.addWidget(self.label_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"color:white;")

        self.verticalLayout_4.addWidget(self.listWidget)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color:white;\n"
"font-size:18px;")

        self.verticalLayout_4.addWidget(self.label_8)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)


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
        self.back_2.setText(QCoreApplication.translate("MainWindow", u"Errors", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Export errors:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Include datetime", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Include any personal info", None))
        self.export_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Network Errors", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Eroor", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Error", None))
    # retranslateUi

