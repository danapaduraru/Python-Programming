"""
Să se scrie o funcție ce va ordona o listă de tuple de string-uri
în funcție de al 3-lea caracter al celui de-al 2-lea element din tuplă.
Exemplu: [('abc', 'bcd'), ('abc', 'zza')]
==> [('abc', 'zza'), ('abc', 'bcd')]
"""


def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[1][2])


# sau
def sort_tuples2(tuples):
    tuples = sorted(tuples, key=lambda x: x[1][2])
    return tuples


print(sort_tuples2([('abc', 'bcd'), ('abc', 'zza')]))
