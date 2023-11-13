
'''
Closure in Python is an inner function object, a function that behaves like an object, that remembers and has access 
to variables in the local scope in which it was created even after the outer function has finished executing. 
'''
'''
def divider(y):
    def divide(x):
        return x / y
    return divide 

d1 = divider(2)
d2 = divider(10)
print(d1(20))
print(d2(50))
'''
'''
def f1(x):
    def f2(y):
        return x+y 
    return f2 

d1=f1(10)
print(d1(10))
'''
def calc():
    num = 1 
    def inner_func():
        nonlocal num 
        num +=2
        return num 
    return inner_func

odd = calc()
print(odd())
print(odd())
print(odd())
odd2 = calc()
print(odd2())