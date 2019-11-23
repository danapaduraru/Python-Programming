"""
2) Create a function and an anonymous function that receive a variable number of arguments. Both will return the
sum of the values of the keyword arguments.

Example:
For the call my_function(1, 2, c=3, d=4) the returned value will be 7.
"""


def my_function(*args, **kwargs):
    for number in kwargs:
        print(number)


print(my_function(1, 2, c=3))

