"""
import keyword

print("The list of keyword is : ")
print(keyword.kwlist)
"""
#None: This is a special constant used to denote a null value or a void. 
#It’s important to remember, 0, any empty container(e.g empty list) does not compute to None.
"""from trace import Trace


print(False == 0)
print(True == 1)

print(True + True + True)
print(False + False + False)

print(None == 0)
print(None == [])
"""
# showing logical operation
# or (returns True)
print(True or False) 
# showing logical operation
# and (returns False
print(False and True)
# showing logical operation
# not (returns False)
print(not True)
# using "in" to check
if 's' in 'srinivas':
    print("s is part of srinivas!!!")
    print("\n")
else:
    print("s is not part of srinivas!!!")
   
#using "in" to loop through    
for i in 'srinivas':
    print(i, end=" ")
    
    #print("\r")
# using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' ' is ' ')
# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})
