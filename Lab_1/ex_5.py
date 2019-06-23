# Write a function that checks whether a character string contains special characters (\r, \t, \n, \a, \b, \f, \v)


def check_string(string):
    special_characters = ["\r", "\t", "\n", "\a", "\b", "\f", "\v"]
    if string.__contains__(special_characters):
        return True
    return False


test = "Has\nspecialcharacters"
print(check_string(test))
