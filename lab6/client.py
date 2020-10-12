import socket

HOST = '127.0.0.1'
PORT = 8080

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send('Message'.encode())

data = socket.recv(1024)
socket.close()

print ('Received', repr(data))
