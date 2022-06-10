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
'''
p = re.compile('[a-e]')
# findall() searches for the Regular Expression
# and return a list upon finding
print(p.findall("Srinivas, is master incursion. Obtained power from Dr.DoomsDay"))
p1 = re.compile('\d')
print(p1.findall("I went to planet 678 to stop incursion, along with my ultron scom4567"))
p2 = re.compile('\d+')
print(p2.findall("I went to planet 678 to stop incursion, along with my ultron scom4567"))
#https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/?ref=lbp
'''
'''
p = re.compile('\w')
print(p.findall(("srinivas i saw * redGiant star ")))
#\w Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_]
#\W Matches any non-alphanumeric character.
#\w+ matches to group of alphanumeric character.
p =re.compile('\w+')
print(p.findall("Nova giant is such big when it explodes we going to see cosmic wonder"))
p =re.compile('\W')
print(p.findall("Black hole occurs when star core become Iron *** Iron ores family with temperature of 10000000 Celsius "))
'''
'''
# '*' replaces the no. of occurrence
# of a character.
p = re.compile('ab*')
print(p.findall("abbaabbdbbdaa"))
'''
'''
re.split()

Split string by the occurrences of a character or a pattern, 
upon finding that pattern, the remaining characters from the string are returned as part of the resulting list.

Syntax : 

re.split(pattern, string, maxsplit=0, flags=0)

The First parameter, pattern denotes the regular expression, string is the given string in 
which pattern will be searched for and in which splitting occurs, maxsplit if not provided is 
considered to be zero ‘0’, and if any nonzero value is provided, then at most that many splits occur. 
If maxsplit = 1, then the string will split once only, resulting in a list of length 2. The flags are very useful and can help to shorten code,
they are not necessary parameters, 
eg: flags = re.IGNORECASE, in this split, the case, i.e. the lowercase or the uppercase will be ignored.
'''
from re import split
# '\W+' denotes Non-Alphanumeric Characters
# or group of characters Upon finding ','
# or whitespace ' ', the split(), splits the
# string from that point
'''
print(split('\W+', 'Words, words ,Words' ))
print(split('\W+', "Word's words Words"))
# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs
print(split('\W+', 'On 12 th Aug, we saw one of the greats of cosmic'))
# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only
print(split('\d+', 'On 12 th Aug 12:00 AM, we saw one of the greats of cosmic'))
'''
'''
# Splitting will occurs only once, at
# '12', returned list will have length 2
print(split('\d+', 'On the 12th Aug, 12:00 AM we saw cosmic miracle',1 ))
# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(split('[a-f]','Hey, I saw North Star in direction of the South', flags=re.IGNORECASE))
'''
'''
re.sub() 

The ‘sub’ in the function stands for SubString, a certain regular expression pattern is searched in the given string(3rd parameter), and upon 
finding the substring pattern is replaced by repl(2nd parameter), count checks and maintains the number of times this occurs. 
Syntax:

 re.sub(pattern, repl, string, count=0, flags=0)
'''
# Regular Expression pattern 'ub' matches the
# string at "Subject" and "Uber". As the CASE
# has been ignored, using Flag, 'ub' should
# match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and
# in "Uber", 'Ub' is replaced.
'''
print(re.sub('ub', '##', "I booked Uber but driver is cancelled the trip", flags=re.IGNORECASE))
print(re.sub('sub','F@#','Organic Chemistry subject is hard to learn'))
print(re.sub('ub','**','Uber deriver is subject of the offensive for driving without seat belt',flags=re.IGNORECASE,count=1))
# 'r' before the pattern denotes RE, \s is for
# start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Frozen beans AND peas are bout to expire'))
'''
'''
re.subn() 

subn() is similar to sub() in all ways, except in its way of providing output.
It returns a tuple with count of the total of replacement and the new string rather than just the string.

Syntax:re.subn(pattern, repl, string, count=0, flags=0)
'''
'''
print(re.subn('ub','UB',"Uber Driver's are not accepting online payments", flags=re.IGNORECASE))
len1 = re.subn('ub', 'UB@#', "Uber Drivers are subjected to take driver license to verification", flags=re.IGNORECASE)
print(len1)
print(len(len1))
# This will give same output as sub() would have
print(len1[0])
print(len1[1])
'''
'''
re.escape()

Returns string with all non-alphanumerics backslashed, this is useful if
you want to match an arbitrary literal string that may have regular expression metacharacters in it.

Syntax:re.escape(string)
'''
'''
# escape() returns a string with BackSlash '\',
# before every Non-Alphanumeric Character
# In 1st case only ' ', is not alphanumeric
# In 2nd case, ' ', caret '^', '-', '[]', '\'
# are not alphanumeric
str1= "I'm the lord of the Dark side bend yours knees!!! ,my slave "
t = re.escape(str1)
print(t)
str2 = "I love [0-9]\t of Masala Dosa, I tasted dosa it's so yummy\t "
print(re.escape(str2))
'''
'''
re.search()

This method either returns None (if the pattern doesn’t match), or a re.MatchObject 
contains information about the matching part of the string. This method stops after the first match, 
so this is best suited for testing a regular expression more than extracting data.

Example: Searching an occurrence of the pattern
'''
'''
# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex,"I was born on May 25")
if match != None:
    # We reach here when the expression "([a-zA-Z]+) (\d+)"
    # matches the date string.
    # This will print [14, 21), since it matches at index 14
    # and ends at 21.
   print ("Match at index %s ,%s" % (match.start(),match.end()))
   # We us group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ... return the capture
    # groups in order from left to right in the input string
    # match.group() is equivalent to match.group(0)
   print ("full match: %s" % (match.group(0)))
   # So this will print "month"
   print("Month match : %s" %(match.group(1)))
   #So this will print "Date"
   print("Date match : %s"%(match.group(2)))
else:
    print("regex pattern doesn't match!!!")
'''
'''
Match Object

A Match object contains all the information about the search and the result and if 
there is no match found then None will be returned. Let’s see some of the commonly used 
methods and attributes of the match object.
Getting the string and the regex

match.re attribute returns the regular expression passed and match.string attribute returns the string passed.

Example: Getting the string and the regex of the matched object
'''
'''
#start() method returns the starting index of the matched substring
#end() method returns the ending index of the matched substring
#span() method returns a tuple containing the starting and the ending index of the matched substring
s = 'common ground'
res = re.search(r"\bco", s)
print(res.re)
print(res.string)
print(res.start())
print(res.end())
print(res.span())
'''
'''
group() method returns the part of the string for which the patterns match. 
See the below example for a better understanding.
Example: Getting matched substring 
'''
s = "Belong to one"
res = re.search(r"\D{2} t" , s)
print(res.group())