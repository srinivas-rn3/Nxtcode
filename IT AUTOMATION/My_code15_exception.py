'''
Python Exception Handling
Difference between Syntax Error and Exceptions
Syntax Error: As the name suggests this error is caused by the wrong 
syntax in the code. It leads to the termination of the program. 

Example: 

# initialize the amount variable
amount = 10000
# check that You are eligible to
# purchase Dsa Self Paced or not
if (amount > 2999)
    print("your eligible!!!")
Exceptions: Exceptions are raised when the program is syntactically correct, but the code resulted 
in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.
# initialize the amount variable
marks = 10000
# perform division with 0
a = marks / 0
print(a)

In the above example raised the ZeroDivisionError as we are trying to divide a number by 0.
'''
'''
"Try and Except Statement – Catching Exceptions"
Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are
kept inside the try clause and the statements that handle the exception are written inside except clause.
'''
'''
# Python program to handle simple runtime error
#Python 3
a = [1,3,4,55]
try:
    print("second element is %d" %(a[1]))
     # Throws error since there are only 3 elements in array
    print("Forth element is %d" %(a[4]))
except:
    b = len(a)
    print("Haaaa there is no 4th element ")
    print("length of the list is", b)
'''
'''
In the above example, the statements that can cause the error are placed inside the try statement 
(second print statement in our case). The second print statement tries to access the fourth element of the 
list which is not there and this throws an exception. This exception is then caught by the except statement.

try:
    # statement(s)
except IndexError:
    # statement(s)
except ValueError:
    # statement(s)
'''
'''
# Program to handle multiple errors with one
# except statement
# Python 3
def fun1(a):
    if a < 4 :
        # throws ZeroDivisionError for a = 3
        b = a /(a-3)
    # throws NameError if a >= 4
    print("Value of b = ", b)

try:
    #fun1(3)
    fun1(5)
# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
    
except NameError:
    print("NameError Occurred and Handled")
'''
'''
Try with Else Clause
In python, you can also use the else clause on the try-except block which 
must be present after all the except clauses. The code enters the else
block only if the try clause does not raise an exception.
'''

# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
'''
def abcr(a, b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in '0'")
    else:
        print(c)
# Driver program to test above function
abcr(3,3)
abcr(89,56)
'''
'''
Finally Keyword in Python
Python provides a keyword finally, which is always executed after 
the try and except blocks. The final block always executes after 
normal termination of try block or after try block terminates due to some exception.

Syntax:

try:
    # Some Code.... 

except:
    # optional block
    # Handling of exception (if required)

else:
    # execute if no exception

finally:
    # Some code .....(always executed)
'''
# Python program to demonstrate finally
# No exception Exception raised in try block


'''
try:
    k = 5//0
    print(k)
except ZeroDivisionError:
    print("Can't divide zero!!")
finally:
     # this block is always executed
    # regardless of exception generatio
    print("Finally always executes!!!")
'''
'''
Raising Exception
The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates 
the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception).
'''
# Program to depict Raising Exception
try:
    raise NameError("Hi error")
except NameError:
    print("An Exception")
    raise # To determine whether the exception was raised or not
#https://www.geeksforgeeks.org/python-try-except/
