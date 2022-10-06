import psutil
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class HomeScan(QtWidgets.QMainWindow):
    def __init__(self):
        super(HomeScan,self).__init__()
        uic.loadUi('HomeScanUi.ui',self)


        self.setFixedSize(720, 1000)
        self.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")
        self.setWindowFlags(Qt.FramelessWindowHint)
   

        self.pushButton.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_2.clicked.connect(self.btn4)
        self.pushButton_3.clicked.connect(self.btn3)
        self.oldPos = self.pos()
        self.show()

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def btn3(self): 
        self.textEdit.append(str(psutil.net_connections()))

    def btn4(self):
        self.textEdit_2.append(str(psutil.net_if_stats()))




    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    window = HomeScan()
    window.show()
    sys.exit(app.exec_())