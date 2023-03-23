'''
If a condition does not meet our criteria but is correct according to the Python interpreter,
we can intentionally raise an exception using the raise keyword. 
We can use a customized exception in conjunction with the statement.

If we wish to use raise to generate an exception when a given condition 
happens, we may do so as follows:
'''
'''
num = [3,4,5,7]
if len(num) >3:
    raise Exception(f"Length is not defined perfectly . Not with statandards . lenght must be 3 but in our case its {len(num)}")
'''
'''
Python examines the adjacent expression,
preferably true when it finds an assert statement. 
Python throws an AssertionError exception if the result of the expression is false.
'''
'''
def square_root(num):
    assert (num < 0), "Give s +VE intger."
    return num**(1/2)

print(square_root(-36))
'''
'''
Try with Else Clause
Python also supports the else clause, which should come after every except clause, 
in the try, and except blocks. Only when the try clause fails to throw an
exception the Python interpreter goes on to the else block.

Here is an instance of a try clause with an else clause.
'''
'''
def reciprocal(num1):
    
    try:
        rec1 = 1/num1
    except:
        print("Cannot divide by zero!!!!")
    else:
        print(rec1)
print(reciprocal(0))
'''
'''
Finally Keyword in Python
The finally keyword is available in Python, and it is always used after the try-except block. The finally code block
is always executed after the try block has terminated normally or after the try block has terminated 
for some other reason.
'''
'''
try:
    dv = 4//0
    print(dv)
except ZeroDivisionError:
    print("cannot divide zero")
finally:
    print("Code is completed!!!")
'''
class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return(repr(self.value))
try:
    raise(MyError(3*2))
except MyError as error:
    print("A New excption occured:",error.value)
help(Exception)