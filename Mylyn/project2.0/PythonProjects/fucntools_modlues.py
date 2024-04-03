import functools 

'''functools.partial: functools.partial(func, *args, **keywords): Returns a 
new partial object which when called will behave like func called 
 with the positional arguments args and keyword arguments keywords'''
 
def multiply(x,y):
    return x * y 

# Create a new function using functools.partial
double = functools.partial(multiply,2)

# Now double behaves like multiply with one fixed argument (2)
print(double(4))


'''functools.reduce: functools.reduce(function, iterable[, initializer]):
Applies function of two arguments cumulatively to the items of iterable,
from left to right, so as to reduce the iterable to a single value.'''

from functools import reduce 

# Define a function that adds two numbers
def add(x,y):
    return x + y 

# Use reduce to sum all elements in a list
numbers = [1,3,5,7,9,11]
result = reduce(add,numbers)
print(result)

'''functools.wraps: functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES): 
This is a decorator for updating the attributes of the wrapping function to reflect the wrapped function.'''

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("Calling function....",func.__name__)
        return func(*args,**kwargs)
    return wrapper 
@decorator 
def example_function():
    """An example function."""
    print("Inside the exmaple_function")

# The original function's metadata is preserved
print(example_function.__name__) 
print(example_function.__doc__) 

'''The __doc__ attribute is used to access the documentation string (docstring) of a 
function or method. Docstrings are used to provide documentation about the purpose 
and usage of the function or method.'''