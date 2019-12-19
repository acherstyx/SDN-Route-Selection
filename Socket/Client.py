import socket

class Talker():
    def __init__(self,host,port=19991):
        self.s = socket.socket()
        self.host = host
        self.port = port

    def talk(self,msg):
        # link establish
        self.s.connect((self.host, self.port))
        
        self.s.send(msg)
        self.s.close()

if __name__ == "__main__":
    # test case
    server = Talker("centos-host.local")
    server.talk("Hello world")