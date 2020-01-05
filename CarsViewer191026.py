# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarsViewer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys 	
import numpy as np
import pyqtgraph as pg
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen,QFont,QPixmap

class Ui_CarsViewer(object):
    def setupUi(self, CarsViewer):
        global init_width
        global init_high
        global qrect
        CarsViewer.setObjectName("CarsViewer")
        CarsViewer.resize(1109, 902)
        self.centralwidget = QtWidgets.QWidget(CarsViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(238, 46, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_IP = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_IP.sizePolicy().hasHeightForWidth())
        self.lineEdit_IP.setSizePolicy(sizePolicy)
        self.lineEdit_IP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.horizontalLayout.addWidget(self.lineEdit_IP)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_port = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_port.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_port.sizePolicy().hasHeightForWidth())
        self.lineEdit_port.setSizePolicy(sizePolicy)
        self.lineEdit_port.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout.addWidget(self.lineEdit_port)
        spacerItem1 = QtWidgets.QSpacerItem(148, 46, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_link = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_link.sizePolicy().hasHeightForWidth())
        self.pushButton_link.setSizePolicy(sizePolicy)
        self.pushButton_link.setObjectName("pushButton_link")
        self.horizontalLayout_2.addWidget(self.pushButton_link)
        self.pushButton_break = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_break.sizePolicy().hasHeightForWidth())
        self.pushButton_break.setSizePolicy(sizePolicy)
        self.pushButton_break.setObjectName("pushButton_break")
        self.horizontalLayout_2.addWidget(self.pushButton_break)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_socket_status = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_socket_status.sizePolicy().hasHeightForWidth())
        self.label_socket_status.setSizePolicy(sizePolicy)
        self.label_socket_status.setObjectName("label_socket_status")
        self.horizontalLayout_2.addWidget(self.label_socket_status)
        spacerItem3 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout.addWidget(self.horizontalScrollBar, 5, 2, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalScrollBar.sizePolicy().hasHeightForWidth())
        self.verticalScrollBar.setSizePolicy(sizePolicy)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout.addWidget(self.verticalScrollBar, 3, 3, 1, 1)
        self.groupBox_map = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_map.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_map.sizePolicy().hasHeightForWidth())
        self.groupBox_map.setSizePolicy(sizePolicy)
        self.groupBox_map.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_map.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_map.setObjectName("groupBox_map")
        self.verticalScrollBar.raise_()
        self.verticalScrollBar.raise_()
        self.verticalScrollBar.raise_()
        self.gridLayout.addWidget(self.groupBox_map, 3, 2, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        CarsViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CarsViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1109, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        CarsViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CarsViewer)
        self.statusbar.setObjectName("statusbar")
        CarsViewer.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(CarsViewer)
        self.pushButton_add.clicked.connect(CarsViewer.show)
        QtCore.QMetaObject.connectSlotsByName(CarsViewer)
        self.pushButton_add.clicked.connect(self.inputIP_UI)#把添加车辆按钮关联到inputIP_UI()函数

#    def  changeEvent(self,event):#检测窗口事件
#        a = self.isMaximized()#判断是否最大化，最大化为True
#        print("是否最大化", a)

    def inputIP_UI(self, event):#添加车辆弹窗界面
        value, ok = QInputDialog.getText(self, "输入IP", "将要连接机器人的IP地址:", QLineEdit.Normal, "192.168.192.5")
        self.lineEdit_IP.setAlignment(QtCore.Qt.AlignVCenter)
        print(value)
        
    def paintEvent(self, e):#绘制事件
        qp = QPainter()
        qp.begin(self)
        self.drawGrid(qp)
        qp.end()
        
    def drawGrid(self, qp):#绘制网格
        global ratio_height
        global ratio_width
        qrect = self.frameGeometry()
        print("绘制空间大小：", qrect)
        now_width = qrect.width()#最大化后窗口的宽度
        now_height= qrect.height()#最大化后窗口的高度
        start_x, start_y = 55, 175#网格绘制起点坐标（55,175）
        pixe = 30   # 像素
        row =  int((now_height-254)/30)#用界面总高度 - 除实时位置外的区域-Y轴起点宽度（调试）
        column = int((now_width-54-50)/30)#用界面总宽度-除实时位置外的区域-x轴起点宽度（调试）
