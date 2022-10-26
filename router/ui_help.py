# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 1141)
        MainWindow.setStyleSheet(u"border: unset;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(46, 46, 46, 255));")
        self.app = QWidget(MainWindow)
        self.app.setObjectName(u"app")
        self.verticalLayout = QVBoxLayout(self.app)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.label = QLabel(self.app)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:24px;\n"
"color:white;\n"
"text-align:center;")

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(self.app)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"font-size:20px;")

        self.verticalLayout.addWidget(self.textEdit)

        self.pushButton = QPushButton(self.app)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 100))
        self.pushButton.setStyleSheet(u"BACKGROUND-COLOR: qlineargradient(spread:pad, x1:0, y1:0, x2:0.306, y2:0.909091, stop:0.00568182 rgba(227, 198, 43, 255), stop:1 rgba(191, 32, 32, 255));\n"
"font-size:24px;\n"
"color:white;")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.app)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Open Sans,Arial,sans-serif'; font-size:12pt; color:#000000; background-color:#ffffff;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc auctor vestibulum urna, at tempor lorem facilisis at. Praesent ut risus at turpis auctor finibus eget non dui. Ut mattis massa lectus, a pretium nisi vulputate at. Aenean vel ex nec quam mattis volutpat. Aliquam erat volutpat. In hac habitasse platea dictumst. Duis at molestie sapien.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Open Sans,Arial,sans-serif'; font-size:12pt; color:#000000; background-color:#ffffff;\">Curabitur pulvinar sit amet sapien quis pharetra. Etiam varius rutrum posuere. Nulla dolor nunc, posuere id vehicula sed, aliquet in dolor. Vestibulum sit amet purus congue, fermentum metus eget, tincidunt nibh. Vestibulum interdum viverra feugiat. Mauris ex enim, sagittis sit amet dapibus in, venenatis quis eros. Phasellus ut rhoncus augue. Phasellus eleifend dui metus, eu dictum urna tristique non. Praesent efficitur augue egestas aliquam aliquet. Aenean diam nunc, scelerisque vitae tincidunt ac, iaculis a ligula.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Open Sans,Arial,sans-serif'; font-size:12pt; color:#000000; background-color:#ffffff;\">Aenean scelerisq"
                        "ue mollis felis vitae volutpat. Praesent imperdiet fermentum risus in varius. Aliquam ullamcorper lacus nisl, et dignissim lectus dictum condimentum. Donec quis tincidunt ex. In a nisi leo. Vestibulum pellentesque mattis aliquet. Praesent consectetur nec nisi nec fermentum.</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GO BACK", None))
    # retranslateUi

