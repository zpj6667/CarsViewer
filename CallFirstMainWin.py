# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout, QMainWindow
from PyQt5.QtGui import QIntValidator , QDoubleValidator , QFont
from PyQt5.QtCore import Qt
import socket 
import sys 	
from CarsViewer190914 import *

class MyMainWindow(QMainWindow, Ui_CarsViewer):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self) 
            
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()    
    IPaddress = textchanged(text)
    print(IPaddress)
    client = socket.socket()   
    client.connect(( IPaddress, 19204)) 
#    logger.info("connected")
#    master = modbus_tcp.TcpMaster(host="192.168.192.5", port=502)
    
    sys.exit(app.exec_())  
