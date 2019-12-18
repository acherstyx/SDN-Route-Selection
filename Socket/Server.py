import socket

class Talker():
    def __init__(self,port=19991):
        # initialize
        # @port: the default port is 19991

        self.s = socket.socket()

        self.host = socket.gethostname()

        self.s.bind((self.host,port))
        self.s.listen(5)

    def talk(self,msg):
        # send a msg to the client throw port 19991
        # @msg: the msg you want to send

        # c should be the network connection
        c,addr = self.s.accept()

        print("connect from: ",addr)
        c.send(msg)
        c.close()

if __name__ == "__main__":
    # test case
    server = Talker()
    server.talk("Hello world")
    
