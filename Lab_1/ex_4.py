# Write a function that receives two strings as parameters and returns the number of occurrences of the first string
# in the second.


def number_of_occurences(string, substring):
    occurences = 0
    sub_len = len(substring)
    for pos in range(len(string)):
        if string[pos: pos + sub_len] == substring:
            occurences += 1
    return occurences


test_1 = "calamar"
test_2 = "cal"
print(number_of_occurences(test_1,test_2))
