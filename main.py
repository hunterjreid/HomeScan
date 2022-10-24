import psutil
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import pyqtgraph as pg
import numpy as np
from pyqtgraph import PlotWidget, plot
import sys  # We need sys so that we can pass argv to QApplication
from random import randint
from pyqtgraph import PlotWidget, plot
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import socket
import os
import subprocess

global time
time = QtCore.QTime(0, 0, 0)

#main Window
class HomeScanMain(QMainWindow):
    def __init__(self):
        super(HomeScanMain,self).__init__()
        uic.loadUi('mainwindow.ui',self)
        self.setFixedSize(920, 1000)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        #connect min full and exit tab (top right) to UI
        self.min.clicked.connect(self.showMinimized)
        self.full.clicked.connect(self.toggleFull)
        self.exit.clicked.connect(QtWidgets.qApp.quit)

        #uptimer
        self.curr_time = QtCore.QTime(00,00,00)
        self.timer0 = QtCore.QTimer()

        self.timer0.setInterval(1000)
        self.timer0.timeout.connect(self.startTimer)
        self.timer0.start()

        self.pushButton.clicked.connect(self.goToLivePanel)
        self.pushButton_2.clicked.connect(self.goToPorts)
        self.pushButton_3.clicked.connect(self.goToDevices)
        
    # router
    def goToLivePanel(self):
        livePanel = LivePanel()
        widget.addWidget(livePanel)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToPorts(self):
        ports = Ports()
        widget.addWidget(ports)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToDevices(self):
        devices = Devices()
        widget.addWidget(devices)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # used for the full screen btn (top right)
    def toggleFull(self):
            if self.windowState() & QtCore.Qt.WindowFullScreen:
                self.showNormal()
            else:
                self.showFullScreen()

    #Start timer and update UI
    def startTimer(self):
        global time
        time = time.addSecs(1)
        self.label_TimerText.setText("Uptime: " + str(time.toString("hh:mm:ss")))

class LivePanel(QMainWindow):
    def __init__(self):
        super(LivePanel,self).__init__()
        uic.loadUi('live_panel.ui',self)
        
        #connect min full and exit tab (top right) to UI
        self.min.clicked.connect(self.showMinimized)
        self.full.clicked.connect(self.toggleFull)
        self.exit.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_14.clicked.connect(self.goBack)
    

    def goBack(self):
        print("clicked")
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # used for the full screen btn (top right)
    def toggleFull(self):
            if self.windowState() & QtCore.Qt.WindowFullScreen:
                self.showNormal()
            else:
                self.showFullScreen()

class Ports(QMainWindow):
    def __init__(self):
        super(Ports,self).__init__()
        uic.loadUi('ports.ui',self)
        
        #connect min full and exit tab (top right) to UI
        self.min.clicked.connect(self.showMinimized)
        self.full.clicked.connect(self.toggleFull)
        self.exit.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_14.clicked.connect(self.goBack)
    

    def goBack(self):
        print("clicked")
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # used for the full screen btn (top right)
    def toggleFull(self):
            if self.windowState() & QtCore.Qt.WindowFullScreen:
                self.showNormal()
            else:
                self.showFullScreen()

class Devices(QMainWindow):
    def __init__(self):
        super(Devices,self).__init__()
        uic.loadUi('devices.ui',self)
        
        #connect min full and exit tab (top right) to UI
        self.min.clicked.connect(self.showMinimized)
        self.full.clicked.connect(self.toggleFull)
        self.exit.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_14.clicked.connect(self.goBack)
    

    def goBack(self):
        print("clicked")
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # used for the full screen btn (top right)
    def toggleFull(self):
            if self.windowState() & QtCore.Qt.WindowFullScreen:
                self.showNormal()
            else:
                self.showFullScreen()


#init app !
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    window = HomeScanMain()
    widget.setFixedSize(920, 1000)
    widget.setWindowFlags(Qt.FramelessWindowHint)
    widget.addWidget(window)
    widget.show()
    sys.exit(app.exec_())