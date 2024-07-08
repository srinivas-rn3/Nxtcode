'''
Abstraction
Abstraction means hiding the complex implementation details and showing only the necessary features of an object.
'''
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  
    
    @abstractmethod
    def perimeter(self):
        pass   
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width 
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10,20)
print(f"Area:{rect.area()}")
print(f"Perimeter:{rect.perimeter()}")

'''
Polymorphism
Polymorphism allows methods to do different things based on the object 
it is acting upon, even though they share the same name
'''
class Bird:
    def fly(self):
        print("Bird Flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def make_it_flying(flying_object):
    flying_object.fly()
    
bird = Bird()
sparrow = Sparrow()
airplane = Airplane()

make_it_flying(bird)
make_it_flying(sparrow)
make_it_flying(airplane)
