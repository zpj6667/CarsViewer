# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarsViewer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CarsViewer(object):
    def setupUi(self, CarsViewer):
        CarsViewer.setObjectName("CarsViewer")
        CarsViewer.resize(971, 774)
        self.centralwidget = QtWidgets.QWidget(CarsViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_map = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_map.setGeometry(QtCore.QRect(11, 78, 949, 634))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_map.sizePolicy().hasHeightForWidth())
        self.groupBox_map.setSizePolicy(sizePolicy)
        self.groupBox_map.setObjectName("groupBox_map")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(11, 11, 572, 23))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_IP = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_IP.sizePolicy().hasHeightForWidth())
        self.lineEdit_IP.setSizePolicy(sizePolicy)
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.horizontalLayout.addWidget(self.lineEdit_IP)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_port = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_port.sizePolicy().hasHeightForWidth())
        self.lineEdit_port.setSizePolicy(sizePolicy)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout.addWidget(self.lineEdit_port)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_socket_status = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_socket_status.sizePolicy().hasHeightForWidth())
        self.label_socket_status.setSizePolicy(sizePolicy)
        self.label_socket_status.setObjectName("label_socket_status")
        self.horizontalLayout.addWidget(self.label_socket_status)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(11, 41, 195, 30))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_link = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_link.sizePolicy().hasHeightForWidth())
        self.pushButton_link.setSizePolicy(sizePolicy)
        self.pushButton_link.setObjectName("pushButton_link")
        self.horizontalLayout_2.addWidget(self.pushButton_link)
        self.pushButton_break = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_break.sizePolicy().hasHeightForWidth())
        self.pushButton_break.setSizePolicy(sizePolicy)
        self.pushButton_break.setObjectName("pushButton_break")
        self.horizontalLayout_2.addWidget(self.pushButton_break)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(820, 10, 93, 28))
        self.pushButton_add.setObjectName("pushButton_add")
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

    def retranslateUi(self, CarsViewer):
        _translate = QtCore.QCoreApplication.translate
        CarsViewer.setWindowTitle(_translate("CarsViewer", "MainWindow"))
        self.groupBox_map.setTitle(_translate("CarsViewer", "实时位置显示"))
        self.label.setText(_translate("CarsViewer", "IP："))
        self.lineEdit_IP.setText(_translate("CarsViewer", "127.0.0.1"))
        self.label_2.setText(_translate("CarsViewer", "端口："))
        self.lineEdit_port.setText(_translate("CarsViewer", "19204"))
        self.label_3.setText(_translate("CarsViewer", "状态："))
        self.label_socket_status.setText(_translate("CarsViewer", "TextLabel"))
        self.pushButton_link.setText(_translate("CarsViewer", "链接"))
        self.pushButton_break.setText(_translate("CarsViewer", "断开"))
        self.pushButton_add.setText(_translate("CarsViewer", "Add Robots"))
        self.menu.setTitle(_translate("CarsViewer", "文件"))
        self.menu_2.setTitle(_translate("CarsViewer", "工具"))
        self.menu_3.setTitle(_translate("CarsViewer", "设置"))
        self.menu_4.setTitle(_translate("CarsViewer", "关于"))
