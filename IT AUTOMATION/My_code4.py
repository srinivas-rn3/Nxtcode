
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
#Lambda keyword is used to make inline returning functions with no statements allowed internally. 
g = lambda x:x*x*x
print(g(7))    
    