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


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi('mainwindow.ui',self)
        self.graphicsView.setBackground('black')
        # self.graphicsView.setTitle("Real-Time network graph", color="lightgray", size="16pt")
        self.graphicsView.setLabel('left', "<span style=\"color:darkgray;font-size:20px\">Value 1</span>")
        self.graphicsView.setLabel('bottom', "<span style=\"color:darkgray;font-size:20px\">Value 2</span>")

        self.graphicsView2.setBackground('black')
        # self.graphicsView.setTitle("Real-Time network graph", color="lightgray", size="16pt")
        self.graphicsView2.setLabel('left', "<span style=\"color:darkgray;font-size:20px\">Value 3</span>")
        self.graphicsView2.setLabel('bottom', "<span style=\"color:darkgray;font-size:20px\">Value 4</span>")

        pen = pg.mkPen(color=(91, 93, 225), width=1, style=QtCore.Qt.DashLine)
        self.graphicsView.setBackground('white')
        self.graphicsView.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45], pen=pen)


        pen = pg.mkPen(color=(91, 93, 225), width=1, style=QtCore.Qt.DashLine)


        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphicsView2.setBackground('w')
        self.x = list(range(50))  # 100 time points
        self.y = [randint(30,70) for _ in range(50)]  # 100 data points



        self.data_line = self.graphicsView2.plot(self.x, self.y, pen=pen)




app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())