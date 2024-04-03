'''
enumerate() for this task. The enumerate () method
adds a counter to an iterable and returns it in the
form of an enumerating object. This enumerated object 
can then be used directly for loops or converted into 
a list of tuples using the list() function.
#https://www.geeksforgeeks.org/enumerate-in-python/
'''


#e.g:1
lst = ['shine','star','space']
str1 = 'supernova'
'''
print("Before return type",end="\n")
print(type(lst),type(str1))
obj1 = enumerate(lst)
obj2 = enumerate(str1)
print("After :",end="\n")
print(type(obj1),type(obj2))

print(list(enumerate(lst)))
print(list(enumerate(str1)))

'''
#e.g:2
lst = ['shine','star','space']
str1 = 'supernova'
for ele in enumerate(lst):
    print(ele)
for count ,ele in enumerate(lst,1000):
    print("count: ",count,"ele: ",ele)

#e.g:3
lst = ['shine','star','space']
str1 = 'supernova'
enm1 = enumerate(lst)
#print(list(enm1))
next_elm = next(enm1)
next_elm1 = next(enm1)
print(f"next element:{next_elm}")

print(f"next element:{next_elm1}")
