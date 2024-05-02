def log_function_call(func):
    def wrapper(*args,**kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args,**kwargs)
        print(f"Function {func.__name__} called suucessfully")
        return result 
    return wrapper 


#Lambda function decoratoed with function call logging 
decorated_lambda =  log_function_call(lambda x:x**2)

result = decorated_lambda(5)
print("Result:", result)
'''
my_lmabda = lambda x : x**2 # Define the lambda function separately

## Decorate the lambda function using @decorator_name syntax

deco = log_function_call(my_lmabda)
result = deco(10)
print(result)
'''