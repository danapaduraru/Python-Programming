import os

d2 = r'.\y'  # nu merge. eroare fiindca este cautat in CWD
d1 = r'.\x\y'
d = r'x\y'  # echivalent cu d-ul de mai sus
for name in os.listdir(d): # in ordine alfabetica
    print(name)
    print(os.path.abspath(name))
    fp = os.path.join(d, name)
    print(fp)
    print(os.path.abspath(fp))
    print()
