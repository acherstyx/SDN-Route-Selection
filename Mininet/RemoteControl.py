from Socket.Server import Listener

class MininetController(Listener):
    
    def __init__(self,net,listen_port=19991):
        super().__init__("localhost")
        # @listen_port: 接收远程指令的端口
        # @net: 对应的之前创建的mininet拓扑，传进来以供后面调用

        self.port = listen_port
        self.net = net

    def Listen(self):
        net = self.net

        while True:
            try:
                msg = super.Listen()
                exec(msg)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    # test case
    from Mininet.FullMesh import Mytopo as topo
    import thread

    t = topo(5)

    net = t.start_mn()

    ctrl = MininetController(net)

    thread.start_new_thread(ctrl.Listen)

    print("Can goon")

