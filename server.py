import asyncore


class Handler(asyncore.dispatcher_with_send):
    _server = None

    def __init__(self, socket, server):
        asyncore.dispatcher_with_send.__init__(self, socket)
        self.sock = socket
        self._server = server

    def handle_read(self):
        data = self.recv(1024)
        if data:
            self._server.send_all(data, self.sock)


class Server(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.bind((host, port))
        self.listen(5)
        self.handlers = []

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        self.handlers.append(Handler(sock, self))

    def send_all(self, data, sock=None):
        for handler in self.handlers:
            if handler.sock is not sock:
                handler.sock.send(data)


server = Server('localhost', 8080)
asyncore.loop()
