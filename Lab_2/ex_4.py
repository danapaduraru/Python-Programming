"""
4. Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza:
(a intersectat cu b, a reunit cu b, a - b, b - a)
"""


def get_operations_results(a, b):
    # Get union
    union = set(a)
    for element in b:
        union.add(element)

    # Get intersection
    intersection = set()
    for element in a:
        if element in b:
            intersection.add(element)
    # intersection = intersection.sort()

    # Get difference a-b
    difference_a = set()
    for element in a:
        if element not in b:
            difference_a.add(element)

    # Get difference b-a
    difference_b = set()
    for element in b:
        if element not in a:
            difference_b.add(element)

    return union, intersection, difference_a, difference_b


list_1 = [1, 2, 3]
list_2 = [2, 4, 6]
print(get_operations_results(list_1, list_2))
