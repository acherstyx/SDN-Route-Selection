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
        self.Button_Connect.clicked.connect(self.ConnectMsg)
        self.Button_Connect.clicked.connect(self.ConnectMsg2)
        self.Button_Break.clicked.connect(self.BreakMsg)

    def ConnectMsg(self):
        print('Connect!')
        self.matplotlibwidget_dynamic.mpl.update_figure(\
            np.array([[0,0,0,1,0,3,6],[1,2,3,4,5,6,7],[1,0,0,0,0,3,5]]))
        myWin.show()

    def ConnectMsg2(self):
        print('Connect2!')
        self.matplotlibwidget_dynamic.mpl.update_figure()

    def BreakMsg(self):
        print('Break!')
        self.matplotlibwidget_dynamic.mpl.update_figure()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.treeWidget.expandAll() # 树节点全部展开
    myWin.show()
    sys.exit(app.exec_())
