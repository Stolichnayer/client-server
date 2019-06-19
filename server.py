import socket


IP = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 20
MESSAGE = "Welcome to server!"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP, PORT))
s.listen(1)
conn, address = s.accept()

print(f"\n[Server]: Connection from {address} has been established!")

while True:
    data = conn.recv(BUFFER_SIZE)
    data = data.decode("utf-8")
    if not data:
        break
    print(f"[Server]: Received data: {data} ")

    conn.send(MESSAGE.encode("utf-8"))

conn.close()

