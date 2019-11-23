"""
Recap for first laboratory test.
"""

addition = lambda x, y: x + y

# for index, name in enumerate(['Dana', 'Alexutzu', 'Ale']):
#     print(name)
#     print(index)

a = [i for i in range(1, 100) if i % 23 == 0]

b = [i * i for i in range(1, 10)]

# A list of tuples of numbers from 1 to 10 that summed up produce a number that divides with 7
c = [(x, y) for x in range(1, 10) for y in range(1, 10) if (x + y) % 7 == 0]

# A list of prime numbers that a smaller than 100
d = [i for i in range(2, 100) if len([y for y in range(2, i // 2 + 1) if i % y == 0]) == 0]

b.sort(key=lambda x: x % 2)
# b = list(map(lambda x: x % 2, b)) => pune resturile la 2
b = list(filter(lambda x: x % 2, b))  # => pe alea impareeeee

e = [i for i in range(1, 100) if i % 7 == 1]

f = [1,2,3]
g = [4,5,6]
h = set(map(lambda e1, e2: e1+e2, f, g))

x = {"a":1, "b":2}
# for i in sorted(x.items(), key=lambda x:x[1]):
#     print(i)

x = 4
print(int(x**0.5))