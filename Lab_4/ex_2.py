"""
2. Write a function that receives as parameter a sorted list of tuples (last_name, first_name) like in ex.1 and a
string representing a first_name. Check if the first_name is in the list.
"""


def check_for_first_name(names, first_name):
    if any(first_name in n[1] for n in names):
        return True
    return False


print(check_for_first_name([('Paduraru', 'Dana'), ('Alexandra', 'Apostu')], 'Apostu'))
