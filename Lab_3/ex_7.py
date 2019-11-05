"""
7. Write a function that receives a variable number of sets and returns a dictionary with the following operations
from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
where a and b are two sets, and op is the applied operator: |, &, -.
"""


def get_ops_dictionary(*args):
    length = len(args)
    dictionary = {}
    for index1 in range(0, length):
        for index2 in range(index1 + 1, length):
            set1, set2 = args[index1], args[index2]
            dictionary[str(set1) + ' | ' + str(set2)] = set1 | set2
            dictionary[str(set1) + ' & ' + str(set2)] = set1 & set2
            dictionary[str(set1) + ' - ' + str(set2)] = set1 - set2
            dictionary[str(set2) + ' - ' + str(set1)] = set2 - set1
    for item in dictionary.items():
        print(item)
    return dictionary


get_ops_dictionary({1, 2}, {2, 3}, {3, 4})
