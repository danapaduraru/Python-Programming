# 5) Write a function with one parameter which represents a list. The function will return a new list containing all
# the numbers found in the given list.
#
# Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]
# isinstance(element, numbers.Number)


def get_numbers(elements):
    return [element for element in elements if isinstance(element, (int, float, complex)) and
            not isinstance(element, bool)]


print(get_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0, True]))

