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