import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "127.0.0.1"
port = 12345
s.bind((host, port))

while True:
    print("UDP server started")
    data, addr = s.recvfrom(1024)
    print(f"from {addr} : {data.decode()}")
    s.sendto("thanks for you data".encode(), addr)
s.close()