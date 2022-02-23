'''
A Python module is a file containing Python definitions and statements.
A module can define functions, classes, and variables. A module can also include runnable code.
Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.
'''
'''
def add (x, y):
    return(x+y)
def subtraction(x, y):
    return(x-y)
'''
'''
Import Module in Python –  Import statement
We can import the functions, classes defined in a module to another module
using the import statement in some other Python source file. 
'''
''''
import My_code11 as calc

print(calc.add(5,9))
print(calc.subtraction(10,9))
'''
'''
The from import Statement
Python’s from statement lets you import specific attributes from a module
without importing the module as a whole.
'''

# importing sqrt() and factorial from the
# module mat
'''
from math import sqrt, factorial
print (sqrt(16))
print (factorial(6))
'''
'''
Import all Names – From import *  Statement
The * symbol used with the from import statement is used to import 
all the names from a module to a current namespace.

The use of * has its advantages and disadvantages. 
If you know exactly what you will be needing from the module,
it is not recommended to use *, else do so.

'''
'''
# importing sqrt() and factorial from the
# module math

from math import *

# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.

print(int(sqrt(25)))
print(factorial(12))

'''
'''
Locating Modules
Whenever a module is imported in Python the interpreter looks for several locations. First, 
it will check for the built-in module, if not found then it looks for a list of directories defined in the sys.path. 

'''
'''
# importing sys module
import sys

# importing sys.path
print(sys.path)
'''
'''
Importing and renaming module
We can rename the module while importing it using the as keyword. 
'''
'''
# importing sqrt() and factorial from the
# module math
import math as g 
p = (g.sqrt(36))
print(int(p))
q = g.factorial(0)
print(q)
'''
'''
The dir() function
The dir() built-in function returns a sorted list of strings containing 
the names defined by a module. The list contains the names of all the modules, 
variables, and functions that are defined in a module.
'''
'''
import random
print(dir(random))
'''
'''
Python Random module is an in-built module of 
Python which is used to generate random numbers. These are pseudo-random 
numbers means these are not truly random. This module can be used to 
perform random actions such as generating random numbers, print random a
value for a list or string, etc.

Example: Printing a random value from a list
'''
'''
import random
list1 = [1,23,45,67,99,000,9999]
print(random.choice(list1))
'''
'''
As stated above random module creates pseudo-random numbers.
Random numbers depend on the seeding value. For example, if the seeding value 
is 5 then the output of the below program will always be the same.
Example: Creating random numbers with seeding value
'''
'''
import random as r

r.seed(5)
print(r.random())
print(r.random())
'''
'''
import math as m
import random as r
def math_fun(x):
    s =m.sqrt(x)
    q = m.factorial(x)
    q = m.sin(x)
    pi = m.pi
    t = m.tan(x)
    c = m.cos(x)
    print("sqrt: ",s)
    print("factorial:" ,q)
    print("pi:", pi)
    print("sin:", q)
    print("cos:", c)
    print("tan:", t)
def random_as(y):
    # printing random integer between 0 and 5
    print(r.randint(0,y))
    # print random floating point number between 0 and 1
    print(r.random())
    # random number between 0 and 100
    print(r.random()*100)    
    # using choice function in random module for choosing
    # a random element from a set such as a list
    list1 = [1,333,45,"srini",29]
    print(r.choice(list1))
print("random function execution:")
input1 = int(input("enter the intger value for random module:"))
random_as(input1)
print()
print("math functions:")
input2 = int(input("Enter the intger value for math module:"))
math_fun(10)
'''
## importing built in module datetime
'''
import datetime 
from datetime import date
import time
# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print(time.time())
# Converts a number of seconds to a date object
print(date.fromtimestamp(454554))
'''
'''
# Python3 code to demonstrate 
# Getting current date and time using  
# now(). 
    
# importing datetime module for now() 
import datetime as dt
# using now() to get current time 
current_time = dt.datetime.now()
#print("current date and time is ", end = "")
#print(current_time)
# Printing attributes of now().
print("Year: ", end = "")
print(current_time.year)
print("Month: ", end = "")
print(current_time.month)
print("Day: ", end = "")
print(current_time.day)
print("Hour: ", end = "")
print(current_time.hour)
print("Minute: ", end = "")
print(current_time.minute)
print("Second: ", end = "")
print(current_time.second)
print("Micro seconds: ", end ="")
print(current_time.microsecond)

'''
var1 = '*.cross.admlabs.aws.swinfra.net'
print(var1)