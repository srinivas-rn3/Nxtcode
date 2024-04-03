'''
for _ in range(1,10):
    print("How are you!!")
'''
'''
In this example, set_attribute is the setter method, and get_attribute is the getter method.
The setter is used to set the value of _my_attribute, and the getter is used to retrieve its value.
'''
'''
class Myclass:
    def __init__(self):
        self._my_attribute = None 
    #Setter method
    def set_attribute(self,value):
        self._my_attribute = value
    #Gettter mrthod
    def get_attribute(self):
        return self._my_attribute
#Usage
obj = Myclass()
# Set value 
obj.set_attribute(45)
result = obj.get_attribute()
print(result)
'''
'''
# Using Property
class Myclass:
    def __init__(self):
        self._my_attribute = None 
    @property 
    def attribute(self):
        return self._my_attribute
    @attribute.setter 
    def attribute(self,value):
        self._my_attribute = value 
#Usage
obj = Myclass()
#Set Value 
obj.attribute = 90
result = obj.attribute
print(result)
'''

class Circle:
    def __init__(self,radius):
        self._radius = radius

    @property 
    def radius(self):
        return self._radius 

    @radius.setter
    def radius(self,value):
        if value < 0 :
            raise ValueError("Radius Connot be -ve")
        self._radius = value 

    @property 
    def area(self):
        return 3.14 * self._radius ** 2
#Usage
my_circle = Circle(radius=5)
#Get Radius
print("Radius is :",my_circle.radius)
#Get the area
print("Area:",my_circle.area)
#Set radius 
my_circle.radius = 10
print(f"Updated Radius and Area is {my_circle.radius} and {my_circle.area}")