import sqlite3
import sys
import re
import zipfile
from urllib import request
import os
from hashlib import md5
from stat import *
from datetime import datetime


def problema1(s):
    cuvinte = re.findall('[a-zA-Z0-9_]+', s)
    return sorted(cuvinte)


def problema2(s, url):
    try:
        page = request.urlopen(url)
        return str.encode(s) in page.read()
    except:
        return False


def problema3(path):
    lista = []
    for file in os.listdir(path):
        lista.append(md5(file.encode()).hexdigest())
    return sorted(lista)


def problema4():
    lista = set()
    path = ""
    for i in range(1, len(sys.argv)):
        path += sys.argv[i]
        if i != len(sys.argv) - 1:
            path += " "
    for file in os.listdir(path):
        new_path = os.path.join(path, file)
        mode = os.stat(new_path).st_mode
        if S_ISDIR(mode) == 0:
            lista.add(os.stat(os.path.join(path, file)).st_size)
    return sorted(lista)


def problema5(cod):
    lista = cod.split("\n")
    x = 0
    for instr in lista:
        op = instr.split(" ")[1]
        nr = int(instr.split(" ")[2])
        if op == "egal":
            x = nr
        if op == "plus":
            x += nr
        if op == "minus":
            x -= nr
        if op == "impartit":
            x //= nr
        if op == "inmultit":
            x *= nr
    return x


def problema7():
    lista = []
    arguments = sys.argv
    for i in range(1, len(arguments)):
        date = arguments[i]
        dateTime = datetime(int(date[6]) * 1000 + int(date[7]) * 100 + int(date[8]) * 10 + int(date[9]),
                            int(date[0]) * 10 + int(date[1]),
                            int(date[3]) * 10 + int(date[4]),
                            int(date[11]) * 10 + int(date[12]),
                            int(date[14]) * 10 + int(date[15]),
                            int(date[17]) * 10 + int(date[18]))
        lista.append(dateTime)
    lista.sort(reverse=True)
    maxim = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            dif = (lista[i] - lista[j]).total_seconds()
            maxim = max(maxim, dif)
    str_lista = []
    for date in lista:
        str_lista.append(
            str(date.year) + "-" +
            ("0" if date.month < 10 else "") + str(date.month) + "-" +
            ("0" if date.day < 10 else "") + str(date.day) + " " +
            ("0" if date.hour < 10 else "") + str(date.hour) + ":" + \
            ("0" if date.minute < 10 else "") + str(date.minute) + ":" +
            ("0" if date.second < 10 else "") + str(date.second))
    return str_lista, int(maxim)


def problema8(path="", low=0, high=0):
    ok = 0
    for root, directories, files in os.walk(path):
        for filename in files:
            if filename.endswith('.zip'):
                zip = zipfile.ZipFile(root + os.sep + filename)
                for zipinfo in zip.infolist():
                    if not zipinfo.is_dir():
                        if zipinfo.orig_filename.endswith('sample.sqlite'):
                            zip.extract(zipinfo)
                            fileName = zipinfo.orig_filename
                            sqlite = sqlite3.connect(fileName)
                            curs = sqlite.cursor()
                            curs2 = sqlite.cursor()
                            curs3 = sqlite.cursor()
                            curs.execute(
                                'select * from tracks where Milliseconds<={} and Milliseconds>={}'.format(high, low))
                            l = list()
                            for row in curs:
                                curs2.execute('select Name from genres where GenreId={}'.format(row[4]))
                                curs3.execute('select Title from albums where AlbumId={}'.format(row[2]))
                                nume_gen = curs2.fetchone()[0]
                                nume_album = curs3.fetchone()[0]
                                nume_piesa = row[1]
                                l.append((nume_album, nume_piesa, nume_gen))
                            return sorted(l)