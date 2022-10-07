#https://www.youtube.com/watch?v=PJ4t2U15ACo&ab_channel=codebasics
import time 
import threading 

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