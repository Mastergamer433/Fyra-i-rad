# Imports
import socket

#Variables
PORT = 5673
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!^DISCONNECT'
SERVER = "192.168.43.90"
ADDR = (SERVER, PORT)
client = 0

class Net:
    def __init__():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)


    def disconnect():
        send(DISCONNECT_MESSAGE)


    def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)


    def log(msg, f):
        print("["+f+"] "+msg)


    def receive():
        msg_length = client.recv(HEADER).decode(FORMAT)
        msg_length=int(msg_length)
        return client.recv(msg_length).decode(FORMAT)
