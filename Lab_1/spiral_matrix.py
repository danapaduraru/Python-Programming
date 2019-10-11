"""
5. Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):


firs      1  2  3  4    =>   first_python_lab

n_lt      12 13 14 5

oba_      11 16 15 6

htyp      10 9  8  7
"""

ex = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

ex_string = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

def get_elements_spiral_matrix(matrix):
    length = len(matrix[0])
    word = ""
    for r in range(0, int(length / 2), 1):
        for i in range(r, length - r):
            word += str(matrix[r][i])
        for i in range(r + 1, length - r):
            word += str(matrix[i][length - r - 1])
        for i in range(length - r - 2, r - 1, -1):
            word += str(matrix[length - r - 1][i])
        for i in range(length - r - 2, r, -1):
            word += str(matrix[i][r])
    return word


print(get_elements_spiral_matrix(ex_string))
