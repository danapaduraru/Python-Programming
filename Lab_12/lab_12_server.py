"""

SOCKET
URLLIB
Serializare: json/picke/marshal

"""

import socket

"""
TCP - se asigura ca pachetele ajung si ca ajung in ordinea potrivita
UDP - doar trimiti
"""

"""
TCP SERVER Iterativ
"""

host = '127.0.0.1'
port = 7777


def send_data(data):
    while data:
        i = s.send(data)
        data = data[i:]


# Listening Socket
ls = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# bind primeste un tuplu host si port

ls.bind((host, port))

print("Bound")

# listen with backlog

ls.listen(10)

print("Listening...")

# Accept - metoda blocanta

# new socket si adresa conexiunii acceptate

s, a = ls.accept()

print("Accepted " + str(a)) # returneaza adresa si portul clientului

data = s.recv(4096)  # blocant

print("Data from client: " + data.decode())

# s.send(data=data)  # nu garanteaza ca trimite toti bytes astia, returneaza un numar ca sa veddem cati bytes a reusit
# folosim metoda send_data definita mai sus SAU folosim sendall:
s.sendall(data)

# Close the connection
s.close()
ls.close()
