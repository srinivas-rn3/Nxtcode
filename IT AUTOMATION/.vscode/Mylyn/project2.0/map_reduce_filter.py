'''
Certainly! map, reduce, and filter are three built-in functions in Python that are commonly 
used for functional programming and data manipulation tasks.
'''


'''
1. map(function, iterable)
The map function applies a given function to each item of an iterable 
(e.g., list, tuple) and returns a map object (an iterator) containing the results.

'''

# Double each number in a list
numbers = [1,2,3,4,5,6]
doubled = map(lambda x:x *2,numbers)
print(list(doubled))

'''
2. filter(function, iterable)
The filter function constructs a new iterable from those elements of the iterable for which a function returns True.

'''
# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter(lambda x:x%2 ==0,numbers)
#print(list(even))
print(tuple(even))

'''
3. reduce(function, iterable, initializer)
The reduce function performs a rolling computation to combine elements of an iterable,
applying the function cumulatively to the items. It is part of the functools module in Python 3.x and needs to be imported.

from functools import reduce
reduce(function, iterable, initializer)

'''
from functools import reduce 
# Sum all numbers in a list
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x,y:x+y ,numbers)
print(sum_all)


#with tuple 
def square(x):
    return x *x
def is_evenx(x):
    return x % 2 == 0

my_tuple = (1, 2, 3, 4, 5)
# Using map() with a tuple
squared_tuple = map(square,my_tuple)
print(tuple(squared_tuple))
print(type(squared_tuple))

## Using filter() with a tuple
even_tuple = filter(is_evenx,my_tuple)
print(tuple(even_tuple))

