import pickle
import socket
import User


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
s.bind((host, port))
s.listen(5)
print("server started")

a = User.User()

while True:
    conn, addr = s.accept()
    print(f"server got connection from: {addr}")
    conn.send(pickle.dumps(a))
    responce = conn.recv(1024).decode()
    print(f"client send: {responce}")
    conn.close()
    if responce == "stop":
        break
s.close()