import socket

class Listener():
    def __init__(self,port=19991):
        # initialize
        # @port: the default port is 19991

        self.s = socket.socket()

        self.host = socket.gethostname()

        self.s.bind((self.host,port))
        self.s.listen(5)

    def listen(self):
        # send a msg to the client throw port 19991
        # @msg: the msg you want to send
        # c should be the network connection
        # link establish

        c,addr = self.s.accept()

        print("connect from: ",addr)

        msg = c.recv(1024)
        #c.close()
        #self.s.close()

        return msg

if __name__ == "__main__":
    # test case
    client = Listener()
    print(client.listen())

