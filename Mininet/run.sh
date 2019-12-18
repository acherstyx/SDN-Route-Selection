#!/bin/bash
# 用于通过linux命令创建拓扑，可以使用但是没有必要，FullMesh.py中已经实现了相关功能
mn --custom FullMesh.py --topo mytopo --mac --controller=remote,ip=127.0.0.1,port=6653