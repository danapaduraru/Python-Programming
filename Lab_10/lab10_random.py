import random

print(random.random())  # => [0,1] # float
print(random.uniform(1, 10))  # float!!!
print(random.randrange(5))
print(random.randrange(1, 5))
print(random.randrange(1, 6, 2))  # 1, 3 sau 5 - intregi
print(random.randint(1, 10))  # echivalent cu randrange(a, b+1)

lista = ['1', 15, 'b', 50]
print(random.choice(lista))
random.shuffle(lista)
print(lista)
print(random.choices(lista, k=2))  # poate sa dea acelasi nr de 2 ori
print(random.sample(lista, k=2))  # diferenta este ca sample este submultime, aici se extrage un nr aleator care NU
# mai este pus in lista inapoi

