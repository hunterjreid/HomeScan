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


class HomeScan(QtWidgets.QMainWindow):
    def __init__(self):
        super(HomeScan,self).__init__()
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
        global time
        time = QtCore.QTime(0, 0, 0)
        self.timer0.setInterval(1000)
        self.timer0.timeout.connect(self.startTimer)
        self.timer0.start()
        
        # Set Wifi Name
        results = subprocess.check_output(["netsh", "wlan", "show", "network"])
        results = results.decode("ascii")
        results = results.replace("\r","")
        ls = results.split("\n")
        ls = ls[4:]
        self.label_WifiName.setText(ls[0][9:])

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

#init app !
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = HomeScan()
    window.show()
    sys.exit(app.exec_())