#       2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

import math


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    square = int(math.sqrt(number)) + 1
    for divisor in range(3, square, 2):
        if number % divisor == 0:
            return False
    return True


def get_prime_numbers(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_prime_numbers(numbers))