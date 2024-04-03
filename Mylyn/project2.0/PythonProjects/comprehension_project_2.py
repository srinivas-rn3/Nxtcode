'''
def square_number(numbers):
    return [num ** 2 for num in numbers]

if __name__ == '__main__':
    input_numbers =[1,2,3,4,5]
    square_numbers = square_number(input_numbers)
    print("Orginal numbers: ",input_numbers)
    print("Square numbers: ",square_numbers)
'''
'''
def filter_words_by_length(words,min_length):
    return [word for word in words if len(word) >= min_length]

if __name__ == '__main__':
    #Example : FIltering word with length greater than or equal to 5
    input_words= ['apple','banana','kiwi','orange','grape','pear']
    min_word_legth = 5
    filter_words = filter_words_by_length(input_words,min_word_legth)
    print("Orginal words: ",input_words)
    print(f"words with lenght >= {min_word_legth}:",filter_words)
'''
#Dictionary Comprehension 
'''
def count_chars(input_string):
    return{char:input_string.count(char) for char in input_string}

if __name__ =='__main__':
    #Example :  Counting characters  in string
    input_word = "Hello Cat Cat"
    char_count_dict= count_chars(input_word)
    
    print("Orginal string:",input_word)
    print("Character count dictionary:",char_count_dict)
'''
#Sample Data: List of students and their scores
students = {'Alice': 75, 'Bob': 60, 'Charlie': 85, 'David': 45, 'Eva': 95}

#Passing Code
passing_code = 70
'''
#Dictionary comprehension to categorize students as 'Pass' or 'Fail'
result_dict = {name:'Pass' if score >= passing_code else 'Fail' for name,score in  students.items()}
print(result_dict)

#Printing Original Data
print("Original data - Student and their scores:")
for name,score in students.items():
    print(f"{name}:{score}")
#print the dictionary categorizing  students
print("\nCategorized results: Pass or Fail.")
for name,score in result_dict.items():
    print(f"{name}:{score}")
'''
def dict_comp(students_dict):
    result_dict ={name:"PASS" if score >= passing_code else "FAIL" for name,score in students_dict.items()}
    return result_dict

def printing_dict(student_dict):
    cate_dict = dict_comp(student_dict)
    print("Original Data - Student and their scores:")
    for name,score in student_dict.items():
        print(f"{name}:{score}")
    print("")    
    print("Categorized Data - Student and their scores:")
    for name,score in cate_dict.items():
        print(f"{name}:{score}")
    
if __name__ =='__main__':
   printing_dict(students)