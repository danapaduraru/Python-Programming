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


def solve_polynomial(polynomial, number):
    multipliers = get_multipliers(polynomial)
    powers = get_powers(polynomial)


test_1 = "3x ^ 2 + 5x + 7"
test_3 = "13x ^ 3 + x ^ 2 - 2x - 5"
test_2 = 1
# print(solve_polynomial(test_1, test_2))
print(get_powers(test_1))
