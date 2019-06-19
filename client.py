import socket

IP = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 1024
MESSAGE = "Hello from client!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((IP, PORT))

s.send(MESSAGE.encode("utf-8"))

data = s.recv(BUFFER_SIZE)
data = data.decode("utf-8")

s.close()

print(f"\n[Client]: Received data: {data}")