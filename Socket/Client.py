import socket


class Talker():
    def __init__(self, host, port=19991):
        self.s = socket.socket()
        self.host = host
        self.port = port
        self.s.connect((self.host, self.port))

    def talk(self, msg):
        # link establish

        self.s.send(msg)
        # self.s.close()
        # self.s.close()


if __name__ == "__main__":
    import time

    # test case

    # server.talk("print('a+d')\n")
    # server.talk("print(net)\n")
    input("wait...")
    server = Talker("centos-host.local")
    server.talk("net.configLinkStatus('s0','h0','down')\n")
    time.sleep(5)
    server = Talker("centos-host.local")
    server.talk("net.pingAll()\n")
    input("wait...")
    server = Talker("centos-host.local")
    server.talk("net.configLinkStatus('s0','h0','up')\n")
    time.sleep(5)
    server = Talker("centos-host.local")
    server.talk("net.pingAll()\n")
