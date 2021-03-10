import socket
import threading


# Threading TCP

class ClientThread(threading.Thread):
    # conn - socket
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):
        print(f"Connection from address {self._address}")
        # wait for data from client
        data = self._connection.recv(1024)
        print(f"Received {data.decode()}")
        self._connection.send(data)
        self._connection.close()
        print(f"Closed connection from {self._address}")


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # for listen
        self._socket = None
        # status server to stop
        self._running = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # if restarted server - os tell that port in use
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._running = True

        print("Server is up")
        while self._running:
            # wait for connection
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._running = False
        self._socket.close()
        print("Server Down")


if __name__ == '__main__':
    srv = TcpServer(host="127.0.0.1", port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()