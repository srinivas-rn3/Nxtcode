
#Example 1

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

book_id = 5
book = next((book for book in books if book['id'] == book_id),None)
print(book)

#Example 2
numbers = [1, 3, 5, 8, 9, 10, 11,12,13,15,16,18,17,19,20]
# Find the first even number
even_number = next((num for num in numbers if num % 2 == 0),None)
print(even_number)

#Example 3
# Sample dictionary of students and their ages
students = {
    "Alice": 20,
    "Bob": 22,
    "Charlie": 18,
    "David": 25
}

# Find the first student whose age is above a certain threshold
age_threshold = 21
first_student_above_threshold = next((name for name,age  in students.items() if age >age_threshold),None)

if first_student_above_threshold :
    print(f"The frist student  above {age_threshold} years of old: {first_student_above_threshold}")
else:
    print(f"No student found above {age_threshold} years old.")
    
    
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using items() method to get key-value pairs
items = my_dict.items()
print(items)

# Displaying the key-value pairs
for key,value in items:
    print(key,value)