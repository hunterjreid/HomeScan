import ipaddress
import os
import os.path
import socket
import sys  # We need sys so that we can pass argv to QApplication
import time
import webbrowser
from datetime import datetime
from random import randint

import numpy as np
import psutil
import pyqtgraph as pg
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QColor, QFont, QFontDatabase, QPainter, QPen
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from pyqtgraph import PlotWidget, plot


#main Window
class HomeScanMain(QMainWindow):
    def __init__(self):
        super(HomeScanMain,self).__init__()
        uic.loadUi('mainwindow.ui',self)
        global hostname, IPAddr 

      
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname) 
        self.label_TimerText.setText(str(IPAddr))


        #connect min full and exit tab (top right) to UI
        self.minn.clicked.connect(self.mintab)
        self.full.clicked.connect(self.toggleFull)
        self.exit.clicked.connect(self.quit)
        self.pushButton.clicked.connect(self.goToLivePanel)
        self.pushButton_2.clicked.connect(self.goToPorts)
        self.pushButton_3.clicked.connect(self.goToDevices)

        self.pushButton_16.clicked.connect(self.advanced_module)
        self.pushButton_13.clicked.connect(self.goToHelp)

        self.pushButton_9.clicked.connect(self.goToSettings)
        self.pushButton_10.clicked.connect(self.goToScan)
        self.pushButton_8.clicked.connect(self.goToOverview)
        self.pushButton_5.clicked.connect(self.goToAlerts)
        self.pushButton_4.clicked.connect(self.goToAScan)
        self.pushButton_11.clicked.connect(self.goToQscan)
   
       #graphs
        global conn
        conn=psutil.net_connections()



        
        pen = pg.mkPen(color=(227, 198, 43), width=4, style=QtCore.Qt.DashLine)
        pen2 = pg.mkPen(color=(191, 32, 32), width=5, style=QtCore.Qt.DashLine)




        self.graphicsView2.setBackground(QColor(12, 12, 12))
        self.graphicsView.setBackground(QColor(12, 12, 12))
        # self.graphicsView2.setLabel('left', "<span style=\"color:orange;font-size:10px\">Port #</span>")
        # self.graphicsView2.setLabel('bottom', "<span style=\"color:darkgray;font-size:10px\">PID</span>")



        row = 0
        self.x = []
        self.y = []
        stats=psutil.net_if_stats()

        
        for key in stats:
            self.x.append(stats[key][3])  
            self.y.append(stats[key][2])
            row=row+1





     
        
        



        self.loadtable()
        self.loadtable2()

        self.x3 = list(range(100))  # 100 time points
        self.y3 = [randint(0,0) for _ in range(100)]  # 100 data points'

 
        self.y5 = [randint(0,0) for _ in range(100)]  # 100 data points'

        # styles = {"color": "#f00", "font-size": "20px"}
        # self.graphicsView.setLabel("left", "Connections", **styles)
        # self.graphicsView.setLabel("bottom", "Seconds", **styles)
        

 
        self.data_line = self.graphicsView.plot(self.x3, self.y3, pen=pen)
        self.data_line_2 = self.graphicsView2.plot(self.x3, self.y5, pen=pen2)

        

        self.timer4 = QtCore.QTimer()
        self.timer4.setInterval(50)
        self.timer4.timeout.connect(self.update_plot_data)
        self.timer4.start()
                

    def update_plot_data(self):
        conn_nol=psutil.net_connections()
        self.x3 = self.x3[1:]  # Remove the first y element.
        self.x3.append(self.x3[-1] + 1)  # Add a new value 1 higher than the last.

        self.y3 = self.y3[1:]  # Remove the first
        self.y3.append((len(conn_nol)))  # Add a new random value.
        self.graphicsView.setRange(yRange=[int(len(conn_nol)-5),int(len(conn_nol)+5)])


        print(round(psutil.net_io_counters().bytes_sent / 1024.0 / 1024, 2))
        theval = round(psutil.net_io_counters().bytes_sent / 1024.0 / 1024, 2)

        self.y5 = self.y5[1:]  # Remove the first
        self.graphicsView2.setRange(yRange=[(theval-0.1),(theval+0.1)])
        self.y5.append(theval)  # Add a new random value.

        self.data_line.setData(self.x3, self.y3)  # Update the data.
        self.data_line_2.setData(self.x3, self.y5)
        #UPDATE TEXT ASWELL




        self.label_7.setText("Net Conns Live: " + str(len(conn_nol)))
        self.label_9.setText("Total transfer: " + str(theval))






  
    def closeEvent(self, event):
        if not self.isStarted:
            self.animation.start()
            self.isStarted = True
            event.ignore()
        else:   
            QWidget.closeEvent(self, event)


    # - btn
    def toggleFull(self):
            if widget.windowState() & QtCore.Qt.WindowFullScreen:
                for i in range(10):
                    i = i / 10
                    widget.setWindowOpacity(1 - i)
                    time.sleep(0.024)
                
                widget.showNormal()

                for i in range(10):
                    i = i * 10
                    widget.setWindowOpacity(1 + i)
                    time.sleep(0.014)

                widget.setWindowOpacity(1)
            else:

                for i in range(10):
                    i = i / 10
                    widget.setWindowOpacity(1 - i)
                    time.sleep(0.024)
                
                widget.showFullScreen()

                for i in range(10):
                    i = i * 10
                    widget.setWindowOpacity(1 + i)
                    time.sleep(0.014)

                widget.setWindowOpacity(1)
    # [] btn
    def mintab(self):
        # for i in range(10):
        #     i = i / 10
        #     widget.setWindowOpacity(1 - i)
        #     time.sleep(0.004)
        widget.showMinimized()
    # x btn
    def quit(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure you want to exit HomeScan?")
        msgBox.setWindowTitle("HomeScan")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setWindowIcon(QIcon("assets/icon.ico"))

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            for i in range(20):
                i = i / 20
                widget.setWindowOpacity(1 - i)
                time.sleep(0.1)

            QtWidgets.qApp.quit()





    def nofity_test(self):
        
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Ello :3")
        msgBox.setWindowTitle("HomeScan")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setWindowIcon(QIcon("assets/icon.ico"))

        # ph = self.parent().geometry().height()
        # dw = msgBox.width()
        # dh = msgBox.height()
        
        # px = int(self.parent().geometry().x())
        # py = int(self.parent().geometry().y())

        # msgBox.setGeometry((self.parent().geometry().height()/2), py+ph-dh, dw, dh )
        # print(px, py+ph-dh, dw, dh)
 
   
        msgBox.exec()
       


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



            if people[key][0] == False:
                self.tableWidget_2.item(row, 1).setBackground(QColor(100,4,1))
            else:
                self.tableWidget_2.item(row, 1).setBackground(QColor(1,100,1))


                

            row=row+1

        row = 0



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


    def goToQscan(self):
        qscan = Qscan()
        widget.addWidget(qscan)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToPorts(self):
        ports = Ports()
        widget.addWidget(ports)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToAlerts(self):
        alerts = Alerts()
        widget.addWidget(alerts)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToDevices(self):
        devices = Devices()
        widget.addWidget(devices)
        widget.setCurrentIndex(widget.currentIndex()+1)

    
    def goToScan(self):
        scan = Scan()
        widget.addWidget(scan)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToAScan(self):
        ascan = AScan()
        widget.addWidget(ascan)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToHelp(self):
        help = Help()
        widget.addWidget(help)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToOverview(self):
        overview = Overview()
        widget.addWidget(overview)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Verify the Network; 
# Configure and Turn off Sharing.
#  Remember that hackers are very clever, so its better to surf and play smart. ... 
# Use a VPN. A VPN (Virtual Private Network) is the most secure option to surf on public networks. ... 
# Use HTTPS. ... 
# Keep the Firewall Enabled. ...
#  Use Antivirus.

class LivePanel(QMainWindow):
    def __init__(self):
        super(LivePanel,self).__init__()
        uic.loadUi('router/live_panel.ui',self)
        global _last_net_io_meta
        _last_net_io_meta = 0
        self.x = list(range(300))  # 100 time points
        self.y = [randint(0,0) for _ in range(300)]  # 100 data points'

        # styles = {"color": "#f00", "font-size": "20px"}
        # self.graphicsView.setLabel("left", "Connections", **styles)
        # self.graphicsView.setLabel("bottom", "Seconds", **styles)
        self.y3z =  [randint(0,0) for _ in range(300)]

        pen = pg.mkPen(color=(255,4,111), width=4, style=QtCore.Qt.DashLine)
        self.data_line = self.graphicsView.plot(self.x, self.y, pen=pen, symbol='+', symbolSize=30, symbolBrush=('orange'))
        self.data_line3 = self.graphicsView.plot(self.x, self.y3z, pen=pen, symbol='x', symbolSize=10, symbolBrush=('blue'))

        

        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
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


        self.y3z = self.y3z[1:] 
        self.y3z.append(psutil.net_io_counters().bytes_sent)
        self.graphicsView.setRange(yRange=[int(len(conn_nol)-20),int(len(conn_nol)+20)])

        self.data_line.setData(self.x, self.y)  # Update the data.
        self.data_line3.setData(self.x, self.y3z)
        #UPDATE TEXT ASWELL
       
        #print(self.net_io_usage)


        self.label_6.setText("Total Net Connections Live: " + str(len(conn_nol)))






    def net_io_usage():
        global _last_net_io_meta

        net_counters = psutil.net_io_counters()
        tst = time.time()

        send_bytes =  psutil.net_io_counters().bytes_sent
        recv_bytes = net_counters.bytes_recv
        if _last_net_io_meta is None:
            _last_net_io_meta = (send_bytes, recv_bytes, tst)
            return None

        last_send_bytes, last_recv_bytes, last_time = _last_net_io_meta
        delta_time = tst - last_time
        recv_speed = (recv_bytes - last_recv_bytes) / delta_time
        send_speed = (send_bytes - last_send_bytes) / delta_time

        _last_net_io_meta = (send_bytes, recv_bytes, tst)

        print(recv_speed, send_speed)
        return recv_speed, send_speed 


    
  
    

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

# Network Overview
class Overview(QMainWindow):
    def __init__(self):
        super(Overview,self).__init__()
        uic.loadUi('router/overview.ui',self)

        
        #connect min full and exit tab (top right) to UI
        

        self.pushButton.clicked.connect(self.goBack)

        global conn
        conn=psutil.net_connections()
        self.graphicsView_2.setBackground(QColor(12,12,12,0))
        #self.graphicsView_2.setLabel('left', "<span style=\"color:darkgray;font-size:20px\">Speed</span>")
        #self.graphicsView_2.setLabel('left', "<span style=\"color:orange;font-size:20px\">Port</span>")

        pen = pg.mkPen(color=(191, 32, 32), width=0.5, style=QtCore.Qt.DashLine)


        row = 0
        port_x = []
        PID_y = []
        people=psutil.net_connections()
        for person in people:
            port_x.append(person[6])  
            PID_y.append(people[row][3][1])
            row=row+1


                


        
        
        

        #self.graphicsView.plot(port_x, PID_y, pen=pen, symbol='x', symbolSize=4, symbolBrush=('red'))
        self.graphicsView_2.plot(port_x, PID_y, pen=pen, symbol='+', symbolSize=15, symbolBrush=('red'))
        #self.graphicsView_3.plot(port_x, port_x, pen=pen, symbol='+', symbolSize=7, symbolBrush=('blue'))
    

    def goBack(self):
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)


         



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

        

        self.back.clicked.connect(self.goBack)
        self.help.clicked.connect(self.goHelp)

        
    def goHelp(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Help Iinformation about this screen goes here")
        msgBox.setWindowTitle("HomeScan")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("assets/icon.ico"))

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')


  
    

    def goBack(self):
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Alerts(QMainWindow):
    def __init__(self):
        super(Alerts,self).__init__()
        uic.loadUi('router/alert.ui',self)

        

        self.back.clicked.connect(self.goBack)
        self.help.clicked.connect(self.goHelp)

        
    def goHelp(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Help Iinformation about this screen goes here you will get alerts about this that happen live.")
        msgBox.setWindowTitle("HomeScan")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("assets/icon.ico"))

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')


  
    

    def goBack(self):
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Help(QMainWindow):
    def __init__(self):
        super(Help,self).__init__()
        uic.loadUi('router/help_ui.ui',self)

        

        self.back.clicked.connect(self.goBack)
        self.export_2.clicked.connect(self.goHelp)

        
    def goHelp(self):
        webbrowser.open('https://github.com/hunterjreid/HomeScan')  


  
    

    def goBack(self):
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)


