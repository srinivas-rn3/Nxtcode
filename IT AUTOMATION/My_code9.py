# Define higher order function
def fun1(foo):
    result = foo('welcome!!!')
    return result

def fun2(str):
    return str.lower()

def fun3(str):
    return str.upper()

str1 = fun1(fun2)
print (str1)

str2 = fun1(fun3)
print(str2)