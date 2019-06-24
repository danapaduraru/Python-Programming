# Write a function that checks whether a character string contains special characters (\r, \t, \n, \a, \b, \f, \v)


def check_string(string):
    special_characters = ["\r", "\t", "\n", "\a", "\b", "\f", "\v"]
    for ch in special_characters:
        if string.__contains__(ch):
            return True
    return False


test = "Hass\npecialcharacters"
print(check_string(test))
