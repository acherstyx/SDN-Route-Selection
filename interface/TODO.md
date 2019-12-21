## 基础工作
- [x] 选择使用的绘图方式
NetworkX+malplotlib （而不是用它自带的库）
[用Python的networkx绘制精美网络图](https://blog.csdn.net/qq951127336/article/details/54586869)
[[python] 基于NetworkX实现网络图的绘制](https://blog.csdn.net/LuohenYJ/article/details/102787660)
到时候做的精致一点，如果可以加网络设备的图标最好。

- [ ] 文档

[《快速掌握PyQt5》第十三章 学会使用文档——Qt Assistant](https://blog.csdn.net/La_vie_est_belle/article/details/82662937)

	
- [ ] 更细致地复习、了解 Qt 的设计模式
- [ ] 信号和槽的实验（Qt的核心机制）
- [ ] 对接逻辑程序
- [ ] 绘图库的对接实现
- [ ] 实时更新
	1. 界面文件和逻辑文件分离的方式
	1. 和后端连接的方式
	1. MatPlotlib
	1. 合适的文档
- [ ] 了解对应的控件的属性（以便后续的调用）
- [ ] 完整地去做

## 优化工作
- [ ] 图标、图片（增强可视化）
- [ ] 打包资源文件问题

为了展示效果，要么演示屏幕放大，要么UI界面调大

## 汇报
### 没有完全完成？
别人的方案（看不到的地方）：
1. 写死数据
1. 随机生成时延
1. Postman 假装

最重要的是自圆其说，
不是掩饰，而是展示这个想法的价值。

### 关键
一体化、展示效果、连贯性
终端要集中，不要零零散散。
拓扑要复杂（哭笑不得），其实也能更体现自己的方案适用于复杂工程问题。



MainWin.ui 
MainWin copy是副本，因为如果.ui更改的话，会覆盖MainWin.py；
MatplotlibWidget.py 是对 MainWin.ui 里面自定义的一个 MatplotlibWidget 组件的实现；
Project.py 就是运行程序