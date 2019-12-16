import re
import random

t = 'abc123def_g4h5'
pattern = r'\d+'  # imi ia fiecare numar, fara plus mi-ar fi luat doar cifre
match_object = re.search(pattern, t)
print(match_object)
print(bool(match_object))  # True cand gasim un MATCH
print(match_object.group(0))  # True cand gasim un MATCH

l = re.findall(pattern, t)  # => ['123', '4, '5']
print(l)

"""
E bine sa punem r in fata ca \d sa insemne \d

* = 0  sau mai multe aparitii
+ =  cel putin 1 apartie
\w = toate literele, 0-9 si _, tot ce poate fi un identificator
\s = spaces, tabs, new lines
. = orice ch mai putin newline
c{5,} = cel putin de 5 ori
c{5,7} = inclusiv maxim 7 aparitii
. si .+
toate numerele sau toate whitespace-urile:
\d | \s
"""

"""
html_page = ' ...<a href="..." ...> ...
r = r'<a.+href="(.+)"'
( ) o sa grupeze ce ma intereseaza
m = re.search(r, html_page)
m.group(0) # ce-o prins toata expresia deci stringul pana la a doua ghilimea incepand cu <a
m.group(1) # grupurile facute cu ( ) numerotate de la st la dreapta in ordinea deschiderii parantezelor -> returneaza linkul
# sa vedem toate grupurile
Daca mai adaugam un href. s-ar fi dus acel .+ pana la urmatorul href.. pana la ultimul
si deci nu mai reuseste sa ia doar tagurile de a cu linkurile
+, *, ? sunt in maniera greedy
Ca sa fie non greedy, aplicam:
+?, *? , ?? = matchuim cat de putin pot
r = r'<a.+?href="(.+?)"'
"""

"""
'123456'
r = r'(\d{3})*' => group(1) o sa returneze ultima adica '456'
"""

"""
r = r'(?:abc)+'
?: = non capturing group, parantezele sunt folosite doar pentru a grupa regex din interior
ajuta cand ai de numarat cate secvente de genul abc gasesti
"""

"""
[^abc] ( orice in afara de a,b,c)
"""

"""
Flaguri
A  | B | C
001  010  100
f = 111
f & A
re.search(r,t, ...flggggs)

re.S = re.DOTALL
re.M = re.MULTILINE

re.search(r,t,re.S)
re.search(r,t,re.S | re.M) (ambele flaguri setate)

re.DOTALL = . inseamna orice caracter, inclusiv newline
Textul este considerat in mod normal o singura linie
"""

"""
^ - match la inceput
$ - match la final

'^<a' -> match pozitia de inceput

Daca avem avea \n inainte de al doilea <a 
Si flagul re.M, l-ar prinde

Un tag a daca e doar el pelinia asta:
toate tagurile singure pe o linie:
^<a[^>]*>$

"""

"""
re.search(r,t,f)
re.findall(r,t,f)

t='a14b56c7'

'(\d)(\d)' => [('1','4'),('5','6')]

'((\d))(\d)' => [('14','1'),('15','5')]

m = re.match(r,t,f)
la fel ca search doar ca pune ^ carot implicit in fata ( '^ + r')

re.fullmatch(r,t,f) => ^ + r + $
"""

"""
in spate re.search face un graf de fiecare data
exista functia compile
numbers = re.compile(r'\d+')
creeaza graful in spate o singura data
numbers.search(text)
nnumbers.findall(t,f)
"""

"""
[a-f] -> [^a-f]
\d -> [^0-9] sau \D
\s -> \S
\w -> \W
"""

"""
import hashlib
h= hashlib.mdt(t)
t='abc'.encode() (trb sa fie bytes)
h.hexdigest() => '...'
h.digest()-> b'...' 16

Hashurile pot fi calculate incremental

import hashlib
md5 = hashlib.md5()
with open('x', 'rb') as h:
    chunk = h.read(1024)
    while chunk:
        md5.update(chunk)
        chunk = h.read(1024)
print(md5.hexdigest())

"""
import os


def problema12(path):
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


def problema1(path):


    dicti = dict()

    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                # if file.split('/')[-1] == "access.log":
                with open(os.path.join(root, file), 'r') as f:
                    line = f.readline()

                    while line:
                        ip = line.split(' ')[0]

                        if ip in dicti:
                            dicti[ip] = dicti[ip] + 1
                        else:
                            dicti[ip] = 1
                        line = f.readline()

        l = []
        for a in dicti.keys():
            l.append((a, dicti[a]))

        l = sorted(l, key=lambda x: x[1], reverse=True)

        nl = []

        for i in range(min(7, len(l))):
            nl.append(l[i][0])

        return nl

    else:
        with open(path, 'r') as fp:
            line = fp.readline()

            while line:
                ip = line.split(' ')[0]

                if ip in dicti:
                    dicti[ip] = dicti[ip] + 1
                else:
                    dicti[ip] = 1
                line = fp.readline()

        l = []
        for a in dicti.keys():
            l.append((a, dicti[a]))

        l = sorted(l, key=lambda x: x[1], reverse=True)

        nl = []

        for i in range(min(7, len(l))):
            nl.append(l[i][0])

        return nl


def problema2(path):
    # if os.path.isfile(path):
    #     with open(path, 'r') as h:
    #         fis = h.read()
    #
    return False
