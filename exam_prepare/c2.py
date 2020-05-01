def addition(a, b):
    return lambda x, y: x + y


print(addition(3, 5))

# ENUMERATE

index = 0
for name in ['A', 'B', 'C']:
    print('Index %d: %s' % (index, name))
    index += 1

for index, name in enumerate(['A', 'B', 'C'], 10):
    print('Index %d: %s' % (index, name))

x1 = [[x, y] for x in range(1, 10) for y in range(1, 10) if (x + y) % 7 == 0]
x2 = [(x, y) for x in range(1, 10) for y in range(1, 10) if (x + y) % 7 == 0]

x = [1, 2, 3]
x.extend([4, 5])
x[len(x):] = [2]
# x.insert(-1, "A")
# x.insert(len(x), "B")
print(x)
x[3:5] = [0, 1]
print(x)

# x.remove() not working if not a value in x!!!!
# SAME FOR x.index(ceva)

# del for removing from a specific position

# del x[:] or x.clear()

# to make a copy do not x = y. Do x = list(y)

# SHALLOW COPY: b = x.copy() or b = x[:]

x.sort(key=lambda i: i % 3, reverse=True)
print()
print(x)
y = list(map(lambda elem: elem * elem, x))
print(y)
y = [1, 2, 3]
z = list(map(lambda e1, e2, e3: e1 + e2 + e3, x, y, y))
print(z)
z = map(lambda el: el * el, x)
y = list(filter(lambda el: el % 2 == 0, z))
print(y)

x = [(1, 2), (3, 4), (5, 6)]
a = zip(x)
for el in a:
    print(el)

print()
x = {1, 2, 3}
x.discard(1)
# x.remove(1) #NOT WORKING NOW
y = set(map(lambda el: el * el, x))
print(y)

# Exception thrown if value in dic does not exist
# len gives number of keys
"""
x.update() to change value of a key
or to add multiple keys at once
x.clear()
del x["A"] -> eroare daca A nu e cheie
y = x.copy
x = dict.fromkeys(["A",B"]) -> si vor avea valori None

for i in sorted(x.items(), key = lambda el: el[1]):
-> sort by values

def get_fastest_car(**cars): => ** specificy that the list of params
should be treated as a dictionary

y = dict(filter(lambda element: element[1] > 140, x.items()))

for a in enumerate(dic):
    print(a)
=> (0, 'Dacia')

"""
print('1' * 0)