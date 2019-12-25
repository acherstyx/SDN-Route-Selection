# CallMyjiekou.py
import sys
from PyQt5.QtWidgets import *
from MainWin import Ui_MainWindow
import random
import time
# Remote ctrl
from Mininet.Commander import Commander


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.matplotlibwidget_dynamic.setVisible(True)
        self.matplotlibwidget_dynamic.mpl.update_figure()
        # 信号与槽
        self.Button_Connect.clicked.connect(self.ConnectTextMsg)
        self.Button_Connect.clicked.connect(self.ConnectTreeMsg)
        self.Button_Break.clicked.connect(self.BreakTextMsg)
        self.Button_Break.clicked.connect(self.BreakTreeMsg)
        # init the commander of mininet
        # TODO: change the hostname to fit the need of task
        self.cmd = Commander("centos-host.local")

    # 简单的输入合法性检查
    def invalid_check(self):
        check1 = (self.lineEdit.text()[:9] == 'openflow:') and (self.lineEdit_2.text()[:9] == 'openflow:')
        check2 = (len(self.lineEdit.text()) == 10) and (len(self.lineEdit_2.text()) == 10)
        return (check1 and check2)

    # TODO:
    def ConnectTextMsg(self):
        if self.invalid_check():
            print("up:")
            print(self.lineEdit.text(), end="")
            print(", ")
            print(self.lineEdit_2.text())
            self.cmd.addLink("s" + self.lineEdit.text()[-1:], "s" + self.lineEdit_2.text()[-1:])
            time.sleep(5)
            self.cmd.pingAll()

    def BreakTextMsg(self):
        if self.invalid_check():
            print("down:")
            print(self.lineEdit.text(), end="")
            print(", ")
            print(self.lineEdit_2.text())
            self.cmd.delLink("s" + self.lineEdit.text()[-1:], "s" + self.lineEdit_2.text()[-1:])
            time.sleep(5)
            self.cmd.pingAll()

    # 树控件
    ## 维护一个索引列表
    TreeLst = [
        [0, 0, 0, 0, 0],
        [0, 2, 3, 4, 5],
        [0, 1, 3, 4, 5],
        [0, 1, 2, 4, 5],
        [0, 1, 2, 3, 5],
        [0, 1, 2, 3, 4],
        [0, 0, 0, 0, 0]
    ]

    # TreeeLst[e1][e2]
    # 输入 e1, e2，返会 e2 在 tree 中的索引（TreeLst -1 -> tree）
    def FindIndex(self, e1, e2):
        for i in range(len(self.TreeLst[e1])):
            if self.TreeLst[e1][i] == e2:
                return i - 1
        return -1

    def msg(self):
        reply = QMessageBox.information(self,  # 使用infomation信息框
                                        "警告",
                                        "查询不到要删除的链路！",
                                        QMessageBox.Yes | QMessageBox.No)

    def msg_c(self):
        reply = QMessageBox.information(self,  # 使用infomation信息框
                                        "警告",
                                        "该链路已经连接！",
                                        QMessageBox.Yes | QMessageBox.No)

    def ConnectTreeMsg(self):
        if self.invalid_check():
            e1 = eval(self.lineEdit.text()[9])
            e2 = eval(self.lineEdit_2.text()[9])
            if self.FindIndex(e1, e2) != -1:
                self.msg_c()
                return

            curretNode = self.treeWidget.topLevelItem(e1 - 1).child(3)
            addChild1 = QTreeWidgetItem()
            addChild1.setText(0, "openflow:" + str(e2))
            addChild1.setText(1, "时延 " + str(int(12 * random.random())) + "ms")
            curretNode.addChild(addChild1)

            curretNode = self.treeWidget.topLevelItem(e2 - 1).child(3)
            addChild2 = QTreeWidgetItem()
            addChild2.setText(0, "openflow:" + str(e1))
            addChild2.setText(1, "时延 " + str(int(12 * random.random())) + "ms")
            curretNode.addChild(addChild2)

            self.TreeLst[e1].append(e2)
            self.TreeLst[e2].append(e1)

    def BreakTreeMsg(self):
        if self.invalid_check():
            e1 = eval(self.lineEdit.text()[9])
            e2 = eval(self.lineEdit_2.text()[9])

            index = self.FindIndex(e1, e2)
            curretNode = self.treeWidget.topLevelItem(e1 - 1).child(3).child(index)
            if curretNode == None:
                self.msg()
                return
            parent = curretNode.parent()
            parent.removeChild(curretNode)
            self.TreeLst[e1].remove(e2)

            index = self.FindIndex(e2, e1)
            curretNode = self.treeWidget.topLevelItem(e2 - 1).child(3).child(index)
            if curretNode == None:
                self.msg()
                return
            parent = curretNode.parent()
            parent.removeChild(curretNode)
            self.TreeLst[e2].remove(e1)
            # self.removeChild(self.treeWidget.topLevelItem(1).child(3).child(0))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.treeWidget.expandAll()  # 树节点全部展开
    myWin.show()
    sys.exit(app.exec_())
