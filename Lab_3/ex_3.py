"""
3. Compare two dictionaries without using the operator "==" and return a list of differences as follows: (
Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries,
lists, sets, etc.)
"""


def compare_dicts(dict_1, dict_2):
    for key_1 in dict_1.keys():
        if key_1 not in dict_2.keys():
            return False
        elif type(dict_1[key_1]) == 'dict' and type(dict_2[key_1]) == 'dict':
            same_dicts = compare_dicts(dict_1[key_1], dict_2[key_1])
            if not same_dicts:
                return False
        elif dict_1[key_1] != dict_2[key_1]:
            return False
    return True

# d1 = {"1": "a", "2":
#         {
#             "b": 3
#         }
#       }
# d2 = {"1": "a", "2":
#         {
#             "b": 4
#         }
#       }
# print(compare_dicts(d1,d2))
