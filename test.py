import socket

print(socket.gethostbyname(socket.getfqdn(socket.gethostname())))
