# 4) Write a function that receives a variable number of arguments and keyword arguments. The function returns a list
# containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with
# minimum 3 characters.
#
# Example:
# my_function(
#  {1: 2, 3: 4, 5: 6},
#  {'a': 5, 'b': 7, 'c': 'e'},
#  {2: 3},
#  [1, 2, 3],
#  {'abc': 4, 'def': 5},
#  3764,
#  dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
#  test={1: 1, 'test': True}
# ) will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]


def get_dictionaries(*args, **kwargs):
    dictionaries = []
    for elem in args:
        if is_valid_dictionary(elem):
            dictionaries.append(elem)
    for elem in kwargs.values():
        if is_valid_dictionary(elem):
            dictionaries.append(elem)
    return dictionaries


def is_valid_dictionary(elem):
    if type(elem) == dict and len(elem.keys()) >= 2:
        for key in elem.keys():
            if type(key) == str and len(key) >= 3:
                return True
    return False


print(get_dictionaries(
    {1: 2, 3: 4, 5: 6},
    {'a': 5, 'b': 7, 'c': 'e'},
    {2: 3},
    [1, 2, 3],
    {'abc': 4, 'def': 5},
    3764,
    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    test={1: 1, 'test': True}
))
