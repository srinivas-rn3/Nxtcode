import time 

def timing_and_counting(func):
    count = 0 # Closure variable to count the number of calls
    
    def wrapper(*args,**kwargs):
        nonlocal count 
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        count += 1 # Increment the count for each call
        print(f"Function'{func.__name__}' execution time:{end_time - start_time} seconds.")
        print(f"Function '{func.__name__}'has been called {count} times")
        return result
    return wrapper 

@timing_and_counting
def example1(n):
    return sum(range(n))
print(example1(10))
print(example1(1000))
