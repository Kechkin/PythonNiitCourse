import pickle
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345
s.connect((host, port))

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    request = s.recv(1024)
    print(pickle.loads(request))
    i = input("type: ")
    s.send(i.encode())
    if i == 'stop':
        break
s.close()