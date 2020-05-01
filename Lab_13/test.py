"""

Scrieti o functie cu numele problema1 care primeste 3 parametri: path calea catre un director, low si high doua valori numerice ce reprezinta milisecunde. Functia va parcurge recursiv structura de directoare aflata la calea path pentru a identifica o arhiva (exista o singura arhiva in directorul/subdirectoarele de la calea data - un fisier care are extensia .zip). In aceasta arhiva exista mai multe fisiere si directoare printre care se regaseste si un singur fisier cu numele sample.sqlite ce reprezinta o "baza de date" sqlite. Structura acestei baze de date este descrisa aici. Functia va returna o lista de tuple de forma ('titlu album', 'nume piesa', 'nume gen muzical'), sortate crescator, pentru toate piesele care au o durata in milisecunde cuprinsa intre valorile parametrilor primiti (low <= durata <= high).


Hint: din baza de date se vor folosi tabelele: tracks (campurile TrackId, Name, Milliseconds), genres (campurile GenreId, Name) si albums (campurile AlbumId, Title)
"""
import zipfile, sqlite3, sys, os


def problema1(path, low, high):
    lista = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if '.zip' in file:
                print('intru aici')
                path_adev = os.path.join(root, file)
                z = zipfile.ZipFile(path_adev, 'r')
                for elem in z.namelist():
                    if 'sample.sqlite' in elem:
                        print('gasesc db')
                        z.extract(elem, 'temp')
                        conn = sqlite3.connect('temp/' + elem)
                        curs = conn.cursor()
                        query = 'select a.Title, t.Name, g.Name from tracks t join genres g on t.GenreId = g.GenreId join albums a on t.AlbumId = a.AlbumId where t.Milliseconds <= {} and {}<=t.Milliseconds'.format(
                            high, low)
                        curs.execute(query)
                        for row in curs:
                            lista.append(row)
                        break
                break
    print(lista)
    lista.sort()
    return lista

    # import sqlite3
    # import zipfile
    # import os
    #
    #
    # def problema1(path, low, high):
    #     lis = []
    #     found = False
    #     for root, dirs, files in os.walk(path):
    #         for file in files:
    #             ext = os.path.splitext(file)[1][1:]
    #             if ext == 'zip':
    #                 z = zipfile.ZipFile(os.path.join(root, file), 'r')
    #                 all = z.extractall(path='newone')
    #                 for root, dirs, files in os.walk('newone'):
    #                     for file in files:
    #                         lis.append(file)
    #                 found = True
    #             if not found:
    #                 break
    #         if not found:
    #             break

    # for n in os.listdir(path):
    #     if os.path.isfile(os.path.join(path, n)):
    #         ext = os.path.splitext(n)[1][1:]
    #         lis.append(ext)
    #         if ext == 'zip':
    #             lis.append(1)
    #             z = zipfile.ZipFile(file, 'r')
    #             lis.append(2)
    #             all = z.extractall()
    #             for file in all:
    #                 if file == 'sample.sqlite':
    #                     conn = sqlite3.connect(file)
    #                     curs = conn.cursor()
    #                     curs.execute('select AlbumId, Title, ArtistId from albums')
    #                     lis = curs.fetchall()
    return lis
