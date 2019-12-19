try:
    from Socket.Client import Talker
except:
    from Client import Talker
import time
import socket
import thread


class Commander(Talker):

    def __init__(self, host, port=19991):
        Talker.__init__(self, host, port)
        self.host = host
        self.port = port

    def delLink(self, node1, node2):
        """
        delete the link between node1 and node2
        :param node1: the name of node1     e.g. "s1"
        :param node2: the name of node2     e.g. "s2"
        """
        thread.start_new_thread(self.__delLink__, (node1, node2))

    def __delLink__(self, node1, node2):
        """
        separate function for multi-thread
        :param node1:
        :param node2:
        """
        try_count = 0
        while True:
            try_count += 1
            try:
                Talker.__init__(self, self.host, self.port)
                self.talk("net.configLinkStatus('{}','{}','down')\n".format(node1, node2))
                print("Successfully delete link:", node1, "<-x->", node2)
                break
            except socket.error as e:
                print("Error in delLink:", e)
                print("retry", try_count)
                Talker.__init__(self, self.host, self.port)
                time.sleep(1)

    def addLink(self, node1, node2):
        """
        add link between node1 and node2
        :param node1: string    e.g. "s0"
        :param node2: string    e.g. "s1"
        """
        thread.start_new_thread(self.__addLink__, (node1, node2))

    def __addLink__(self, node1, node2):
        """
        for multi-thread
        :param node1:
        :param node2:
        """
        try_count = 0
        while True:
            try_count += 1
            try:
                Talker.__init__(self, self.host, self.port)
                self.talk("net.configLinkStatus('{}','{}','up')\n".format(node1, node2))
                print("Successfully add link:", node1, "<--->", node2)
                break
            except socket.error as e:
                print("Error in addLink:", e)
                print("retry", try_count)
                Talker.__init__(self, self.host, self.port)
                time.sleep(1)

    def pingAll(self):
        """
        ping all node
        """
        thread.start_new_thread(self.__pingAll__, ())

    def __pingAll__(self):
        """
        for multi-thread
        """
        try_count = 0
        while True:
            try_count += 1
            try:
                Talker.__init__(self, self.host, self.port)
                self.talk("net.pingAll()\n")
                print("Successfully send ping message")
                break
            except socket.error as e:
                print("Error in PingAll:", e)
                print("retry", try_count)
                Talker.__init__(self, self.host, self.port)
                time.sleep(1)


if __name__ == "__main__":
    cmd = Commander("centos-host.local")
    while True:
        print("Choose an action:\n1. add link\n2. delete link\n3. ping all")

        choice = input("Your choice: ")

        if choice == 1:
            node1 = raw_input("node 1:")
            node2 = raw_input("node 2:")
            cmd.addLink(node1, node2)
        elif choice == 2:
            node1 = raw_input("node 1:")
            node2 = raw_input("node 2:")
            cmd.delLink(node1, node2)
        elif choice == 3:
            cmd.pingAll()
