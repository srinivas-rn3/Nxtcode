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

#Example 2

class Vehicle:
    def __init__(self, make,model,year):
        self.make = make 
        self.model = model
        self.year = year 
    
    def start_engine(self):
        print(f"{self.make} {self.model} engine started.")

class Car(Vehicle):
    def __init__(self,make,model,year,num_doors):
        super().__init__(make,model,year)
        self.num_doors = num_doors 
        
    def open_door(self):
        print(f"Opening {self.num_doors} doors on the {self.model}.")
        
class ElectricCar(Car):
    def __init__(self,make,model,year,num_doors,battery_range):
        super().__init__(make,model,year,num_doors)
        self.battery_range = battery_range
    
    def charge_battery(self):
        print(f"Plugging in {self.model} to charge (range:{self.battery_range}) KM.")
        
# Create a Vehicle object (not recommended for practical use)
# vehicle = Vehicle("Tesla", "Model S", 2024)  # Would lack specific methods
# Create a Car object
car = Car("Toyota","Camry",2020,4)
car.start_engine()
car.open_door()
print("\n")
# Create an ElectricCar object (inherits from Car and Vehicle)
electric_car = ElectricCar("Tesla","Model 3","2023",4,289)
electric_car.open_door()
electric_car.start_engine()
electric_car.charge_battery()

#Example3

class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary 
        
    def work(self):
        raise NotImplementedError("Subclass must implment abstract method.")
    
    def get_details(self):
        return f"Name: {self.name} and Salary:{self.salary}"

class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size = team_size
    
    def work(self):
        return f"{self.name} is managing a team of {self.team_size} people."
    
class Developer(Employee):  
    def __init__(self,name,salary,programming_lang):
        super().__init__(name,salary)
        self.programming_lang = programming_lang
        
    def work(self):
        return f"{self.name} is writing code in {self.programming_lang}."

# Create instances of Manager and Developer
manager = Manager('Sam',90000,10)
developer = Developer('Bob',80000,'Python')

# Call methods for each instance
print("\n")
print(manager.get_details())
print(manager.work())
print("\n")
print(developer.get_details())
print(developer.work())
print("\n")