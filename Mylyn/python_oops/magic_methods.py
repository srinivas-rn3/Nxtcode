'''
Magic methods in Python, also known as dunder (double underscore) methods, are special
methods that start and end with double underscores (__). They are predefined methods
that you can override to change the behavior of your objects. 
These methods allow you to define how objects of your class behave 
with built-in Python functions and operators.

Understanding other
In magic methods, 'self' refers to the current instance of the class, and 'other' 
refers to another instance of the class (or another object) that is being interacted
with. The other object is the one you are comparing to or performing an operation with.
'''

class Vector:
    def __init__(self,x,y):
        self.x, self.y = x, y
    
    def __repr__(self):
        return f"Vector({self.x},{self.y})"
    
    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y)
    
    def __eq__(self,other):
        return Vector(self.x == other.x ,self.y == other.y)
    
    def __len__(self):
        return int((self.x ** 2 +self.y ** 2)**0.5)
    
#Usage

v1 = Vector(10,25)
v2 = Vector(25,25)

print(v1,end='\n\n')
print(v2,end='\n\n')
print(v1 + v2)
print(v1 == v2)
print(len(v1))

#Example 2

class ComplexNumber:
    def __init__(self,real,imag):
        
        self.real = real
        self.imag = imag 
    
    def __repr__(self):
        return f"ComplesNumber({self.real},{self.imag})"
    
    def __add__(self,other):
        return ComplexNumber(self.real + other.real,self.imag + other.imag)
    
    def __eq__(self,other):
        #return ComplexNumber(self.real == other.real,self.imag == other.imag)
        return (self.real == other.real and self.imag == other.imag)
    
    def __abs__(self):
        return (self.real **2 + self.imag**2) ** 0.5

#Usage
c1 = ComplexNumber(10,5)
c2 = ComplexNumber(20,10)
c3 = ComplexNumber(20,10) 

# Printing the complex numbers
print(c1)
print(c2)
print("\n")
# Adding two complex numbers
c_sum = c1 + c2
print(c_sum)
print("\n")
# Checking equality
print(c1 == c2)
print(c2 == c3)
# Calculating the magnitude (absolute value) of a complex number
print(abs(c1))