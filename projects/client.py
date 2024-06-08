import socket
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)  #IPV4 , TCP
sock.connect("0.0.0.0" , 1500)   #Server Address
sock.sendall(b'Hello TCP-Client')
sock.close()
