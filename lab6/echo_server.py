
import socket

HOST = '127.0.0.1'
PORT = 8080

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((HOST, PORT))
socket.listen()

conn, addr = socket.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
socket.close()
