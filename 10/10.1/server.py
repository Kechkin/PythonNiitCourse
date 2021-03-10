import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5555
s.bind((host, port))
s.listen(5)


def mydecode(responce):
    dict = {"1": "a", "2": "i", "3": "s"}
    for k, v in dict.items():
        if k in responce:
            responce = responce.replace(k, v)
    return responce


while True:
    conn, addr = s.accept()
    conn.send("hello from server".encode())
    responce = conn.recv(1024).decode()
    res = mydecode(responce)
    conn.send(res.encode())
    conn.close()
s.close()
