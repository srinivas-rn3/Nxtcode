'''
def greet():
    print("Hello I'm IO",end = '\n')
def mydecor(fn):
    fn()
    print("I'm one of the moon of Jupiter planet")
mydecor(greet)
'''
'''
def mydecor(fn):
    def inner_function():
        fn()
        print("I'm IO moon of the Juipter")
    return inner_function

@mydecor
def greet():
    print("Hello Interstellar!!!", end = "\n")

greet()
'''
'''
from datetime import datetime
def log_datetime(func):
    def wrapper():
        print(f'function:{func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper
@log_datetime
def daily_backup():
    print('Daily backup job has finshed')

daily_backup()
'''

from datetime import datetime
from functools import wraps
import tracemalloc
from time import perf_counter

def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current,peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function:{func.__name__}')
        print(f'Method:{func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memoru usage:\t {peak / 10**6:.6f} MB')
        print(f'Time elased  is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper

@measure_performance
def make_list():
    '''Range'''
    my_list = list(range(1000))

@measure_performance
def make_list2():
    '''List comprehension'''
    my_list2 = {1 for l in range(1000)}

@measure_performance
def make_list3():
    '''Append'''
    my_list3 = []
    for i in range(1000):
        my_list3.append(i)

@measure_performance
def make_list4():
    '''Concatnation'''
    my_list4 = []
    for i in range(1000):
        my_list4 =  my_list4+[i]

print(make_list())
print(make_list2())
print(make_list3())
print(make_list4())

#Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters
#https://www.youtube.com/watch?v=jCzT9XFZ5bw

