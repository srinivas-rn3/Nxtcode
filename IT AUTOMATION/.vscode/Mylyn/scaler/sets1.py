'''
Sets: he formal definition of a set in Python will be: Set is an unordered collection of items,
where every element is unique and immutable. However, the set itself is mutable.

'''
'''
#Creating Sets in Python - Using Curly Braces'{ }'
evenNumber = {2,4,6}
print(evenNumber)
print(type(evenNumber))
stringNo= {'cat', 2,3}
print(stringNo)
'''
'''
#Using set() function
set1 = set([1,2,'cat'])
print(set1)
'''
'''
a = {"one":1,"two":2}
b = [100,200,300]
c = 'python'
print(set(a),end="\n")
print(set(b),end="\n")
print(set(c))
'''
'''
mySet = {1,2,3,[5,6]}## This wont work
print(mySet)
'''
'''
myset2 = {1,3,(4,5)}
print(myset2)
'''
#Adding Items in a Python Set
#add()
#update()
'''
intial_set = {1,2} 
intial_set.add(3)
print(intial_set)
toAdd= [99,999]
intial_set.update(toAdd)#update() takes an iterable like string, list, dictionary as an argument.
print(intial_set)
'''
'''
#Removing Items from a Set in Python
# 1. remove(element) 
# 2. discard(element) 
# 3. clear()
myset = {1,2,3,4,5}
print(myset)
myset.remove(3)
print(myset)
myset.discard(4)
print(myset)
myset.clear()
print(myset)
'''

#Set Operations in Python
'''
#1.Using operator
#2.Using methods
car1 = {'Honda','Toyota','Nissan'}
car2 = set(['Audi','BMW','JLR'])
print("cars union:\n",car1 | car2)
print("cars union:\n", car1.union(car2))
'''
#Intersection
'''
chemicalOne = {'Na', 'K','cl'}
chemicalTwo = set(['HCL','cl','Ba'])
print(chemicalOne & chemicalTwo)
print(chemicalOne.intersection(chemicalTwo))
'''
'''
#Difference
le1 = {'python','Javascript','C++'}
le2 = {'Assembly','C++'}
print(le1 - le2)
print(le1.difference(le2))
print('Changing order we get: ')
print(le2 - le1)
print(le2.difference(le1))
'''

'''
Symmetric Difference
The symmetric difference of two sets A and B is a set that contains elements in either A or B but not both. 
“^” operator or symmetric_difference() method in python is used to perform this operation.
'''
'''
a = {1,2,3}
b = {3,4,5}
print(a ^ b)
print(a.symmetric_difference(b))
'''
'''
Frozen Set
Frozen set is a built-in data type in Python. It is a set that is immutable (once defined, cannot be changed).
It supports all non-modifying operations of the set. Operations like add() won’t work in the case of a frozen set.
'''
'''
a = frozenset(['one','two','three'])
print(a)
#A common use case of frozenset can be to store dictionary keys. Here is an example showing that
myDict = {'name':"Python",'type':'Interpreated'}
setofdict = frozenset(myDict)
print(setofdict)
'''