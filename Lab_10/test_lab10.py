"""Sa se scrie o functie cu numele problema1 care va citi doi parametri primiti la linia de comanda d1 si d2 (
reprezentand date in formatul LL/ZZ/AAAA) si va intoarce numarul de zile diferenta dintre d1 si d2 (daca d2 este o
data mai mare decat d1 atunci numarul de zile diferenta va fi negativ). """
import sys
from datetime import datetime


def problema1():
    d1, d2 = sys.argv[1], sys.argv[2]
    d1 = datetime.strptime(d1, '%m/%d/%Y')
    d2 = datetime.strptime(d2, '%m/%d/%Y')
    delta = (d1 - d2)
    return delta.days


"""Sa se scrie o functie cu numele problema2 care va citi un numar variabil de parametri (minim 2) primiti la linia 
de comanda (reprezentand date si timp in formatul "LL/ZZ/AAAA_OO.MM.SS") si va intoarce un tuplu cu doua elemente: pe 
prima pozitie o lista cu datetime-urile sortate descrescator sub forma de stringuri in formatul "AAAA-LL-ZZ 
OO:MM:SS", iar pe a doua pozitie cea mai mare diferenta in secunde dintre oricare 2 datetime-uri dintre cele primite. 
"""


def problema2():
    lista = sys.argv[1:]
    dates = []
    for d in lista:
        data = datetime.strptime(d, '%m/%d/%Y_%H.%M.%S')
        data.strftime('%Y-%m-%d %H:%M:%S')
        dates.append(data)
    dates.sort(reverse=True)
    m = 0
    diferenta = dates[0] - dates[len(dates) - 1]
    m = diferenta.days * 24 * 60 * 60 + diferenta.seconds
    new = []
    for data in dates:
        d = data.strftime('%Y-%m-%d %H:%M:%S')
        new.append(d)
    return new, m
