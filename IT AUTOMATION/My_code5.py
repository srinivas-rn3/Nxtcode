"""
# Python program processing
# global variable

count = 5 
def some_fun():
    global count 
    count = count + 1
    print(count)
some_fun()
"""
"""
# Python program showing
# a scope of object
def some_fun():
    print("Inside the fun.")
    def inner_fun():
        var = 10
        print("Inside the inner function var value is :", var)
    inner_fun() 
    print("priting var value:",var)
some_fun()
"""
'''
#Declared using Continuation Character (\)
s = 1 + 2 + 3 + 4 +5 + \
    6 + 7 + 8 
print(s) 
#Declared using parentheses () :
n = (1 * 2 * 3 + 7 + 9)
print(n)

#Declared using square brackets [] :

footballer = ['Messi',
              'CR',
              'Malpe']
print (footballer)

#Declared using braces {} :

x = {1 + 2 + 3 + 4}
print(x)
#Declared using semicolons(;) :
flag = 2; ropes =3;  pole = 4;
print (flag ,ropes ,pole) 

'''
'''
# Python program showing
# indentation

site = 'srinin'
if site == 'srini':
    print('logging srini!!!')
else:
    print('not valid logger!!!')
print("All the Best!!!")
'''
'''
j = 1 # Declaring integer value
while(j<100):
    print(j)
    j += 10 
'''
# Python 3 code to demonstrate variable assignment
# upon condition using One liner if-else
 
# initialising variable using Conditional Operator
# a = 20 > 10 ? 1 : 0 is not possible in Python
# Instead there is one liner if-else
a = 1 if 20 > 10 else 0
# printing value of a
print ("The value of a is:" + str(a))