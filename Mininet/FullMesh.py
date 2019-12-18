from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController

class MyTopo(Topo):
    def __init__(self,switchs=5):
        # create a full mesh network topology based on the number of switch
        # @switchs: the total number of switchs in the network 
        Topo.__init__(self)

        s = []
        h = []

        for i in range(switchs):
            s.append(self.addSwitch("s{}".format(i)))
            h.append(self.addHost("h{}".format(i)))
            self.addLink(s[i],h[i])

        for i in range(switchs):
            for ii in range(switchs):
                if i!=ii:
                    self.addLink(s[i],s[ii])

    def start_mn(self):
        net = Mininet(topo=self,controller=None)
        net.addController('c0',controller=RemoteController,ip='127.0.0.1',port=6653)
        net.start()
        return net

topos = {'mytopo':(lambda: MyTopo())}

if __name__ == "__main__":
    topo = MyTopo()
    net = topo.start_mn()

    # 两组Ping，返回节点延迟的相关信息
    print(net.pingAll())
    print(net.pingAllFull())
    # 开启mininet的交互界面，不需要直接注释掉
    net.interact()
    
    net.stop()
