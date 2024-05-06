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