#SCAN ---------------------------------------

class Scan(QMainWindow):
    def __init__(self):
        super(Scan,self).__init__()
        uic.loadUi('router/scan_ui/NetworkScan.ui',self)

        

        self.back.clicked.connect(self.goBack)
        self.help.clicked.connect(self.goHelp)
        self.pushButton.clicked.connect(self.runScan)
        self.pushButton_15.clicked.connect(self.scanIP)
        
        global conn
        self.selected_port = 10
        self.listWidget.itemClicked.connect(self.Clicked)

    
    def scanIP(self):
        try: 
            ipaddress.ip_address(self.lineEdit.text())

            self.label_9.setText('IP Valid')
        except: 
           
            self.label_9.setText('IP is not valid, NOT IPv4 or IPv6 address')
        


    def Clicked(self,item):
        index = self.listWidget.currentRow()
        self.lineEdit.setText(str(conn[index][3][1]))
        # self.selected_port = conn[item.in][3][1]
        self.textEdit.append(str( "You clicked: "+item.text() + " Port :" + str(conn[index][3][1])))

    def runScan(self):
        row = 0
        for person in conn:
            self.listWidget.addItem(str(conn[row][3][0]) + ":" + str(conn[row][3][1]) + " | " + str(person[5]))
            if str(person[5]) == "NONE":
                self.listWidget.item(row).setBackground(QColor(113,54,51,0))
            elif str(person[5]) == "CLOSE_WAIT":
                self.listWidget.item(row).setBackground(QColor(255,255,102,122))
            elif str(person[5]) == "ESTABLISHED":
                self.listWidget.item(row).setBackground(QColor(76,154,1,122))
            elif str(person[5]) == "LISTEN":
                self.listWidget.item(row).setBackground(QColor(0,254,251,122))
            elif str(person[5]) == "SYN_SENT":
                self.listWidget.item(row).setBackground(QColor(255,4,111,122))
            elif str(person[5]) == "FIN_WAIT2":
                self.listWidget.item(row).setBackground(QColor(150,145,251,122))
    
            row=row+1
        
    def goHelp(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Help Iinformation about this screen goes here")
        msgBox.setWindowTitle("HomeScan")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("assets/icon.ico"))

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')


  
    

    def goBack(self):
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)


