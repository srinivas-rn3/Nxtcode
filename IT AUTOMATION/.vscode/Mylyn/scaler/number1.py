'''
num1 = 112
num2 = 10.4
print("Data Type  of {} is {}".format(num1,type(num1)))
print("Data type of {} is {}".format(num2, type(num2)))
'''
#Inetger Number
'''
myNum1 = 1117
myNum2 = 0x1117
myNum3 = 0o1117
myNum4 = 0b1110

print("Data Type of num {} is {}".format(myNum1,type(myNum1)))
print("Data Type of num {} is {}".format(myNum2,type(myNum2)))
print("Data Type of num {} is {}".format(myNum3,type(myNum3)))
print("Data Type of num {} is {}".format(myNum4,type(myNum4)))
'''
#Float Number
'''
myNum = 12.78
print("Data Type  of {} is {}".format(myNum,type(myNum)))

m1 = 1.2;m2 = 2.2
sumofNum = m1 + m2
num3 = 3.4
isequal = num3 ==sumofNum
print("Sum of {} and {} is {}?:{}".format(m1,m2,num3,isequal))
'''
#Complex Numbers
'''
myNum = 3 +2j
print("Data Type of {} is {}".format(myNum,type(myNum)))
myNum = complex(3,2)
realPart = myNum.real 
imagPart = myNum.imag
print("Complex No is {}->Real part is {} and imaginary part is {}".format(myNum,realPart,imagPart))
'''
'''
#conjugate() method
myNum = complex(3,2)
conjugateNumber = myNum.conjugate()
print("Conjugate of {} is {}".format(myNum,conjugateNumber))
'''
'''
#Python Decimal
import decimal 
#myNum =  decimal.Decimal("11.11")
#print(type(myNum))


#You have to keep in mind that you must not convert a floating point number to a decimal number.

myNum = decimal.Decimal(12.22)
print("decimal value of {} and type is {}".format(myNum,type(myNum)))
'''
'''
#Python Fractions
import fractions 
#myNum = fractions.Fraction(1,2)
#print("Data Type of {} is {}".format(myNum ,type(myNum)))
#You can also convert a floating point value to fraction using the Fraction() method as follows.
myn = fractions.Fraction(0.5)
print("Data type  of {} is {}".format(myn,type(myn)))
'''
'''
#Data Type Conversion in Python
#String to Integer Conversion
#We can convert a string into an integer using the int() method. 
# The int() method takes the string as input and returns an integer value with base 10.
mystr = '1112'
myInt = int(mystr)
print("The data type is {} is {}". format(myInt,type(myInt)))
#Here, the string can contain only the combination of digits from 0 to 9. 
# If any characters other than these digits are present in the string, the int() method will raise ValueError.
mystr1 = '12.22'
myInt = int(mystr1)
print("Data type of {} is {}".format(myInt,type(myInt)))
'''
'''
#String to Float Conversion
#https://www.scaler.com/topics/python/numbers-in-python/

myString = "11.17"
myFloat = float(myString)
print(type(myFloat))
print(myFloat)

mystr = "11.12a1"
myflo = float(mystr)
print(type(myflo))
print(mystr)
#String to Decimal Conversion
'''
'''
#String to Decimal Conversion
import decimal 
myString = "11.11"
myfloat = decimal.Decimal(myString)
print(type(myfloat))
print(myfloat)

mystr = "11.34aw"
myfloat = decimal.Decimal(mystr)
'''
'''
#String to Fraction Conversion
import fractions 
mystring = "11/18"
myfloat = fractions.Fraction(mystring)
print(type(myfloat))
print(myfloat)
mystr ="11a/1"
myfloat = fractions.Fraction(mystr)
print(myfloat)
'''
'''
#Integer to Float Conversion
myInt = 1111
myFloat = float(myInt)
print("The datatype  of {} is {}".format(myFloat,type(myFloat)))
#Float to Integer Conversion
myFloat = 11.78
myInt = int(myFloat)
print("The data is {} and Datatype is {}".format(myInt,type(myInt)))
'''
'''
#Float to Decimal Conversion
import decimal 
myFloat = 11.22
myDec = decimal.Decimal(myFloat)
print("The data is {} and type {}".format(myDec,type(myDec)))
'''
'''
#Decimal to Float Conversion
import decimal 
myDec = decimal.Decimal(11.89)
myfloat = float(myDec)
print("The data is {} and type is {}".format(myfloat,type(myfloat)))
'''
'''
#Float to Fraction Conversion
#The limit_denominator() method takes
# the maximum allowed value which you want to set for the denominator and modifies the fraction according to it as follows.
import fractions 
myFlost = 11.44
myFrac = fractions.Fraction(myFlost)
NewmyFrac= myFrac.limit_denominator(100)
print("Data is {} and type is {}".format(NewmyFrac,type(NewmyFrac)))
'''
'''
#Fraction to Float Conversion
import fractions 
myFranc = fractions.Fraction("1111/200")
myFloat = float(myFranc)
print("Data is {} and type is {}".format(myFloat,type(myFloat)))

'''
'''
#Fraction to Decimal Conversion
import fractions,decimal 
myFrans = fractions.Fraction("1118/908")
myDec = decimal.Decimal(myFrans)
print("Data is {} and type is {}".format(myDec,type(myDec)))
'''
'''
#Decimal to Fraction Conversion
import fractions,decimal 
myDec = decimal.Decimal("11.89")
myFrac = fractions.Fraction(myDec)
print("Data is {} and type is {}".format(myFrac,type(myFrac)))
'''

