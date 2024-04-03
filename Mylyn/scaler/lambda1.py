#print((lambda x : 6 + x)(4))
# Regular function
'''
def sum(num1,num2):
    print("Function is executed")
    return num1 + num2
#Lambda function
sum_lambda = lambda num1,num2 : num1 + num2 

print(sum(19,10))
print("lambda is executed")
print(sum_lambda(10,10))
'''
'''
#Use of the Python Lambda Function Inside the filter() Function'
#List of numbers
num = [1,2,3,4,5,5,6,8,9]
# one liner code to make list of even numbers using filter() function
even_no = list(filter((lambda x : x % 2 ==0),num))
# even numbers list
print(even_no)
#odd liner code
odd_no = list(filter((lambda x : x % 2 !=0),num))
print(odd_no)
'''
'''
# Use of the Python Lambda Function Inside the map() Function
num = [0,1,2,3,4,5]
sq_num = list(map((lambda x : x*x),num))
print(sq_num)
'''
#Use of the Python Lambda Function Inside reduce() Function
from functools import reduce 
num = [1,2,3,4,4,5,5,6,6,6,6,100]
sum1 = reduce((lambda x,y:x+y),num)
print(sum1)
