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
from datetime import datetime
from PyQt5.QtGui import QPainter, QColor, QPen

global conn
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
        self.pushButton.clicked.connect(self.goToLivePanel)
        self.pushButton_2.clicked.connect(self.goToPorts)
        self.pushButton_3.clicked.connect(self.goToDevices)
        self.pushButton_12.clicked.connect(self.open)
        self.pushButton_16.clicked.connect(self.advanced_module)
        self.pushButton_13.clicked.connect(self.goToHelp)
        self.pushButton_7.clicked.connect(self.gotoTrafficHistory)
        self.pushButton_9.clicked.connect(self.goToSettings)
        self.pushButton_10.clicked.connect(self.goToScan)

        #graphs
        
        self.graphicsView.setBackground('black')
        self.graphicsView.setLabel('left', "<span style=\"color:darkgray;font-size:20px\">Value 1</span>")
        self.graphicsView.setLabel('bottom', "<span style=\"color:darkgray;font-size:20px\">Value 2</span>")

        pen = pg.mkPen(color=(227, 198, 43), width=1, style=QtCore.Qt.DashLine)
        self.graphicsView.setBackground('black')
        self.graphicsView.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45], pen=pen)

        self.graphicsView2.setBackground('black')

        self.graphicsView2.setLabel('left', "<span style=\"color:darkgray;font-size:20px\">Value 3</span>")
        self.graphicsView2.setLabel('bottom', "<span style=\"color:darkgray;font-size:20px\">Value 4</span>")


        pen = pg.mkPen(color=(191, 32, 32), width=1, style=QtCore.Qt.DashLine)


        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphicsView2.setBackground('black')
        self.x = list(range(50))  # 100 time points
        self.y = [randint(30,70) for _ in range(50)]  # 100 data points

        global conn
        conn=psutil.net_connections()
        stats=psutil.net_if_stats()


        self.label_13.setText("Welcome back, Total Net Connections: " + str(len(conn)) + " Network Interfaces: " + str(len(stats)))

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


            if str(person[5]) == "NONE":
                self.tableWidget.item(row, 0).setBackground(QColor(33,34,31))
            elif str(person[5]) == "CLOSE_WAIT":
                self.tableWidget.item(row, 0).setBackground(QColor(255,255,102))
            elif str(person[5]) == "ESTABLISHED":
                self.tableWidget.item(row, 0).setBackground(QColor(76,154,1))
            elif str(person[5]) == "LISTEN":
                self.tableWidget.item(row, 0).setBackground(QColor(0,254,251))
            elif str(person[5]) == "SYN_SENT":
                self.tableWidget.item(row, 0).setBackground(QColor(255,4,111))
            elif str(person[5]) == "FIN_WAIT2":
                self.tableWidget.item(row, 0).setBackground(QColor(150,145,251))
     
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


            if people[key][0] == False:
                self.tableWidget_2.item(row, 1).setBackground(QColor(100,4,1))
            else:
                self.tableWidget_2.item(row, 1).setBackground(QColor(1,100,1))

            row=row+1

        self.tableWidget_2.resizeRowsToContents()
        self.tableWidget_2.resizeColumnsToContents()  





    # router
    def gotoTrafficHistory(self):
        trafficHistory = TrafficHistory()
        widget.addWidget(trafficHistory)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToLivePanel(self):
        livePanel = LivePanel()
        widget.addWidget(livePanel)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def advanced_module(self):
        Advancedscreen = AdvancedScreen()
        widget.addWidget(Advancedscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    
    def goToSettings(self):
        settings = Settings()
        widget.addWidget(settings)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToPorts(self):
        ports = Ports()
        widget.addWidget(ports)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToDevices(self):
        devices = Devices()
        widget.addWidget(devices)
        widget.setCurrentIndex(widget.currentIndex()+1)

    
    def goToScan(self):
        scan = Scan()
        widget.addWidget(scan)
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

class LivePanel(QMainWindow):
    def __init__(self):
        super(LivePanel,self).__init__()
        uic.loadUi('router/live_panel.ui',self)

        self.x = list(range(100))  # 100 time points
        self.y = [randint(200,201) for _ in range(100)]  # 100 data points'

        styles = {"color": "#f00", "font-size": "20px"}
        self.graphicsView.setLabel("left", "Connections", **styles)
        self.graphicsView.setLabel("bottom", "Seconds", **styles)
       

        pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.DashLine)
        self.data_line = self.graphicsView.plot(self.x, self.y, pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
                
        #connect min full and exit tab (top right) to UI
        self.exit.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_14.clicked.connect(self.goBack)

    def update_plot_data(self):
        conn_nol=psutil.net_connections()
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append((len(conn_nol)))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.

        #UPDATE TEXT ASWELL
       



        self.label_6.setText("Total Net Connections Live: " + str(len(conn_nol)))







  
    

    def goBack(self):

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

        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # used for the full screen btn (top right)
    def toggleFull(self):
            if self.windowState() & QtCore.Qt.WindowFullScreen:
                self.showNormal()
            else:
                self.showFullScreen()

class TrafficHistory(QMainWindow):
    def __init__(self):
        super(TrafficHistory,self).__init__()
        uic.loadUi('router/traffic_history.ui',self)

        
        #connect min full and exit tab (top right) to UI

        self.pushButton.clicked.connect(self.goBack)
    

    def goBack(self):

        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # used for the full screen btn (top right)
    def toggleFull(self):
            if self.windowState() & QtCore.Qt.WindowFullScreen:
                self.showNormal()
            else:
                self.showFullScreen()

class Settings(QMainWindow):
    def __init__(self):
        super(Settings,self).__init__()
        uic.loadUi('router/settings.ui',self)

        
        #connect min full and exit tab (top right) to UI

        self.pushButton_14.clicked.connect(self.goBack)
    

    def goBack(self):

        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # used for the full screen btn (top right)
    def toggleFull(self):
            if self.windowState() & QtCore.Qt.WindowFullScreen:
                self.showNormal()
            else:
                self.showFullScreen()


class Scan(QMainWindow):
    def __init__(self):
        super(Scan,self).__init__()
        uic.loadUi('router/scan.ui',self)

        
        #connect min full and exit tab (top right) to UI

        self.pushButton_4.clicked.connect(self.goBack)
    

    def goBack(self):

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
        global conn
        self.textEdit.append(str(conn))
    

    def goBack(self):
   
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # used for the full screen btn (top right)
    def toggleFull(self):
            if self.windowState() & QtCore.Qt.WindowFullScreen:
                self.showNormal()
            else:
                self.showFullScreen()
class AdvancedScreen(QMainWindow):
    def __init__(self):
        super(AdvancedScreen,self).__init__()
        uic.loadUi('router/advanced_scan_module.ui',self)
        
        #connect min full and exit tab (top right) to UI
        self.min.clicked.connect(self.showMinimized)
        self.full.clicked.connect(self.toggleFull)
        self.exit.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_14.clicked.connect(self.goBack)
        global conn
        print(len(sys.argv))
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname)   
        #target = socket.gethostbyname(sys.argv[1])
        self.textEdit.append(str("Hostname : " + str(hostname)))
        self.textEdit.append(str("Scanning IP : " + str(IPAddr)))
        self.textEdit.append(str("Scan Init : " + str(datetime.now())))

        self.pushButton.clicked.connect(self.addTxt)

    
    def addTxt(self):
        global clicked

        target = self.lineEdit.text()
        s_port = int(self.lineEdit_2.text())
        e_port = int(self.lineEdit_3.text())
        ms = int(self.lineEdit_4.text())

        self.progressBar.setMinimum(s_port)
        self.progressBar.setMaximum(e_port)
        self.progressBar.setValue(s_port)

        self.textEdit.append(str("-" * 45))
        self.textEdit.append(str("Scanning Target: " + target))
        self.textEdit.append(str("Scanning Ports: " + self.lineEdit_2.text() + " - " + self.lineEdit_3.text()))
        self.textEdit.append(str("Scanning started at: " + str(datetime.now())))
        self.textEdit.append(str("-" * 45))
        try:
            for port in range(s_port, (e_port+1)):
                print(self.progressBar.setValue(self.progressBar.value() + 1))
                # self.horizontalSlider.setValue(self, 1)
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(ms/1000)
                #print(str(s.connect_ex((target, port))))
                res = s.connect_ex((target, port))
                #self.textEdit.append(str(s.connect_ex((target, port))))
            
                if res == 0:
                    print("Port " + str(port) + " is OPEN")
                    self.textEdit.append(str("Port " + str(port) + " is OPEN✅"))
                else:
                    print("Port " + str(port) + " is close")
                    self.textEdit.append(str("Port " + str(port) + " is closed❌"))
                # 
                # if result==0:
                #     self.textEdit.append(str("Port " + str(port) + " is open"))
                # else:
                #     self.textEdit.append(str("Port " + str(port) + " is Closed"))
                self.textEdit.repaint()
                s.close()
        except:
            print("Something else went wrong")



  
            

    def goBack(self):
   
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


        last_received = psutil.net_io_counters().bytes_recv
        last_sent = psutil.net_io_counters().bytes_sent
        last_total = last_received + last_sent
        mb_new_received = last_received / 1024 / 1024
        mb_new_sent = last_sent / 1024 / 1024
        mb_new_total = last_total / 1024 / 1024
        self.lineEdit.setText(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total.")

        
    

    def goBack(self):
   
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
