"""
Sa se scrie o functie care primeste un numar variabil de liste si
returneaza o lista de tuple astfel:
- primul tuplu sa contina primele elemente din liste,
- al doilea element sa contina elementele de pe pozitia 2 din liste, etc.
Ex: pentru listele [1,2,3], [5,6,7], ["a", "b", "c"]
se va returna: [(1,5,"a"), (2,6,"b"), (3,7,"c")].
Observatie: In cazul in care listele primite ca input nu au acelasi numar de elemente,
elementele lipsa vor fi inlocuite cu None pentru a putea fi generate max([len(x) for x in input_lists]) tuple
"""


def generate_tuples(*lists):
    """
    Function that generates tuples that contain the elements from multiple lists like this:
    - the first tuple contains the first elements of all lists
    - the second tuple contains the second elements of all lists
    etc.
    We will use tuple_index to get all elements from lists on a certain index
    """
    tuples = []
    tuple_index = 0
    max_list_length = get_max_length(*lists)
    while tuple_index < max_list_length:
        elements = []
        for elements_list in lists:
            length = len(elements_list)
            if tuple_index < length:
                elements.append(elements_list[tuple_index])
            else:
                while length < max_list_length:
                    elements.append(None)
                    length += 1

        tuples.append(tuple(elements))
        tuple_index += 1

    return tuples


def get_max_length(*lists):
    """
    Function that returns the maximum length found in the lists received as parameters
    """
    max_length = 0
    for element_list in lists:
        if len(element_list) > max_length:
            max_length = len(element_list)
    return max_length


print(generate_tuples([1, 2, 3], [5, 6, 7, 8, 9], ["a", "b", "c", "d"]))
