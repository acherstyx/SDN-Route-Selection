#CallMyjiekou.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWin import Ui_MainWindow
import numpy as np
import random

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
        self.Button_Connect.clicked.connect(self.BreakTreeMsg)
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
            print(self.lineEdit_2.text(), end="")

    def BreakTextMsg(self):
        if self.invalid_check():
            print("down:")
            print(self.lineEdit.text(), end="")
            print(", ")
            print(self.lineEdit_2.text(), end="")

    def ConnectTreeMsg(self):
        pass
    def BreakTreeMsg(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.treeWidget.expandAll() # 树节点全部展开
    myWin.show()
    sys.exit(app.exec_())