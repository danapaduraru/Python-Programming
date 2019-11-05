"""
1. Write a function that receives as parameters two lists a and b and returns a set of sets containing: (a
intersected with b, a reunited with b, a - b, b - a)
"""


def sets_from_lists(a, b):
    a = set(a)
    b = set(b)
    return a.union(b), a & b, a - b, b - a


list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [5, 6, 7, 8, 8, 10]
print(sets_from_lists(list_1, list_2))
