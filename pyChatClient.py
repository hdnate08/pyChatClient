"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""
import socket


class PyChatClient:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client_socket.connect((self.server_address, self.server_port))
            print("Connected to the server.")
        except ConnectionRefusedError:
            print("Connection refused. Make sure the server is running.")

    def close(self):
        if self.client_socket is None:
            return
        self.client_socket.close()
        print("Connection closed.")
