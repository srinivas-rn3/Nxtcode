'''
Python Class and Objects
A class is a user-defined blueprint or prototype from which objects are created.
Classes provide a means of bundling data and functionality together. Creating a new class
creates a new type of object, allowing new instances of that type to be made.
Each class instance can have attributes attached to it for maintaining its state.
Class instances can also have methods (defined by their class) for modifying their state.

Class creates a user-defined data structure, which holds its own data members and member functions,
which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.

Some points on Python class:

1. Classes are created by keyword class.
2. Attributes are the variables that belong to a class.
3. Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

Class Definition Syntax:

class ClassName:
    # Statement-1
    .
    .
    .
    # Statement-N
'''
# Python3 program to
# demonstrate defining
# a class
#
#class Dog:
#    pass
'''
Class Objects
An Object is an instance of a Class. A class is like a blueprint while an 
instance is a copy of the class with actual values.It’s not an idea anymore, 
it’s an actual dog, like a dog of breed pug who’s seven years old. You can have many 
dogs to create many different instances, but without the class as a guide, you would be lost, 
not knowing what information is required.An object consists of : 

State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.

Declaring Objects (Also called instantiating a class)
When an object of a class is created, the class is said to be instantiated. 
All the instances share the attributes and the behavior of the class. 
But the values of those attributes,
i.e. the state are unique for each object. A single class may have any number of instances.
'''
'''
# Python3 program to
# demonstrate instantiating
# a class
class Dog:
    # A simple class
    # attribute
    atr1 = "Mammal"
    atr2 = "Dog"
    # A simple method
    def fun1(self):
        print("I'm a", self.atr1)
        print("I'm a", self.atr2)
# Driver code
# Object instantiation
Rodger =  Dog()
print(Rodger.atr1)
print(Rodger.atr2)
Rodger.fun1()
'''

'''
The self
Class methods must have an extra first parameter in the method definition. 
We do not give a value for this parameter when we call the method, Python provides it.
If we have a method that takes no arguments, then we still have to have one argument.
This is similar to this pointer in C++ and this reference in Java.
When we call a method of this object as myobject.method(arg1, arg2),
this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.
 

__init__ method
The __init__ method is similar to constructors in C++ and Java. Constructors are used to 
initializing the object’s state. Like methods, a constructor also contains a collection of 
statements(i.e. instructions) that are executed at the time of Object creation. 
It runs as soon as an object of a class is instantiated. The method is useful to 
do any initialization you want to do with your object.
'''
'''
class person:
     # init method or constructor 
     def __init__(self, name):
         self.name = name
    # Sample Method 
     def say_hi(self): 
         print("Hello, my name is :",self.name)
p = person("Srini")
p.say_hi()
'''
'''
class details1:
    def __init__(self,full_name,last_name):
        self.full_name = full_name
        self.last_name = last_name
    def person_details(self):
        print("My Full name is :", self.full_name)
        print("My last name is :", self.last_name)
myName = details1("srini", "RN")
myName.person_details()
print("")
myname1 = details1("Dani","Lopez")
myname1.person_details()

#https://www.geeksforgeeks.org/python-classes-and-objects/?ref=lbp
'''
'''
Class and Instance Variables
Instance variables are for data, unique to each instance and class variables
are for attributes and methods shared by all instances of the class. 
Instance variables are variables whose value is assigned inside a constructor or method 
with self whereas class variables are variables whose value is assigned in the class.
Defining instance variable using a constructor. 
'''
# Python3 program to show that the variables with a value 
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.
'''
#Class Dog
class Dog:
    #class variable
    animal = 'dog'
    # The init method or constructor
    def __init__(self,breed, colour):
        #Instance variable
        self.breed= breed
        self.colour = colour
#object of class 
Rodger = Dog("Pug","brown")
Buzo = Dog("Bulldog","black")

print("Rodger details:",end ="\n")
print("Rodger is a :", Rodger.animal)
print("Rodger Breed : ", Rodger.breed)
print("Rodger color :", Rodger.colour)
print("")
print("Buzo details:", end="\n")
print("Buzo is a :", Buzo.animal)
print("Buzo breed : " ,Buzo.breed)
print("Buzo color is :",Buzo.colour)
# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)
'''
#Defining instance variable using the normal method.

from turtle import color


class Cat:
    #class variable
    animal = 'Cat'
    #The init method or constructor
    def __init__(self, breed):
        self.breed = breed
    # Adds an instance variable 
    def setColor(self, color):
        self.color = color
    def getcolor(self):
        return self.color
#Driver Code
Meenu = Cat("Turkish Angora")
Meenu.setColor("white")
print(Meenu.getcolor())
print(Meenu.animal)