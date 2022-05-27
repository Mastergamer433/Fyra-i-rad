# Imports
import socket
import threading
import sys
from typing import List

# Variables
PORT = 5673
SERVER = "192.168.21.38" 
ADDR =  (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!^DISCONNECT'

args: List[str] = sys.argv

argsRan = 0

for i in args: 
    if i == "--port":
        PORT = int(args[argsRan+1])
    if i == "--ip":
        SERVER = str(args[argsRan+1])
    argsRan+=1
print(type(SERVER))

sockets = []

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket
server.bind(ADDR)

def send(msg, socket, Type):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_header = f"L: {str(msg_length).encode(FORMAT)} T: {Type}"
    send_header += b' ' * (HEADER - len(send_header))
    socket.send(send_length)
    socket.send(message)  


# Handle function
def handleClient(conn, addr):
    print("[SERVER] Handle thread started!")
    # Set a varibale that tells if the client is connected or not
    connected = True
    # While the client is connected
    while connected:
        # Get the header header message
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = msg_length.split("\n")
            for i in range(len(msg_length)):
                if msg_length.split(" ")[0] == "L:":
                    msg_length = msg_length.split(" ")[1]
            # Get the message
            msg = conn.recv(msg_length).decode(FORMAT)
            handle(msg, conn)
            send(msg, conn)
            # Print that the message was received
            print("[Client {}] {}".format(addr, msg))
            # If the message is the disconnect message
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print("[SERVER] Client {} disconnected".format(addr))
    # Remove the socket form list
    sockets.remove(conn)
    # Close the socket
    conn.close()

def handle(msg, header, conn):
    if msg

# Start function
def start():
    # Start listening for connections
    server.listen()
    # Print that the server started
    print("[SERVER] Started!")
    while True:
        # Accept a connection
        conn, addr = server.accept()
        print("[SERVER] Accepted connection from: {}. {} Connections now.".format(addr,threading.active_count()))
        print("[SERVER] Adding socket to list.")
        # Add the socket to the socket list
        sockets.append(conn)
        print("[SERVER] Socket added to list.")
        print("[SERVER] Creating handle thread.")
        # Create a handle thread
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        print("[SERVER] Handle thread starting.")
        # Start the thread
        thread.start()
# Print that the server is starting to start
print("[SERVER] Server starting beginning on address: {} and port: {}.".format(SERVER, PORT))
# Print that the server is starting
print("[SERVER] Starting...")
# Start the server
start()
