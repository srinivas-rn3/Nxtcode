class Animal:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def sound(self):
        pass 

# Dog class inheriting from Animal
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed
    
    def sound(self):
        return "Woof!!!"

# Cat class inheriting from Animal
class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    
    def sound(self):
        return "Meow!!!"

# Create a list of animals
animals = [
    Dog("Buddy", 3, "Golden Retriever"),
    Cat("Whiskers", 2, "Black"),
    Dog("Charlie", 4, "Labrador"),
    Cat("Luna", 3, "White")
]

# Get information of all animals
animal_info = [f"{animal.name} is a {type(animal).__name__} and says {animal.sound()}" for animal in animals]
print("\nAnimal Information: ")
for info in animal_info:
    print(info)

# Filter dogs
dogs = [animal for animal in animals if isinstance(animal,Dog)]
dog_names = [dog.name for dog in dogs]
print("\nDog name:")
print(dog_names)

# Filter animals older than 2 years
older_animal = [animal for animal in animals if animal.age > 2]
older_animal_names = [animal.name for animal in older_animal]
print("\nAnimal older than 2 years: ")
print(older_animal_names)