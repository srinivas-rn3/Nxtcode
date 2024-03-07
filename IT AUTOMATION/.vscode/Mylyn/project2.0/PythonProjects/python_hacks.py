'''
Swapping Values Without Temp Variable:
You can swap the values of variables without using a temporary variable by utilizing tuple unpacking.
'''
a = 5
b = 10
a,b = b,a 
print(a,b)

'''
Multiple Assignments in One Line:
Python allows you to assign multiple variables in a single line.
'''
a,y,z = 10,12,13
print(a,y,z)

'''
List Comprehensions:
List comprehensions offer a concise way to create lists.
'''
square = [x**2 for x in range(10)]
print(square)

'''
Dictionary Comprehensions:
Similar to list comprehensions, but for dictionaries.
'''
square_dict = {x: x**2 for x in range(10)}
print(square_dict)

'''
zip Function:
zip aggregates the elements of two or more iterables into tuples.
'''
list1 = [1,2,3]
list2 = ['a','b','c']
zipped = list(zip(list1,list2))
print(zipped)


'''
enumerate Function:
enumerate adds counter to an iterable and returns it as an enumerate object.
'''
for index,value in enumerate(['a','b','c']):
    print(index,value)


'''
collections.Counter:
Counter is a subclass of dictionary used to count hashable objects.
'''
from collections import Counter 
c = Counter('hello')
print(c)

'''
Unpacking Operator (*):
The unpacking operator * allows you to unpack iterables into function arguments or list elements.
'''
numbers = [1,2,3,4,5,6,7]
print(*numbers)

'''
'any' and 'all' Functions:
'any' returns True if at least one element of the iterable is true. all returns True if all elements of the iterable are true
'''
print(any([False,True,False]))
print(all([True,True,False]))

'''
Using defaultdict from collections:
defaultdict is a subclass of the built-in dict class. It returns a new dictionary-like object.
'''
from collections import defaultdict
d = defaultdict(int)
print(d)

#any and all example

# Example using all
list4 = [True, True, True]
list5 = [True, False, True]
list6 = [1, 'hello', [1, 2], {'a': 1}]  # Truthy values in Python

print(all(list4))
print(all(list5))
print(all(list5))

# Example using any
list1 = [False, True, False, False]
list2 = [0, '', None, [], False]  # Falsy values in Python
list3 = [0, '', None, [], False, 'hello']  # Contains both falsy and truthy values

print(any(list1))
print(any(list2))
print(any(list3))


fruits = ['apple', 'banana', 'cherry', 'date']
# Enumerate adds a counter to an iterable and returns it as an enumerate object
# The counter starts from 0 by default, but you can specify the starting value if needed
for index,value in enumerate(fruits):
    print(f"Index {index}: {value}")