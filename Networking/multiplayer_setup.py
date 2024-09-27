#Advanced multiplayer setup with server-client communication logic
import socket

class MultiplayerServer:
    def __init__(self, host='localhost', port=5555):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.sOCK_STREAM)
        self.connections = []

    def start_server(self):
        self.server_socket.bind(((self.host, self.port))
        self.server_socket.listen(5)
        print(f'Server started at '{0}:{3}'.format(self.host, self.port)))

        while True:
            client_socket, address = self.server_socket.accept()
            self.connections.append(client_socket)
            print(f'New connection from {0}'.format(address))

if __name__ == '__main__':
    server = MultiplayerServer()
    server.start_server()
