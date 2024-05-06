'''
Absolutely! List comprehensions are a concise and Pythonic way to create lists. 
They allow you to generate lists using a single line of code. Here's a basic syntax:

python
Copy code
new_list = [expression for item in iterable if condition]
Here's a breakdown:

expression: The expression to evaluate and include in the new list.
item: The variable representing each element in the iterable (e.g., list, tuple, etc.).
iterable: The iterable object you're iterating over (e.g., list, tuple, range, etc.).
condition (optional): A condition that must be true for the item to be included in the new list.
'''
# Example 1: Square numbers from 0 to 9 using list comprehension
square = [x**2 for x in range(10)]
print(square)

# Example 2: Get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
# Example 3: Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
flattened = [num for row in matrix for num in row]
print(flattened)

'''
Suppose you have a list of strings, and you want to create a new list that contains 
the lengths of those strings, but only for strings with lengths greater than 
3, and you want to convert those lengths into strings:
'''
# Example 3
# Original list of strings
words = ["apple", "banana", "orange", "grape", "kiwi", "watermelon", "pineapple","fig"]
# List comprehension to get lengths of strings longer than 3 and convert them to strings
#leng = [str(len(word)) for word in words if len(word) > 3]
leng = [(word,len(word)) for word in words if len(word) > 5]
print(leng)

# Example 4
# Original list of filenames
filenames = ["example.txt", "document.docx", "picture.jpg", "data.csv", "notes.txt", "presentation.pptx"]
result = [(filename,str(len(filename))) for filename in filenames if len(filename)> 5 ]
print(result)

#Example 5 

# Original list of email addresses
# List comprehension to get email addresses and their domains, but only for Gmail addresses
email_addresses = ["user1@gmail.com", "user2@hotmail.com", "user3@gmail.com", "user4@yahoo.com", "user5@gmail.com"]
result1 = [(email,email.split('@')[1]) for email in email_addresses if email.endswith('@gmail.com')]
print(result1)