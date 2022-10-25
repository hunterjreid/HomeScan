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
import webbrowser



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
        self.pushButton_12.clicked.connect(self.open)
        self.pushButton_13.clicked.connect(self.goToHelp)
        
        self.graphicsView.setBackground('black')
        # self.graphicsView.setTitle("Real-Time network graph", color="lightgray", size="16pt")
        self.graphicsView.setLabel('left', "<span style=\"color:darkgray;font-size:20px\">Value 1</span>")
        self.graphicsView.setLabel('bottom', "<span style=\"color:darkgray;font-size:20px\">Value 2</span>")

        self.graphicsView2.setBackground('black')
        # self.graphicsView.setTitle("Real-Time network graph", color="lightgray", size="16pt")
        self.graphicsView2.setLabel('left', "<span style=\"color:darkgray;font-size:20px\">Value 3</span>")
        self.graphicsView2.setLabel('bottom', "<span style=\"color:darkgray;font-size:20px\">Value 4</span>")

        pen = pg.mkPen(color=(227, 198, 43), width=1, style=QtCore.Qt.DashLine)
        self.graphicsView.setBackground('black')
        self.graphicsView.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45], pen=pen)


        pen = pg.mkPen(color=(191, 32, 32), width=1, style=QtCore.Qt.DashLine)


        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphicsView2.setBackground('black')
        self.x = list(range(50))  # 100 time points
        self.y = [randint(30,70) for _ in range(50)]  # 100 data points



        self.data_line = self.graphicsView2.plot(self.x, self.y, pen=pen)
        self.loadtable()
        self.loadtable2()

     

    def open(self):
        webbrowser.open('https://github.com/hunterjreid/HomeScan')  

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

            

     

            # self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person[row][1])))
            # self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person[row][5])))
            # self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(person[row][3])))
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

    def goToHelp(self):
        help = Help()
        widget.addWidget(help)
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
        uic.loadUi('router/live_panel.ui',self)
        
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

class Help(QMainWindow):
    def __init__(self):
        super(Help,self).__init__()
        uic.loadUi('router/help.ui',self)
        
        #connect min full and exit tab (top right) to UI

        self.pushButton.clicked.connect(self.goBack)
    

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
        uic.loadUi('router/ports.ui',self)
        
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
        uic.loadUi('router/devices.ui',self)
        
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