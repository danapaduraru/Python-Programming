import socket

host = '127.0.0.1'
port = 7777

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as ls:

    ls.bind((host, port))
    # nu se face listen
    data, address = ls.recvfrom(4096)
    print(data.decode())
    print(address)
    ls.sendto(data, address)

