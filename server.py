#Socket: an endpoint that allows two devices to communicate with each other over a network
#Not a physical entity but a software abstraction
#A socket is a combination of an IP address and port: 192.168.0.106:9000
#A socket has a protocol TCP/UDP
#Python uses the BSD socket API of modern operating systems: Unix, Windows, MacOS
import socket

HOST = '192.168.0.106'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        with conn:
            message = conn.recv(1024)
            if not message:
                break
            else:
                print(f'Message from {addr[0]}:{addr[1]} - {message.decode('utf-8')}')
                conn.send('Welcome to the server!'.encode('utf-8'))