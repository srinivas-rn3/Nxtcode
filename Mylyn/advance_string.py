#String Formatting
name = "Alice"
age = 30
greetings = f"Hello , my name is {name} and I am {age} years old."
print(greetings)

#format() method: Allows more control over formatting
greetings1 = "Hello, my name is {}  and I am {} years old.".format(name,age)
print(greetings1)

#Old-style formatting (%): Still in use but less common.
greetings3 = "Hello, my name is %s and I am %d years old." %(name,age)
print(greetings3)

# Regular Expressions
import re 
text = "The quick brown fox jumps over the lazy dog"
pattern = r'\b\w{4}\b' # Matches words with exactly 4 letters
matches = re.findall(pattern,text)
print(matches)

'''
String Methods
Python provides many built-in string methods that can be used for string manipulation:
str.split(): Splits a string into a list.
str.join(): Joins elements of a list into a string.
str.replace(): Replaces a substring with another substring.
str.strip(): Removes leading and trailing whitespace.
'''
#String Encoding and Decoding
utf8_en = "Hello World!".encode('utf-8')
orginal_string = utf8_en.decode('utf-8')
print(utf8_en)
print(orginal_string)

#Checking the Type of a String
s = "Hello, World!"  # This is a Unicode string
print(type(s))

b = s.encode('utf-8')
print(type(b))

#String Interpolation
from string import Template
temp = Template('Hello,$name!')
result = temp.substitute(name ='Mia')
print(result)

'''
Class is a simple and flexible way to perform string substitution
Basic Usage of string.Template
The string.Template class uses $ to indicate placeholders:

Simple Substitution:

$variable: Replaces $variable with the value of variable.
${variable}: Use curly braces when the placeholder is followed by characters that are not part of the variable name
'''
# Define a template with placeholders
t1 = Template("Hello, $name! Welcome to $place")

# Substitute values for the placeholders
r1 = t1.substitute(name ='Angel',place ="Portland")
print(r1) 


#If you want to know the usage of a module and its functions in Python
'''
import math 
help(math)
#To get help on a specific function within the module:
help(math.sqrt) ## Displays documentation for the sqrt function

#Using dir() to List All Functions and Attributes
print(dir(math))

#Using __doc__ Attribute
print(math.__doc__)


import pydoc
pydoc.render(math,'Help on %s')
'''
'''
safe_substitute(): Similar to substitute(), but it won't raise a KeyError if a
placeholder is missing. Instead, it leaves the placeholder unchanged.
'''
template = Template("Hello!, $name and Welcome to $place")
result = template.safe_substitute(name='Mia')
print(result)

#Using a Dictionary for Substitution:You can pass a dictionary to the substitute() or safe_substitute() method.
template1 = Template("Hey!, your from $place and your name is $name is this correct.")
values = {"name": "Alice", "place": "Wonderland"}
result1 = template1.substitute(values)
print(result1)