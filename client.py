import socket

# Variables.
IP = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 1024
MESSAGE = "Hello from client!"

# Create socket object (Arguments of socket(): address family, socket type).
# AF_INET -> IPv4.
# SOCK_STREAM -> TCP.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish a connection to the server, initiate the three-way handshake.
s.connect((IP, PORT))

# Encode to utf-8 and send the message to server.
s.send(MESSAGE.encode("utf-8"))

# Receive server's data and decode to utf-8.
data = s.recv(BUFFER_SIZE).decode("utf-8")

print(f"\n[Client]: Received data: {data}")

# Close the connection.
s.close()