#SCAN
class Qscan(QMainWindow):
    def __init__(self):
        super(Qscan,self).__init__()
        uic.loadUi('router/scan_ui/Quick.ui',self)
    
    #connect min full and exit tab (top right) to UI
        global conn, IPAddr, hostname
        
        self.QuickScan_Btn.clicked.connect(self.quickscan)

        self.back.clicked.connect(self.goBack)
        self.help.clicked.connect(self.goHelp)
        
    
    def quickscan(self):
       
        #Gets the host IP address
        ip = socket.gethostbyname(socket.gethostname())
        self.label_6.setText(ip)
        
        #Shows if there is an internet connection
        if ip == "127.0.0.1":
        
            self.label_5.setText("No Current Internet Connection")
        else:
            self.label_5.setText("Connected to the internet")\
        
        for port in range(65535):
            try:
                serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                serv.bind((ip,port))
            except:
                self.textEdit.append(str("        ✅      ")+ str("          Open Port Nunber:           ") + str( port))

        print("ok")
    def goHelp(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Help Iinformation about this screen goes here")
        msgBox.setWindowTitle("HomeScan")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("assets/icon.ico"))

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')


  
    

    def goBack(self):
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)


    
#SCAN


class AdvancedScreen(QMainWindow):
    def __init__(self):
        super(AdvancedScreen,self).__init__()
        uic.loadUi('router/scan_ui/Angry_scan.ui',self)

        
        #connect min full and exit tab (top right) to UI
        global conn, IPAddr, hostname


        #target = socket.gethostbyname(sys.argv[1])
        self.textEdit.append(str("Hostname : " + str(hostname)))
        self.textEdit.append(str("Home IP : " + str(IPAddr)))
        self.textEdit.append(str("Scan Init : " + str(datetime.now())))

        self.pushButton_4.clicked.connect(self.addTxt)
 
        self.pushButton_3.clicked.connect(self.set_IP)
        self.pushButton.clicked.connect(self.clear_fields)

        self.back.clicked.connect(self.goBack)
        self.help.clicked.connect(self.goHelp)

        
    def goHelp(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Help Iinformation about this screen goes here")
        msgBox.setWindowTitle("HomeScan")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("assets/icon.ico"))

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')


  
    
 
    def goBack(self):
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)





    def set_IP(self):
        global conn, IPAddr, hostname
        self.lineEdit_5.setText(IPAddr)

    


    def addTxt(self):
        global clicked

        if (self.lineEdit_5.text() == ''):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Please enter a Target")
            msgBox.setWindowTitle("HomeScan")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setWindowIcon(QIcon("assets/icon.ico"))
            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok:
                return

        elif (self.lineEdit_6.text() == ''):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Please enter a Starting port")
            msgBox.setWindowTitle("HomeScan")
            msgBox.setStandardButtons(QMessageBox.Yes)
            msgBox.setWindowIcon(QIcon("assets/icon.ico"))
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                return

        
        
        elif (int(self.lineEdit_7.text()) - int(self.lineEdit_6.text()) > 200):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("You are questing to scan more than 200+ ports\n\nAre you sure you want to do this? \n\nIt may crash the application or take along time to complete use low ms")
            msgBox.setWindowTitle("HomeScan")
            msgBox.setStandardButtons(QMessageBox.Ok  | QMessageBox.Abort)
            msgBox.setWindowIcon(QIcon("assets/icon.ico"))
            returnValue = msgBox.exec()


            if returnValue == QMessageBox.Abort:
                return
         
        elif (self.lineEdit_7.text() == ''):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Please enter a End port")
            msgBox.setWindowTitle("HomeScan")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setWindowIcon(QIcon("assets/icon.ico"))
            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok:
                return
        elif (self.lineEdit_8.text() == ''):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Please enter a Time delay")
            msgBox.setWindowTitle("HomeScan")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setWindowIcon(QIcon("assets/icon.ico"))
            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok:
                return

        target = self.lineEdit_5.text()
        s_port = int(self.lineEdit_6.text())
        e_port = int(self.lineEdit_7.text())
        ms = int(self.lineEdit_8.text())

        self.progressBar_2.setMinimum(s_port)
        self.progressBar_2.setMaximum(e_port)
        self.progressBar_2.setValue(s_port)


            


        self.textEdit.append(str("-" * 45))
        self.textEdit.append(str("Scanning Target: " + target))
        self.textEdit.append(str("Scanning Ports: " + self.lineEdit_6.text() + " - " + self.lineEdit_7.text()))
        self.textEdit.append(str("Scanning started at: " + str(datetime.now())))
        self.textEdit.append(str("-" * 45))
        try:
            for port in range(s_port, (e_port+1)):
                print(self.progressBar_2.setValue(self.progressBar_2.value() + 1))
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(ms/1000)
                res = s.connect_ex((target, port))
                self.textEdit.repaint()
            
                if res == 0:
                    self.textEdit.append(str("Port " + str(port) + " is OPEN✅"))
                else:
                    self.textEdit.append(str("Port " + str(port) + " is closed❌"))
                self.textEdit.repaint()
                s.close()
        except:
            print("")
            self.textEdit.append("ERROR: Something else went wrong - No IPv4 or IPv6 Found or bad connection")
            
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("ERROR: Something else went wrong, No IPv4 or IPv6 Found or bad connection, Faliure.")
            msgBox.setWindowTitle("HomeScan")
            msgBox.setStandardButtons(QMessageBox.Close)
            msgBox.setWindowIcon(QIcon("assets/icon.ico"))

            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Close:
                print('OK clicked')

    def clear_fields(self):
        global clicked

        if (self.lineEdit_5.text() == '' and self.lineEdit_6.text() == '' and self.lineEdit_7.text() == '' and self.lineEdit_8.text() == ''):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Nothing to clear")
            msgBox.setWindowTitle("HomeScan")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setWindowIcon(QIcon("assets/icon.ico"))
            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok:
                return

     

        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')


            


    
    def export(self):
        now = datetime.now()

        current_time = now.strftime("%m-%d-%Y--%H-%M-%S")

        name_of_file = "AngryScan-" + str(current_time)
        completeName = 'exports/'+ name_of_file + ".log"
        file1 = open(completeName , "w")
        toFile = self.textEdit.toPlainText()
        file1.write(toFile)
        file1.close()

      

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Thank you for using HomeScan.\n\nYour exports has been saved under ScanModule-" + str(current_time) + ".log \n\nDo you think there is something wrong with your exports? or have you found a bug? Email support@homescan.com to open a support ticket! Show the github some aswell\nhttps://github.com/hunterjreid/HomeScan")
        msgBox.setWindowTitle("HomeScan")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("assets/icon.ico"))

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')


  
            

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


