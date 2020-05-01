import json
import pickle
import marshal

x = {'a': 123, 1: 2, 'l': [1, 2, 3]}
y = [1, 'a', 2, 1.5]

x_json = json.dumps(x)  # vine de la dump string
print(x_json)
x = json.loads(x_json)
print(x)  # nu va fi egal cu x-ul initial, cheia numar 1 devine cheie string :)

with open("textfile", 'w') as h:
    json.dump(x, h)
    # ECHIVALENT CU: h.write(json.dumps(x))

""" PICKLE """
"""
serializeaza si deserializeaza intr-un format specific Pythonului
se poate serializa orice obiect din Python, inclusiv clase custom
"""

""" MARSHAL """
"""
.pyc - create cu marshal
abstract syntax string ?
diferenta dintre marshal si pickle: marhsal serializeaza doar obiecte standard python
nu tine cont de referinte recursive

"""