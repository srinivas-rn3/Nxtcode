'''
#Define Decorator a functions
def decorator1(func):
    def wrapper():
        print("Something is happening before the functions is called.")
        func()
        print("Somehting is happening after the functions is called.")
    return wrapper 

#Use  the decortaor  with the  @ syntax
@decorator1
def say_hello():
    print("Hello!!")

#Call the decorated functions
say_hello()
'''
'''
def upper_case_decorator(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        if isinstance(result,str):
            result = result.upper()
        return result 
    return wrapper 
#Apply the uppercase_decorator to a function
@upper_case_decorator
def greet(name):
    return f"Hello, {name}!"

#Call the decorator 
result = greet("srinivas")
print(result)
'''
'''
class Animal:
    pass 
dog = Animal()
cat = Animal()

print(isinstance(dog,Animal))
print(isinstance(cat,Animal))

# Check if an object is an instance of a tuple of classes
print(isinstance(dog,(int,str,Animal)))
print(isinstance(cat,(int,str,Animal)))

# Check if an object is an instance of any numeric type
print(isinstance('Hello',int))
print(isinstance(14,int))

#Check if an object is an instance of any numeric type
print(isinstance(3.4,float))
print(isinstance(3.14,(int,float)))

#Check if an object is an instance of a specific class or its subclass
class Mamal(Animal):
    pass 
whale = Mamal()
print(isinstance(whale,Animal))
print(isinstance(whale,Mamal))
'''
'''
def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                result = func(*args,**kwargs)
            return result 
        return wrapper 
    return decorator 

@repeat_n_times(3)
def greet(name):
    print(f"Hello , {name}")
    
greet("Alice")
'''
for _ in range(10):
    print(_)