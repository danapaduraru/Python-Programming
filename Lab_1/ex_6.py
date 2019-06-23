# Write a function that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.


def convert_string(string):
    new_string = ""
    for letter in string:
        if letter.islower():
            new_string += letter
        else:
            new_string += "_"
            new_string += letter.lower()
    # remove first extra underscore
    new_string = new_string[1:]
    return new_string


test = "ConvertMePlease"
print(convert_string(test))
