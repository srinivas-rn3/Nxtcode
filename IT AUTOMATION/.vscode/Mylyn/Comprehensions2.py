'''
#e.g:1
my_list = []

for num in range(5):
    my_list.append(num)
print(my_list)
'''
'''
List comprehension is a fast, short, and elegant way to create lists compared to other iterative methods, like for loops.
#https://www.freecodecamp.org/news/list-comprehension-in-python-with-code-examples/

'''
'''
#e.g:2
new_list = [num for num in range(6)]
print(new_list)
'''
'''
#e.g:3 
#You can even perform mathematical operations on the items contained in the iterable and the result will be added to the new list:
new_list1 = [num *2 for num in range(6)]
print(new_list1)
'''
#e.g:4
#What if you had a pre-existing list where you wanted to manipulate and modify each item in it? 
#This would be similar to the example from earlier on, where we created a list of squares.
'''
numbers = [1,2,3,4,5,6,7,8,9]
new_list3 = [num * num for num in numbers]
print("Square Numbers are:",end='\n')
print(new_list3)
'''
#e.g:5
#Conditionals act as a filter and add an extra check for additional precision and customisation when creating a new list.

#This means that the value in the expression has to meet certain criteria and a 
#certain condition you speficy, in order to go in the new list.
'''
list4 = [num for num in range(500) if num % 2 ==0]
print(list4)
'''
'''
#e.g:6
list6 = [num for num in range(500) if num > 20 and num % 2 ==0 ]
print(list6)
'''
#use list comprehension on strings in Python
#You can create a new list with the individual characters contained in a given string.

#The new list that gets created is comprised of all the separate letters 
#contained in the string "Python", which acts as an iterable.
#e.g:7
lang = [letter for letter in 'LokinewKingOfMultiverse']
print(lang)

#e.g:8
#Here you use the .upper() method to convert every single letter in "Python"
#to uppercase and add them to the fave_language_chars_upper variable.

lang_u = [letters.upper() for letters in 'LokinewKingOfMultiverse']
print(lang_u)