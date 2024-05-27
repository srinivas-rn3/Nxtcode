'''
Writing clean, readable, and maintainable code is essential in Python. 
The Python community adheres to a style guide known as PEP 8,
which provides conventions for writing code. Here’s an example
of well-written, PEP 8-compliant Python code that incorporates
functions, classes, and decorators.
'''
# Standard library imports should be placed at the top
import os 
import sys 

# Third-party imports
import requests 

# Local application/library specific imports
#from mypackage import mymodule 


def my_decorator_function(func):
    """A simple decorator that prints messages before and after a function call."""
    def wrapper(*args,**kwargs):
        print("Somehting is happening before the function the call")
        result = func(*args,**kwargs)
        print("Somehting is happening after the function the call")
        return result
    return wrapper 


@my_decorator_function
def greet(name,greetings="hello"):
    """Greet someone with a given greeting."""
    print(f"{greetings},{name}")


class Greeter:
    """Class that represents a greeter."""
    
    def __init__(self,name):
        self.name = name 
        
    def greet(self,greetings="Hello"):
         """Method to greet someone."""
         print(f"{greetings},{self.name}")

    @staticmethod
    def static_greet(name,greetings="Hello!!"):
     """Static method to greet someone."""
     print(f"{greetings},{name}!")

def main():
    """Main function to demonstrate the usage of the Greeter class and greet function."""
    greet("Alice!!")
    
    greeter = Greeter("Bob")
    greeter.greet()
    greeter.greet("Hi")    
    
    greeter.static_greet("Charlie","Hey")
    
if __name__ == '__main__':
    main()
    