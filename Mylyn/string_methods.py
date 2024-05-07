'''
endswith() is a string method in Python that checks if a string ends with a specified suffix. 
It returns True if the string ends with the specified suffix, and False otherwise.

In Python, endswith() is a method. Specifically, it's a string method.

A method in Python is a function that belongs to an object. In this case, 
endswith() is a method that belongs to string objects.

When you call endswith() on a string, you're invoking that method on that
string object to perform a specific operation, which is checking whether the string
ends with a specified suffix.
'''
#Exmaple 1
email = 'xxx_b@xxx.com'
# Check if the email ends with ".com"
if email.endswith('.com'):
    print("The email address belong to a '.com' domain")
else:
    print("The email address not belong to '.com' domain")


#Example2
#.lower(): Converts all characters in a string to lowercase.
text = "Hello,Srinu!!"
print(text.lower())

#.upper(): Converts all characters in a string to uppercase.
print(text.upper())

#.strip(): Removes leading and trailing whitespace from a string.
text1 = "    Srinu Can we Talk   "
print(text1.strip())

#.split(): Splits a string into a list of substrings based on a delimiter.
text3 = "apple,|banana,|orange"
print(text3.split(',|'))

#.join(): Joins elements of an iterable (e.g., a list) into a string, using a specified separator.
fruits = ['apple', 'banana', 'orange']
print(','.join(fruits))

#.replace(): Replaces occurrences of a specified substring with another substring.
print(text.replace('Srinu','Srinu00'))

#.startswith() and .endswith(): Checks if a string starts or ends with a specified substring.
print(text3.startswith('apple'))
print(text3.endswith('orange'))
print(text3.endswith('apple'))
print(text3.startswith('banana'))

#.find() and .index(): Finds the index of the first occurrence of a substring within another string.
print(text.find('Srinu'))
print(text.index('Srinu'))

#.count(): Counts the occurrences of a substring within a string.
text4 = "apple,banana,orange,banana"
print(text4.count('apple'))
print(text4.count('banana'))

#.capitalize(): Capitalizes the first character of a string.
text5 = "hello srinu!!!"
print(text5.capitalize())