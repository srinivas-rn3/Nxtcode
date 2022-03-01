"""
myNumber = 3 
print (myNumber)

myNumber2 =4.5
print(myNumber2)

myNumber = 'srini'
print (myNumber)
"""
"""
# List

# Python program to illustrate a list 
  
# creates a empty list
list1 = []
# appending data in list
list1.append (21)
list1.append(40.5)
list1.append("srini")

print (list1)
"""
""" 
# Python program to illustrate
# getting input from user
name = input("Enter the name:")
# user entered the name
print ("Hello", name)
"""
"""
# Python3 program to get input from user
  
# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = int(input("Enter the number1 value: "))
num2 = int(input("Enter the number2 value: "))
num3 = num1 * num2
print ("product is:", num3)
num4 = num1 + num2
print ("Addition is:",num4)
"""
"""
# Python program to illustrate
# selection statement
num1 = 50
if(num1<20):
    print ("num1 is valid")
elif(num1>40):
    print ("num1 is not-valid.......")
else:
    print ("num1 is neutral no......")
"""
"""
# Python program to illustrate
# functions
def hello():
    print("Hello")
    print("srini!!!")
hello()
#caling fun
hello()
"""
"""
# Python program to illustrate 
# function with main
def getInt():
    int1 = int(input("Enter the interger no: "))
    return int1
def Main():
    # calling the getInteger function and 
    # storing its returned value in the output variable
    print("Started")
    output = getInt()
    print (output)
# now we are required to tell Python 
# for 'Main' function existence
if __name__ == "__main__":
    Main()
"""
"""
# Python program to illustrate
# a simple for loop

for step in range(10):
    print(step)
"""
import math

def Main():
    num = -90
     # fabs is used to get the absolute 
     # value of a decimal
    num = math.fabs(num)
    print(num)
    
if __name__=="__main__":
    Main()