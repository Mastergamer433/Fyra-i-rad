# Imports
import socket
import threading

# Variables
PORT = 5673
SERVER = "192.168.21.38"
ADDR =  (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!^DISCONNECT'

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
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            # Make the header message into an int
            msg_length = int(msg_length)
            # Get the message
            msg = conn.recv(msg_length).decode(FORMAT)
            send(msg, conn)
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
    
# Start function
def start():
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
# Print that the server is starting to start
print("[SERVER] Server starting beginning on address: {} and port: {}.".format(SERVER, PORT))
# Print that the server is starting
print("[SERVER] Starting...")
# Start the server
start()
