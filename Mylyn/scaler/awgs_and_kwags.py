"""
def multiply(num1,num2):
    #return num1 * num2
    num3 = num1 * num2
    yield num3

a = multiply(2,3)
print(list(a))
""" 
'''
def mul(num1 ,num2):
    return num1 * num2
print(mul(5,5))
'''
'''
#multiple of three number
def mul3(num1,num2,num3):
    return num1 * num2 * num3
print("Product =\n",mul3(9,100,900))
'''
#*args can save you the trouble here.
'''
Python has *args, which allows us to pass a variable number of non-keyword arguments to a function. 
Non-keyword here means that the arguments should not be a dictionary (key-value pair), and 
they can be numbers or strings.
'''
'''
def mul(*numbers):
    p = 1
    for n in numbers:
        p *= n 
    return p
print(mul(1,2,3,4,5,6))
'''
#**kwargs in Python
'''
def makesent(**words):
    sentence = ''
    #In the makeSentence function, we are iterating over a dictionary, so we have to use values() to use the values. 
    # Otherwise, it will only return the keys and not the values.
    for word in words.values():
        sentence += word 
    return sentence 
print(makesent(a='kwargs ',b='are ',c='awesome '))
'''
'''
def whattechUse(**kwargs):
    result = []
    #In this code, we have used .items() because we want to get both the key and the value.
    for key,value in kwargs.items():
        result.append("{} uses {}".format(key,value))
    return result
print(whattechUse(Google ='Angular',Facebook='react',Microsoft='.Net'))
'''
#Using Both *args and *kwargs in a Python Function
'''
So if you are using standard arguments along with *args and **kwargs, then you have to follow this order-

Standard Arguments
*args
**kwargs
'''
'''
def printingData(codeName,*args,**kwargs):
    print("I'am",codeName)
    for arg in args:
        print("I Am arg:",arg)
    for k in kwargs.items():
        print("I AM Kwargs:",k)
        
printingData('007','agent',firstname = 'James', lastname='Bond')
'''
#Packing and Unpacking Using *args and **kwargs in Python

'''
The single and double asterisks that we use are called unpacking operators.

Unpacking operators are used to unpack the variables from iterable data types like lists, tuples, and dictionaries.

A single asterisk(*) is used on any iterable given by Python.

The double asterisk(**) is used to iterate over dictionaries.

'''
#carCompany = ['Audi','BMW','Lexus']
#print(*carCompany)
'''
Here the asterisk(*) passed before carCompany unpacked all the values. 
In other words, the values are printed as separate strings rather than a list.
'''
techStackOne = {"React" : "Facebook", "Angular" : "Google", "dotNET" : "Microsoft"}
techStack2 = {"Java":"Oracle"}
mergeStack = {**techStackOne,**techStack2}
print(techStackOne)
print(techStack2)
print(mergeStack)