class AScan(QMainWindow):
    def __init__(self):
        super(AScan,self).__init__()
        uic.loadUi('router/scan_ui/BasicScan.ui',self)

        
        #connect min full and exit tab (top right) to UI
        

        self.back.clicked.connect(self.goBack)
        self.help.clicked.connect(self.goHelp)

        
    def goHelp(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Help Iinformation about this screen goes here")
        msgBox.setWindowTitle("HomeScan")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("assets/icon.ico"))

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')


  
    

    def goBack(self):
        homeScanMain = HomeScanMain()
        widget.addWidget(homeScanMain)
        widget.setCurrentIndex(widget.currentIndex()+1)



#SCAN END -------------------------------Scan END








class Ports(QMainWindow):
    def __init__(self):
        super(Ports,self).__init__()
        uic.loadUi('router/ports.ui',self)
        
        #connect min full and exit tab (top right) to UI
        self.min.clicked.connect(self.showMinimized)
        self.full.clicked.connect(self.toggleFull)
        self.exit.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_14.clicked.connect(self.goBack)
        self.pushButton_22.clicked.connect(self.arpscan)

    def arpscan(self):
        devices = []
        for device in os.popen('arp -a'):
            devices.append(device)
            self.listWidget.addItem(str(device))


    

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
        self.pushButton_4.clicked.connect(self.export)
        self.exit.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_14.clicked.connect(self.goBack)


        last_received = psutil.net_io_counters().bytes_recv
        last_sent = psutil.net_io_counters().bytes_sent
        last_total = last_received + last_sent
        mb_new_received = last_received / 1024 / 1024
        mb_new_sent = last_sent / 1024 / 1024
        mb_new_total = last_total / 1024 / 1024
        self.lineEdit.setText(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total.")
        

    def export(self):
        now = datetime.now()

        current_time = now.strftime("%m-%d-%Y--%H-%M-%S")

        name_of_file = "Devices-" + str(current_time)
        completeName = 'exports/'+ name_of_file + ".log"
        file1 = open(completeName , "w")
        toFile = self.lineEdit.text()
        file1.write(toFile)
        file1.close()


        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Thank you for using HomeScan.\n\nYour exports has been saved under Devices-" + str(current_time) + ".log \n\nDo you think there is something wrong with your exports? or have you found a bug? Email support@homescan.com to open a support ticket! Show the github some aswell\nhttps://github.com/hunterjreid/HomeScan")
        msgBox.setWindowTitle("HomeScan")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("assets/icon.ico"))

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')


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
    widget.setWindowTitle("HomeScan Pro Edition")
    widget.setFixedSize(920, 550)
    #widget.setFixedSize(920, 900)
    widget.setWindowFlags(Qt.FramelessWindowHint)
    widget.addWidget(window)
    widget.setWindowIcon(QIcon('assets/icon.ico'))
    widget.show()

    QFontDatabase.addApplicationFont("assets/Gilroy.ttf")
    font = QFont("Gilroy")
    widget.window().setFont(font)
    QApplication.setFont(font, "QLabel")
    QApplication.setFont(font, "QCheckBox")
    QApplication.setFont(font, "QPushButton")
    QApplication.setFont(font, "QTextEdit")
    QApplication.setFont(font, "QListWidget")
    QApplication.setFont(font, "QLineEdit")
    QApplication.setFont(font, "QPlotWidget")
    QApplication.setFont(font, "QTableWidget")
    QApplication.setFont(font, "QGraphicsWidget")
    sys.exit(app.exec_())
