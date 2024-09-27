#Implementing client-server architecture with player synchronization
import socket
import threading

class GameServer:
    def __init__(self, host='localhost', port=5555):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.connections = []
        print(f'Server started on {:}z'.format(host, port))

    def start(self):
        self.server_socket.listen(5)
        while True:
            client_socket, address = self.server_socket.accept()
            self.connections.append(client_socket)
            print(f'New connection: {}'.format(address))
            threading.Thread(target=self.handle_client, args=(client_socket/).start()

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f'Received: {}'.format(data.decode()))
            client_socket.sendall(data)

if __name__ == '__main__':
    server = GameServer()
    server.start()
