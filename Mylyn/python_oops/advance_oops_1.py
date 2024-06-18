'''
Class Methods: These methods are bound to the class and not the instance. 
They can modify the class state that applies across all instances of the class. 
Class methods are defined using the @classmethod decorator and the first 
parameter is cls, which refers to the class itself.
'''
class Myclass:
    class_variable = 0 
    
    def __init__(self):
        Myclass.class_variable += 1
    
    @classmethod
    def get_class_method(cls):
        return cls.class_variable

m = Myclass()
print(m.get_class_method()) 


'''
Without @staticmethod Decorator
When you define a method without the @staticmethod decorator, 
it is treated as an instance method by default. This means it 
takes the instance (self) as its first parameter. 
You need to create an instance of the class to call the method.
'''
class MathOperation:
    def add(self,a,b):
        return a + b 
    
# Using the instance method
math_operation =  MathOperation()
result = math_operation.add(10,1000)
print(result)

'''
With @staticmethod Decorator
When you define a method with the @staticmethod decorator, it does not take 
the instance (self) or class (cls) as its first parameter. This means
you can call the method on the class itself without creating an instance.
'''
class MathOperation1:
    @staticmethod
    def add(a,b):
        return a + b 

# Using the static method
result = MathOperation1.add(10,111)
print(result)

'''
Abstract Base Classes (ABCs) in Python are a way to define a blueprint for a class,
specifyingcertain methods that must be implemented by any class that inherits from it. 
They allow you to define a common interface for a group of related classes 
without necessarily providing concrete implementations for all methods.

Python's abc module provides the necessary tools for defining and working
with ABCs. To create an ABC, you typically subclass abc.ABC or abc.ABCMeta.
You then use method decorators like @abstractmethod to mark methods as 
abstract, indicating that they must be implemented by concrete subclasses.
'''
import abc  
class Shape(abc.ABC):
    @abc.abstractmethod 
    def area():
        pass 

    @abc.abstractmethod
    def perimeter():
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side 

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side 


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius 
    
# Instantiating objects
square = Square(5)
circle = Circle(3)

# Using methods
print("Square Are:",square.area())
print("Circle Area:",circle.area())
print("Square perimeter:",square.perimeter())
print("Circle perimeter:",circle.perimeter())
