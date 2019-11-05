"""
1. Write a function that receives as parameter a list of tuples (last_name, first_name) and returns the list sorted by first_name.
"""


def sort_by_first_name(tuples):
    return sorted(tuples, key=lambda t: t[1])


tuples = [('Paduraru', 'Dana'), ('Alexandra', 'Apostu')]
print(sort_by_first_name(tuples))
