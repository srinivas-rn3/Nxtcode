'''
# Define higher order function
def fun1(foo):
    result = foo('welcome!!!')
    return result

def fun2(str):
    return str.lower()

def fun3(str):
    return str.upper()

str1 = fun1(fun2)
print (str1)

str2 = fun1(fun3)
print(str2)
'''
'''
class check:
    def __init__(self):
        print("adddress of self :", id(self))
'''
'''
class car():
    def __init__(self,model,color):
        self.model = model
        self.color = color
    def show(self):
        print("Model", self.model)
        print("color", self.color)
        
audi = car("audi a4", "black")
ferrari = car("ferrari 488", "red")    

audi.show()
ferrari.show()

'''
'''
class game():
    def __init__(self,developer,gameName):
        self.developer = developer
        self.gameName = gameName
    def playGame(self):
        print("Myfavorite game developers :" , self.developer)
        print ("My favorite game is :" , self.gameName)
        
hello = game("Hello Game","The Last Campfire")
giant_squid_studios = game("giant squid studios", "The Pathless" )
print("##########################")
print("")
hello.playGame()
print("")
giant_squid_studios.playGame()
print("")
print("##########################")
'''
'''
a = 10

b = a 
print(b)
# Add and assign value
b += a 
print(b)
b -= a 
print(b)
# multiply and assign
b *= a 
print(b)
# bitwise lishift operator
b <<= a
print(b)

'''
'''
#is          True if the operands are identical 
#is not      True if the operands are not identical 

a = 10
b = 20
c = a
print(a is c)
print(a is not b)
'''
'''
#in            True if value is found in the sequence
#not in        True if value is not found in the sequence

a = 20 ; b =24 ;
list1 = [33,44,55,24,45]

if (a in list1):
    print("You are present in list1")
else:
    print("You are not present in list1")
if (b not in list1):
    print("you are not present in the list1 again!!!!")
else:
    print("You ae presnt in list1 again!!!")
'''
'''
# Examples of Operator Precedence
 
# Precedence of '+' & '*'

expr = 10 + 20 + 30 
print(expr)
# Precedence of 'or' & 'and'
name = "Alex"
age = 0
if name == 'Alex' or name == 'John' and age >= 2:
    print("Hello Welcome!!")
else:
    print("Not welcome!!!!")
'''
'''Ternary operators are also known as conditional expressions are 
#operators that evaluate something based on a condition being true or false.
syntax : [on_true] if [expression] else [on_false] 


a = 10 
b = 20 
min = a if a < b else b
print(min)
'''
'''
class A:
    def __init__(self, a):
        self.a = a 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
obj1 = A(1)
obj2 = A(2)
obj3 = A("geek")
obj4 = A("ten")

print(obj1 + obj2)
print(obj3+ obj4)
'''   
'''
class B:
    def __init__(self, a, b):
        self.a = a 
        self.b = b
        
        #addning two object
    def __add__(self, other):
        return self.a + other.a , self.b + other.b
object1 = B(2, 5)
object2 = B(5, 8)
object3 = object1 + object2
print(object3)
'''
'''

class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
     # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
 
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)
'''
#https://www.geeksforgeeks.org/operator-overloading-in-python/

class I:
    def __init__(self ,a):
        self.a = a
    def __lt__(self, other):
        if(self.a < other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is greater than ob1"
    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
ob1 = I(4)
ob2 = I(3)
print(ob1 < ob2)

ob3 = I(5)
ob4 = I(9)
print(ob3 == ob4)

       