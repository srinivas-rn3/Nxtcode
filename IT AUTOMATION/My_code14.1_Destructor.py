'''
##
#Destructors in Python
Destructors are called when an object gets destroyed. In Python, 
destructors are not needed as much as in C++ because Python has a 
garbage collector that handles memory management automatically. 
The __del__() method is a known as a destructor method in Python. 
It is called when all references to the object have been deleted 
i.e when an object is garbage collected. 
Syntax of destructor declaration : 
 

def __del__(self):
  # body of destructor
Note : A reference to objects is also deleted when the object goes 
out of reference or when the program ends. 
Example 1 : Here is the simple example of destructor. By using del 
keyword we deleted the all references of object ‘obj’, therefore destructor invoked automatically.
'''
'''
class Employee:
    def __init__(self):
        print("employee is created")
    #deleting (Calling Destructor)
    def __del__(self):
        print("Destructor is called!!")
obj = Employee()
del obj
'''
'''
class Employee:
    def __init__(self):
        print("Employee is created!!!")
    def __del__(self):
        print("Destructor is called!!!")
def create_object():
        print("Making object!!")
        obj = Employee( )
        print("function ends!!")
        return obj
print("Calling Create_object() function")
obj =create_object()
print("program end!!!!")
'''
from msilib.schema import BBControl

'''
class A:
    def __init__(self, bb):
        self.b = bb
        print("calling BB")
class B:
    def __init__(self):
        self.a = A(self)
        print("calling 'A'")
    def __del__(self):
        print("die!!!")
def fun ():
    b = B()
fun()
'''
class DarthVader:
    def __init__(self, darthvader):
        self.b = darthvader
        print("Dark force is more stronger!!")
        print("I will make you my 'apprentice'")
        print("come and join the dark force!!")
    def __del__(self):
        print("deleing the object for Dark Vader!!")
class Jedi:
    def __init__(self ,jedi):
        self.j = jedi
        print("come and join the force" )
        print("lets bring peace to galaxy!!")
        print("May the force be with you!!!")
    def __del__(self):
        print("deleing the object for Jedi!!")
#obj1 = DarthVader("dark")
#obj2 = Jedi("force")
print("Where you want to join!!!")
print("type '1' for Dark side & type '2' to join jedi")
a = int(input ("enter your choice: "))
if a == 1:
    print("")
    obj1 = DarthVader("dark")
else :
    print("")
    obj2 = Jedi("force")