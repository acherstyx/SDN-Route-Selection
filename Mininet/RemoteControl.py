try:
    from Socket.Server import Listener
except:
    from Server import Listener

from mininet.cli import CLI
import time
import thread


class MininetController(Listener):

    def __init__(self, net, topo, listen_port=19991):
        Listener.__init__(self, listen_port)
        # @listen_port: read remote message from port
        # @net: the topology from mininet

        self.port = listen_port
        self.net = net
        self.topo = topo

    def Listen(self):
        # start listen
        print("Start listen")
        while True:
            try:
                msg = self.listen()
                print("Receive command: ", msg)
                thread.start_new_thread(self.run, (msg,))
            except Exception as e:
                print(e)

    def run(self, msg):
        net = self.net
        topo = self.topo
        exec msg


if __name__ == "__main__":
    # test case
    try:
        from Mininet.FullMesh import MyTopo as topo
    except:
        from FullMesh import MyTopo as topo
    import thread

    t = topo(5)

    net = t.start_mn()

    ctrl = MininetController(net, t)
    # time.sleep(10)

    net.start()
    net.pingAll()
    thread.start_new_thread(ctrl.Listen, ())

    print("Can goon")

    try:
        net.interact()
        time.sleep(3600)
    except KeyboardInterrupt:
        net.stop()
    net.stop()
    
