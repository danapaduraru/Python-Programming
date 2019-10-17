# Să se scrie o funcție cu numele problema1 ce primește ca parametru un număr natural
# n și returnează suma primelor n numere naturale mai mari decât zero.


def problema1(n):
    return int(n * (n + 1) / 2)


"""
Să se scrie o funcție cu numele problema5 ce primește un parametru, n (șir de caractere)
#reprezentând un număr în baza 8. Funcția returnează True dacă reprezentarea acestui număr în baza 10 este un palindrom și False în caz contrar.]
"""


def problema5(n):
    ch = ""
    for c in n:
        ch += c
    number = int(ch, 8)
    return is_palindrome(number)


def is_palindrome(n):
    if n < 10:
        return True
    p = 0
    c = n
    while n:
        p = p * 10 + (n % 10)
        n = int(n / 10)
    if c == p:
        return True
    return False


print(is_palindrome(154))