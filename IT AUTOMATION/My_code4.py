
"""
def fun():
    print("Inside the function!!!")
    
fun()    
"""
"""
def fun1():
    S = 0
    for i in range(10):
        #print(i)
        S += i
    return S
print(fun1())
"""
"""
# Yield Keyword

def fun():
    S = 0
    
    for i in range(10):
        S += 1
        yield S
        
for i in fun():
    print(i) 

    """
"""
# class example

class Dog:
    
    attr1 = "Mammal"
    attr2 = "dog"
    
    def fun(self):

     print("I'm a", self.attr1)
     print("I'm a", self.attr2)
# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()
"""
# using with statement
# with keyword is used to wrap the execution of block 
# of code within methods defined by context manager. This keyword is not used much in day to day programming.
"""
with open ("C:\\Users\\rnsri\\Desktop\\name.txt",'w') as file:
    file.write("Hello srini!!!")
"""
#as
#as keyword isused to create the alias for the module imported. 
#i.e giving a new name to the imported module. E.g import math as mymath.    
"""
import math as gfg
print(gfg.factorial(5))
"""
#pass is the null statement in python. 
#Nothing happens when this is encountered. This is used to prevent indentation errors and used as a placeholder.
"""
n = 10
for i in range(n):
    # pass can be used as placeholder
    # when code is to added later
pass
"""
"""
#Lambda keyword is used to make inline returning functions with no statements allowed internally. 
g = lambda x:x*x*x
print(g(7))    
""" 
"""
import math
print(math.factorial(5))
print("using from")

from math import factorial

print(factorial(5))
""" 
# initializing number
"""
a = 4
b = 0
try:
    k = a//b
    print(k)
except ZeroDivisionError:
    print("Can't Divide by zero")
finally:
    print("This always executed!!")

print("The value is a / b is:  ")       
assert b != 0, "Divide by 0 errro"
print(a/b)
"""
#'del' is used to delete a reference to an object. Any variable or list value can be deleted using del.

from numpy import delete


"""
my_A = 20
my_B = 'Geek'

print(my_A)
print(my_B)

# delete both the variables

del my_A ,my_B

print(my_A)
print(my_B)
"""

# global variable
a = 10
b = 20
# function to perform addition
def add():
    c = a+b
    print (c)
# Calling funcation add    
add()
   
def fun():
    var1 = 10
    
    def gun():
        nonlocal var1
        var1=var1 + 10
        print(var1)
    gun()
fun()

"""
'global' : This keyword is used to define a variable inside the function to be of a global scope.
'non-local' : This keyword works similar to the global, but rather than global, this keyword declares 
              a variable to point to variable of outside enclosing function, in case of nested functions.
"""