#Python Math Module
'''
import math 
myNum = 11.13
#math.ceil():This function rounds a floating point number to the nearest integer greater than the number.
result = math.ceil(myNum)
print("Ceiling of {} is {}.".format(myNum,result))
'''
#When an integer is passed to the function as input, the output remains the same as the input number.
import math 
'''
myNum = 1117 
result = math.ceil(myNum)
print("Ceiling of {} of {}".format(myNum,result))
'''
'''
#math.floor():This function rounds a floating point number to the nearest integer less than the number given as input.
myNum = 11.17 
result = math.floor(myNum)
print("Floor of {}  is {}".format(myNum,result))
'''
'''
#When an integer is passed to the function as input, the output remains the same as the input number.
myNum = 1117
result = math.floor(myNum)
print(result)
'''
#math.exp():This function takes a number, say x as input and returns ex (exponential of x) .Here e is the Euler’s number having value 2.718282.
#https://www.scaler.com/topics/python/numbers-in-python/
'''
myNum = 11
result = math.exp(myNum)
print("Exponential of {} is {}.".format(myNum,result))
'''
'''
#math.factorial()
myNum =11 
result = math.factorial(myNum)
print("Factroial of {} is{}.".format(myNum,result))
'''
'''
As we know that factorial of a number is defined only for non negative integers,
if we pass a floating point value as input to the factorial() function, 
It raises ValueError exception with a message “ValueError: factorial() only accepts integral values”.`
'''
'''
myNum = 11.17
result1 = math.ceil(myNum)
print(result1)
result2 = math.floor(myNum)
print(result2)
result = math.factorial(result2)
print(result)
result4 = math.factorial(-112)
print(result4)
'''
'''
#math.gcd()
result = math.gcd(23,45)
print("Greatest common divisor of 23 and 45 is {}.".format(result))
result2 = math.gcd(1.2,22)
print(result2)
'''
'''
#math.log()
myNum = 5 

result = math.log(myNum,5)
#If there is no input given as base, the function calculates the natural log of the input number (with base e).
result1 = math.log(myNum)
result2 = math.log(-4)
print("Log of {} to base 5 is {}.".format(myNum,result))
print("Log of {} to {}.".format(myNum,result1))
print(result2)
'''
'''
#math.log10()
#The log10() function is used to calculate the logarithm of a positive number to the base 10. 
myNum  = 1172
result = math.log10(1172)
print("Log of {} to base 10 is {}.".format(myNum,result))
#Logarithms are not defined for 0 and negative numbers.
#myNum2 = -1172
#print(math.log10(myNum2))
#math.log2()
#The log2() function is used to calculate the logarithm of a positive number to the base.
result1 = math.log2(myNum)
print("Log of {} to base 2 is {}.".format(myNum,result1))
#Logarithms are not defined for 0 and negative numbers.
print(math.log2(-10))
'''
'''
#math.sqrt()
#The sqrt() function is used to calculate the square root of non negative numbers. 
myNum = 4
myNum2 = -4
result = math.sqrt(myNum)
result1 = math.sqrt(myNum2)
print("Square root of {} is {}.".format(myNum,result))
print("Square root of {} is {}.".format(myNum2,result1))
'''
#math.pow()
#The pow() function is used to calculate power of one number to another
#result = math.pow(2,3)
#print("2 raised to power 3 is {}.".format(result))
'''
#Trigonometric Functions
#math.sin():This function takes a number as input and returns its sine.
myNum = 110 

result1 = math.sin(110)
print("Sine of {} is {}.".format(myNum,result1))
#math.tan():This function takes a number as input and returns the tangent of the number.
result2 = math.tan(110)
print("Tan of {} is {}.".format(myNum,result2))
#math.cos():This function takes a number as input and returns its cosine.
result3 = math.cos(myNum)
print("Cos of {} is {}.".format(myNum,result3))
#math.asin():This function takes a number as input and returns its arc sine.
print("arc sine of ",math.asin(0.5))
#math.acos():This function takes a number as input and returns its arc cosine.
print("Arc cosine of ",math.acos(0.5))
#math.atan():This function takes a number as input and returns the arc tangent of the input number.
print("Arc tangent of ",math.atan(0.5))
'''
'''
Random Numbers in Python
If you want to generate random numbers for any use case like OTP generation or many more then you can use the 
random module in python for generating random numbers. You can import the module using the import statement as follows.
'''
import random 

myNum = random.random()
print("The random number is",myNum)
#To generate a random integer value, you can use the randint() function.
myNum2 = random.randint(0,1000)
print("The random number is", myNum2)