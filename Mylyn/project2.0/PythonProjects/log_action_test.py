'''
def log_action(action):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            args_str = ", ".join(map(repr, args))
            kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            print(f"{action}: {func.__name__}({args_str}, {kwargs_str})")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator


def log_functions(action):
    def decorator(func):
        def wrapper(self,*args,**kwargs):
            print(f"{action}:{func.__name__}({args},{kwargs})")
            return func(self,*args,**kwargs)
        return wrapper
    return decorator
'''
'''
#repr
x = 42 
print(type(x))
p=repr(x)
print(type(p))
print(p)
'''
'''
#Map()
number = [1,2,3,4,5]
l = map(lambda x :x**2,number)
print(list(l))
'''
'''
#repr and map(() exaple
import math 

# Example list of numbers
numbers = [4,9,16,25]

# Square roots of list
sqrt_values = list(map(math.sqrt,numbers))
# Using map to calculate a string represntation 
sqrt_str = "  ".join(map(repr,sqrt_values))

#print the result
print(f"square roots (vlaues):{sqrt_values}")
print(f"Square Roots (strng representation):{sqrt_str}")
print(type(sqrt_values))
print(type(sqrt_str))
'''
'''
Certainly! The join method in Python is a string method that concatenates elements of an 
iterable (e.g., a list) into a single string. It is called on a string and takes an iterable as its argument. 
The elements of the iterable are joined together with the string on which the method is called acting as the separator.
'''
'''
# Example list of word
words = ["Hello","World","Python"]
#Using join to concatenate element with a spces seperator
result = "|".join(words)
print(result)
'''