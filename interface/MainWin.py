# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(360, 20, 181, 341))
        self.treeWidget.setMinimumSize(QtCore.QSize(2, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(201, 16777215))
        self.treeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.treeWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setObjectName("treeWidget")
        ## add
        self.treeWidget.setColumnWidth(0,88)
        self.treeWidget.setColumnWidth(1,110)

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
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 191, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_Connect = QtWidgets.QPushButton(self.layoutWidget)
        self.Button_Connect.setObjectName("Button_Connect")
        self.horizontalLayout.addWidget(self.Button_Connect)
        self.Button_Break = QtWidgets.QPushButton(self.layoutWidget)
        self.Button_Break.setObjectName("Button_Break")
        self.horizontalLayout.addWidget(self.Button_Break)
        self.Button_Refresh = QtWidgets.QPushButton(self.layoutWidget)
        self.Button_Refresh.setObjectName("Button_Refresh")
        self.horizontalLayout.addWidget(self.Button_Refresh)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        # modify
        self.matplotlibwidget_dynamic = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget_dynamic.setEnabled(True)
        self.matplotlibwidget_dynamic.setGeometry(QtCore.QRect(20, 90, 321, 271))
        self.matplotlibwidget_dynamic.setObjectName("matplotlibwidget_dynamic")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 18))
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
        self.Button_Connect.setText(_translate("MainWindow", "连接"))
        self.Button_Break.setText(_translate("MainWindow", "断开"))
        self.Button_Refresh.setText(_translate("MainWindow", "刷新"))
        self.label.setText(_translate("MainWindow", "节点1："))
        self.label_2.setText(_translate("MainWindow", "节点2："))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

## add
from MatplotlibWidget import MatplotlibWidget