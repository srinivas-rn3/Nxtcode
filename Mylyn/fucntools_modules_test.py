from functools import reduce,partial ,lru_cache,wraps
#partial
def power(base,exponent):
    return base ** exponent 

square = partial(power,exponent=2)
cube = partial(power,exponent=3)

print(square(2))
print(square(3))

#reduce
numbers = [1,3,5,7,9,11]
total = reduce(lambda x,y:x+y,numbers)
print(total)

'''
functools.lru_cache(): This function is a decorator that caches the results of a function, avoiding unnecessary 
re-computation when the same inputs occur again. It's useful for optimizing functions that are called 
frequently with the same arguments.
'''
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n 
    return fib(n-1) +fib(n-2)
print(fib(10))
print(fib(5))
print(fib(5)) # Output: 5 (computed instantly, using the cached result)
#nother example
@lru_cache(maxsize=2) #cache upto 2 recent call
def add(a,b):
    print("Calcualting the sum of",a, "and",b)
    return a + b

print(add(1,2))
print(add(3,4))
print(add(100,98900))

'''
functools.wraps(): This function is a decorator that copies metadata
(such as function name, docstring, module name) from the original 
function to the decorated function. It's useful for maintaining
introspection and debugging capabilities when decorating functions.
'''
def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Calling decorated functions")
        return func(*args,**kwargs)
    return wrapper
@my_decorator
def example():
    """ Docstring of exmaple function"""
    print("Called example function")

print(example.__name__)
print(example.__doc__)

'''

If you want to remove or disable the cache created by functools.
lru_cache, you can do so by setting the cache_clear() method 
of the decorated function. Here's how you can do it:
'''
@lru_cache(maxsize=2)
def my_func(x):
    return x * x

print(my_func(10))
print(my_func(12))

print(my_func(10))
my_func.cache_clear()   # Clear the cache
print(my_func(10))
print(my_func(100))