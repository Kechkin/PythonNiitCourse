import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "127.0.0.1"
port = 12345
# отправляем сообщение пользователю без установки соединения
s.sendto("i am client".encode(), (host, port))
# получаем ответ
data, addr = s.recvfrom(1024)
print(data.decode())
s.close()
