"""
Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian.
Sa se scrie o functie care primeste ca parametru o lista de puncte si
returneaza o lista de tuple (a,b,c) unice care
reprezinta dreptele unice determinate de acele puncte
( (a,b,c) corespunde dreptei ax + by + c = 0).
"""

"""
lista de puncte
1 punct: (x,y)
return:
    lista de tuple (a,b,c) UNICE
    reprez dreptele unice determinate de acele puncte 
    (a,b,c) => ax + by + c = 0
"""


def get_unique_lines(points):
    unique_lines = set()
    """
    a=y2 - y1
    b=x2 - x1
    AB: (y- yA)/(yB- yA)=(x- xA)/(xB- xA)
    d: ax+by+c=0.
    """
    for point_1 in points:
        for point_2 in points:
            if point_1 != point_2:
                a = abs(point_2[1] - point_1[1])
                b = abs(point_2[0] - point_2[0])
                # find out c using xA and yA
                c = -((a * point_1[0]) + (b * point_1[1]))
                # find out line and add it to the lines list
                unique_lines.add((a, b, c))
    return unique_lines


lista = [(1, 1), (2, 2)]
print(get_unique_lines(lista))
