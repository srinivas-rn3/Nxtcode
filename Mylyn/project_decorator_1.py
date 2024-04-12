'''
Create a Python script that implements a logging decorator. This decorator can be 
applied to any function to log its execution time, parameters, and return value. 
You can use the time module to measure execution time and the logging module 
to log information.
'''
import logging,time,sys,time

## Configure logging
log_file_location = r"C:\Users\srini\OneDrive\Documents\app.log"

#logging.basicConfig(filename = log_file_location,level=logging.INFO,format='%(asctime)s -- %(message)s',stream = sys.stdout)
logging.basicConfig(level=logging.INFO,format = '%(asctime)s -- %(message)s')
# Create a file handler to write logs to a file
file_handler = logging.FileHandler(log_file_location)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s  -- %(message)s'))
logging.getLogger('').addHandler(file_handler)
#Define the logging decorator
def log_function(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}.Execution time: {round(execution_time,3)} seconds.Returned:{result}")
        return result
    return wrapper
def sleep_time(func):
    def wrapper(*args,**kwargs):
        time.sleep(5)
        return func(*args,**kwargs)
    return wrapper

# Apply the decorator to a function
@log_function
@sleep_time
def example_function(x,y):
    return x + y

#Test the decorated function
result = example_function(100,10000)
print(f"Result: {result}") 

@log_function
@sleep_time
def example2(x,y):
    return x * y 

#Test the decorted function
result1 = example2(100,90)
print(result1)