#        print("行and列：", row, "  ", column)
        pen = QPen(Qt.gray, 1, Qt.SolidLine) #pen = QPen(灰色, 线条粗细, 【3】线条形式)
        #################用线创建列################# 
        for c in range(0, pixe * (column+1), pixe):  
            x0, y0, x1, y1 = c+start_x, 0+start_y, c+start_x, (row * pixe+start_y)  #线段的起点坐标和终点坐标
            qp.setPen(pen)
            qp.drawLine(x0, y0, x1, y1)
        # 绘制Y轴距离尺的基座线
        pen = QPen(Qt.black, 2, Qt.SolidLine) #pen = QPen(【1】颜色, 【2】线条粗细, 【3】线条形式)
        qp.setPen(pen)
        qp.drawLine(start_x, start_y, start_x, (row * pixe+start_y))
        ###############用线创建行###################
        pen = QPen(Qt.gray, 1, Qt.SolidLine) 
        for r in range(0, pixe * (row+1), pixe):  # 创建行
            x0, y0, x1, y1 = 0+start_x, r+start_y, (column * pixe+start_x), r+start_y
            qp.setPen(pen)
            qp.drawLine(x0, y0, x1, y1)
            
        # 绘制X轴距离尺的基座线
        pen = QPen(Qt.black, 2, Qt.SolidLine) 
        qp.setPen(pen)
        qp.drawLine(start_x, start_y, (column * pixe+start_x), start_y)
        #绘制坐标原点红色行线
        pen = QPen(Qt.red, 1, Qt.SolidLine) 
        qp.setPen(pen)
        qp.drawLine(start_x, start_y+2*pixe, (column * pixe+start_x), start_y+2*pixe) 
        #绘制坐标原点红色列线
        pen = QPen(Qt.red, 1, Qt.SolidLine) 
        qp.setPen(pen)
        qp.drawLine(start_x+2*pixe, start_y, start_x+2*pixe, (row * pixe+start_y))
        #绘制Y轴坐标尺短刻度线
        for r in range(0, pixe * (row+1), pixe): 
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            qp.setPen(pen)
            qp.drawLine(start_x-3, start_y+r, start_x, start_y+r)
        #绘制X轴坐标尺短刻度线
        for r in range(0, pixe * (column+1), pixe):  
            pen = QPen(Qt.black, 2, Qt.SolidLine) 
            qp.setPen(pen)
            qp.drawLine(start_x+r, start_y-3, start_x+r, start_y)
        #从坐标原点开始绘制Y轴坐标尺长刻度线并标明刻度
        for r in range(2*pixe, pixe * (row+1), pixe*5): 
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            qp.setPen(pen)
            qp.drawLine(start_x-10, start_y+r, start_x, start_y+r)
            scale = (r/pixe-2)*-100#刻度值放大100
            scale = str(int(scale))
            qp.drawText(start_x-40, start_y+r-5, scale)  #绘制字体
        #从坐标原点开始绘制X轴坐标尺长刻度线并标明刻度
        for r in range(2*pixe, pixe * (column+1), pixe*5):  
            pen = QPen(Qt.black, 2, Qt.SolidLine) 
            qp.setPen(pen)
            qp.drawLine(start_x+r, start_y-10, start_x+r, start_y)
            scale = (r/pixe-2)*100
            scale = str(int(scale))
            qp.drawText(start_x+r-20, start_y-13, scale)  #绘制字体
        #绘制坐标原点蓝色圆圈
        pen = QPen(Qt.blue, 3, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawEllipse((start_x+2*pixe-pixe/2),(start_y+2*pixe-pixe/2),30,30)#椭圆左上角的 X/y 坐标，宽、高
        #绘制坐标原点蓝色行线和列线
        qp.drawLine(start_x+30, start_y+60, start_x+90, start_y+60)#行
        qp.drawLine(start_x+60, start_y+30, start_x+60, start_y+90)#列
        
    def retranslateUi(self, CarsViewer):
        _translate = QtCore.QCoreApplication.translate
        CarsViewer.setWindowTitle(_translate("CarsViewer", "MainWindow"))
        self.label.setText(_translate("CarsViewer", "IP："))
        self.lineEdit_IP.setText(_translate("CarsViewer", "192.168.192.5"))
        self.label_2.setText(_translate("CarsViewer", "端口："))
        self.lineEdit_port.setText(_translate("CarsViewer", "19204"))
        self.pushButton_add.setText(_translate("CarsViewer", "添加车辆"))
        self.pushButton_link.setText(_translate("CarsViewer", "链接"))
        self.pushButton_break.setText(_translate("CarsViewer", "断开"))
        self.label_3.setText(_translate("CarsViewer", "状态："))
        self.label_socket_status.setText(_translate("CarsViewer", "未连接"))
        self.groupBox_map.setTitle(_translate("CarsViewer", "实时位置显示"))
        self.menu.setTitle(_translate("CarsViewer", "文件"))
        self.menu_2.setTitle(_translate("CarsViewer", "工具"))
        self.menu_3.setTitle(_translate("CarsViewer", "设置"))
        self.menu_4.setTitle(_translate("CarsViewer", "关于"))
