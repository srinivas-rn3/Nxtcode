
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() 
        print(func.__name__ +" took " +str((end-start)) + " seconds" )
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result = []
    for numbers in numbers:
        result.append(numbers*numbers)
    return result
@time_it
def calc_cube(numbers):
    result = []
    for numbers in numbers:
        result.append(numbers*numbers*numbers)
    return result

array = range(1,500000)
sq = calc_square(array)
cu = calc_cube(array)
print("sqaure is :", end ='\n')
print(sq)
print("####################")
print("cube is :", end ='\n')
print(cu)