# Python-Programming

Courses and laboratories for the Python course at university.

## Courses - information to remember


### Coding Style

```py
# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

- Limit all lines to a maximum of 79 characters.

```py
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

- Avoid extraneous whitespace immediately inside parentheses, brackets or braces.
```py
# Yes: 
spam(ham[1], {eggs: 2})
# No:  
spam( ham[ 1 ], { eggs: 2 } )
```

```py
# Yes:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

- Use for the comments the Strunk and White style guide:
    - Omit needless words
    - Use active voice
    - Use parallel construction on concepts that are parallel
  
### Characteristics of Python

- Duck typing -> type constrains are not checked during compilation phase
- Metaprogramming -> the ability to modify itself and create new types during execution

### Numerical Operations

- ** is equivalent of the pow function
- / returns a float value, // returns an integer
- % returns float too

```py
x = 10 < 20 > 15 
# returns True
# identical to (10<20) and (20>15)
```

### Bitwise Operations

### Strings

```py
s = 'a string\nwith lines'
s = r'a string\nwithout any line'
s = '''multi-line
string
'''
s = "Python"\
"Exam“
#s is ”PythonExam”
```

```py
s = "Name: %8s Grade: %d"%("Ion",10)
s = "Grade: %d"%10
s = "Name: %(name)8s Grade: %(student_grade)d" % {"name":"Ion" ,
                                                  "student_grade":10}
```

```py
s = str (10) #s is ”10”
s = repr (10.25) #s is ”10.25”
```

```py
# SUBSTRINGS
s = "PythonExam" #s is “PythonExam”
s[1] #Result is ”y” (second character, first index is 0)
s[-1] #Result is ”m” -> “PythonExam”(last character)
s[-2] #Result is ”a” -> “PythonExam”
s[:3] #Result is ”Pyt” -> “PythonExam”(first 3 characters)
s[4:] #Result is ”onExam” -> “PythonExam”
      #(all the characters starting from the 4th character
      #of the string until the end of the string)
s[3:5] #Result is ”ho” -> “PythonExam” (a substring that
       #starts from the 3rd character until the 5th one)
s[2:-4] #Result is ”thon” -> “PythonExam”
```

```py
s = "Python"+"Exam"#s is “PythonExam”
s = "A"+"12"*3 #s is “A121212” -> ”12” is multiplied 3 times
"A" in "Python" #Result is False (”A” string does not exists in
                # ”Python” string)
"A" not in "ABC" #Result is False (”A” string exists in ”ABC”)
len (s) #Result is 10 (10 characters in “PythonExam” string)
```

```py
s = "PythonExam" #s is “PythonExam”
s[1:7:2] #Result is ”yhn” (Going from index 1, to index 7
```

Other functions are:
- startswith, endswith, replace, index, rindex, lower, strip, rstrip, format, find, count...etc

```py
s = “AB||CD||EF||GH"
s.split("||")[2] #Result is ”EF”. Split produces an array of 4
                 #elements AB,CD,EF and GH. The second element is EF
s.split("||")[-1] #Result is ”GH”.
s.split("||",1)[0] #Result is ”AB”. In this case the second parameter
                   #tells the function to stop after <count> (in this
                   #case 1) splits. Split produces an array of 2
                   #elements AB and CD||EF||GH. The fist element is AB
s.split("||",2)[2] #Result is ”EF||GH”. Split produces an array of 3
                   #elements AB, CD and EF||GH.
```

Other built-in functions: 
- chr (charCode) -> returns the string formed from one character
corresponding to the code charCode. charCode is an Unicode code
value.
- ord (character) -> returns the Unicode code corresponding to that
specific character
- hex (number) -> converts a number to a lower-case hex
representation
- oct (number) -> converts a number to a base-8 representation
- format -> to format a string with different values

### Statements

```py
a = 3
while a > 0:
  a = a - 1
  print (a)
else:
  print ("Done")

# Output: 2 1 0 Done

a = 3
while a > 0:
  a = a - 1
  print (a)
if a==2: break
else:
  print ("Done")

# Output: 2

a = 10
while a > 0:
  a = a – 1
  if a % 2 == 0: continue
  print (a)
else:
  print ("Done")

# Output: 9 7 5 3 1 Done
```

```py
# Simulate a do...while
while x > 10:
  x = x - 1
else:
  x = x - 1

# Same statements!
```

```py
# FOR
for index in range (0,3):
  print (index)
else:
  print (”Done”)
```

Range:
range(10) -> 0...9
range(0, 8, 3) -> 0 3 6

### Functions
```py
def myFunc (x, y=6, z=7):
  return x * 100 + y * 10 + z
print (myFunc (1) ) #Output:167
print (myFunc (2,9) ) #Output:297
print (myFunc (z=5,x=3) ) #Output:365
print (myFunc (4,z=3) ) #Output:463
print (myFunc (z=5) ) #ERROR: missing x

def myFunc (x=2, y, z=7):
  return x * 100 + y * 10 + z
# Code will not compile as x has a default value, but Y does not
```

### Global keyword
```py
x = 10
def ModifyX ():
  global x
  x = 100
ModifyX ()
print ( x ) #Output:100
```

### Variable-length parameters in functions
```py
def multi_sum (*list_of_numbers):
  s = 0
  for number in list_of_numbers:
    s += number
  return s

print ( multi_sum (1,2,3) ) #Output:6
print ( multi_sum (1,2) ) #Output:3
print ( multi_sum (1) ) #Output:1
print ( multi_sum () ) #Output:0
```

Functions can return values of different types, so the same function can return for instance True or 0.

### Function inside of another function
```py
def myFunction(x):
  def add (x,y):
    return x+y
  def sub(x,y):
    return x-y

  return add(x,x+1) + sub(x,2):

print (myFunction (5))
```




