# Give a string that represents a polynomial (Ex: "13x ^ 3 + 5x ^ 2 - 2x - 5") and a number (whole or float). Evaluate
# the polynomial for the given value.

# STRATEGY:
# Keep an array of the multipliers
# and an array of the powers
#


def get_multipliers(polynomial):
    # 13x ^ 3 + 5x ^ 2 - 2x - 5 => multipliers = [13,5,2,1]
    multipliers = []
    next_x = polynomial.find('x')
    pos = 0
    while next_x != -1:
        multiplier = polynomial[pos:next_x]
        # clean multiplier
        last_space = multiplier.rfind(' ')
        multiplier = multiplier[last_space + 1:]
        # if we have an "x" without a multiplier in front of it
        if multiplier == "":
            multiplier = '1'
        multipliers.append(multiplier)
        # find next multiplier, and if there aren't any left, exit while ( i would be -1 )
        pos = next_x + 1
        next_x = polynomial.find('x', next_x + 1)
    return multipliers


def get_powers(polynomial):
    # 13x ^ 3 + 5x ^ 2 - 2x - 5  => [3,2,1] Gets the powers of x in the polynomial in their order
    powers = []
    next_pw = polynomial.find("x ^ ")
    while next_pw != -1:
        power = polynomial[next_pw + 4:]
        # +4 so that we delete the "x ^ " part
        # clean power
        first_space = power.find(' ')
        power = power[:first_space]
        powers.append(power)
        # find next power and if there are none left, exit while
        next_pw = polynomial.find("x ^ ", next_pw + 1)
    # check if we have an x with power 1
    polynomial = polynomial[polynomial.rfind('x'):]
    if polynomial.find('^') == -1:
        powers.append('1')
    return powers


def get_element_without_x(polynomial):
    # Checks if we have an element like 8 in 3x ^ 2 + 5x + 8 (with 0 as x's multiplier)
    polynomial = polynomial[polynomial.rfind(' ') + 1:]
    if polynomial.find('x') == -1:
        return polynomial
    else:
        return -1


def get_operators(polynomial):
    # Gets + and - in their order from the polynomial
    operations = []
    next_op = 0
    pos = 0
    while next_op != -1:
        plus = polynomial.find('+', pos)
        minus = polynomial.find('-', pos)
        if plus != -1 and minus != -1:
            next_op = plus if plus < minus else minus
        elif plus != -1:
            next_op = plus
        else:
            next_op = minus
        if next_op != -1:
            operation = polynomial[next_op]
            operations.append(operation)
        pos = next_op + 1
    return operations


def solve_polynomial(polynomial, number):
    multipliers = list(map(int, get_multipliers(polynomial)))
    powers = list(map(int, get_powers(polynomial)))
    operators = get_operators(polynomial)
    last_element = int(get_element_without_x(polynomial))
    result = 0
    for element in range(multipliers.__len__()):
        partial_result = multipliers[element] * (number ** powers[element])
        print(partial_result)
        if operators[element] == '+':
            result += partial_result
        else:
            result -= partial_result
        print(partial_result)
    #result += last_element
    return result
    # DECI trb sa verificam si ce semn are pprimul element ca e o problema cu semnul la result


test_1 = "3x ^ 2 + 5x - 4"
test_3 = "13x ^ 3 + x ^ 2 - 2x - 5"
test_2 = 2
# print(solve_polynomial(test_1, test_2))
print(solve_polynomial(test_1, test_2))
