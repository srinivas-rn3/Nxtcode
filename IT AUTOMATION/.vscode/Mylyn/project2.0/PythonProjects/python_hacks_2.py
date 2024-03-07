'''
lambda Functions: Anonymous functions can be created using the lambda keyword.
'''
add = lambda x,y:x+y 
print(add(3,4))

'''
map() Function: It applies a function to all the items in an input list.
'''
nums = [1,2,3,4,5,6]
squared = list(map(lambda x : x**2,nums))
print(squared)

'''
*args and **kwargs: Used for variable-length arguments in function definitions.
'''
def my_func(*args,**kwargs):
    print(args)
    print(kwargs)
    
#enumerate() in Python:
#Example 1: Iterating Over a List with Index
fruits = ['Apple', 'Banana', 'Orange', 'Grapes']

for index,value in enumerate(fruits):
    print(f"Index:{index} - {value}")

#Example 2: Updating Elements in a List
numbers = [1, 2, 3, 4, 5]
for index,value in enumerate(numbers):
    numbers[index] = value ** 2
print(numbers)

#Example 3: Debugging Using Enumerate
values = ['a', 'b', 'c', 'd']
for index ,value in enumerate(values):
    print(f"Porcessing items at index {index} : {value}")
    # Additional debugging or processing steps here

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for row_index,row in  enumerate(matrix):
    #print(row_index,row)
    for col_index,value in enumerate(row):
        #print(col_index,value)
         print(f"Element at row  {row_index} ,column {col_index}:{value}")