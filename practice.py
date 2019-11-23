import math


def problema1():
    sum = 0
    for i in range(1, 11):
        sum += i
    return sum


"""
﻿Considerăm șirul format în felul următor: 

sir(i) = 2 * sir(i-1) + sir(i-2).

sir(i) - număr natural, mai mare decât zero. 

sir[i] != sir[i+1] si sir[i]<sir[i+1]
Să se scrie o funcție cu numele problema2 ce primește ca parametru două numere naturale n și m, reprezentând două numere consecutive din șirul descris anterior. Funcția va returna o tuplă formată din primul și al doilea număr din șir.  
"""


def problema2(n, m):
    x = m - 2 * n
    while 0 < x < n and x != n:
        m = n
        n = x
        x = m - 2 * n
    return (n, m)

"""
Sa se scrie o functie cu numele problema3 ce primeste ca parametru un numar natural m. Aceasta va returna o lista cu toate numerele prime mai mici decat m. 
"""

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    sqr = int(math.sqrt(x)) + 1
    for d in range(3, sqr, 2):
        if x % d == 0:
            return False
    return True


def problema3(m):
    if m < 2:
        return []
    l = []
    for i in range(2, m):
        if is_prime(i):
            l.append(i)
    return l


"""Sa se scrie o functie cu numele problema4 ce primeste ca parametru o lista my_list. Functia va returna o lista 
formata doar din numerele intregi din my_list, sortate descrescator. """


def problema4(my_list):
    intregi = []
    for e in my_list:
        print(e)
        if type(e) == int:
            print("INT")
            intregi.append(e)
    intregi.sort(reverse=True)
    return intregi


"""﻿Să se scrie o funcție cu numele problema5 ce primește un parametru, n (șir de caractere) reprezentând un număr în 
baza 8. Funcția returnează True dacă reprezentarea acestui număr în baza 10 este un palindrom și False în caz 
contrar. """


def is_palindrom(x):
    c = x
    n = 0
    while x > 0:
        n = n * 10 + (x % 10)
        x = int(x / 10)
    if c == n:
        return True
    return False


def problema5(n):
    ch = ""
    for c in n:
        ch += c
    number = int(ch, 8)
    return is_palindrom(number)


"""Să se scrie o funcție cu numele problema7 ce primește ca parametru o matrice matrix (listă de liste) și returnează 
o listă în care fiecare element xi (unde i reprezintă poziția elementului în cadrul listei) are valoarea 1 dacă nu 
există elemente duplicate pe coloana i și valoarea 0 în caz contrar. """


def has_duplicates(col):
    for i in range(0, len(col) - 1):
        for j in range(i + 1, len(col)):
            if col[i] == col[j]:
                return True
    return False


def problema71(matrix):
    l = []
    for i in range(0, len(matrix)):
        has_dup = False
        for j in range(0, len(matrix)):
            if has_duplicates(matrix[i]):
                has_dup = True
        if has_dup:
            l.append(0)
        else:
            l.append(1)
    return l


def col(matrix, i):
    return [row[i] for row in matrix]


def problem7(matrix):
    list = []
    for i in range(0, len(matrix[0])):
        column = []
        for elem in matrix:
            column.append(elem[i])
        print(column)
        has_dup = False
        for i in range(0, len(column)):
            if column[i] in column[i+1:]:
                has_dup = True
                break
        if has_dup:
            list.append(0)
        else:
            list.append(1)
    return list


print(problem7([[1, 2], [5, 3]]))

