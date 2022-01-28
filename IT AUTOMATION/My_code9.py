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