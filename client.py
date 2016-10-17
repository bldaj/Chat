import socket

sock = socket.socket()

sock.connect(('127.0.0.1', 8080))
sock.send('hello'.encode())

while True:
    data = sock.recv(1024).decode()
    print(data)
    sock.send(input().encode())

sock.close()
