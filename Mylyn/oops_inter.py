'''
Classes and Objects
Class: A blueprint for creating objects. It defines a set of attributes and methods that the created objects can use.
Object: An instance of a class.
'''
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} say woof!")
    
    def show_age(self):
        print(f"{self.name} age is {self.age}")

d = Dog('buddy',3)
d.bark()
d.show_age()
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

'''
Encapsulation
Encapsulation restricts direct access to some of an object's components, which can help prevent the accidental modification of data.
'''
class Person:
    def __init__(self,name,age,sex):
        self.__name = name 
        self.__age = age 
        self.sex = sex
    
    def get_name(self):
        return self.__name 
    
    def get_sex(self):
        return self.sex
    
    def set_age(self,age):
        if age > 0:
            self.__age = age 
        else:
            print("Age must be Postive number")
    
    def get_age(self):
        return self.__age 

# Accessing private variables through methods
person = Person("Jane",30,'f')
print(person.get_name())
print(person.get_age())
person.set_age(32)
print(person.get_age())
print(person.get_sex())
print(person.sex)

'''
Inheritance
Inheritance allows a class to inherit attributes and methods from another class. This promotes code reusability.
'''
class Animal:
    def __init__(self,name):
        self.name = name 
    
    def speak():
        pass
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} say woof!!!"

class  Cat(Animal):
    def speak(self):
        return f"{self.name} say meowww!!!"

dog = Dog("Buddy")
cat = Cat("Mimi")
print(dog.speak())
print(cat.speak())


#Encapsulation restricts access to certain methods and attributes to prevent data from being modified directly
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposite(self,amount):
        if amount > 0:
            self.__balance +=  amount 
    
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balnce(self):
        return self.__balance 

account = BankAccount(10000)
print(account.get_balnce())
account.deposite(500)
print(account.get_balnce())
account.withdraw(500)
print(account.get_balnce())

'''
Composition
Composition is a design principle that models a "has a" relationship.
'''
class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self,make,model,engine):
        self.make = make
        self.model = model 
        self.engine = engine 

engine = Engine(200)
car = Car('Ford','Mustang',engine)
print(f"{car.make} {car.model} with {car.engine.horsepower} hp")

#Composition e.g:2
class Vehicle:
    def __init__(self,name):
        self.name = name 
    
    def move(self):
        pass 
#Derived class Car
class Car(Vehicle):
    def move(self):
        return f"{self.name} drives on road."


# Derived class Boat
class Boat(Vehicle):
    def move(self):
        return f"{self.name} sails on water."

#Creating instances of Car and Boat
car = Car('Honda')
boat = Boat('Sailboat')

#List of vehicle
vehicles = [car,boat]

# Making all vehicles move
for vehicle in vehicles:
    print(vehicle.move())
    
    
    
#Example:Shapes Hierarchy

import math 

class Shape:
    def area(self):
        pass 
    
    def perimeter(self):
        pass 
# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width 
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Circle class inheriting from Shape

class Circle(Shape):
    
    def __init__(self,radius):
        self.radius = radius 
    
    def area(self):
        return math.pi  * self.radius **2
    
    def perimeter(self):
        return 2 * math.pi  * self.radius

# Function to print details of each shape
def print_shape_info(shape):
    print(f"Area: {shape.area():.3f}")
    print(f"perimeter:{shape.perimeter():.3f}")

# Function to calculate total area of shapes
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

# Usage of the classes and functions
shapes = [Rectangle(4,5),Circle(3)]
print("Total area of all shapes:{:.3f}".format(total_area(shapes)))

for shape in shapes:
    print("\nShape details: ",end="\n")
    print_shape_info(shape)

#####################################################
class Solid:
    def volume(self):
        pass 
    def  surface_area(self):
        pass   
    
# Cube class inheriting from Solid
class Cube(Solid):
    def __init__(self,side_length):
        self.side_length = side_length
    
    def volume(self):
        return 3 * self.side_length
    
    def surface_area(self):
        return 6 *( self.side_length **2)
    
# Sphere class inheriting from Solid
class Sphere(Solid):
    def __init__(self,radius):
        self.radius = radius
    
    def volume(self):
        return (4/3) * math.pi * (self.radius **3)
    
    def surface_area(self):
        return 4 * math.pi * (self.radius  **2)

# Function to print details of each solid with formatting
def print_solid_info(solid):
    solid_type = type(solid).__name__
    print(f"Solid Details for : {solid_type}")
    print(f"Volume: {solid.volume():.3f}")
    print(f"Surface Area: {solid.surface_area():.3f}")

# Creating instances of Cube and Sphere
cude = Cube(3)
sphere = Sphere(2)

solids = [cude,sphere]
for solid in solids:
    print("\n")
    print_solid_info(solid)
######################################
class ElectronicDevice:
    def battery_life(self):
        pass 
    
    def screen_size(self):
        pass
# Laptop class inheriting from ElectronicDevice
class Laptop(ElectronicDevice):
    def __init__(self,battery_hours, screen_inches):
        self.battery_hours = battery_hours 
        self.screen_inches = screen_inches
        
    def battery_life(self):
        return self.battery_hours
    
    def screen_size(self):
        return self.screen_inches
# Smartphone class inheriting from ElectronicDevice 
class Smartphone(ElectronicDevice):
    def __init__(self,battery_hours,screen_inches):
        self.battery_hours = battery_hours
        self.screen_inches = screen_inches
    
    def battery_life(self):
        return self.battery_hours
    
    def screen_size(self):
        return self.screen_inches

# Creating instances of Laptop and Smartphone
laptop = Laptop(10,15.6)
smartphone = Smartphone(24,6.5)


# List of electronic devices
devices = [laptop,smartphone]

for device in devices:
    print("\n")
    device_type = type(device).__name__
    print(f"Device Detials for : {device_type}")
    print(f"Battery Life : {device.battery_life():.1f} hours")
    print(f"Screen Size : {device.screen_size():.1f} inches")
    