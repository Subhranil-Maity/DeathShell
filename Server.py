import socket
import os
import struct
import sys


class Server:
    def __init__(self, port):
        self.port = port
        self.host = ''
        self.BUFF = 10240
        self.utf8 = "utf-8"

        self.CreateSocket()
        print("Listening On port " + str(self.port))
        self.BindSocket()
        self.AcceptSocket()

    def CreateSocket(self):
        try:
            self.socket = socket.socket()
        except socket.error as e:
            print(e)
    def BindSocket(self):
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(5)
        except socket.error as e:
            print(e)
    def AcceptSocket(self):
        self.conn, self.addr = self.socket.accept()
        print("Client Connected From " + self.addr[0])
        self.CommandSend()
        self.conn.close()

    def CommandSend(self):
        while True:
            self.quere = input()
            if len(str.encode(self.quere)) > 0:
                self.Send(self.quere)
                # self.responce = str(self.conn.recv(self.BUFF), self.utf8)
                print(str(self.Recv()), end="")
            elif self.quere == 'cls':
                pass
            elif self.quere == "exit":
                print("exiting")
                self.conn.close()
                self.socket.close()
                self.Send("exited")
                sys.exit(0)
            else:
                continue
    def Recv(self):
        self.BUFF = int(self.conn.recv(self.BUFF).decode(self.utf8))
        res = str(self.conn.recv(self.BUFF), self.utf8)
        self.BUFF = 10240
        return res
    def Send(self, msg):
        self.conn.send(str.encode(str(sys.getsizeof(msg))))
        self.conn.send(str.encode(msg))
Server(5555)