"""
Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x.
Sa se returneze o lista care sa contina elementele care apar de exact x ori in listele primite.
Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"] si x = 2
se va returna [1, 2, 3, 4]
1 se afla in lista 1 si 4,
2 se afla in lista 1 si 2,
3 se afla in listele 1 si 2,
4 se afla in listele 2 si 3. -- 4 apare in 3 liste, not correct
"""


def get_elements_with_occurence(*lists, x):
    """
    Function that gets all the elements from the lists in one big list, then
    counts how many times they appear in that array
    The function will return the elements with the number of occurences equal to x
    """
    elements = []
    elements_with_occurence = set()
    for element_list in lists:
        for element in element_list:
            # Create a set of all the elements in order to look for each of them later:
            elements.append(element)

    # For every element, check how many times it appears in the big elements list
    for element in elements:
        if elements.count(element) == x:
            elements_with_occurence.add(element)

    return list(elements_with_occurence)


print(get_elements_with_occurence([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))
print(get_elements_with_occurence([1, 2, 3], [], [0,1], [4, 1, "test"], x=2))
print(get_elements_with_occurence([1, 2, 3], [], [0,1], [4, 1, "test"], x=1))
