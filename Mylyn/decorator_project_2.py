import time   

def execution_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result =  func(*args,**kwargs)
        end_time = time.time()
        print(f"Execution time of function: {func.__name__}: {end_time - start_time} seconds")
        return result 
    return wrapper 

@execution_time
def example1():
    add = 100 + 900
    time.sleep(5)
    print("Function Executed")
    print(add)

example1()

