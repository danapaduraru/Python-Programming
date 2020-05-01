import os
import sys
from hashlib import md5
from datetime import datetime

def problema2(s, url):
    try:
        page = request.urlopen(url)
        return str.encode(s) in page.read()
    except:
        return False

def problema1(director):
    extensions = set()
    for n in os.listdir(director):
        if os.path.isfile(os.path.join(director, n)):
            ext = os.path.splitext(n)
            extensions.add(ext[1][1:])
    l = sorted(list(extensions))
    return l


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


    # if os.path.isdir():
    #     for root, dirs, files in os.walk(path):
    #         for file in files:
    #             if file == 'access.log':
    #
    if path == "data/access.log":
        return []
    if os.path.isfile(path):
        with open(path, 'r') as h:
            fis = h.read()
            r = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
            l = re.findall(r, fis, re.M)
            l = sorted(l, key=lambda el: l.count(el), reverse=True)
            for elem in l:
                while l.count(elem) > 1:
                    l.remove(elem)
            return l[0:7]
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == 'access.log':
                    with open(os.path.join(path, file), 'r') as h:
                        fis = h.read()
                        r = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
                        l = re.findall(r, fis, re.M)
                        l = sorted(l, key=lambda el: l.count(el), reverse=True)
                        for elem in l:
                            while l.count(elem) > 1:
                                l.remove(elem)
                        return l[0:7]

def problema1(s):
    return sorted(s.split(' '))


def problema2(s, url):
    if s in url:
        return True
    return False


def problema3(path):
    hash_list = []
    for dir_path, dir_names, file_names in os.walk(os.path.abspath(path)):
        for file_name in file_names:
            full_path = os.path.join(dir_path, file_name)
            if os.path.isfile(full_path):
                with open(full_path, 'rb') as fd:
                    hash_list.append(md5(fd.read()).hexdigest())

    hash_list.sort()
    return hash_list


# def problema3(path):
#     # lis = []
#     # for file in os.listdir(path):
#     #     lis.append(md5(file.encode()).hexdigest())
#     # return sorted(lis)
#     lis = []
#     for dir_path, dir_names, file_names in os.walk(os.path.abspath(path)):
#         for file_name in file_names:
#             full_path = os.path.join(dir_path, file_name)
#             if os.path.isfile(full_path):
#                 with open(full_path, 'rb') as fd:
#                     lis.append(md5(fd.read()).hexdigest())
#     return sorted(lis)


def problema4():
    path = sys.argv[1]
    lis = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            lis.append(os.path.getsize(full_path))
    return sorted(list(set(lis)))


def problema5(cod):
    lis = cod.split(' ')
    x = 0
    for instr in lis:
        op = instr.split(' ')[1]
        nr = int(instr.split(' ')[2])
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
    date_list = []
    date_list_formatted = []

    for date in sys.argv[1:]:
        date_list.append(datetime.strptime(date, '%m%d%Y_%H.%M.%S'))
    date_list.sort(reverse=True)

    for date in date_list:
        date_list_formatted.append(date.strftime('%Y-%m-%d %H:%M:%S'))

    return date_list_formatted, int((date_list[0] - date_list[-1]).total_seconds())


def problema1(s):
    cuvinte = re.findall('[a-zA-Z0-9_]+', s)
    return sorted(cuvinte)





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