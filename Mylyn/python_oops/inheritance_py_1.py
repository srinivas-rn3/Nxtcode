'''
In Python, inheritance allows a class to inherit attributes and methods from another class. 
This facilitates code reuse and promotes the concept of hierarchical relationships among classes
'''

class Animal:
    def __init__(self,name):
        self.name = name 
    
    def speak(self):
        raise NotImplementedError("Subclass must to implmented abstract method.")

class Dog(Animal):
    def speak(self):
        return f"{self.name} say woof!!!"

class Cat(Animal):
    def speak(self):
       return f"{self.name} say Meow!!!" 
    #pass 
#if speak method() not used in class NotImplementedError exeception raise
'''
The NotImplementedError exception is raised when an abstract method, like speak() 
in the example, is called but not implemented in a subclass.
When this exception is raised, it indicates that the method should have been overridden by the subclass but wasn't.
'''

#Create instances of Dog and Cat
dog = Dog('Buddy')
cat = Cat('Whiskas')

#call the speak method for each instance
print(dog.speak())
print(cat.speak())