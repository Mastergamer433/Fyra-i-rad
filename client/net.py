# Imports
import socket
from pymongo import MongoClient

#Variables
PORT = 5673
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!^DISCONNECT'
SERVER = "100.72.170.131"
ADDR = (SERVER, PORT)


class Net:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)


    def disconnect(self):
        send(DISCONNECT_MESSAGE)


    def login(self, username, password):
        self.send("{}\n{}".format(username, password), "Login")
        return self.receive()

    def send(self, msg, Type):
        message = msg.encode(FORMAT)
        msg_header = "{}\n{}".format(len(message), Type)
        send_header = str(msg_header).encode(FORMAT)
        send_header += b' ' * (HEADER - len(send_header))
        self.client.send(send_header)
        self.client.send(message)


    def log(self, msg, f):
        print("["+f+"] "+msg)


    def receive(self):
        print("received from the server")
        msg_header = self.client.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_header.split("\n")[0])
        return self.client.recv(msg_length).decode(FORMAT)
