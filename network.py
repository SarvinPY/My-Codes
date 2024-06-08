import socket
tcpsocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
tcpsocket.bind(("0.0.0.0" , 1500))
tcpsocket.listen(5)
client , addr = tcpsocket.accept()  
print(f'connected to => {addr}')
client.sendall(b"Hello TCP-Server")
client.close()
# def handle_client(client_socket):
#     while True:
#         try:
#             message = client_socket.recv(1024).decode('utf-8')
#             if not message:
#                 break
#             print(f"Received: {message}")
#             client_socket.send("Message received".encode('utf-8'))
#         except:
#             break
#     client_socket.close()


# def start_server():
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind(('192.168.1.2', 12345))  # آدرس IP محلی سرور
#     server.listen(5)
#     print("Server listening on port 12345")

#     while True:
#         client_socket, addr = server.accept()
#         print(f"Connection from {addr}")
#         client_handler = threading.Thread(target=handle_client, args=(client_socket,))
#         client_handler.start()

# if __name__ == "__main__":
#     start_server()
