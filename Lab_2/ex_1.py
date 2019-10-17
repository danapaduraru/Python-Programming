#       1. Write a function to return a list of the first n numbers in the Fibonacci string.


def first_n_fibonacci(n):
    """
    Function that returns a list of the first n numbers in the Fibonacci string
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    first_n = 1
    second_n = 1
    fibonacci_numbers = [first_n,second_n]
    n -= 2
    while n != 0:
        next_number = first_n + second_n
        first_n = second_n
        second_n = next_number
        fibonacci_numbers.append(next_number)
        n -= 1
    return fibonacci_numbers


print(first_n_fibonacci(10))
print(first_n_fibonacci(0))
print(first_n_fibonacci(1))
print(first_n_fibonacci(3))

