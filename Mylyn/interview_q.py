#Reverse a String:
def reverse_string(str1:str) -> str:
    return str1[::-1]

print(reverse_string('srini'))

#s: str specifies that the parameter s should be of type str (a string).
#-> str specifies that the function reverse_string will return a value of type str.

#Check if a Number is Prime:

def is_prime(n:int)->bool:
    if n <= 1:
        return False 
    
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False 
        return True

print(is_prime(10))

n = 20
a = int(n**0.5) 
print("a:",a)
b = a+1
for i in range(2,b):
    print("prime_status",n%i,"where i:",i,"and n:",n)
    
#Find the Maximum Element in a List:
def find_max(lst1:list) -> int:
    return max(lst1)

# Example
max_list = find_max([1, 3, 5, 7, 9])
print("maximum number is",max_list)

#Remove Duplicates from a List:
def remove_duplicates(lst:list)->list:
    return list(set(lst))

dup = remove_duplicates([1, 2, 2, 3, 4, 4, 5])

print("After Duplicates are removed list:",dup)

#Fibonacci Sequence:

def fib(n:int) -> list:
    a,b = 0,1 
    result = []
    for _ in range(n):
        result.append(a)
        a,b = b,a+b 
    return result 
print(fib(10)) 

#Check for Anagrams:
def are_anagrams(s1:str,s2:str) -> bool:
    s1 = sorted(s1)
    print(f"s1:{s1}")
    s2 = sorted(s2)
    print(f"s2:{s2}")  
    return s1 == s2

#example
print(are_anagrams("listen","silent"))
print(are_anagrams("srini","silent"))
 
#Calculate Factorial:

def factorial(n:int) ->int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
#Question: Write a Python list comprehension that squares each odd number from 1 to 10 and stores the results in a list.
odd_square_list = [x**2 for x in range(1,11) if x % 2 != 0]
print(odd_square_list)


#Write a Python list comprehension to flatten a list of lists.
#nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
#flattened_list = [1, 2, 3, 4, 5, 6, 7, 8]

nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
#flat_list = [item for sublist in nested_lists for item in sublist]

#print(flat_list)
flat1 =[]
for su in nested_lists:
    print(su)
    for item in su:
        flat1.append(item)
print(flat1)

'''
You are given a list of n-1 integers and these integers are in the range of 1 to n. 
There are no duplicates in the list. One of the integers is missing. Write a function to find the missing integer.
i/p:[1, 2, 4, 6, 3, 7, 8]
o/p:5

'''
def find_miising(arr):
    n = len(arr) + 1 # Since one number is missing, the list length should be n-1
    print(n)
    print(len(arr))
    total_sum = n * (n+1) // 2 # Sum of first n natural numbers
    print(total_sum)
    actual_sum =  sum(arr)
    print(actual_sum)
    missing_number = total_sum - actual_sum
    return missing_number

#example
input_list = [1,2,3,4,5,6,7,8,9,11,12,13,14]
result = find_miising(input_list)
print("missing number is:",result)

'''
Problem: Find the Duplicate Number
Input: [1, 3, 4, 2, 2]
Ouput: 2

'''
def find_duplicate(arr):
    seen = set()
    for num in arr: 
        print(num)
        if num in seen: # Check if the number is already in the set
            return num # If yes, return the duplicate number
        seen.add(num)# If not, add the number to the set
        print(seen)
    return -1 # If no duplicate is found, though the problem guarantees one duplicate
# Example usage:
arr = [1, 3, 4, 2, 7,1]
duplicate_number = find_duplicate(arr)
print("The Duplicate number is:",duplicate_number)

#using comprehensions and generator
def find_dup(arr):
    seen = set()
    return next(num for num in arr if num in seen or seen.add(num))

# Example usage:
arr = [1, 3, 4, 2, 2]
dup = find_dup(arr)
print("The duplicate number is: ",dup)


'''
Given a string, find the length of the longest substring without repeating characters.
Input : "abcabcbb"
output: 3
We can solve this problem using the sliding window technique with two pointers.
'''
def length_of_longest_substring(s):
    char_set = set()
    left = 0 
    max_length = 0 
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length,right - left + 1)
    return max_length

# Example usage:
s = "abca"
result = length_of_longest_substring(s)
print("Lenght of the longest substring string without repaeting characters:",result)


'''
Problem: Container With Most Water
Given an array height of non-negative integers, where each element represents the height of a vertical line on a coordinate plane, find 
two lines that together with the x-axis form a container that holds the most water. Return the maximum amount of water a container can store.
input:[1,8,6,2,5,4,8,3,7]
output:49

Explanation: The vertical lines are drawn at indices 1 and 8 with heights 8 and 7.
The maximum area of water that can be contained is 49.

Solution Explanation:
We can use the two-pointer technique to solve this problem. 
The idea is to use two pointers, one at the beginning and one at 
the end of the array, and move them towards each other while calculating the area.
'''
def max_area(height):
    left = 0 
    right = len(height) - 1 
    max_water = 0
    
    while left < right:
        width = right - left
        current_heigth = min(height[left] , height[right])
        current_water = width * current_heigth
        max_water = max(max_water,current_water)
    
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
       
# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(height)
print("The max amount of water the container can store is:",result)