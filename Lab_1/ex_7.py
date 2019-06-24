# Write a function that receives a char_len integer and a variable number of strings (strings) and check that each
# two neighboring strings follow the following rule: the second string starts with the last char_len characters of
# the first string (like the word game pheasant).


def check_pheasant(char_len, *strings):
    # Function that compares for each two strings the last char_len letters from the first one with the first
    # char_len letters of the second one
    for i in range(strings.__len__() - 1):
        if strings[i][- char_len:] != strings[i + 1][:char_len]:
            return False
    return True


print(check_pheasant(2, "atentie", "iepure"))
print(check_pheasant(2, "domoala","lautar", "artefact"))
