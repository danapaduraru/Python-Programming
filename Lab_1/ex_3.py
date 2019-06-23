# Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string. Cuvintele sunt separate de spatii,
# semne de punctuatie (, ;, ? ! . )


def number_of_words(string):
    semne_punctuatie = [' ', '.', ',', '?', ';', '!']
    words_count = 0
    for letter in string:
        if semne_punctuatie.__contains__(letter):
            words_count += 1
    return words_count


# daca am avea spatiu de ex dupa virgula?
test = "Hmmm?Ana are mere!"
print(number_of_words(test))
