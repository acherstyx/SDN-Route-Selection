# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 窗体“舞台”
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ## 按钮与布局
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 178, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_Connect = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Button_Connect.setObjectName("Button_Connect")
        self.horizontalLayout.addWidget(self.Button_Connect)
        self.Button_Break = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Button_Break.setObjectName("Button_Break")
        self.horizontalLayout.addWidget(self.Button_Break)
        self.Button_Move = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Button_Move.setObjectName("Button_Move")
        self.horizontalLayout.addWidget(self.Button_Move)

        ## TreeWidget
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(290, 70, 201, 192)) # 坐标
        self.treeWidget.setMinimumSize(QtCore.QSize(201, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(201, 16777215))
        self.treeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.treeWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setObjectName("treeWidget")
        #### Add
        self.treeWidget.setColumnWidth(0,100)
        
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setSortIndicatorShown(False)

        ## 图片
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 70, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_Connect.setText(_translate("MainWindow", "连接"))
        self.Button_Break.setText(_translate("MainWindow", "断开"))
        self.Button_Move.setText(_translate("MainWindow", "移动"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "项目名"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "信息"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "节点名"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "OpenFlow 2"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "负载"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("MainWindow", "2.1"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "连接设备"))
        self.treeWidget.topLevelItem(2).setText(1, _translate("MainWindow", "3台"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "h1"))
        self.treeWidget.topLevelItem(2).child(0).setText(1, _translate("MainWindow", "↑ 20KB/s ↓11KB/S"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "h2"))
        self.treeWidget.topLevelItem(2).child(1).setText(1, _translate("MainWindow", "↑ 10KB/s ↓21KB/S"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "h3"))
        self.treeWidget.topLevelItem(2).child(2).setText(1, _translate("MainWindow", "↑ 11KB/s ↓53KB/S"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "已禁用设备"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "h4"))
        self.treeWidget.topLevelItem(3).child(0).setText(1, _translate("MainWindow", "已禁用"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "连接到的交换机"))
        self.treeWidget.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "OpenFlow 1"))
        self.treeWidget.topLevelItem(4).child(0).setText(1, _translate("MainWindow", "时延 10ms"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

from interface.MatplotlibWidget import MatplotlibWidget