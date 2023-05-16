#https://www.geeksforgeeks.org/python-docstrings/
"""
def my_fun():
    '''Demo of tripple double quotes
    docstring and does nothing really'''
    return None 

print("Using __doc__:")
print(my_fun.__doc__)

print("using help:")
help(my_fun)

""" 
"""
#One-line Docstrings
def power(a,b):
    '''Return arg1 raised to power arg2.'''
    return a ** b
print(power.__doc__)
""" 
def myFunc(arg1):
    """
    Summary line.
    Extended description of functino
    
    parameters:
    arg1(int):Description of arg1 
    
    Return:
    int: Descriptino of return value
    """
    return arg1 
print(myFunc.__doc__)
help(myFunc)