import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = '127.0.0.1'
port = input("enter the port: ")

server = (ip,int(port))

s.bind(server)
s.listen(5)

