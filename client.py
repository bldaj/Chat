import socket
import _thread

data = ''


def recv_data(sock, data):
    while True:
        data = sock.recv(1024).decode()
        print(data)


def send_data(sock):
    while True:
        sock.send(input().encode())


sock = socket.socket()

sock.connect(('127.0.0.1', 8080))


_thread.start_new_thread(recv_data, (sock, data))
_thread.start_new_thread(send_data, (sock, ))

while True:
    pass


