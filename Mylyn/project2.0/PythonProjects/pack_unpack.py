'''
# Packing multiple values into a tuple
my_tuples =  10,20,30,'hello'
# This is equivalent to:
# my_tuple = (10, 20, 30, 'hello')
print(my_tuples)

# Unpacking a tuple into multiple variables
a,b,c,d = my_tuples
print(a)
print(b)
print(c)
print(d)
'''
'''
#Packing
def get_user_info():
    name = "Alice"
    age = 30 
    email = "alice@xxx.com"
    return name,age,email

user_info = get_user_info()
print(user_info)

#unpacking

name,age,email, = get_user_info()
print(name)
print(age)
print(email)
'''
'''
a=5;b=10

print(f"Before:The value of a {a} and The value of b {b}")
#Swap using unpacking
a,b = b,a
print(f"After:The value of a {a} and The value of b {b}")

#Unpacking elements of a list or tuple in a loop.
coordinates = (3,4,5)
#unpacking element in loop
for c in coordinates:
    print(c)
'''
'''
#Packing argument into a function
def add(*args):
    return  sum(args)
result = add(2,3,4,5,6)
print(result)

#Unpacking argument from a collection into a function
values = (1,2,3,4,5,6,7)
result = add(*values)
print(result)
'''
'''
In Python, the * operator is used for unpacking iterable objects like lists, tuples, or sets into separate elements. 
When used in a function call, it unpacks the elements of an iterable object and passes them as individual arguments to the function.
'''

# Unpacking using slicing
my_list = [1,2,3,4,5,6]
first,*middle,last = my_list
print(first)
print(middle)
print(last)

# Nested unpacking
nested_tuple = ((1, 2), (3, 4), (5, 6))
for (x,y) in nested_tuple:
    print(f"x:{x} and y:{y}")

# Unpacking items from a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key,value in my_dict.items():
    print(f"key:{key},value:{value}")