#import time
#import multiprocessing as m
'''
def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()
if __name__ == '__main__':
    balance =  m.Value('i',200)
    lock = m.Lock()
    d = m.Process(target = deposit, args = (balance,lock))
    w = m.Process(target= withdraw,args = (balance,lock))

    d.start()
    w.start()
    d.join()
    w.join()
    print("balance is {}".format(balance.value))
'''
#https://www.youtube.com/watch?v=_1ZwkCY9wxk&ab_channel=codebasics
#Multiprocessing Pool (Map Reduce)
'''
def f(n):
    return n*n

if __name__ =='__main__':
    arr = [1,2,8,99,75]
    
    result = []
    for i in arr:
        result.append(f(i))
    print("result", result)
'''
from multiprocessing import Pool
import time 
'''
def f(n):
    return n*n

if __name__ == '__main__':
    arr = [3,5,7,9,11]
    p = Pool()
    result = p.map(f,arr)
    print("result",result)
'''
'''
def f(n):
    sum = 0 
    for x in range(n):
        sum += x*x
    return sum

if __name__ =="__main__":
    
    t1 = time.time()
    p = Pool()
    result = p.map(f,range(10))
    p.close()
    p.join()
    print(result)
    print("Pool took",time.time()-t1)
    
    result1 = []
    t2 = time.time()
    for x in range(10):
        result1.append(f(x))
    print(result1)
    print("serial pool took",time.time()-t2)
'''
for i in range(10):
    print("Hello World!!")