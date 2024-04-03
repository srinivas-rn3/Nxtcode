#packing and unpacking Demo

#packing 
'''
def pack_value(*args):
    return args 

packed_values = pack_value(1,2,3,4)
print("Packing Values",packed_values)

#Unpacking
def unpack_values(a,b,c,d):
    return a,b,c,d 
unpack_values = unpack_values(*packed_values)
print("Unpacked values:",unpack_values)
'''
#packing and unpacking with dictionaries
def pack_dict(**kwargs):
    return kwargs 
packed_dict = pack_dict(name = "Alice", age = 30, city = "Wonderland")
print("Packed dicitionary:",packed_dict)


def unpack_dict(name,age,city):
    return name,age,city 
unpacked_dict = unpack_dict(**packed_dict)
print("Unpacked dictionary:",unpacked_dict)

'''
1. Packing and unpacking in Python typically refer to operations involving tuples, 
lists, and dictionaries.
2. where packing is the process of collecting multiple values into a single object
3. And unpacking is the process of extracting values from a packed object into separate variables.
'''
#Packing
#Tuple Packing: Creating a tuple by placing multiple comma-separated values inside parentheses.
my_tuple = 1,2,3,4
#List Packing: Creating a list by enclosing multiple values inside square brackets
my_list = [1,2,3,4]
#Dictionary Packing: Creating a dictionary using key-value pairs.
my_dict = {'a':1,'b':2,'c':3,'d':4}

#Unpacking: Extracting values from a packed object into separate variables.

#Tuple Unpacking: Assigning individual values from a tuple to separate variables.
a,b,c,d = my_tuple 
#List Unpacking: Assigning individual values from a list to separate variables
x,y,z,r = my_list
#Dictionary Unpacking: Extracting keys and values from a dictionary.
for key,value in my_dict.items():
    print(key,value)