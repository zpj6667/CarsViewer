# -*- coding: utf-8 -*-
import socket 
import sys 	
from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout, QMainWindow
from PyQt5.QtGui import QIntValidator , QDoubleValidator , QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from CarsViewer191026 import *
from ReadMap import *
from draw import *

class MyMainWindow(QMainWindow, Ui_CarsViewer):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    
    
    
#    demo=Drawing()
#    demo.show() #显示点和线
    myWin.show()  #显示主窗口
    Mapreading()
#    Change_Format()  
#    Get_position_line()
    sys.exit(app.exec_())  
    
