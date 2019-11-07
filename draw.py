import math
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Drawing(QWidget):
    def paintEvent(self,event):
        #初始化绘图工具
        qp=QPainter()
        #开始在窗口绘制
        qp.begin(self)
        #自定义画点方法
        self.drawPoints(qp)
        #结束在窗口的绘制
        qp.end()
        
    def drawPoints(self,qp):
        qp.setPen(Qt.red)
#        size=self.size()
        qp.drawPoint(0,0)
        qp.drawPoint(0,1)
        qp.drawPoint(0,2)

