#https://www.youtube.com/watch?v=Z7D9yv21tig&ab_channel=codebasics
'''
class Vehicle:
    def general_usage(self):
        print("general usage: transporation")
class Car(Vehicle):
    def __init__(self):
        print("I'm  car")
        self.wheel = 4
        self.has_door = 5
        self.has_roof = True
    def specific_usage(self):
        self.general_usage()
        print("specific usage: commute to work , vacation with family")

class MotorBike(Vehicle):
    def __init__(self):
        self.wheel =2
        self.has_door = 0
        self.has_roof = False
    def specific_usage(self):
        self.general_usage()
        print("specific usage: road trip,racing")

c = Car()
#c.general_usage()
c.specific_usage()

m = MotorBike()
#m.general_usage()
m.specific_usage()
print(isinstance(c,Car))
print(issubclass(Car,Vehicle))
print(isinstance(c,MotorBike))
'''
# Multiple Inheritance

'''
class Father():
    def gardening(self):
        print("I enjoy the gardening!!!!")
class Mother():
    def cooking(self):
        print("I love cooking!!!!")
class Children(Mother,Father):
    def sports(self):
        print("I enjoy sports!!!!")
c = Children()
c.sports()
c.gardening()
c.cooking()
'''
class Father():
    def skills(self):
        print("Gardening,Coding")
class Mother():
    def skills(self):
        print("cooking","art")

class child():
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("playing: VolleyBall,BasketBall")
c = child()
c.skills()
