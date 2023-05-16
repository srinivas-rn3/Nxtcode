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