#Creating Lists in Python

#creating empty list 
empty_list=[]

#interger list
int_list=[26,23,44,9]

#float list
flo_list = [1.4,4.5,0.5]

#diffrent data type list 
lis = [1,"life",8.5]

#list with duplicates
lis = [11,11,22,22,1,2,3,1]

#creating a nested list
nested_list = [[6,2,5],["alpha",5.6,9],"prep"]
'''
#Accessing Values/Elements in List in Python
My_List = [3, 4, 6, 10, 8]
print("values accessble using +ve index")
print(My_List[1])
print(My_List[2])
print("values accessble using -ve index")
print(My_List[-1])
print(My_List[-2])
'''
'''
## Nested List
nested_List = [[6, 2, 8], [1, 3.5, "Interviewbit"], "preparation"]
print(nested_List[0][0])
print(nested_List[0][1])
print(nested_List[-1])
'''
'''
#Updating List in Python
my_list = [1,2,367,76,90]
print(my_list)
#Change value of index
my_list[3] = 999
# Changing value to index -1, i.e the last value.
my_list[-1] = 9
print(my_list)
'''
'''
#Add/Change list Elements in Python
#We use the append() method to add a single element at the end of the list and 
#the extend() method to add multiple elements at the end of the list.
vowels = ['a', 'e']
print(vowels)
## Appending an element in list
vowels.append('i')
print(vowels)
# Extending an element in list
vowels.extend(['o','u'])
print(vowels)
#The insert() method takes two arguments, the first is the index at which the element is to be inserted,
# and the second is the value/ element to be inserted.
int1 = [1,2,37,8,9]
int1.insert(0,11)
print(int1)
'''

'''
# Deleting/Removing items from the List.
my_list = [2,4,6,8,10,12]
print(my_list)
# Deleting/Removing a single item from the list
del my_list[3]
print(my_list)
#deleting entire list 
del my_list
print(my_list)
'''
'''
We have three more methods remove(), pop(), and clear() for this purpose.

The remove() method takes the item as an argument that must be deleted or removed. 
If the item isn’t present within the list, a ValueError is raised.
The pop() method takes the index as an argument and deletes and returns the deleted item. 
If the index isn’t given, pop() deletes and returns the list's last element.
The clear() method in python makes the list empty.
'''
'''
# Deleting/Removing items from List using various methods
my_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_List)
# Deleting/Removing using remove() method
my_List.remove(4)
print(my_List)
# Deleting/Removing using pop() method
print(my_List.pop(1))
print(my_List)
# pop() method with no arguments
print(my_List.pop())
print(my_List)
# clear() method
my_List.clear() 
print(my_List)
'''
#List Operations in Python
#Concatenation: One list may be concatenated with itself or another list using ‘+’ operator.
'''
l1 = [1,3,5,7]
l2 =[2,4,6,8]
concat_list = l1+l2 
print(concat_list)
'''
'''
#Repeating the elements of the list: We can use the ‘*’ operator to repeat the list elements as many times as we want.
l2 = [1,3,5,7]
print(l2)
print(l2*2)
#Membership Check of an element in a list: We can check whether a specific element is a part/ member of a list or not
my = [1,2,3,4]
print(3 in my)
print(1 in my)
print(111 in my)
#Iterating through the list: We can iterate through each item within the list by employing a for a loop.
my_l = [2,4,6,8,10,12]
for n in my_l:
    print(n)
'''
'''
#Slicing a List in Python
my_List = ['i', 'n', 't', 'v', 'i', 'e', 'w', 'b', 'i', 't']
# Accessing elements from index beginning to 5th index
print(my_List[:6])
# Accessing elements from index 3 to 6
print(my_List[3:7])
# Accessing elements from index 5 to end
print(my_List[5:])
# Accessing elements from beginning to end
print(my_List[:])
# Accessing elements from beginning to 4th index
print(my_List[:-6])
'''
'''
#We can also use slicing to change,
# remove/delete multiple elements from the list. Let’s see some code examples and understand them.
List = [1, 2, 3, 4, 5, 6, 7, 8]
print(List)
# Changing elements from index 2nd to 5th
List[2:5] = [0.5,0.5,0.5]
print(List)
# Deletion multiple items from the List
del List[2:5]
print(List)
'''
'''
#Iterating Over a Python List
my_List = ['i', 'n', 't', 'e', 'r', 'n']
# Traversing using for loop.
for i in my_List:
    print(i,end=" ")    

size =len(my_List)
# Traversing using for loop.
for i in range(size):
    print(my_List[i], end =" ")
'''
'''
#By using while loop:
# Initializing a List
my_List = ['i', 'n', 't', 'e', 'r', 'n']
size = len(my_List)
i = 0
# Traversing using a while loop.
while i < size:
    print(my_List[i],end=" ")
    i += 1
'''
'''
#List comprehension: Using List comprehension is one of the best possible ways to iterate over a list. List
#comprehension makes the program look more elegant and easily understandable.

my_List = ['i', 'n', 't', 'e', 'r', 'n']
# iterating using List Comprehension
[print(x ,end = ' ') for x in my_List]
'''
#my_list1 = [22,3,4,5]
#[print(i , end= " ") for i in my_list1 if i %2 ==0]
'''
#Using the enumerate(): enumerate() in python allows us to loop through elements as well as the index within the list. 
#This is helpful when we want to traverse only certain index elements in the list based on certain condition(s).
my_List = ['i', 'n', 't', 'e', 'r', 'n']
# iterating using enumerate
for i,item  in enumerate(my_List):
    if i%2 != 0:
        print(i,item)
'''