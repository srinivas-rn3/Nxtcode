'''
class cat:
    def __init__(self , name ,age):
        self.age = age
        self.name = name
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} year old!!")
    def make_sound(self):
        print("Meooooow!!")

cat1 = cat('meenu' ,5)
cat2 = cat('ora', 2)
cat1.info()
cat2.info()
cat1.make_sound()
cat2.make_sound()
'''
'''
class point(object):
    
    def __init__(self,x = 0,y = 0):
        self.x = x; self.y =y;
    def distance(self):
        """Find distance from origin"""
        return(self.x**2 + self.y**2)**0.5
dis = point(3,3)
print(dis.distance())
'''
'''
class A(object):
    @staticmethod
    def start_meth():
        print("look no self is passed")
A1 = A()
A1.start_meth()
'''
#https://www.programiz.com/article/python-self-why#:~:text=The%20self%20keyword%20is%20used,information%20for%20both%20these%20objects.
'''
def inc(x):
    return x + 1
def dec(x):
    return x - 1
def operation(func, x):
    result = func(x)
    return result
d1 = operation(dec ,3)
print(d1)
'''
#main
'''
print("hello")
def main():
    print("Hello function")
if __name__ == "__main__":
    main()
'''
print(__name__)