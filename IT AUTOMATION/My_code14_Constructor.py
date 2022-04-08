'''
Prerequisites: Object-Oriented Programming in Python, Object-Oriented Programming in Python | Set 2 
Constructors are generally used for instantiating an object. 
The task of constructors is to initialize(assign values) to the data members of the 
class when an object of the class is created. I
n Python the __init__() method is called the constructor and is always called when an object is created.
Syntax of constructor declaration : 
def __init__(self):
    # body of the constructor
"default constructor": The default constructor is a simple constructor which doesn’t accept any 
arguments. Its definition has only one argument which is a reference to the instance being constructed.

"parameterized constructor": constructor with parameters is known as parameterized constructor. 
The parameterized constructor takes its first argument as a reference to the instance being
constructed known as self and the rest of the arguments are provided by the programmer.
'''
'''
#Example of default constructor
class learn:
    #default constructor
    def __init__(self):
        self.learn = "python"
    #a method for printing data members
    def print_learn(self):
        print(self.learn)
# creating object of the class
obj = learn()
obj.print_learn()
'''
##Example of the parameterized constructor
class Calc:
    first = 0
    second = 0
    answer  = 0
    # parameterized constructor
    def __init__(self,f,s):
        self.first = f
        self.second = s
    def display(self):
        print("First number is :" +str(self.first))
        print("Second number is :" +str(self.second))
        print("Result of number is :" +str(self.answer))
    def calc_add(self):
        self.answer = self.first + self.second
    def calc_sub(self):
        self.answer = self.first - self.second
    def calc_mul(self):
        self.answer = self.first * self.second
# creating object of the class
# this will invoke parameterized constructor
obj = Calc(100,200)
# perform Addition
print("##Addition##")
obj.calc_add()
#display result
obj.display()
#perfrom subtraction
print("")
print("##Subtraction##")
obj.calc_sub()
#display result
obj.display()
#perfrom multiplication
print("")
print("##Multiplication##")
obj.calc_mul()
#display result
obj.display()