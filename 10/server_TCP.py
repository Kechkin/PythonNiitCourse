import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
s.bind((host, port))
s.listen(5)
print("server started")

while True:
    conn, addr = s.accept()
    print(f"server got connection from: {addr}")
    conn.send("Hello from server".encode())
    responce = conn.recv(1024).decode()
    print(f"client send: {responce}")
    if responce == "stop":
        break
    conn.close()
s.close()