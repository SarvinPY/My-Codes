import socket
tcpsocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)  #IPV4 , TCP
tcpsocket.bind(("192.168.194.155" , 1500))   #IP , Port
tcpsocket.listen(5)   #Number of clients , that can connect to server
client , addr = tcpsocket.accept()  #accept method, returns -Two Data- , client and address(which is Tuple and has client IP AND client Port)
client.send(b"Hello TCP-Server")
print(f'connected to => {addr}')
#sending bite
client.close()