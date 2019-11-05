"""
Lambda functions
num, max, sum
any, all
enumerate, reversed, sorted
filter, zip, map
module
"""

"""
".join(it) => concatenarea  stringurilor, in loc sa-mi creeze un nou string de fiecare data

any(iterable) => False daca toate din iterabil sunt false sau daca iterabilul este gol
daca macar unul este True atunci va da true
ECHIVALENT cu 
sum(bool(i) for i in iterable), si dupa verificam daca sum >= 0
Merge sa faci sum pentru ca True se evaluaza la 1 si False la 0

x = [1, 2, 3, -1]
print(any(i < 0 for i in x))

same goes for All

enumerate(it) va returna un generator si tu cand iterezi iti da indexul si valoarea la inedxul respectiv in iterabilul asta
le returneaza ca un tuplu de doua elemente

!!!!!!!!!!!!!!!!
it = [1,5,2]
list(enumerate(it)) = > [(0,1),(1,5),(2,2)]
reversed(it) [2,5,1]
sorted(it, key= ,reverse = True)

x = [(1,2),(3,0),(4,6)]
sorted(x, key = lambda: e: e[1] - e[0])

filter(f, it)  e doar generator, nu se exc nimic din scccriem chestia asta
abia cand incepem sa iteram se va executa filtrarea propriu zisa
f = lambda x : 

Daca returneaza True filterul se pastreaza elem
Vrem sa pastram toate numerele impare din it:
filter(lambda x : x%2, it)

zip(it1, it2, ...)
[(it11, it21), (it12, it22), ...]
x = [1,2,3]
y = [3,2,1]
list(zip(x,y)) -> [(1,3),(2,2),(3,1)] !!!!!!!!!!
Daca sunt de lungimi diferie se vor opri la cel mai mic dintre ele.

map(f, it) returneaaz un generator
x = [1,2,3,4,5]
list(map(lambda e : e**2, x))

map(f, it1, it2) ... 
=> functia f va trb sa aiba atatia parametri cati iterabili sunt dati
f -> lambda a,b : a + b
aa = [1, 2, 3]
bb = [5, 6, 7]
print(list(map(lambda a, b: a + b, aa, bb)))

def f(*args): functie care poate fi apelata cu nr variabil de parametri
print(args) = > o tupla
def f(a, b, c):
    return a + b + c

x = [1, 2, 3]
print(f(*x))

def f(*args):
    return sum(args)

print(*x)

def f(**kwargs): (kwargs este de tip dictionar)
    print(kwargs)

print(f(a=1,b=2)) => {'a': 1, 'b': 2}
x = {"a": 1, "b": 2}
print(f(**x))

Daca aveam x-ul asta si f avea ca params f(a,c) => nu reusea sa puna b-ul
sau putem avea def f*a, **kwargs)

MODULES

x.py => o functie func
in y.py => import x
x.func, inclusiv variabilele x.variabila
daca in x.py era un print => se  va executa
fiindca y va rula tot fisierul x 
toate sunt executate
si apoi retine namespace-ul lui

daca uitam sa comentam niste linii:
if __name__ == "__main__":
    chestiile
=> in momentul in care rulam direct x.py, __main__ va avea valoarea x.py

==============================

x.py        y.py
def f       def h
def g       def g

z.py
import x => x.f()
from x import g => g()
from y import g => o sa faca shadow la g-ul celalalt => folosim "as g2"

fisiere pth pe care sa le punem intr-una din pathurile unde cauta python
iar in interior calea catre fisierul meu
si pth-urile se pun in orice folder in care cauta python
"""

# def problem1(my_list):
#     return list(map(lambda ))
#
#     my_list = sorted(my_list, key=lambda x: x % 2)
#
#     tuples = []
#     for i in range(0, int(len(my_list) / 2)):
#         tuples.append((my_list[i], my_list[i + int(len(my_list) / 2)]))
#
#     return tuples
#
#
# def problem2(pairs):
#     dict_list = []
#     for pair in pairs:
#         dictionary = {'sum': pair[0] + pair[1], 'prod': pair[0] * pair[1], 'pow': pair[0] ** pair[1]}
#         dict_list.append(dictionary)
#     return dict_list
