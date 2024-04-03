'''
F-strings (formatted string literals): Introduced in Python 3.6, they provide a
concise and readable way to embed expressions inside string literals.
'''
name = 'Alice'
age = 30 
print(f"My name is '{name}' and I am '{age}' years old.")

'''
collections.namedtuple: Creates simple classes to store values, providing named fields.
'''

'''
collections.namedtuple is a function in the Python standard library's collections module that creates 
a new tuple subclass with named fields. It allows you to create simple classes that contain just a few 
named attributes without defining a full class. This can be particularly useful when dealing with simple 
data structures or when you need lightweight objects.
'''
from collections import namedtuple 

point = namedtuple('Point',['x','y'])
p = point(1,2)
print(p.x,p.y)

'''
itertools module: Offers a collection of fast, memory-efficient tools for working with iterators.
'''
from itertools import permutations, combinations
my_list = [1,2,4]
perms = permutations(my_list)
comb = combinations(my_list,2)
print(list(perms))
print(list(comb))

'''
functools.partial: Allows you to "freeze" some portion of a function's arguments and/or 
keywords, making a new callable with a simplified signature.
'''

'''
functools.partial is a function in the Python standard library's functools module that allows you to create
a new function with some of the original function's arguments "pre-set" or "frozen". 
This is particularly useful when you want to create a simplified version of a function with certain arguments already filled in.
'''
from functools import partial 

def power(base,exponent):
    return base ** exponent 

square = partial(power,exponent=2)
cube = partial(power,exponent=3)

print(square(3))
print(cube(10))