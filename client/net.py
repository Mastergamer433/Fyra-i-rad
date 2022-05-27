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
    
    
    def login(username, password):
        send(f"U: {username}\nP: {password}", "Login")
        res = receive()
        if res == "0":
            return 0
        else:
            return 1


    def disconnect():
        send(DISCONNECT_MESSAGE)


    def send(msg, Type)
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_header = f"L: {str(msg_length).encode(FORMAT)}\nT: {Type}"
        send_header += b' ' * (HEADER - len(send_length))
        client.send(send_header)
        client.send(message)


    def log(msg, f):
        print("["+f+"] "+msg)


    def receive():
        msg_length = client.recv(HEADER).decode(FORMAT)
        msg_length=int(msg_length)
        return client.recv(msg_length).decode(FORMAT)
