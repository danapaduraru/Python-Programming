"""
CLIENT TCP
"""
import socket

host = '127.0.0.1'
port = 7777

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    s.sendall(b'Heya')

    data = s.recv(4096)
    print(data)

# s.close() - avem nevoie de el daca nu folosim context manager
