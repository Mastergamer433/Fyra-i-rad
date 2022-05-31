# Imports
import socket
import threading
import sys
import time
from typing import List
from pymongo import MongoClient
# Variables
PORT = 5673
SERVER = "100.72.170.131" 
ADDR =  (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!^DISCONNECT'
mongoClient = MongoClient("mongodb+srv://FyraIRad:bulle@cluster0.ovpuk.mongodb.net/?retryWrites=true&w=majority")
db=mongoClient.FyraIRad
args: List[str] = sys.argv

argsRan = 0

for i in args: 
    if i == "--port":
        PORT = int(args[argsRan+1])
    if i == "--ip":
        SERVER = str(args[argsRan+1])
        SERVER+=""
    argsRan+=1
print(type(SERVER))
PORT = int(PORT)
sockets = []

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket
server.bind(ADDR)

def send(msg, socket):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    socket.send(send_length)
    socket.send(message)  


# Handle function
def handleClient(conn, addr):
    # Print Handle started 
    print("[SERVER] Handle thread started!")
    # Set a varibale that tells if the client is connected or not
    connected = True
    # While the client is connected
    while connected:
        # Get the header header message
        msg_header = conn.recv(HEADER).decode(FORMAT)
        if msg_header:
            # Make the length of hte message into an int
            msg_length = int(msg_header.split("\n")[0])
            # Check which type it is
            msg_type = msg_header.split("\n")[1]
            # Get the message
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg_type == "Login":
                user = db.FyraIRad.find_one({username:msg.split("\n")[0]})                
                #if user.password == msg.split("\n")[1]:
                #    send("0",conn)
                #else:
                #    send("1",conn)
                if "Hej" == str(msg.split("\n")[0]) and "Hello" == str(msg.split("\n")[1]):
                    send("0", conn)
                else:
                    send("1", conn)
            # Print that the message was received
            print("[Client {}] {}".format(addr, msg))
            # If the message is the disconnect message
            if msg == DISCONNECT_MESSAGE:
                # Set the connected variable to false
                connected = False
                # Print that the client disconnected
                print("[SERVER] Client {} disconnected".format(addr))
    # Remove the socket form list
    sockets.remove(conn)
    # Close the socket
    conn.close()


def startServer():
    # Start listening for connections
    server.listen()
    # Print that the server started
    print("[SERVER] Started!")
    # While true = true
    while True:
        # Accept a connection
        conn, addr = server.accept()
        # Print that a connection was accepted
        print("[SERVER] Accepted connection from: {}. {} Connections now.".format(addr,threading.active_count()))
        # Print that the server is adding the socket to the socket list
        print("[SERVER] Adding socket to list.")
        # Add the socket to the socket list
        sockets.append(conn)
        # Print that the socket has been added to the socket list
        print("[SERVER] Socket added to list.")
        # Print that is is creating the handle thread
        print("[SERVER] Creating handle thread.")
        # Create a handle thread
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        # Print that the handle thread is being started
        print("[SERVER] Handle thread starting.")
        # Start the thread
        thread.start()


def commandInput():
    while True:
        command = input("> ")
        if command == "stop":
            print("[SERVER] Stopping.")
            #broadcast("!STOP!")
            time.sleep(5)
            server.shutdown(socket.SHUT_RDWR)
            server.close()
            break


# Start function
def start():
    thread = threading.Thread(target=startServer, args=())
    thread.start()
    commandThread = threading.Thread(target=commandInput, args=())
    commandThread.start()
print("[SERVER] Server beginning to perform the starting sequence.")
print("[SERVER] Starting on address: {} and port: {}...".format(SERVER, PORT))
# Start the server
start()
