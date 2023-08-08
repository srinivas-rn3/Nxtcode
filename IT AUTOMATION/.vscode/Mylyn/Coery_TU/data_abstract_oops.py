from abc import ABC,abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed Value:", x)
    @abstractmethod
    def task(self):
        print("We are inside the abstract class")

class test_class(Absclass):
    def task(self):
        print("We are inside the test_class")
class example_class(Absclass):
    def task(self):
        print("We are inside the example_class")
        
test_obj = test_class()
test_obj2 = example_class() 

test_obj.task()
test_obj.print(100)

test_obj2.task()
test_obj2.print(1222)

print("test_obj is instance of abstract class?",isinstance(test_obj,Absclass))
print("test_obj2 is instance of abstract class?",isinstance(test_obj2,Absclass))
#https://www.askpython.com/python/oops/abstraction-in-python