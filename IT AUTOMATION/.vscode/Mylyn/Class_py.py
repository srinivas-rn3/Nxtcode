'''
class Human:
    def __init__(self,n,o):
      self.name = n
      self.occupation = o
x   
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"Plays Tennis")
        elif self.occupation == "actor":
            print(self.name,"Shoot a film")

    def speaks(self):
        print(self.name,"Say How Are you?")
tom = Human("Tom Cruise","actor")
tom.do_work()
tom.speaks()
maria = Human("Maria Sharpova", "tennis player")
maria.do_work()
maria.speaks()
'''
'''
class calc:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        try:
            return self.x / self.y
        except ZeroDivisionError as e:
            print("Zero by error\n")
            return None

x1 = int(input("enter the no. : "))
x2 = int(input("Enter the No. : "))
print("\n")

z = calc(x1,x2)

print("addition value is: ",z.add())
print("Subtraction value is: ",z.sub())
print("Multilcation vlaue is: ", z.mul())
print("Divion value is: ", z.div())
'''
'''
class polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputsides(self):
        self.sides = [float(input("Enter sides "+str(i+1)+" : "))for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Sides",i+1,"is",self.sides[i])

class Tringle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
    def FindArea(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))** 0.5
        print("The area of the triangle is %0.2f" %area)

t= Tringle()
t.inputsides()
t.dispSides()
t.FindArea()
'''
'''
class TakeINputs():
    def __init__(self,no_of_inputs):
        self.n = no_of_inputs
        self.inputs = [0 for i in range(no_of_inputs)]
    def Inputs_by_user(self):
        self.inputs = [int(input("Enter the int vlaues "+str(i+1)+" : "))for i in range(self.n)]
    def Display_inputs(self):
        for i in range(self.n):
            print("No. inputs are ", i+1, "is",self.inputs[i])
a=TakeINputs(4)
a.Inputs_by_user()
a.Display_inputs()
'''
class inputs():
    def __init__(self,no_of_inputs):
        self.n = no_of_inputs
        #self.no = [0 for i in range(no_of_inputs)]
    def call_inputs(self):
        self.no = [int(input("enter the values"+str(i+1)+":"))for i in range(self.n)]
    def display(self):
        for i in range(self.n):
            print("No. Inputs are", i+1, "is", self.no[i])
            
a = inputs(3)
a.call_inputs()
a.display()