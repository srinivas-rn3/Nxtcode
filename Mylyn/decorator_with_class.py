'''
EX:Decorator
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is  happening after the function is called")
    return wrapper 

@decorator
def say_hello():
    print("Hello!!") 
    
say_hello()   

def repeat_method(func):
    def wrapper():
        for _ in range(1,3):
            func()
    return wrapper 

@repeat_method
def print_hello():
    print("hello!!!")
print_hello()
    
'''
'''
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                func(*args,**kwargs)
        return wrapper 
    return decorator_repeat
@repeat(4)
def say_hello(name,greetings):
    print(f'{greetings},{name}')

say_hello('Helloo!!!','Alice')
'''

#Ex: class
class Dog:
    #Class attribute
    species =  'Canis Fmailies'
     
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old!!"
    
    def speak(self,sound):
        return f"{self.name} say {sound}"
    
# Creating an instance of the Dog class
my_dog = Dog("Buddy",2)
print(my_dog.description())
print(my_dog.speak("Woof Woof"))


#Ex:Decorator
def method_decorator(method):
    def wrapper(*args,**kwargs):
        print("Method is called")
        return method(*args,**kwargs)
    return wrapper 

class Myclass:
    @method_decorator
    def say_hello(self):
        print("Hello from Myclass!!")
        
obj = Myclass()
obj.say_hello()


#Class Decorators
#Class decorators are used to modify or enhance classes. 
#They work similarly to function decorators but take a class as an argument.

def class_decorator(cls):
    cls.extra_attribute = "This  is an extra attribute"
    return cls 


@class_decorator
class MYclass:
    def __init__(self,name):
        self.name = name 

obj = MYclass("Test")
print(obj.name)
print(obj.extra_attribute)


def add_method_decorator(cls):
    def new_method(self):
        print("This is the new method added by decorator!!")
        
    cls.new_method = new_method
    return cls 

@add_method_decorator
class MYCLASS:
    def __init__(self,name):
        self.name = name 
    
    def greet(self):
        print(f"Hello, {self.name}!!!")
# Creating an instance of MyClass
obj = MYCLASS("Alice")
obj.greet()
obj.new_method()    