#https://www.youtube.com/watch?v=Lu5LrKh1Zno&ab_channel=codebasics

import time
#from multiprocessing import Process
import multiprocessing
'''
def Calc_Square(numbers):
    for n in numbers:
        time.sleep(5)
        print("Square is {}".format(str(n*n)))

def Calc_Cube(numbers):
    for n in numbers:
        time.sleep(5)
        print("Cude is {}".format(str(n*n*n)))

if __name__ =='__main__':
    arr = [1,3,6,9,27,36]
    p1 = multiprocessing.Process(target=Calc_Square, args=(arr,))
    p2 = multiprocessing.Process(target=Calc_Cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("\nDONE!!!!")
'''
square_result = []
def Calc_square(numbers):
    global square_result
    for i in numbers:
        time.sleep(1)
        print("Square is {}".format(str(i*i)))
        square_result.append(i*i)
    print('within process:result' + str(square_result))

if __name__ =='__main__':
    arr = [1,3,5,7,9,12]
    p1 = multiprocessing.Process(target=Calc_square,args=[arr])
    p1.start()
    p1.join()
    print('result' + str(square_result))
    print("Done!!!")