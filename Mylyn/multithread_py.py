#https://www.youtube.com/watch?v=PJ4t2U15ACo&ab_channel=codebasics
import time 
from threading import *
'''
def Calc_square(numbers):
    print("Calculate square of numbers:")
    for i in numbers:
        time.sleep(0.2)
        print('sqaure is : ',i*i)

def Calc_cube(numbers):
    print("Calaculate cube of numbers:")
    for i in numbers:
        time.sleep(0.2)
        print('cube is : ',i*i*i)

arr = [2,3,4,5]
t = time.time()
#Calc_square(arr)
#Calc_cube(arr)
t1 = threading.Thread(target=Calc_square,args=(arr,))
t2 = threading.Thread(target=Calc_cube, args=(arr,))
t1.start()
t2.start()

t1.join()
t2.join()
print("Done in : ", time.time()-t)
print("Haah....Coding is done!!!!")
'''
'''
def print_hello():
    for i in range(20):
        if i == 10:
            time.sleep(2)
        print("Hello :",i)
def print_numbers(num):
    for i in range(num+1):
        print(i)
print("Greeting from main thread.")
thread1 = threading.Thread( target= print_hello,args=())
thread2 = threading.Thread(target = print_numbers,args =(20,))
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("It's main therad again")
print("Thread 1 & 2 have finished executing!!!")
'''
'''
def square1(numbers):
    for i in numbers:
        print(f'\nSqaure is {i}^2 = {i*i}')
        time.sleep(1)
def cube1(numbers):
    for i in numbers:
        print(f'\nCube is {i}^3 = {i*i*i}')
        time.sleep(1)

numbers=[1,2,3,4,5]
start = time.time()
t1 = threading.Thread(target = square1,args=(numbers,))
t2 = threading.Thread(target = cube1, args=(numbers,))
t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()
print("execution of time : {}".format(end-start))
'''
'''
def Thread1():
    print("I Am in thread1","Current Thread in Execution is",current_thread().name)
def Thread2():
    print("I Am in thread2","Current Thread in Execution is",current_thread().name)
t1 = Thread(target = Thread1,args=[])
t2 = Thread(target = Thread2, args=[])

t1.start()
t2.start()
'''
'''
Using the ThreadPoolExecutor
The easiest way to work with multiple threads is by using the ThreadPoolExecutor, 
part of the standard Python library. It falls under the concurrent.features library.

Using the with statement, you can create a context manager. 
It would enable you to create and delete a pool efficiently. 
We can also import the ThreadPoolExecutor directly from the concurrent.features library.
'''
from concurrent.futures import ThreadPoolExecutor
import random , threading

def task():
    print("Executing the given task!!!")
    result = 0
    i = 0 
    for i in range(10):
        result = result + i 
    print("I:{}".fomrat(result))
    print("The task is executed {}".format(threading.current_theread()))
def main ():
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task)
    task2 = executor.submit(task)

if __name__ == '__main__':
    main()