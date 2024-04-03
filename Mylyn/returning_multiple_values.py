#https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
'''
# e.g:1
# A Python program to return multiple
# values from a method using class
class Test:
    def __init__(self):
        self.str  = 'Srinivas'
        self.x = 20
def func():
    return Test()

t = func()
print(t.str)
print(t.x)
'''
'''
#e.g:2

# A Python program to return multiple
# values from a method using tuple
 
# This function returns a tuple
def func():
    str = 'Black Hole in center'
    x = 20
    return str,x
str,x = func()
print(str)
print(x)
'''
'''
#e.g :3
# A Python program to return multiple
# values from a method using list
 
# This function returns a list

def func():
    str = 'geekforgeek'
    x = 20
    return [str,x]
list = func()
print(list)
'''
'''
# A Python program to return multiple
# values from a method using dictionary
 
# This function returns a dictionary
def func():
    d = dict()
    d['str']='In Center we found the blackhole'
    d['x'] = 20
    return d  
d = func()
print(d)
'''
'''
Using Data Class (Python 3.7+): In Python 3.7 and above the Data Class can be used 
to return a class with automatically added unique methods. The Data Class module 
has a decorator and functions for automatically adding generated special methods 
such as __init__() and __repr__() in the user-defined classes. 
'''
'''
from dataclasses import dataclass 
@dataclass 
class Book_list:
    name : str 
    perunit_cost :float
    quantity_avilable:int = 0

    def total_cost(self)->float:
        return self.perunit_cost * self.quantity_avilable 

book = Book_list("Journey to the center of the Earth",300,100)
x = book.total_cost()
# print the total cost
# of the book
print(x)
# print book details
print(book)

book1 = Book_list(name="Pyhton",
                  perunit_cost=450.5,
                  quantity_avilable=400)
print(book1)
y = book1.total_cost()
print(y)
'''
'''
def get_values():
    yield 42
    yield 'hello'
    yield [1,2,3]
test = get_values()
print(next(test))
print(next(test))
print(next(test))
'''
from dataclasses import dataclass
@dataclass
class Space:
    object1:str
    object_type:str
    telscope_name:str
    distance:float
    no_radio_telescope_x_axis:float
    no_radio_telescope_y_axis:float

    def space_count(self)->float:
        cal= self.no_radio_telescope_x_axis + self.no_radio_telescope_y_axis
        print(f"Radio telescope counted:",cal,"axis used to capture image")
        print("\n")

    def space_info(self):
        print(f"space object is "+self.object1+" and type is "+self.object_type+" and its observed by telescope "+self.telscope_name,end='\n')
        print("\n")

    def s_distance(self):
        print("Distance of the object is :",self.distance,"Lightyear",end='\n')
        print("\n")

    def travel_possible(self):
        if self.distance < 100:
            print("travel is possible we have spaceship to examine such space object!!!!")
            print("Spaceshipt 'RT-vulcon100' is suitable spaceship!!!")
            print("\n")
        elif self.distance >=100:
            print("With current distance is",self.distance,"Lightyear.","Not possible with current spaceship tech..."\
                  "Development is under process to go beyond 100 Ligtyears!!!!")
        else:
            print("Certainly not sure ask admin team!!!!")

s1 = Space("Pendora","exo-planet","Hubble",891,102.67,100.5)
s1.space_count()
s1.space_info()
s1.s_distance()
s1.travel_possible()