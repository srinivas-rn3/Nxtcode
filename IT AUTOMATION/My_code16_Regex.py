'''
A Regular Expressions (RegEx) is a special sequence of characters that uses
a search pattern to find a string or set of strings. It can detect the presence
or absence of a text by matching with a particular pattern, and also can split
a pattern into one or more sub-patterns. Python provides a re module that supports
the use of regex in Python. Its primary function is to offer a search, where it takes a
regular expression and a string. Here, it either returns the first match or else none.
'''
import re
'''
s = 'Srinivas saw super nova in the sky!!!'
match = re.search(r'nova', s)
print('Start Index', match.start())
print('End Index', match.end())

s1 = 'nova.release'
m = re.search(r'.',s1)
print(match)
m = re.search(r'\.',s1)
print(m)
'''
'''
re.findall()
Return all non-overlapping matches of pattern in string, as a list of strings. 
The string is scanned left-to-right, and matches are returned in the order found.
'''
''''
string1 = """Hello my number 696966 and
            my Dog no is 67676799"""
regEx = '\d+'
match12 = re.findall(regEx,string1)
print(match12)
'''
'''
re.compile()
Regular expressions are compiled into pattern objects, which have methods for 
various operations such as searching for pattern matches or performing string substitutions.
'''
# compile() creates regular expression
# character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with
# 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')
# findall() searches for the Regular Expression
# and return a list upon finding
print(p.findall("Srinivas, is master incursion. Obtained power from Dr.DoomsDay"))
p1 = re.compile('\d')
print(p1.findall("I went to planet 678 to stop incursion, along with my ultron scom4567"))
p2 = re.compile('\d+')
print(p2.findall("I went to planet 678 to stop incursion, along with my ultron scom4567"))
#https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/?ref=lbp