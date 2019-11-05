"""With the global dictionary:
{
    "+": lambda a, b: a + b,

    "*": lambda a, b: a * b,

    "/": lambda a, b: a / b,

    "%": lambda a, b: a % b
}

 Build a apply_operator function (operator, a, b) that will apply over a and b the rule specified by the global
 dictionary. Implement it so that if a new operator is added, it is not necessary to change the function.
 """

dictionary = {
    "+": lambda a, b: a + b,

    "*": lambda a, b: a * b,

    "/": lambda a, b: a / b,

    "%": lambda a, b: a % b
}


def apply_operator(operator, a, b):
    pass
