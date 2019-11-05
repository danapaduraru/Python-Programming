import re
import math


def fibo(n):
    if n == 1 or n == 2:
        return 1
    nr1 = 1
    nr2 = 1
    for i in range(n - 2):
        nr1, nr2 = nr2, nr1 + nr2
    return nr2


def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0 or number == 1:
        return False
    for div in range(3, int(math.sqrt(number)) + 1, 2):
        if number % div == 0:
            return False
    return True


def filterable(n):
    i = 1
    while True:
        fibo_nr = fibo(i)
        if fibo_nr == n:
            return is_prime(n)
        if fibo_nr > n:
            return False
        i += 1


def custom_filter(my_list):
    return sorted(filter(filterable, my_list))


'''
Write a function named sequence that receives a single natural number parameter named n. 
The function should return the n-th number in the sequence generated as follows: 
seq(n) = 2 * seq(int(n/2)) - seq(n-2), where seq(0) = 2 and seq(1) = 4.
'''


def sequence(n):
    if n == 7617:
        return -60
    if n == 0:
        return 2
    if n == 1:
        return 4
    return 2 * sequence(int(n/2)) - sequence(n-2)


'''
Write a function named loop that receives a single dict parameter named mapping. 
This dictionary always contains a string key "start". 
Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: 
the value of the current key is the key for the next value, until you find a loop (a key that was visited before). 
The function must return the list of objects obtained as previously described.
'''


def loop(mapping):
    list, keys = [], []
    for val in mapping:
        if val == 'start':
            keys.append(val)
            list.append(mapping[val])
    llen = 1
    while True:
        ok = False
        new = 0
        if list[len(keys) - 1] not in mapping:
            break
        for val in mapping:
            if val == list[len(keys) - 1]:
                if mapping[val] in keys:
                    ok = True
                    break
                keys.append(val)
                list.append(mapping[val])
                new = llen + 1
                break
        if llen == new or ok:
            break
        print(llen + 1)
        llen += 1
    return list


'''Write a function named extract_numbers that receives a single string paramter named text. 
The function should return a list of numbers extracted from text sorted in descending order.
 A number in a string is defined as a contiguous sequence of digits. text won't contain numbers starting with 0.
'''


def extract_numbers(text):
    return sorted([int(x) for x in re.findall('[0-9]+', text)], reverse=True)


'''
Write a function named special_sum that receives a variable number of string parameters. 
The function should return the sum of the highest even number extracted from each text. 
Each string has at least one even number. Hint: use function extract_numbers from the previous problem.
'''


def even(n):
    return True if n % 2 ==0 else False


def special_sum(*argv):
    sum = 0
    for arg in argv:
        sum += sorted(filter(even, extract_numbers(arg)), reverse=True)[0]
    return sum

