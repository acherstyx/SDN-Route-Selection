from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
import  mininet.cli as cli

class MyTopo(Topo):
    def __init__(self, switches=5):
        # create a full mesh network topology based on the number of switch
        # @switchs: the total number of switchs in the network 
        Topo.__init__(self)

        self.s = []
        self.h = []
        self.l = []

        for i in range(switches):
            self.s.append(self.addSwitch("s{}".format(i)))
            self.h.append(self.addHost("h{}".format(i)))
            self.l.append(self.addLink(self.s[i], self.h[i]))

        for i in range(switches):
            for ii in range(switches):
                if i != ii:
                    self.addLink(self.s[i], self.s[ii])

        # self.link = l
        # self.host = h
        # self.switches = s
        # self.net = None        # self.link = l
        # self.host = h
        # self.switches = s
        # self.net = None

    def start_mn(self):
        net = Mininet(topo=self, controller=None)
        net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)
        net.start()
        self.net = net
        return net

topos = {'mytopo': (lambda: MyTopo())}

if __name__ == "__main__":
    topo = MyTopo()
    net = topo.start_mn()

    data = net.pingAll()
    print(data)
    data = net.pingAllFull()
    print(data)

    net.interact()

    net.stop()
