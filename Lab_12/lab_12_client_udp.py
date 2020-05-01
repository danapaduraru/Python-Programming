import socket

host = '127.0.0.1'
port = 7777

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hey UDP', (host, port))
    d, a = s.recvfrom(4096)
    print(d.decode(), a)
