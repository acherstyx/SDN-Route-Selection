#CallMyjiekou.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWin import Ui_MainWindow
import numpy as np

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
        self.Button_Connect.clicked.connect(self.ConnectChangeTreeMsg)
        self.Button_Break.clicked.connect(self.BreakTextMsg)
        self.Button_Connect.clicked.connect(self.BreakChangeTreeMsg)
    # TODO:
    def TextMsg(self):
        print("up:")
        print(self.lineEdit.text(), end="")
        print(self.lineEdit_2.text(), end="")

    def BreakTextMsg(self):
        print("down:")
        print(self.lineEdit.text(), end="")
        print(self.lineEdit_2.text(), end="")

    def ConnectChangeTreeMsg(self):
        pass
    def BreakChangeTreeMsg(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.treeWidget.expandAll() # 树节点全部展开
    myWin.show()
    sys.exit(app.exec_())
