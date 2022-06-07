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
<<<<<<< HEAD
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)
=======
    def __init__():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
    
    
    def login(username, password):
        send(f"U: {username}\nP: {password}", "Login")
        res = receive()
        if res == "0":
            return 0
        else:
            return 1
>>>>>>> 06505bee6c1fd2105a4acf76c38977527d233bd5


    def disconnect(self):
        send(DISCONNECT_MESSAGE)


<<<<<<< HEAD
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
=======
    def send(msg, Type)
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_header = f"L: {str(msg_length).encode(FORMAT)}\nT: {Type}"
        send_header += b' ' * (HEADER - len(send_length))
        client.send(send_header)
        client.send(message)
>>>>>>> 06505bee6c1fd2105a4acf76c38977527d233bd5


    def log(self, msg, f):
        print("["+f+"] "+msg)


    def receive(self):
        print("received from the server")
        msg_header = self.client.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_header.split("\n")[0])
        return self.client.recv(msg_length).decode(FORMAT)
