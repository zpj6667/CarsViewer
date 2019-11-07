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
        CarsViewer.resize(971, 817)
        self.centralwidget = QtWidgets.QWidget(CarsViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addLayout(self.horizontalLayout)
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
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.gridLayout_3.addWidget(self.groupBox_map, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        CarsViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CarsViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 971, 26))
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
        
        qrect = self.frameGeometry()#获取初始窗口位置和大小
        init_width = qrect.width()#初始窗口的宽度
        init_high= qrect.height()#初始窗口的高度
        

        
    def  changeEvent(self,event):#检测窗口事件
        global ratio_height
        global ratio_width
        ratio_height = 1
        ratio_width = 1
        a = self.isMaximized()#判断是否最大化，最大化为True
        print("是否最大化", a)
        if a == True :
            qrect = self.frameGeometry()#获取此刻窗口位置和大小
            print(qrect)
            now_width = qrect.width()#最大化后窗口的宽度
            now_height= qrect.height()#最大化后窗口的高度

            ratio_width = now_width/init_width
            ratio_height = now_height/init_high
            
        print(ratio_width,"  ", ratio_height )
    
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
        print("初始状态的窗口大小：", qrect)
        pixe = 30   # 像素
        row =   int(init_high*ratio_height/40) # 行数
        column =  int(init_width*ratio_width/32) # 列数
        print("行and列：", row, "  ", column)
        pen = QPen(Qt.gray, 1, Qt.SolidLine) #pen = QPen(【1】颜色, 【2】线条粗细, 【3】线条形式)
        # 用线创建网格
        for c in range(0, pixe * (column+1), pixe):  # 创建列
            x0, y0, x1, y1 = c+60, 0+180, c+60, (row * pixe+180) 
            qp.setPen(pen)
            qp.drawLine(x0, y0, x1, y1)
        for r in range(0, pixe * (row+1), pixe):  # 创建行
            x0, y0, x1, y1 = 0+60, r+180, (column * pixe+60), r+180

            qp.setPen(pen)
            qp.drawLine(x0, y0, x1, y1)
            

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
