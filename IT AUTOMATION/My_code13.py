'''
'''
#string1 = '''I'm the one who owns the time!!!'''
#print(string1)
#string2 = '''
#           I'm the one who ones the light
#          I'm creator of the Big Bang!!!
#           '''
#print(string2)
'''
'''

'''
Accessing characters in Python
In Python, individual characters of a String can be accessed by using the method of Indexing. 
Indexing allows negative address references to access characters from the back of the String,
e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 
'''
'''
string1 = "Man who Eats Time"
print("Initial string is : ")
print(string1)
print("first index is :")
print(string1[0])
'''
'''
String Slicing
To access a range of characters in the String, the method of slicing is used. 
Slicing in a String is done by using a Slicing operator (colon). 
'''
'''
string1 = "My Dog having black spots"
print(string1)
print("slicing")
print(string1[2:6])
print(string1[-4])
print(string1[-4:3])
##https://www.geeksforgeeks.org/python-strings/
'''
'''
Strings in Python can be formatted with the use of format() method which is a very versatile and
powerful tool for formatting Strings. Format method in String contains curly braces {} 
as placeholders which can hold arguments according to position or keyword to specify the order.
'''
'''
string3 = "{} {} {}".format('srini', 'life','sucks')
print(string3)
string4 = "{2} {0} {1}".format('srini','code','cool!!')
print(string4)
string5 = "{g} {f} {k}".format(g='srini',k='nova',f='love')
print(string5)
'''
'''
map() function returns a map object(which is an iterator) 
of the results after applying the given function to each item of a given iterable (list, tuple etc.)
syntax : map(fun ,iter)
Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

NOTE : You can pass one or more iterable to the map() function.

Returns :

Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) 
 
NOTE : The returned value from map() (map object) then can be
passed to functions like list() (to create a list), set() (to create a set) .
'''
'''
# Python program to demonstrate working
# of map.
  
# Return double of n
def addition1(n):
    return n + n
number  = (1,2,3,4)
result = map(addition1, number)
print(list(result))
'''
'''
num = (1,2,3,4)
result = map(lambda x: x+x ,num)
print(list(result))
'''
'''
num1 = [1,2,4]
num2 = [3,4,5]
result = map(lambda x ,y : x + y, num1,num2)
print(list(result))
'''
l = ['sat','mon','wed']
test = list(map(list , l))
print(test)