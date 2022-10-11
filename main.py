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
   
        self.pushButton_6.clicked.connect(self.showMinimized)
        self.pushButton_5.clicked.connect(QtWidgets.qApp.quit)
        self.oldPos = self.pos()
        self.show()
        self.loadtable()
        self.loadtable2()
        people=psutil.net_connections()
        stats=psutil.net_if_stats()
        self.label_2.setText("Total Net Connections: " + str(len(people)))
    
        
    
        self.label_3.setText("Network Interfaces: " + str(len(stats)))
    

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

    def setColortoRow(table, rowIndex, color):
        for j in range(table.columnCount()):
            table.item(rowIndex, j).setBackground(color)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())




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

            

     

            # self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person[row][1])))
            # self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person[row][5])))
            # self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(person[row][3])))
            row=row+1
        
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()  

    def loadtable2(self):
        people=psutil.net_if_stats()
        print(people)

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

    def setColortoRow(table, rowIndex, color):
        for j in range(table.columnCount()):
            table.item(rowIndex, j).setBackground(color)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = HomeScan()
    window.show()
    sys.exit(app.exec_())