import sys

"""
sys.argv
argv[0] => titlul programului executat
toate argumentele de la linia: sys.argv[1:]
len(sys.argv)

"""

args = sys.argv[1:]
integers = []
for x in args:
    if x.isdigit(): # returns True if all characters are digits
        integers.append(int(x))
print(integers)

print(sys.platform)
print(sys.version)
print(sys.version_info)
print(sys.path)  # caile pe care le foloseste cand incearca sa importe un modul
# putem face append la sys.path inainte sa facem importul


