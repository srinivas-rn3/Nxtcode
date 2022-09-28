'''
class Human:
    def __init__(self,n,o):
      self.name = n
      self.occupation = o

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