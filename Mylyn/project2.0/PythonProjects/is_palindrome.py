
def is_palindrome(input_string):
    cleaned_string = ''.join(e for e in input_string if e.isalnum()).lower()
    #print(cleaned_string)
    return cleaned_string == cleaned_string[::-1]

#test
print(is_palindrome("hello"))
print(is_palindrome("Able was I ere I saw Elba"))
print(is_palindrome("A 4manss"))
'''
string1 = "Hello Berry"
print(string1[::-1])
print(string1.isalnum())
'''