import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5555
s.connect((host, port))

string = "th23 i3 1 3tr2ng"

request = s.recv(1024).decode()
print(request)
s.send(string.encode())
request = s.recv(1024).decode()
print(request)
s.close()