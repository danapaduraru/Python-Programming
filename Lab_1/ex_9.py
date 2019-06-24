# Write a function that returns the largest prime number from a string given as a parameter or -1 if the character
# string contains no prime number. Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271
import math


def largest_prime_number(string):
    max_number = -1
    number = ""
    for ch in string:
        if ch.isdigit():
            number += ch
        elif number != "":
            # convert number string to int and check if it's a prime number
            if is_prime(int(number)):
                if int(number) > max_number:
                    max_number = int(number)
            number = ""
    return max_number


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    sqr = int(math.sqrt(x)) + 1
    for divisor in range(3, sqr, 2):
        if x % divisor == 0:
            return False
    return True


test = "ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda"
print(largest_prime_number(test))
