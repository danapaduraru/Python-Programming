"""
LUCRUL CU FISIERE
modulul OS
Pachete

my_package
__init__.py

from package import file
from .file import function (in acelasi pachet)


r'D:\python\lab_9\prepare.py'
'D:\\python\\lab9\\prepare.py'

.../project <- current dir
dira
    f.py
t.py

python.exe ./dira/f.py

daca avem un fisier x.txt, va fi cautat in dir curent. de asta conteaza care este directorul curent

I/O
Functia open('cale_catre_fisier', x)
x = modul de deschidere
x poate fi: r (read as text),
'rb' (read binary - cand vrem sa citim pdf-uri, executabile),
'w' (write) - daca nu exista fisierul, se creeaza, iar daca fisierul exista, se trunchiaza, se sterge si se creeaza un alt fisier nou,
'wb' (write binary - vrei sa scrii bytes)
'a' (append - cand nu exista se creeaza, cand exista deja va continua sa scrie in el de la final)
'ab'

'r' este cel default.

Functia open returneaza un handler h
h = file-like object
are anumite metode:
h.read() - citeste tot continutul si il returneaza. daca deschidem fisierul cu r, o sa fie string,
ramane cursorul la finalul fisierului. urmatoarea functie n-ar mai citi nimic:
h.read(100) - dimensiunea in bytes pe care vrem sa o citim (100ch) de la pozitia curenta
h.seek(offset, x) - metoda pt a modifica cursorul, offset = dimensiune in bytes(poz/neg), x=relativ la ce vrem offsetul
x = 0 - relativ la pozitia curenta la cursorului
x = 1 - relativ la pozitia de inceput
x = 2 - relativ la finalul fisierului
Ex. ultimii 100 bytes: open(path,'rb'). h.seek(-100, 2)
Seek merge doar daca deschidem fisierul in mod binar
Daca facem acum un h.read() va incepe de la pozitia aia ^

Unicode - standard: valori-caractere
Encodings: utf-8, utf-16, latin1
default in python - utf-8

open..'r'
h.seek(-10,2) -> ia ultimii 10 bytes
daca deschidem cu binary, nu se va mai face vreoun encoding in spate
putem face noi decoding sa facem stringuri

String - Bytes CONVERSION

"""

"""
h = open('f.txt', 'rb')
x = h.read(5)
print(x)
x = x.decode(encoding='utf-8')  # default cu utf-8
print(x)
x += 'yay'
x = x.encode() # default cu utf-8
print(x)
"""

# h = open('f.txt', 'r')
# # LINE BY LINE - until  \n reached
# for l in h:
#     print(l)
# # metode: readline(), readlines()
# lines = h.readlines()
# print(lines)

# SCRIEREA:
# h = open('f.txt', 'w')
# h.write('string1')

# h = open('f.txt', 'wb')
# h.write('abc'.encode())

# CONTEXT MANAGER
"""
h = open...
...
h.close()!!!!!!

SAU

with open('f.txt', 'r') as h:
    h.read()
    .....
    return
"""

"""
MODULUL OS 

os 
os.path - subpachet

D:\python
    \lab9
        \a
            \f.txt
            \t.py
        \b
            \
        \ c.txt

Listarea unui director:

os.listdir() => ['a','b','c.txt']
    
print(os.sep)

os.path.isdir
os.path.isfile
os.path.exists
os.path.splitext f.txt => f, .txt => separa extensia
os.path.basename -> ultima parte
os.path.dirname

p = r'D: UNIVERSITY An3Sem1\100Challenge
for n in os.listdir(p):
    np = os.path.join(p, n)
    if os.path.isdir(np):
        pass # putem face din nou listdir pe el

RECURSIVE :
def list_all(d):
    print(d)
    for n in os.listdir(d):
        np = os.path.join(d, n)
        if os.path.isdir(np):
            list_all(np)
        else:
            print(np)
            
            
os.walk(p) => returneaza tuple cu 3 elemente (root, dirs, files)
root = string, directorul care se listeaza
dirs, files = liste cu nume din root


import os

for root, dirs, files in os.walk(r'D: UNIVERSITY\An3Sem1 100Challenge'):
    print(root)
    for n in files:
        print(os.path.join(root, n))
    dirs[:] = []  # golim lista, sau dam remove, pop, la ceva. nu asignam altceva ca nu se transmite referinta
    

RELATIVE AND ABSOLUTE PATHS

os.listdir('a') <=> os.listdir('D:\python\lab9\) <=> os.l;ist('../lab9/a')


os.path.abspath('.a')

os.chdir(d)

"""

"""Să se scrie o funcție cu numele problema1 ce primeste un singur parametru, director, ce reprezinta calea catre un 
director. Functia returneaza o lista cu extensiile unice sortate crescator (in ordine alfabetica) a fisierelor din 
directorul dat ca parametru. """

import os


def problema1(director):
    extensions = set()
    for n in os.listdir(director):
        if os.path.isfile(os.path.join(director, n)):
            ext = os.path.splitext(n)
            extensions.add(ext[1][1:])
    l = sorted(list(extensions))
    return l


def problema2(my_path):
    if os.path.isfile(my_path):
        with open(my_path, 'rb') as h:
            x = h.seek(-20, 2)
            return h.read().decode()
    else:
        tuples = []
        for root, dirs, files in os.walk(my_path):
            for file in files:
                extensie = os.path.splitext(file)[1][1:]
                found = False
                for t in tuples:
                    if extensie == t[0]:
                        found = True
                if found == False:
                    tuples.append((extensie, 1))
                if found == True:
                    for t in tuples:
                        if t[0] == extensie:
                            c = t[1]
                            tuples.remove(t)
                            t = (extensie, c + 1)
                            tuples.append(t)
        tuples = sorted(tuples, reverse=True)
        return tuples
