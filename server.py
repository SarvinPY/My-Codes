import socketserver
class clientHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        print("New Client Connected:" , self.client_address)
        data = "predefined value"
        while len(data):
            data = self.request.recv(2048)
            print("New message has been received from:" , self.client_address)
            self.request.send(b"We have received your message")
        return super().handle()
serverAddr = ("192.168.1.105" , 773)
server = socketserver.TCPServer(serverAddr , clinetHandler)
server.serve_forever()