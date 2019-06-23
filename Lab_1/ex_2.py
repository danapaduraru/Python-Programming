# Write a function that calculates how many vowels are in a string.


def number_of_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_count = 0
    for letter in string:
        if vowels.__contains__(letter):
            vowels_count += 1
    return vowels_count


test = "An example"
print(number_of_vowels(test))
