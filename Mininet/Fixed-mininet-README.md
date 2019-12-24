# 使用说明文档
## 前言
在网络性能评估中一个巨大的挑战就是如何生成真实的网络流量，还好可以通过程序来创造人工的网络流量，通过建立测试环境来模拟真实的状况。本文就以数据中心网络为目标场景，来在mininet仿真环境中尽可能地还原数据中心内部的真实流量情况。

## 两种常用的流量模型:

### 随机模型：
主机向在网络中的另一任意主机以等概率发送数据包

为mininet添加自定义命令iperfmulti，依次为每一台主机随机选择另一台主机作为iperf的服务器端，通过调用iperf_single,自身以客户端身份按照指定参数发送UDP流，使用iperfmulti命令，主机随机地向另一台主机发起一条恒定带宽的UDP数据流。
```java
"""在mininet中执行iperfmulti命令，设置带宽参数为0.025M"""
iperfmuti 0.025M 
```

如下图所示，我们就能看到128台主机随机地向另外一台主机发送数据包：
![avatar](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcxLnNkbmxhYi5jb20vd3AtY29udGVudC91cGxvYWRzLzIwMTUvMDQvMTI45Y-w5Li75py66ZqP5py65Zyw5ZCR5Y-m5aSW5LiA5Y-w5Li75py65Y-R6YCB5pWw5o2u5YyFLmpwZw?x-oss-process=image/format,png)

### 概率模型：
为mininet添加自定义命令iperfpb，依次为每一台主机（编号为m）分别以概率Pt 、Pa 、Pc 向主机编号为(m+i)、(m+j)、(m+k)的主机发送数据包，通过调用iperf_single,自身以客户端身份按照指定参数发送UDP流，使用iperfpb命令，主机按概率向其他被选择的主机发起一条恒定带宽的UDP数据流。

```java
"""在mininet中执行iperfPb命令，设置带宽参数为0.025M"""
iperfPb 0.025M
```
依照概率模型，为每一台主机选取对应主机，发送数据包，如下图所示：
![aaa](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcxLnNkbmxhYi5jb20vd3AtY29udGVudC91cGxvYWRzLzIwMTUvMDQv5qaC546H5qih5Z6L77yM5Li65q-P5LiA5Y-w5Li75py66YCJ5Y-W5a-55bqU5Li75py677yM5Y-R6YCB5pWw5o2u5YyF77yM5aaC5LiL5Zu-5omA56S6MS5qcGc?x-oss-process=image/format,png)

概率函数:

```python
"""这个函数可用于以不同的概率从一个列表中随机地选择一些元素"""
#Function：一定概率选择主机
	def  random_pick( self, _list, probabilities):      
		x = random.uniform(0,1)      
		p = None    
		cumulative_probability = 0.0      
		for item, item_probability in zip(_list, probabilities):          
			cumulative_probability += item_probability        
			p = item        
			if x < cumulative_probability:break     
		return p
```
