
'''
x1 =5; y1 =5
x2 = 'Hello'
x3 = 'Hello'
y11 = [1,2,3]
y21 = [1,2,3]
#output : False
print(x1 is not y1)
#output : True
print(x2 is x3)
#output : False
print(y11 is y21)

'''
"""
Here, we see that x1 and y1 are integers of the same values,
so they are equal as well as identical. Same is the case with x2 and x3 (strings).

But y11 and y21 are lists. They are equal but not identical.
It is because the interpreter locates them separately in memory although they are equal.
"""
'''
Membership operators

'in' and 'not in' are the membership operators in Python.
They are used to test whether a value or variable is found in a sequence
(string, list, tuple, set and dictionary).
'''
'''
x = 'Hello World'
y = {1:'a', 2:'b'}
#output : True
print('H' in x)
#output : True
print(1 in y)
#output : False
print(1 in y)
#output : False
print('a' in y)
##https://www.programiz.com/python-programming/operators
'''

x = int(input("Enter the x value:"))
y = int(input("Enter the y value:" ))
if (x is not y):
    print("%d is x value and %d is y value.. Hence 56they are not same" %(x,y))
else:
    print ("%d is x value and %d is y value.. Hence they are same" %(x,y))