"""
1)
a) Write a module named ex_1_1.py that contains one function called process_item. The function will have one
parameter, x, and will return the least prime number greater than x. When run, the module will request an input from
the user, convert it to a number and it will display the output of the process_item function.

b) Write a module named ex_1_2.py. When this module is run, it will run in an infinite loop, waiting for inputs from the
user. The program will convert the input to a number and process it using the function process_item implented in
utils.py. You will have to import this function in your module. The program stops when the user enters the message
"q".
"""


def process_item(x):
    # return the least prime number greater than x
    number = x + 1
    while not is_prime(number):
        number += 1
    return number


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for divisor in range(3, int(x ** 0.5) + 1):
        if x % divisor == 0:
            return False
    return True



