'''
x =[1,2,3,4,5]
print (x)
print(x[1:3])
""" In the above mentioned format, the first 
index is included, but the last index is not
included."""

"""Multiple Statements per Line We can also write multiple statements per line, but it is 
not a good practice as it reduces the readability of the code. Try to avoid writing multiple 
statements in a single line. But, still you can write multiple lines by terminating 
one statement with the help of ‘;’. ‘;’ is used as the terminator of one statement in this case."""
a = 10; b = 5; c = 6; d = a + b + c;

print(a);print(b);print(c);print(d)
'''
'''
# Example 2
# The following code is also valid
  
person_1 = 10 
person_2 = 20
person_3 = 30

if (
    person_1 >=10 and 
    person_2 >=15 and
    person_3 >= 30
):
    print("I'm Stupid!!!")
'''
'''
x = \
    1 + 10 \
    + 15 + 10 \

print(x) 
'''
'''
x = 10
while(x != 0):
    if (x > 5):
        print("X > 5")
    else:
        print("X < 5")    
    x -= 2
"""
Lines 1, 3, 5 are on same level
Line 2 will only be executed if if condition becomes true.
Line 4 will only be executed if if condition becomes false.
"""
'''

#Instead of writing this massive Python code
#we can also code this in a different way
 
#Python code to demonstrate working of iskeyword()
 
# importing "keyword" for keyword operations
'''
import keyword
keys = keys = ["for", "while", "tanisha", "break", "sky",
"elif", "assert", "pulkit", "lambda", "else", "srini"]

for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i] + "-is python keyword!!!")
    else:
        print(keys[i] + "-is not keyword!!!")    
'''     
'''
import keyword
print("The list of keywords are :")
print(keyword.kwlist)
'''
'''
# Create a new dictionary
d = dict()
d['xy'] = 123
d['zz'] = 234
# print the whole dictionary
print(d)
# print only the keys
print(d.keys())
# print only values
print(d.values())
# iterate over dictionary
for i in d:
    print("%s  %d" %(i ,d[i]))
# check if key exist
print("xy" in d)
# delete the key-value pair
del d['xy']

# check again
print("xy" in d)

#https://www.geeksforgeeks.org/python-set-4-dictionary-keywords-python/?ref=rp
'''
'''
break, continue, pass in Python 
break: takes you out of the current loop.
continue: ends the current iteration in the loop and moves to the next iteration.
pass: The pass statement does nothing. 
      It can be used when a statement is required. syntactically but the program requires no action.
'''
'''
arr = [1,2,3,4,5,5,6,7]
def break_test(arr):
    for i in arr:
        if i == 5:
            break
        print("break:", i)
    print("")
#array values
break_test(arr)
            
# Function to illustrate continue in loop
def cont_loop(arr):
    for i in arr:
        if i == 5:
            continue
        print("continue:",i)
        
    print("")
cont_loop(arr)
pass
'''
'''
map: The map() function applies a function to every member of iterable and returns the result. If there are multiple arguments, map() returns a list consisting of tuples containing the corresponding items from all iterables.
filter:  It takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence for which the function returned True.
lambda: Python provides the ability to create a simple (no statements allowed internally) anonymous inline function called lambda function. Using lambda and map you can have two for loops in one line.
'''
'''
item1 = [1,2,3,4,5]
#Using map function to map the lambda operation on items
cubes = list(map(lambda x : x**3,item1))
print(cubes)

smp =list(map(lambda x : x*2, item1))
print(smp)

def lam(cur):
    print("type value", cur)
    val = list(map(lambda y : y+2+10,cur))
    print("Calling Cur fun:")
    print(val)
    print("")
a = [1,4,8,9]
lam(a)
'''
#print((lambda x,y:x + y)(3,4))
'''
def fly(x,y):
    z = (lambda x, y : x ** y)(x,y)
    print(z)
    
fly(1,1)
'''
'''
#Using filter function to filter all
# numbers less than 5 from a list
num_list= range(-10, 10)
less_than_five = list(filter(lambda x : x < 5, num_list))
print(less_than_five)
'''
# Find the number which are odd in the list
# and multiply them by 5 and create a new list
 
# Declare a new list
#x = [2, 3, 4, 5, 6]
'''
y = []
for v in x:
    if v % 2:
        y+= [v*5]
print(y)
'''
x = [2, 3, 4, 5, 6]
y = map(lambda v : v * 5, filter(lambda u : u % 2, x))
print(y)