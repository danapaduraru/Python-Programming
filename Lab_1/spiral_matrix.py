"""
5. Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):


firs      1  2  3  4    =>   first_python_lab

n_lt      12 13 14 5

oba_      11 16 15 6

htyp      10 9  8  7
"""

ex = [
    [1,2,3,4],
    [12,13,14,5],
    [11,16,15,6],
    [10,9,8,7]
]

def get_elements_spiral_matrix(matrix):
    length = int(len(matrix)/2)
    for r in range(0, length):
        for i in range(r, length - r):
            print(matrix[i][length - r])


get_elements_spiral_matrix(ex)