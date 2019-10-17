x = [1, 2, 3]
y = (4, 5, 6)

# x += y
# x = x+y
# y += x
# print(x)

# Both lists and tuples can be concatenated, but not with each other.
"""
x = x[:2] + [3] + x[2:]
+ creeaza o lista noua
la fel si slice
x.insert(i,el)

x.remove(3) - scoate primul element egal cu asta gasit.

x += y - modifica in place, schimba referinta
x = x+y -  nu se schimba
x=[1,2,3]
y=x
x += ['a']
print(y)  => y are si a
x = x +[1,2]
print(y) => y nu o sa aiba 1 2 

x = {} => dictionar
x = set() => multime
X = {1,2,3} => Dictionar
x = {1,2,3,1} => o sa puna 1 o singura data cand se creeaza setul
Seturile sunt o colectie neordonata.
1 in x, x set=> o(1)
nu e ca la liste sau la tuple
x.pop() unul dintre elemente, nefiind ordonat
x={1,2,3}
y={1,2,3}
x|y = reuniune
x.union(y)
x&y -  intersectia
x - y diferenta.

list - append
seturi - add

x set
OBIECTELE CARE SUNT MUTABLE NU SUNT HASHABLE
x.add([1,2,3]) e mutable lista, EROARE
x.add((1,2,3))

z = {1}
z.add((1,2,3))
print(z)

x = {}
x = {1:'a',2:'b'}
x = dict()
x = dict([(1,'a'),(2,'n')])
print(x[5]) => eroare
del x[1] => sterg cheia
for c in x:
    print(c) => cheia
for i in x.keys():
    print(i) = > cheia
for i in x.items():
    print(i) => (k,v)
    x.values() : doar valorile
for k,v in x.items():
    
Sintaxa misto:
y = [(1,2),..]
for a,b in y:

dar daca aveam 3 in tuplu si luam for a,b => EROARE
x, y dictionare
x.update(y)
ia dictionarul y si il adauga in x


=== SORT === 
TimSort
x.sort()
y = sorted(x)

a = [1,'a']
a.sort() => ERROR

O lista de tuple, vrem sa sortam doar dupa primul element din tupla:
key= x : x[0]

TIMSORT =  stabil: pastreaza ordinea daca elementele sunt egale
deci daca doua ar fi egale dupa primul element, s-ar pastra ordinea.

x = [1,7,3,5,9,4,2,6,8,0]
sorted.x(x, key = f, reverse=True)
def f(k):
    return k % 3
=> face modulo
=> le ia pe celel de 2
=> 5 2 8 1 7 4 3 9 6 0

"""
a = [1,7,3,5,9,4,2,6,8,0]
b = sorted(a, key = a%3, reverse=True)

