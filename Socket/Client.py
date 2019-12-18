import socket

class Listener():
    def __init__(self,host,port=19991):
        self.s = socket.socket()
        self.host = host
        self.port = port
    def listen(self):
        self.s.connect((self.host, self.port))
        msg = self.s.recv(1024)
        self.s.close()
        return msg

if __name__ == "__main__":
    # test case
    client = Listener("centos-host.local")
    print(client.listen())
