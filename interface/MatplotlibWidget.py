import sys
import random
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=500, height=400, dpi=100):

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111)

        # self.axes.hold(False)  # 每次绘图的时候不保留上一次绘图的结果
        # matplotlib.pyplot.clf()

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    '''启动绘制动态图'''
    def start_dynamic_plot(self, *args, **kwargs):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure) # 每隔一段时间就会触发一次update_figure函数。
        timer.start(10000)  # 触发的时间间隔为1秒。
    
    '''动态图的绘图逻辑可以在这里修改'''
    # TODO: 
    def update_figure(self, an=np.array([[0,0,0,1,2,3,6],[1,2,3,4,5,6,7],[1,2,1,8,1,3,5]])):
        self.fig.suptitle('当前网络拓扑图')
        row, col, value = an[0], an[1], an[2]

        # 生成一个空的有向图
        G = nx.DiGraph()
        # 为这个网络添加节点
        for i in range(np.size(col)):
            G.add_node(i)
        # 在网络中添加带权中的边
        for i in range(np.size(row)):
            G.add_weighted_edges_from([(row[i],col[i],value[i])])
        
        # 为网路设置布局
        pos = nx.shell_layout(G)
        # nx.draw(G, pos, with_labels=True, node_color='white',\
            # edge_color='red', node_size = 400, alpha = 0.5, ax = self.axes)
        nx.draw(G, pos, ax = self.axes,\
             node_color='w', edge_color='r', with_labels=True, alpha=1, font_size=10, node_size=20, arrows=True)

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.mpl.start_dynamic_plot()
        # self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar
        self.layout.addWidget(self.mpl)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    # ui.mpl.start_dynamic_plot() # 测试动态图效果
    ui.mpl.update_figure()
    ui.show()
    sys.exit(app.exec_())