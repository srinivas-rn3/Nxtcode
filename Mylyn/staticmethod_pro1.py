'''
In Python, a staticmethod is a built-in function that defines a method within a class 
that doesn't require access to the instance of the class itself. This means that 
the method does not implicitly pass the instance (self) to the method when it's called. 
It behaves similarly to a regular function but is defined within the scope of a class.
'''
class Math_operation:
    @staticmethod
    def add(a,b):
        return a + b 
    
    @staticmethod
    def sub(a,b):
        return a - b 

# You can call the static methods directly on the class without creating an instance
print(Math_operation.add(10,10))
print(Math_operation.sub(1,9))

#To check string is palindrome 

class Palindrome:
    @staticmethod
    def is_palindrome(word):
        # Remove spaces and convert to lowercase for case-insensitive comparison
        clean_word =  word.replace(" ","").lower()
        # Check if the word is equal to its reverse
        return clean_word == clean_word[::-1]
# You can call the static method directly on the class without creating an instance
print(Palindrome.is_palindrome("Hello"))
print(Palindrome.is_palindrome("radar"))

class Car:
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model 
    @staticmethod   
    def is_same_brand(car1,car2):
        return  car1.brand == car2.brand

#create instance of the class
car1 = Car("Toyota","Corollo")
car2 = Car("Honda","Civic")
car3 = Car("Toyota","Camry")

#Using the static method
print(Car.is_same_brand(car1,car2))
print(Car.is_same_brand(car1,car3))