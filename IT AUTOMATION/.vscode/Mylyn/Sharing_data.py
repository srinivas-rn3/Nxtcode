#https://www.youtube.com/watch?v=uWbSc84he2Q&ab_channel=codebasics

import multiprocessing 
'''
def calc_square(numbers,result):
    for idx,n in enumerate(numbers):
        result[idx]= n*n
   

if __name__ =='__main__':
    numbers = [2,3,4,5]
    result= multiprocessing.Array('i',4)
    p = multiprocessing.Process(target = calc_square,args=(numbers,result))
    p.start()
    p.join()
    print(result[:])
'''
'''
def calc_square(numbers,result,v):
    v.value = 5.67
    for idx,n in enumerate(numbers):
        result[idx]= n*n

if __name__ =='__main__':
    numbers = [2,3,4,5]
    result= multiprocessing.Array('i',4)
    v = multiprocessing.Value('d',0.0)
    p = multiprocessing.Process(target = calc_square,args=(numbers,result,v))
    p.start()
    p.join()
    print(result[:])
    print(v.value)
'''
'''
l1 = ['eat', 'sleep','repeat']
l2 = 'geek'

en1 = enumerate(l1)
en2 = enumerate(l2)

print("Return Type:", type(en1))
print(list(enumerate(l1)))
print(list(enumerate(l2,2)))
'''
'''
l1 = ['eat','sleep','repeat','fuck']
for ele in enumerate(l1):
    print(ele)
    
for count,ele in enumerate(l1):
    print(count,ele)
for count,ele in enumerate(l1):
    print(count)
    print(ele)
'''
#https://www.youtube.com/watch?v=sp7EhjLkFY4&ab_channel=codebasics
def Calc_Square(numbers,q):
    for n in numbers:
        q.put(n*n)

if __name__ =="__main__":
    numbers = [1,2,3,4,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=Calc_Square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())