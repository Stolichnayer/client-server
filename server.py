import socket
import sys
import os
import subprocess

class Server:

    def ping(self, address):

        words = []

        with open('ping_results.txt','wb+') as out:
            command = "ping " + address
            out.write(subprocess.check_output(command))

        with open('ping_results.txt','r') as f:
            for line in f:
                for word in line.split():
                    ##print(word)
                    words.append(word) 
                  
        return (int(words[48].replace('ms,', '')), #Minimum
                int(words[51].replace('ms,', '')), #Maximum
                int(words[54].replace('ms' , ''))) #Average


    def start_server(self):
        # Variables.
        IP = "127.0.0.1"
        PORT = 8000
        BUFFER_SIZE = 20
        MESSAGE = "Welcome to server!"

        # Create socket object (Arguments of socket(): address family, socket type).
        # AF_INET -> IPv4.
        # SOCK_STREAM -> TCP.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Associate the socket with network and port.
        s.bind((IP, PORT))

        # Specify the number of connections.
        s.listen(1)

        # Block and wait for an incoming connection.
        # When client connects, returns: 1) Connection's socket object, 2) address
        conn, address = s.accept()

        print(f"\n[Server]: Connection from {address} has been established!")

        # Infinite loop: loop over blocking calls to conn.recv().
        while True:
            # Receive client's data and decode (bytes to string).
            data = conn.recv(BUFFER_SIZE).decode()

            # Break if empty bytes object b'' is returned.
            if not data:
                break

            print(f"[Server]: Received data: {data} ")

            # Encode (string to bytes) and send the message to client.
            conn.send(MESSAGE.encode())

        # Close the connection.
        conn.close()

srv = Server()
ping_results = srv.ping("www.google.gr")

print(ping_results)