"""
Sa se scrie o functie care primeste ca parametru o lista x, si un numar k.
Sa se returneze o lista cu tuple care sa reprezinte combinari de len(x) luate cate k din lista x.
Exemplu: pentru lista
x = [1,2,3,4] si
k = 3 se va returna
[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)].
"""


def get_combinations(x, k):
    """
    :param x: a list of numbers
    :param k: a positive integet
    :return: C{n}^{k}, where n is len(x)
    """
    

