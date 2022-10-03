from PyQt5 import QtWidgets, uic
import psutil

app = QtWidgets.QApplication([])
dlg = uic.loadUi("mainwindow.ui")


def btn1():
    dlg.textEdit.append(str(psutil.net_io_counters(pernic=True)))
def btn9():
    dlg.textEdit.clear()


def btn2():
    last_received = psutil.net_io_counters().bytes_recv
    last_sent = psutil.net_io_counters().bytes_sent
    last_total = last_received + last_sent
    mb_new_received = last_received / 1024 / 1024
    mb_new_sent = last_sent / 1024 / 1024
    mb_new_total = last_total / 1024 / 1024
    dlg.textEdit.append(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total.")


def btn3():
    dlg.textEdit.append(str(psutil.net_connections()))

def btn4():
    dlg.textEdit.append(str(psutil.net_if_stats()))

def btn14():


    dlg.textEdit.append(str(psutil.net_connections(kind="tcp")))
   


def btn8():
    dlg.textEdit.append(str(psutil.net_if_addrs()))
def btn5():
    dlg.textEdit.append(str(psutil.net_connections(kind='inet')))


def btn7():
    dlg.textEdit.append(str(psutil.net_if_addrs()))


dlg.pushButton.clicked.connect(btn1)
dlg.pushButton_2.clicked.connect(btn2)
dlg.pushButton_3.clicked.connect(btn4)
dlg.pushButton_4.clicked.connect(btn3)
dlg.pushButton_9.clicked.connect(btn9)
dlg.pushButton_8.clicked.connect(btn8)
dlg.pushButton_5.clicked.connect(btn5)
dlg.pushButton_6.clicked.connect(btn14)
dlg.pushButton_7.clicked.connect(btn7)

dlg.show()
app.exec()
