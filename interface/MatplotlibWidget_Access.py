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

"""
This version add the access of node data get from model 'node.nodemap'
Related functions inherited from model 'MatplotlibWidget'
"""
from interface.MatplotlibWidget import QApplication as QApplication_pre
from interface.MatplotlibWidget import MatplotlibWidget as MatplotlibWidget_pre
from interface.MatplotlibWidget import MyMplCanvas as MyMplCanvas_pre

from node.NodeMap import NodeMap
from node.GetNodeInfo import get_response


class MyMplCanvas(MyMplCanvas_pre):

    def __generate_fromatted_data(self):
        # TODO: change the hostname to fit the need of task, or add it to __init__
        json_dict = get_response("centos-host")
        map = NodeMap(json_dict)

        row = []
        col = []
        value = []

        for src in map.AllNodes:
            for dst in map.AllNodes[src].link_list:
                row.append(src)
                col.append(dst)
                value.append(1)

        return row, col, value

    def update_figure(self):
        self.fig.suptitle('当前网络拓扑图')

        # change: get data from remote
        row, col, value = self.__generate_fromatted_data()

        # 生成一个空的有向图
        G = nx.DiGraph()
        # 为这个网络添加节点
        for i in range(np.size(row)):
            G.add_node(row[i])
        # 在网络中添加带权中的边
        for i in range(np.size(row)):
            G.add_weighted_edges_from([(row[i], col[i], value[i])])

        # 为网路设置布局
        pos = nx.shell_layout(G)
        # nx.draw(G, pos, with_labels=True, node_color='white',\
        # edge_color='red', node_size = 400, alpha = 0.5, ax = self.axes)
        nx.draw(G, pos, ax=self.axes,
                node_color='w',
                edge_color='r',
                with_labels=True,
                alpha=1,
                font_size=10,
                node_size=10,
                arrows=True)


class MatplotlibWidget(MatplotlibWidget_pre):
    # Override the method
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
