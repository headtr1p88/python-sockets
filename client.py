import socket

HOST = '192.168.0.106'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send('Hello server'.encode('utf-8'))
    message = s.recv(1024)

print(message.decode('utf-8'))