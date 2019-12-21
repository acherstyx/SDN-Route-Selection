#CallMyjiekou.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWin import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.matplotlibwidget_dynamic.setVisible(True)
        self.matplotlibwidget_dynamic.mpl.update_figure()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.treeWidget.expandAll() # 树节点全部展开
    myWin.show()
    sys.exit(app.exec_())
