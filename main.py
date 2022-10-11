import psutil
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import pyqtgraph as pg
import numpy as np
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
from pyqtgraph import PlotWidget, plot

DURATION_INT = 60321321

class HomeScan(QtWidgets.QMainWindow):
    def __init__(self):
        super(HomeScan,self).__init__()
        uic.loadUi('HomeScanUi.ui',self)


        self.setFixedSize(720, 1000)
        self.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")
        self.setWindowFlags(Qt.FramelessWindowHint)
   
        self.pushButton_6.clicked.connect(self.showMinimized)
        self.pushButton_5.clicked.connect(QtWidgets.qApp.quit)
        self.oldPos = self.pos()
        self.show()
        self.loadtable()
        self.loadtable2()
        people=psutil.net_connections()
        stats=psutil.net_if_stats()
        self.label_2.setText("Total Net Connections: " + str(len(people)))
    
        
        self.startTimer()

        self.label_3.setText("Network Interfaces: " + str(len(stats)))
    

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)


        #self.plot([1,2,3,4,5,6  ,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])
        #self.plot2([1,2,3,4,5,6  ,7,8,9,10], [23,2,3,43,2,5,65,14,32,32])
        self.graphicsView.setBackground('black')
        # self.graphicsView.setTitle("Real-Time network graph", color="lightgray", size="16pt")
        self.graphicsView.setLabel('left', "<span style=\"color:darkgray;font-size:20px\">Usage (MBs)</span>")
        self.graphicsView.setLabel('bottom', "<span style=\"color:darkgray;font-size:20px\">Time (S)</span>")

        self.start_plot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(150)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()



    def start_plot(self):

        pen = pg.mkPen(color=(91, 93, 225), width=1, style=QtCore.Qt.DashLine)


    
        self.x = list(range(50))  # 100 time points
        self.y = [randint(30,70) for _ in range(50)]  # 100 data points



        self.data_line = self.graphicsView.plot(self.x, self.y, pen=pen)


        



    def update_plot_data(self):


        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append( randint(0,100))  # Add a new random value.
     
        self.data_line.setData(self.x, self.y)


        



        

    def plot2(self, hour, temperature):
        pen = pg.mkPen(color=(91, 93, 225), width=4, style=QtCore.Qt.DashLine)
        self.graphicsView.plot(hour, temperature, pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        

  


    def startTimer(self):
        self.time_left_int = DURATION_INT

        self.myTimer = QtCore.QTimer(self)
        self.myTimer.timeout.connect(self.timerTimeout)
        self.myTimer.start(1000)

    def timerTimeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:
            self.time_left_int = DURATION_INT

        self.update_gui()

    def update_gui(self):
        self.timerLabel.setText(str(self.time_left_int) + "s")


    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def loadtable(self):
        people=psutil.net_connections()

        row = 0
        self.tableWidget.setRowCount(len(people))
        


        for person in people:
            
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(person[5])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(people[row][3][0])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(people[row][3][1])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(person[6])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(person[2])))

            

            row=row+1
        
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()  

    def loadtable2(self):
        people=psutil.net_if_stats()
    

        row = 0
        self.tableWidget_2.setRowCount(len(people))

        for key in people:
            self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(key)))
            self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(people[key][0])))
            self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(people[key][2])))
            self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(people[key][3])))
            self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(people[key][1])))

    

            row=row+1

        self.tableWidget_2.resizeRowsToContents()
        self.tableWidget_2.resizeColumnsToContents()  


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = HomeScan()
    window.show()
    sys.exit(app.exec_())