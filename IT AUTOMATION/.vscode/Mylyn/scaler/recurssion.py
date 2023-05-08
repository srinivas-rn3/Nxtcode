'''
Syntax:

def rec_func_name():
   if(condition)                       # base case
       simple statement without recursion
   else                                # general case
       statement calling rec_func_name()
'''
'''
def sum(n):
    if n <= 1: #Base case
       return n
    else:
        ans = sum(n-1)
    return n + ans 
print(sum(6))
'''
'''
#Example of a Tail Recursive Call
def disply(n):
    if n == 0:
        return #base case
    print(n)
    disply(n - 1)#tail recrussive call
disply(7)
'''
'''
#Example of a Call That is Not Tail-Recursive
def disply(n):
    if n ==0:
        return #base case
    disply(n -1)#not a tail  recusrsive call
    print(n)
disply(10)
'''
    
#Example of a Tail-Recursive Call
#GCD(a,b)=GCD(b,a/b)
'''
def GCD(a,b):
    if b == 0:
        return a #base case
    return GCD(b, a%b) #Tail recursive call 

print(GCD(49,35))
'''
#Example of a Call that is Not Tail-Recursive
'''
def fact(n):
    if n == 0:
        return 1
    return (n*fact(n-1)) #not a tail recusrrsive call
q = fact(5)
print(q)
'''
'''
def tailr(n):
    if n > 0:
        print(n,end=" ")
        tailr(n - 1)
p = 5
tailr(p)
'''
#Head Recursion 
#https://www.scaler.com/topics/python/recursion-in-python/
'''
def headr(n):
    if n > 0:
        headr(n-1)
        print(n,end=" ")

p = 5
headr(p)
'''
#Indirect Recursion
'''
def A(n):
    if n > 0:
        print("",n,end="")
        B(n +1)
def B(n):
    if n > 1:
        print("",n,end ="")
        A(n-5)
A(20)
'''
'''
def isDivisibleBy7(num):
    if num  < 0:
        return isDivisibleBy7(-num)
    if num == 0 or num == 7:
        return True 
    if num < 10:
        return False  
    return isDivisibleBy7(num //10-2 * (num - num // 10 * 10))

print(isDivisibleBy7(23))
'''
'''
def fact(n):
    if n == 1:
        return n 
    else:
        return n *  fact(n-1)
print(fact(1))
'''
'''
def fib(n):
    if n == 0:
        return 0 #best case
    elif  n == 1 or n == 2:
        return 1
    return(fib(n-1) +fib(n-2))
print(fib(8))
'''
'''
res = 0
start =1 
def rerverseDigit(num):
    global res 
    global start 
    if num > 0:
        rerverseDigit(int(num/10))
        res +=(num %10) * start
        start  *=10
    return res

print(rerverseDigit(456))
'''
#Recursion in Python with Strings and Arrays