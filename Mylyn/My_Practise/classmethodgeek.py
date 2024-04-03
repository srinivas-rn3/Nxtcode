'''
The @classmethod Decorator
The @classmethod decorator is a built-in function decorator which 
is an expression that gets evaluated after your function is defined. 
The result of that evaluation shadows your function definition. 

A class method receives the class as the implicit first 
argument, just like an instance method receives the instance

'''
#Create class method using classmethod()
class Person:
     #age = 25

     def __init__(self,age):
         self.age = age

     def print_age(cls,age):
         print('The age is:',age)
## create printAge class method
Person.print_age = classmethod(Person.print_age)
Person.print_age(30)
'''
Factory methods are those methods that return a class object (like constructor) for different use cases.
'''
# Create factory method using class method
from datetime import date
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def frombirthyear(cls,name,birthYear):
        return cls(name, date.today().year - birthYear)
    
    def display(self):
        print(self.name + " 's age is " + str(self.age))

person = Person('Adam',19)
person.display()

person1 = Person.frombirthyear('John',1990)
person1.display()