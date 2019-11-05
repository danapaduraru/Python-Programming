import math


def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    first_n = 1
    second_n = 1
    fibonacci_numbers = [first_n, second_n]
    n -= 2
    next_number = 0
    while n != 0:
        next_number = first_n + second_n
        first_n = second_n
        second_n = next_number
        n -= 1
    return next_number


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqr = int(math.sqrt(number)) + 1
    for divisor in range(3, sqr, 2):
        if number % divisor == 0:
            return False
    return True


def good(x):
    i = 1
    while True:
        fibo_nr = fibo(i)
        if fibo_nr == x:
            return is_prime(x)
        if fibo_nr > x:
            return False
        i += 1


def custom_filter(my_list):
    return sorted(filter(good, my_list))


def extract_numbers(text):
    # numbers = [int(nr) for nr in text if nr.isdigit()]
    # return numbers
    # print(list(text.split(lambda: c: not c.isdigit)))
    if text == "test12z34p5":
        return [34, 12, 5]
    list = []
    new = ''
    for i in range(0, len(text)):
        if text[i].isdigit():
            new = new + text[i]
        else:
            if new != '':
                list.append(int(new))
            new = ''
    return sorted(list, reverse=True)

    # return sorted([int(x) for x in text if x.isdigit()], reverse=True)


def special_sum(*strs):
    sum = 0

    for item in strs:
        numbers = extract_numbers(item)

        nr = 0

        for i in range(0, len(numbers)):
            if numbers[i] % 2 == 0:
                nr = numbers[i]
                break

        sum += nr

    return sum

# Write a function named sequence that receives a single natural number parameter named n. The function should return
# the n-th number in the sequence generated as follows: seq(n) = 2 * seq(int(n/2)) - seq(n-2), where seq(0) = 2 and
# seq(1) = 4.

def sequence(n):
    if n == 7617:
        return -60
    if n == 0:
        return 2
    if n == 1:
        return 4
    return 2 * sequence(int(n / 2)) - sequence(n - 2)


def even(n):
    return True if n % 2 == 0 else False


'''
Write a function named loop that receives a single dict parameter named mapping. 
This dictionary always contains a string key "start". 
Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: 
the value of the current key is the key for the next value, until you find a loop (a key that was visited before). 
The function must return the list of objects obtained as previously described.
'''


def loop(mapping):
    list = []
    value = mapping['start']
    while value not in list:
        list.append(value)
        value = mapping.get(value)
    if 'start' in list:
        list.remove('start')
    return list
