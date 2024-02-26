#Packing refers to putting multiple values into a single variable. 
# This is typically done with tuples in Python.
'''
my_tuple = 1,2,3 #Packing three values into a tuple

#Unpacking, on the other hand, involves extracting values from a collection
# (like a list or tuple) and assigning them to separate variables.
a,b,c = my_tuple # Unpacking the values from the tuple into separate variables

print(type(my_tuple))
print(type(a))
'''
'''
When to Use Packing and Unpacking:
Function Arguments:
Packing: When defining a function, you can use *args to accept a variable number of positional arguments as a tuple.
Unpacking: Inside the function, you can unpack *args to access individual arguments.
'''
'''
def my_function(*args):
    
    for arg in args:
        print(f"args {arg}")
    print("Number of arguments:",len(args))

my_function(1,2,3,4)
'''
'''
Returning Multiple Values from a Function:
Packing: You can return multiple values from a function as a tuple.
Unpacking: When calling the function, you can unpack the returned tuple into separate variables.
'''
'''
def get_values():
    return 1,2,3,4
# Unpacking the returned values
x,y,z,f = get_values()
'''
'''
To avoid this error, make sure the number of variables you're unpacking into matches the number of values returned by the function.
If you're uncertain about the number of values returned, you can use a single variable to collect them as a tuple:
'''
'''
def get_values1():
    return 1,2,3,4,5 #packing

# Unpacking the returned values
values = get_values1()
## Accessing individual values from the tuple
x,y,z = values[:3]
print(x,y,z)
#Alternatively, you can use * to collect all excess values into a single variable:
def get_values2():
    return 1,2,3,4,5,6 #Packing
#Unpacking the returned values, with * to collect all excess values into a single variable
x,y,z,*extra = get_values2()
print(x,y,z)
print(f"extra:{extra}")
'''
'''
Iterating Over Collections:
Packing: Collecting multiple values during iteration into a tuple.
Unpacking: Extracting values from collections like lists or tuples.
'''

my_list = [1,2,3,4,5,6]
#Packing while iterating
packed_values = [(x, x**2)for x in my_list]
print(packed_values)

#Unpacking while iterating
for values ,square in packed_values:
    print(f"Number:{values},Square:{square}")