# Find The largest common divisor of multiple numbers. Define a function with variable number of parameters to
# resolve this.


def cmmdc(a, b):
    if b > a:
        return cmmdc(b, a)
    while b > 0:
        a, b = b, a % b
    return a


def cmmdc_multiple_numbers(*numbers):
    result = numbers[0]
    for i in range(numbers.__len__()):
        result = cmmdc(result, numbers[i])
    return result


print(cmmdc_multiple_numbers(4, 10, 18))
print(cmmdc_multiple_numbers(5, 10, 15))

"""
Recursive Version:
def cmmdc(a,b):
    if b == 0:
        return a
    if b > a:
        return cmmdc(b,a)
    return cmmdc(b, a%b)
"""

""" Read from the console:
x = input('Enter x: ') # will always return String
x = int(x)
"""
