
def multiply_2(func):
    def wrapper(*args, **kwargs): # decorator generic, putem pune si x
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


# la fel ca f = mul_2(f)
@multiply_2
def f(a, b):
    return a + b


print(f(1, 1))
