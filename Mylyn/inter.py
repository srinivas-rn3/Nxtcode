numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
print(numbers[::2]) #every second element
print(numbers[1::3]) #starting from index 1, every third element
print(numbers[::]) #full copy, equivalent to numbers[:]
print(numbers[::-1]) #reverse the list
print(numbers[0::9])

#Palidrome
def paliendrome(num):
    num_str = str(num)
    
    return num_str == num_str[::-1]

num = 'madam'
if paliendrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not palindrome.")

str1 = 'tenet'
if str1 == str1[::-1]:
    print("palindrome:True")
else:
    print("palindrome:False")
    
#
number = list(range(1,101))
## Slicing the list with the expression numbers[0::9]
#0 is the starting index, meaning the slice will start at the first element of the list.
#9 is the step size, meaning the slice will take every 9th element from the list starting from the index 0.
#The absence of a stop index means it will go to the end of the list.
result = number[0::9]
print(result)