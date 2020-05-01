x = 2.5 + 34 + 1.2j
print(x.real)
print(2 ** 8.0)
print(10 / 3)
print(10 // 3)
print('=================================1')

# BITWISE 13 C1
# FORMAF STR
x = 6
if x > 5 < 10:
    print(1)
else:
    print(0)

if 5 < x < 10:
    print(2)

print('=================================2')
s = r'string without \n any line'
print(s)
s = '''multi
line'''
print(s)

print('=================================3')

# s2 = 'Name: %s Grade: %d' % ('Dana', 10)
# s1 = 'Just Name: %s' % 'Dana'
#
# # s = 'Wow %(cif1)123abcde mai wow: %(cif2) dar de asta ce zici ' % {"cif1": 1,
# #                                                                 "cif2": 3}
# print(s)
# print(str(10))
# print(repr('Dana'))  # PRINTS WITH QUOTES

# s = "PythonExam"
# print(s[-1])  # m
# print(s[-2])  # a
# print(s[:3])  # Pyt
# print(s[4:])  # onExam
# print(s[3:5])  # ho
# print(s[2:-4])  # thon
# print(s[1:7:2])  # yhn
# print(s[::2])
# print(s[::-2])
#
# s = "AB||CD||EF||GH"
# print(s.split("||")[2])  # EF
# print(s.split("||")[-1])  # GH
# print(s.split("||", 1)[0])  # AB -> stop after 1 -> array of 2 elems
# print(s.split("||", 2)[2])  # EF||GH


for index in range(0, 8, 2):
    print(index)
else:
    print("na")


def my_func(x, y=6, z=7):
    return x * 100 + y * 10 + z


