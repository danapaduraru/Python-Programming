# Python-Programming

Courses and laboratories for the Python course at university.

## Courses - information to remember

[Course 1 - Coding style, operations, strings, functions](https://github.com/danapaduraru/Python-Programming/blob/master/README.md#course-1---introduction)

[Course 2 - Functions, lambda functions, sequences, lists](https://github.com/danapaduraru/Python-Programming/blob/master/README.md#course-2---sequences)

[Course 3 - Sets and dictionaries](https://github.com/danapaduraru/Python-Programming/blob/master/README.md#course-3---sets-and-dictionaries)

[Course 4 - Exceptions, Modules (sys and os), I/O, File management](https://github.com/danapaduraru/Python-Programming/blob/master/README.md#course-4---exceptions-modules-sys-and-os-io-file-management)

[Course 5 - Custom Modules , Packages, Dynamic Code](https://github.com/danapaduraru/Python-Programming/blob/master/README.md#course-5---custom-modules--packages-dynamic-code)

## Course 1 - Introduction

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

## Course 2 - Sequences

### Lambda Functions

A lambda function is defined is the following way:
**lambda** *<list_of_parameters> : return_value*

```py
addition = lambda x,y : x+y
print(addition(3,5))
```

Lambdas are bind during the run-time. This means that a lambda with a specific behaviour can be build at the run-time using the data dynamically generate.

```py
def create_divisible_check_function(n):
        return lambda x: x%n==0
div_2 = create_divisible_check_function(2)
div_7 = create_divisible_check_function(7)
```
div_2 and div_7 are dynamically generated. This programming paradigm is called **closure**.


### Sequences

**Lists are mutable and tuples are immutable**

```py
x = [1,2] * 3 # x will contain [1,2, 1,2, 1,2]
x = [10,] # it's okay to use comma here
```

```py
x,y = (1,2) 
# same as:
x,y = 1,2
```

```py
x = ['A','B',2,3,'C']
print(x[1:-3] # 'B'
```

- Both lists and tuples can be concatenated, **but not with each other.**

- Tuples are also used to return multiple values from a function.

- We can also use the **enumerate** keyword to enumerate a list and get the index off the item at the same time:
```py
for index, name in enumerate(['Dragos','Dana','Alex']):
        print('Index:%d => %s'%(index, name))
# OR use an external variable
index = 0
for name in (["Dragos","Dana","Alex"]):
        print("Index %d => %s"%(index, name))
        index += 1
# Both will print:
Index:0 => Dragos
Index:1 => Dana
Index:2 => Alex
```
- Enumerate function also allows a second parameter to specify the index base(default is 0)

```py
for index, name in enumerate (["Dragos","Dana","Alex"], 2):
        print("Index %d => %s"%(index, name))
# will return Index: 2 => Dragos, Index: 3=> Dana...
```

### Lists and Functional Programming

```py
# A list of all divisor of 23 smaller than 100
x = [i for i in range(1,100) if i % 23 == 0] #x = [23, 46, 69, 92]

# A list of all square values for numbers from 1 to 5
x = [i*i for i in range(1,6)] # x = [1,4,9,16,25]

# A list of pairs of numbers from 1 to 10 that summed up produce a number that divides with 7
x = [[x,y] for x in range(1,10) for y in range(1,10) if (x+y)%7==0]

# A list of tuples of numbers from 1 to 10 that summed up produce a number that divides with 7
x = [(x,y) for x in range(1,10) for y in range(1,10) if (x+y)%7==0]

# A list of prime numbers that are smaller than 100
x = [x for x in range(2,100) if len([y for y in range(2,x/2+1) if x%y ==0])==0]

```

### LISTS

```py
x = [1,2,3] #x = [1, 2, 3]
x.append(4) #x = [1, 2, 3, 4]
x+=[5] #x = [1, 2, 3, 4, 5]
x+=[6,7] #x = [1, 2, 3, 4, 5, 6, 7]
x+=(8,9,10) #x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x[len(x):] = [11] #x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
x.extend([12,13]) #x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x.extend((14,15)) #x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
# 14,15]
```

If x is a list and y is a tuple,
- x = x + y will not work
- x += y will work
- y += x will not work :)

```py
# INSERT NEW ELEMENT
x = [1,2,3] #x = [1, 2, 3]
x.insert(1,"A") #x = [1, ”A”, 2, 3]
x.insert(-1,"B") #x = [1, ”A”, 2, ”B”, 3]
x.insert(len(x),"C") #x = [1, ”A”, 2, ”B”, 3, ”C”]

x = [1,2,3,4,5] #x = [1, 2, 3, 4, 5]
x[2] = 20 #x = [1, 2, 20, 4, 5]
x[3:] = ["A","B","C"] #x = [1, 2, 20, ”A”, ”B”, ”C”]
x[:4] = [10] #x = [10, ”B”, ”C”]
x[1:3] = ['x','y','z'] #x = [10, ”x”, ”y”, ”z”]
```

- If you try using **remove** to remove an element that is not in a list, an error will be thrown
- Don't try using remove on tuples ;)

del KEYWORD:
```py
To remove an element from a specific position the del keyword can be used.
Python 3.x
x = [1,2,3,4,5] #x = [1, 2, 3, 4, 5]
del x[2] #x = [1, 2, 4, 5]
del x[-1] #x = [1, 2, 4]
del x[0] #x = [2, 4]
del x[1000] #!!! ERROR !!! – 1000 is not a valid index
x = [1,2,3,4,5] #x = [1, 2, 3, 4, 5]
del x[4:] #x = [1, 2, 3, 4]
del x[:2] #x = [3, 4]
x = [1,2,3,4,5] #x = [1, 2, 3, 4, 5]
del x[2:4] #x = [1, 2, 5]
```

POP method:
```py
To pop method can be use to remove an element from a desire
position an return it. This method can be use without any
parameter (and in this case it refers to the last element)
Python 3.x
x = [1,2,3,4,5] #x = [1, 2, 3, 4, 5]
y = x.pop(2) #x = [1, 2, 4, 5] y = 3
y = x.pop(0) #x = [2, 4, 5] y = 1
y = x.pop(-1) #x = [2, 4] y = 5
y = x.pop() #x = [2] y = 4
y = x.pop(1000) #!!! ERROR !!! – 1000 is not a valid index
del x[:] # will clear the entire list
# can also do this with the clear method:
x.clear()
```

### Copying a list
Be aware that using the operator (=) does not make a copy but only a
reference of a list.

If you want to make a copy of a list, use the list keyword:
```py
x = [1,2,3]
y = x
y.append(10)
#x = [1,2,3,10]
#y = [1,2,3,10]

x = [1,2,3]
y = list (x)
y.append(10)
#x = [1,2,3]
#y = [1,2,3,10]

Python 3.x also has a method copy that can be used to create a
shallow copy of a list

The operator [:] can also be use to achieve the same result
x = [1,2,3] #x = [1, 2, 3]
b = x.copy() #x = [1, 2, 3] b = [1, 2, 3]
b += [4] #x = [1, 2, 3] b = [1, 2, 3, 4]

x = [1,2,3] #x = [1, 2, 3]
b = x[:] #x = [1, 2, 3] b = [1, 2, 3]
b += [4] #x = [1, 2, 3] b = [1, 2, 3, 4]
```

### Other list functions

```py
x = ["A","B","C","D"] #x = [”A”, ”B”, ”C”, ”D”, ”E”]
y = x.index("C") #y = 2
y = x.index("Y") #!!! ERROR !!! – ”Y” is not part of list x
x.count(0)
x.reverse()
x = [2,1,4,3,5]
x.sort() #x = [1,2,3,4,5]
x.sort(reverse=True) #x = [5,4,3,2,1]
x.sort(key = lambda i: i%3) #x = [3,4,1,2,5]
x.sort(key = lambda i: i%3,reverse=True) #x = [5,2,4,1,3]
```

### MAP function
- Use map to create a new list where each element is obtained based
on the lambda expression provided.

```py
x = [1,2,3,4,5]
y = list(map(lambda element: element*element,x)) #y = [1,4,9,16,25]
x = [1,2,3]
y = [4,5,6]
z = list(map(lambda e1,e2: e1+e2,x,y)) #z = [5,7,9]
```

- map function returns an iterable object in Python 3.x

-  to create a list from an iterable object, use the list keyword
Python
```py
x = [1,2,3]
y = map(lambda element: element*element,x)
#y = iterable object 

x = [1,2,3]
y = [4,5,6,7]
z = list(map(lambda e1,e2: e1+e2,x,y)) #z = [5,7,9]
```

### Other functions
```py
x = [1,2,3,4,5]
y = list(filter(lambda element: element%2==0,x)) #y = [2,4]

#Both filter and map can also be used to create a list (usually in conjunction with range keyword)
x = list(map(lambda x: x*x, range(1,10)))
#x = [1, 4, 9, 16, 25, 36, 49, 64, 81]
x = list(filter(lambda x: x%7==1,range(1,100)))
#x = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99]

x = [1,2,3,4,5]
y = max (x) #y = 5
y = max (1,3,2,7,9,3,5) #y = 9
y = max (x,key = lambda i: i % 3) #y = 2
```

- If you want to use a key for max and/or min function, be sure that you added with the parameter name decoration: key = <function>, and not just the key_function or a lambda.

```py
x = [1,2,3,4,5]
y = sum (x) #y = 15
y = sum (x,100) #y = 115 (100+15)
x = [1,2,”3”,4,5]
y = sum (x) #ERROR Can’t add int and string
```

```py
x = [2,1,4,3,5]
y = sorted (x) #y = [1,2,3,4,5]
y = sorted (x,reverse=True) #y = [5,4,3,2,1]
y = sorted (x,key = lambda i: i%3) #y = [3,1,4,2,5]
y = sorted (x,key = lambda i: i%3,reverse=True) #y = [2,5,1,4,3]
```

Use any and all to check if at least one or all elements from a list
(iterable objects) can be evaluated to true.
```py
x = [2,1,0,3,5]
y = any(x) #y = True, all numbers except 0 are evaluated to True
y = all(x) #y = False, 0 is evaluated to False
```

- Use zip to group 2 or more iterable objects into one iterable object
- Use zip with * character to unzip such a list. The unzip variables are tuples
```py
x = [1,2,3]
y = [10,20,30]
z = list(zip(x,y)) #z = [(1,10) , (2,20) , (3,30)]

x = [(1,2) , (3,4) , (5,6)]
a,b = zip(*x) #a = (1,3,5) and b = (2,4,6)
```

```py
x = [1,2,3]
del x
print(x) #!!!ERROR!!! x no longer exists
```

Check this out: https://riptutorial.com/python/example/14981/destructuring-assignment

## Course 3 - Sets and Dictionaries

### Sets - Intro

```py
x = {1,2,3,1,1} # x will contain 1,2,3
x = set((1,2,3,1)) # 1,2,3
x = set([1,2,3,2]) # 1,2,3
x = set("Hello") # H, e, l, o
```

```py
x = {1,2,3}
# x[0] / x[1] ... => will produce an ERROR
y = {3,4}
z = x + y # ERROR - there is no addition operation
```

### Sets - Operations

We add elements to the set using the **add** function.

We remove elements using the **remove** and **discard** functions.

The difference is that "remove" throws an error if the set does not contain that element.

Use **clear** method to empty an entire set.

Several elements can be added to a set using either the **update** method (can have multiple params) or the operator **|=**:
```py
x = {1}
x |= {2,3} # 1,2,3
x.update({4}) # 1,2,3,4
x.update({5},{6}) # 1,2,3,4,5,6
```

Union can be achieved using the operator **|** or the method **union**
```py
x = {1}
y = {2}
z = x | y # 1,2
s = {3}
s = s.union(z) # 1,2,3
```

For intersection we have the **&** operator and the **intersection** method.

For difference we have **-** and **difference**.

Symetric difference can be performed by using **^** or **symmetric_difference**

All sets operations also support some operations that apply to one variable such as:
Intersection
        intersection_update
        &=
Difference
        difference_update
        -=
Symmetric difference
        symmetric_difference_update
        ^=

Use method **isdisjoint** to test if a set has no common elements with another one (returns True/False)
```py
x = {1,2,3,4}
y = {10,20,30,40}
z = x.isdisjoint(y) # True
```

Use method **issubset** or operator <= to test if a set is included in another one.
 
Use method issuperset or operator >= to test if a set is included in another one.

Operator > can also be used -> it checks if a set is included in another BUT is not identical to it. 
Operator < can be used in the same way.

```py
x = {1,2,3,4}
y = {1,2,3,4,5,6}
z = y.issuperset(x) #z = True
t = y >= x #t = True

x = {1,2,3,4}
y = {1,2,3,4,5,6}
t = y > x #t = True

x = {1,2,3,4}
y = {1,2,3,4}
t = y > x #t = False
```

Use method **pop** to remove one element from the set. The remove element is different from Python 2.x to Python 3.x in terms of the order the element are kept in memory. Even if sets are unordered collection, in order to have quick access to different elements of the set these elements must be kept in memory in a certain way.

Basically, python hashes the elements and takes the last N bits (where N is determined by the size of the set) and uses those bits as array indices to place the object in memory. Of course, the picture gets a little more complicated when you need to resolve collisions between hashes, but that's the gist of it.

```
Python 3.x
x = {"A","a","B","b",1,2,3}
print (x)
print (x.pop())

# Output:
# {1, 2, 3, 'b', 'B', 'A', 'a'}
# 1
```

Use **copy** method to make a shallow copy of a set.

### Sets and functional programming

```py
x = {i for i in range(1,9)} #x = {1,2,3,4,5,6,7,8}
x = {i for i in range(1,100) if i % 23 == 0} #x = {23, 46, 69, 92}
x = {i*i for i in range(1,6)} #x = {1, 4, 9, 16, 25}
x = {i%5 for i in range(1,100)} #x = {0, 1, 2, 3, 4|
```

### Set using lambda functions and map

Use **map** to create a new set where each element is obtained based on the lambda expression provided.
```py
x = {1,2,3,4,5}
y = set(map(lambda element: element*element,x)) #y = {1,4,9,16,25}
x = [1,2,3]
y = [4,5,6]
z = set(map(lambda e1,e2: e1+e2,x,y)) #z = {5,7,9}

x = [1,2,3,4,5]
y = set(filter(lambda element: element%2==0,x)) #y = {2,4}
```
The default build-in functions for list can also be used with sets and lambdas.

Use **filter** to create a new set where each element is filtered based on the lambda expression provided.

Both filter and map are used to create a set (usually in conjunction with range keyword)
Python 3.x
```py
x = [1,2,3,4,5]
y = set(filter(lambda element: element%2==0,x)) #y = {2,4}

x = set(map(lambda x: x*x, range(1,10)))
# x = {1,4,9,16,25,36,49,64,81}
x = set(filter(lambda: x : x%7 == 1, range(1,100)))
# x = {1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99}
```
Other functions that work in a similar way as the build-in functions for list are:
**min, max, sum, any, all, sorted, reversed**

### Frozenset

Python language also has another type frozenset. A frozen set has all of the characteristics of a normal set, but it can not be modified. To create a frozen set use the frozenset keyword.
Python 3.x
```py
x = frozenset ({1,2,3})
x.add(10) #!!!ERROR!!!
```
### DICTIONARIES

A dictionary is python implementation of a hash-map container. Design as a (key – value pair) where Key is a unique element within the dictionary.
A special keyword dict can be used to create a dictionary. The { and } can also be used to build a dictionary – much like in the case of sets.

```py
x = dict() #x is an empty dictionary
x = {} #x is an empty set !!! (not a dict)
x = {”A”:1, ”B”:2} #x is a dictionary with 2 keys

#(“A” and “B”)

x = dict(abc=1,aaa=2) #equivalent to x= {”abc”:1, ”aaa”:2}
x = dict({”abc”:1,”aaa”:2}) #equivalent to x= {”abc”:1, ”aaa”:2}
x = dict([(”abc”,1) ,(”aaa”,2)]) #equivalent to x= {”abc”:1, ”aaa”:2}
x = dict(((”abc”,1) ,(”aaa”,2))) #equivalent to x= {”abc”:1, ”aaa”:2}
x = dict(zip([”abc”,”aaa”],[1,2]))#equivalent to x= {”abc”:1, ”aaa”:2}
```

Values from a dictionary can also be manipulated with **setdefault** method.

```py
x = {”A”:1, ”B”:2} #x = {”A”:1,”B”:2}
y = x.setdefault(”C”,3) #x = {”A”:1,”B”:2,”C:3”}, y=3
y = x.setdefault(”D”) #x = {”A”:1,”B”:2,”C:3”,”D”:None}, y=None
y = x.setdefault(”A”) #x = {”A”:1,”B”:2,”C:3”,”D”:None}, y=1
y = x.setdefault(”B”,20) #x = {”A”:1,”B”:2,”C:3”,”D”:None}, y=2
```

### Changing values in a dictionary

Method **update** can also be used to change the value associated with a key.
```py
x = {”A”:1, ”B”:2} #x = {”A”:1,”B”:2}
x.update({”A”:10}) #x = {”A”:10,”B”:2}
x.update({”A”:100,”B”:5}) #x = {”A”:100,”B”:5}
x.update({”C”:3}) #x = {”A”:100,”B”:5,”C”:3}
x.update(D=123,E=111) #x = {”A”:100,”B”:5,”C”:3,”D”:123,”E”:111}
```

To delete an element from a dictionary use **del** keyword or **clear** method

To create a new dictionary you can use **copy** or static method **fromkeys**
```py
x = {”A”:1, ”B”:2} #x = {”A”:1,”B”:2}
del x[”A”] #x = {”B”:2}
x.clear() #x is an empty dictionary
del x[”C”] #!!! ERROR !!! “C” is not a key in x

x = {”A”:1, ”B”:2} #x={”A”:1,”B”:2}
y = x.copy() #makes a shallow copy of x
y[”C”]=3 #x={”A”:1,”B”:2},y={”A”:1,”B”:2,”C”:3}
x = dict.fromkeys([”A”,”B”]) #x = {”A”:None,”B”:None}
x = dict.fromkeys([”A”,”B”],2)#x = {”A”:2,”B”:2}
```

### Extracting elements from a dictionary

If a value does not exists, an exception will be thrown when you try to access that value!!!

To check if it exists, use "in" operator.

**len** can also be used to find out how many keys a dictionary has.

Elements from the dictionary can also be accessed with method **get**

An element can also be extracted using **pop** method.
```py
x = {”A”:1, ”B”:2} #x = {”A”:1,”B”:2}
y = x.get(”A”) #y = 1
y = x.get(”C”) #y = None                        !!!!!!
y = x.get(”C”,123) #y = 123                     !!!!!!

x = {”A”:1, ”B”:2} #x={”A”:1,”B”:2}
y = x.pop(”A”) #x={”B”:2}, y = 1
y = x.pop(”C”,123) #x={”B”:2}, y = 123
y = x.pop(”D”) #!!! ERROR !!! Key “D” does not exists
#and no default value was provided
```

### Dictionaries and Functional Programming

A dictionary can also be built using functional programming
```py
x = {i:i for i in range(1,9)}
#x = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8}
x = {i:chr(64+i) for i in range(1,9)}
#x = {1:”A”,2:”B”,3:”C”,4:”D”,5:”E”,6:”F”,7:”G”,8:”H”}
x = {i%3:i for i in range(1,9)}
#x = {0:6,1:7,2:8} # last values that were updated      !!!!!!
x = {i:chr(64+i) for i in range(1,9) if i%2==0}
#x = {2:”B”, 4:”D”, 6:”F”, 8:”H”}
x = {i%3:chr(64+i) for i in range(1,9) if i<7}
#x = {1:”D”, 2:”E”, 0:”F”}
```

### Methods to obtain elements from a dictionary

Keys from the dictionary can be obtained with method **keys**

To iterate all keys from a dictionary:
```py
x = {”A”:1, ”B”:2} #x = {”A”:1,”B”:2}
y = x.keys() #y = [”A”,”B”] # an iterable object

x = {"A":1, "B":2}
for i in x:
    print (i)
x = {"A":1, "B":2}
for i in x.keys():
    print (i)
# both will print A B
```

Values from the dictionary can be obtained with method **values**

To iterate all values from a dictionary:
```py
x = {”A”:1, ”B”:2} #x = {”A”:1,”B”:2}
y = x.values() #y = [”1”,”2”]  an iterable object

x = {”A”:1, ”B”:2}
for i in x.values():
        print (i)

#Output: 1 2
```

*Output order may be different for different versions of python depending on how data is stored/ordered in memory.*

All pairs from a dictionary can be obtained using the method **items** (used in the same manner as above)
Output: ("A",1) ("B",2)

Sort items from a dictionary based on their value:
```py
for i in sorted(x.items(),key = lambda element : element[1]):
        print (i)
```
### Dictionaries and Functions

Operator ****** can be used in a function to specify that the list of parameters of that function should be treated as a dictionary.
```py
def GetFastestCar(**cars):
        min_speed = 0
        name = None
        for car_name in cars:

        if cars[car_name] > min_speed:

        name = car_name
        min_speed = cars[car_name]

        return name

fastest_car = GetFastestCar(Dacia=120,BMW=160,Toyota=140)
print (fastest_car)
#fastest_car = ”BMW”
```

Build-in functions such as **filter** can also be used with dictionaries.
```py
x = {

"Dacia" : 120,
"BMW" : 160,
"Toyota" : 140
}
y = dict(filter(lambda element : element[1]>=140,x.items()))
#y = {”Toyota”:140, ”BMW”:160}
```

To delete an entire dictionary use **del** keyword.

**enumerate** can also be used with dictionaries.
```py
x = {

"Dacia" : 120,
"BMW" : 160,
"Toyota" : 140,
"Volvo" : 115,
"Renault" : 120,
}
for a in enumerate (x):
        print (a)
```
In this case, the resulted touple contains the index and the key !


## Course 4 - Exceptions, Modules (sys and os), I/O, File management

## Course 5 - Custom Modules , Packages, Dynamic Code
