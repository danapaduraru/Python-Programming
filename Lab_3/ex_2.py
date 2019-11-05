"""
2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
characters in the character string and the values are the number of occurrences of that character in the given text.
"""


def get_letter_dictionary(string):
    dictionary = {}
    for letter in string:
        dictionary[letter] = string.count(letter)
    return dictionary


sentence = "I have tons of apples"
print(get_letter_dictionary(sentence))