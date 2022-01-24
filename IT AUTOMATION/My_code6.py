
'''
# Python program showing 
# a use of input()
val = input("Enter value: ")
print (val)
'''
'''
# Program to check input 
# type in Python
num = input("Enter the value for number: ")
print(num)
name1 = input("Enter the name : ")
print(name1)

# Printing type of input value
print ("type of number", type(num))
print ("Type of name" , type(name1))
var1 = int(num)
print ("type of number",type(var1))
'''
'''
# Python program showing 
# a use of raw_input()

g = raw_input("Enter the name!!!  ")

print (g)
'''
'''
# input
a = input()
print(a)
'''
'''
#Typecasting int
num1 = int(input("Enter the integer value1 : ")) 
num2 = int(input("Enter the interger vlaue2 : "))
print (num2 + num1)
#Typecasting float
num3 = float(input())
num4 = float(input())
print(num3)
print(num4)
print (num3 - num4)
'''
'''
Using split() method : 
This function helps in getting multiple inputs from users. It breaks the given input by the specified separator. 
If a separator is not provided then any white space is a separator. 
Generally, users use a split() method to split a Python string but one can use it in taking multiple inputs.

'''
'''
# Python program showing how to
# multiple input using split
# taking two inputs at a time
x , y = input("Enter 2 values : " ).split()
print("number of boys :", x)
print("number of girls :", y)
'''
'''
# taking three inputs at a time
x ,y, z = input("Enter three values :").split()
print ("Total number of students : ",x)
print ("Totoal number of boys :",y)
print ("Total number of girls : ",z)
print()
'''
'''
# taking two inputs at a time
a ,b = input("Enter two values: ").split()
print ("The first number is {} and  second number is {}".format(a,b))
print()
'''
# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter the values: ").split()))
print (x)
#https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/