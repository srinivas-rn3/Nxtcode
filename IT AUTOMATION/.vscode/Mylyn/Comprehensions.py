#Python Tutorial: Comprehensions - How they work and why you should be using them
#eg:1
nums = [1,3,5,7,9,11,13,15,17,19,21]
#my_list = []
#for n in nums:
#   my_list.append(n)
#print (my_list)
#my_list = [n for n in nums]
#print(my_list)
#eg:2
#my_list = []
#for n in nums:
#    my_list.append(n*n)
#print(my_list)

#my_list = [n*n for n in nums]
#print(my_list)

#eg:3
#my_list = list(map(lambda n: n*n , nums))
#print(my_list)
#https://cs.stanford.edu/people/nick/py/python-map-lambda.html

#eg:4
nums1 = [1,2,4,3,6,5,9,12,10,15,16,17,21,19,20,22,23,24,25,30]
'''
my_list_even = []
my_list_odd = []
for n in nums1:
    if n%2 == 0:
        my_list_even.append(n)
    else:
        my_list_odd.append(n)

print("Even list:", end ='\n')
print(my_list_even)
print("Lenght of evne list is ",len(my_list_even))
print("odd list:",end='\n')
print(my_list_odd)
print("Lenght of odd list is", len(my_list_odd))
'''
'''
my_list_even = [n for n in nums1 if n%2 == 0]
my_list_odd = [n for n in nums1 if n%2 != 0 ]
print("Even list is :", end='\n')
print(my_list_even)
print("Odd list is :", end='\n')s
print(my_list_odd)
'''
#my_list_even = list(filter(lambda n: (n%2 == 0),nums1))
#print(my_list_even)
#eg:5
'''
my_list =[]
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)
'''
#my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
#print(my_list)

#eg:6
Names = ['Bruce','Clark','Peter','Logan','Tony']
Heros = ['Batman','Super Man','Spider Man','Wolverine','Iron Man']

#zip = zip(Names,Heros)
#print(list(zip))
'''
my_dict = {}
for Names,Heros in zip(Names,Heros):
    my_dict[Names] = Heros 
print(my_dict)
'''
#my_dict =  {Names:Heros for Names,Heros in zip(Names, Heros) if Names != 'Clark'}
#print(my_dict)
#eg:7
nums3 = [1,2,3,3,3,5,6,6,7,9,9,9,9,10,10,12,12,12,15,15,19,20,20,20,21,12,21,22,21]
'''
my_set = set()
for n in nums3:
    my_set.add(n)
print(my_set)
'''
#my_set = {n for n in nums}
#print(my_set)
#eg:8
'''
def gen_func(nums):
    for n in nums:
        yield n*n 

my_gen = gen_func(nums3)
for i in my_gen:
    print(i)
'''
#generators
my_gen = (n*n for n in nums3)
for i in my_gen:
    print(i)