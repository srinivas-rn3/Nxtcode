import re  


#EX1 : Matching a simple word
text = "Say hello to the world"
pattern = r"hello"

match = re.search(pattern,text)

if match:
    print("Pattern Match!!!")
    print("Matched String:",match.group())
    print("Start Index:",match.start())
    print("End Index:",match.end())
else:
    print("Pattern mis-match!!!")

'''
print(match.group())  # prints the matched string
print(match.start())  # prints the start index of the match
print(match.end())    # prints the end index of the match
print(match.span())   # prints a tuple containing the start and end indices

. matches any single character except newline.
* matches zero or more occurrences of the preceding character.
+ matches one or more occurrences of the preceding character.
? matches zero or one occurrence of the preceding character.
{m} matches exactly m occurrences of the preceding character.
{m, n} matches between m and n occurrences of the preceding character.
'''

#EX2 : Matching an email address
# Define the pattern for email address
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

#Text to search 
text = "sss@xxx.com"

# Search for the pattern
match = re.search(pattern,text)

# Check if the pattern is found
if match:
    print("Pattern Found")
    print("Matched String:",match.group())
    print("Start Index:",match.start())
    print("End Index:",match.end())
else:
    print("Match not found!!!")
    
#EX:3 Matching multiple occurrences

# Define the pattern for finding numbers

pattern = r"\d+"

#Text to search
text = "I have 5 apples and 3 oranges."

# Find all occurrences of numbers in the text
matches = re.findall(pattern,text)

for match1 in matches:
    print("Found:",match1)



# EX:4 
'''
re.findall():
Finds all non-overlapping occurrences of the pattern in the string.
Returns a list of matched strings.
'''
pattern = r'\d+'
text = "I have 5 apples and 3 orange"

match = re.findall(pattern,text)
print("All matches:", match)

#EX:5
'''
re.finditer():
Finds all non-overlapping occurrences of the pattern in the string.
Returns an iterator yielding match objects.
'''

print(" ")
pattern1 = r'\d+'
text1 = "I have 5 apples and 3 orange"
matches = re.finditer(pattern1,text1)

for m in matches:
    print("match Found:",m.group(),"at poistion",m.span())
    
'''
More Advanced Patterns and Techniques
Character Classes:
\d: Any digit (equivalent to [0-9])
\D: Any non-digit
\w: Any word character (equivalent to [a-zA-Z0-9_])
\W: Any non-word character
\s: Any whitespace character
\S: Any non-whitespace character
'''
#EX:6
pattern3 = r'\w+'
text3 = "Python 3.12 is amazing!"

match3 = re.findall(pattern3,text3)
print(match3)

#EX:7
pattern4 =r"^Hello"
text4 = "Hello world"

match4 = re.search(pattern4,text4)
print(match4)
if match4:
    print("Start with hello",match4.group())
else:
    print(" Does not found with hello!!!")
    