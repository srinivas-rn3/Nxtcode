#https://learnpython.com/blog/map-filter-reduce-python/
#map() takes a function and one or more iterables as arguments. The output is an iterator that returns the transformed items.
'''
num = [2,3,5,7,9]
cube = []
for i in num:
    cube.append(i ** 3)
print(cube)
#map() can achieve the same result without a for loop:
def cube(n):
    return n ** 3
num = [2,3,5,7,9,11,13]
cubed = map(cube,num)
print(list(cubed))
'''
''''''
num = [2,3,5,7,9,11,13]
cubed = map(lambda x:x**3,num)
print(list(cubed))
''''''
'''
A filtering operation processes an iterable and extracts the items that 
satisfy a given operation. It can be performed with Python’s FILTER() built-in function.
'''
'''
num = [12, 37, 34, 26, 9, 250, 451, 3, 10]
even = list(filter(lambda x: (x%2 == 0),num))
print(even)
'''
from functools import reduce
import operator 

a = reduce(list.__add__,[[1,3,5],[7,9],[11,13,1,5]])
print(a)

list1 = [1,2,3,4,4,5,55,100]

a1 = reduce(lambda a,b: a+b ,list1)

print(a1)

a2 =  reduce(lambda a ,b: a if a > b else b,list1 )
print(a2)
lis = [1,3,5,7,9]
print("The sum of list is:",end="")
print(reduce(operator.add,lis))
print("The Product of list:",end="" )
print(reduce(operator.mul,lis))
print("The concat is:",end="")
print(reduce(operator.add,['Blackholes ','are ','real ']))