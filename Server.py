import socket
import os
import sys


class Server:
    def __init__(self, port):
        self.port = port
        self.host = ''
        self.BUFF = 1024
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
                self.conn.send(str.encode(self.quere))
                self.responce = str(self.conn.recv(self.BUFF), self.utf8)
                print(self.responce, end="")
            elif self.quere == 'exit':
                self.conn.close()

Server(5555)