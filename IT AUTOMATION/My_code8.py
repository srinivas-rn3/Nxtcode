'''
x =[1,2,3,4,5]
print (x)
print(x[1:3])
""" In the above mentioned format, the first 
index is included, but the last index is not
included."""

"""Multiple Statements per Line We can also write multiple statements per line, but it is 
not a good practice as it reduces the readability of the code. Try to avoid writing multiple 
statements in a single line. But, still you can write multiple lines by terminating 
one statement with the help of ‘;’. ‘;’ is used as the terminator of one statement in this case."""
a = 10; b = 5; c = 6; d = a + b + c;

print(a);print(b);print(c);print(d)
'''
'''
# Example 2
# The following code is also valid
  
person_1 = 10 
person_2 = 20
person_3 = 30

if (
    person_1 >=10 and 
    person_2 >=15 and
    person_3 >= 30
):
    print("I'm Stupid!!!")
'''
'''
x = \
    1 + 10 \
    + 15 + 10 \

print(x) 
'''
'''
x = 10
while(x != 0):
    if (x > 5):
        print("X > 5")
    else:
        print("X < 5")    
    x -= 2
"""
Lines 1, 3, 5 are on same level
Line 2 will only be executed if if condition becomes true.
Line 4 will only be executed if if condition becomes false.
"""
'''

#Instead of writing this massive Python code
#we can also code this in a different way
 
#Python code to demonstrate working of iskeyword()
 
# importing "keyword" for keyword operations
'''
import keyword
keys = keys = ["for", "while", "tanisha", "break", "sky",
"elif", "assert", "pulkit", "lambda", "else", "srini"]

for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i] + "-is python keyword!!!")
    else:
        print(keys[i] + "-is not keyword!!!")    
'''     
'''
import keyword
print("The list of keywords are :")
print(keyword.kwlist)
'''
# Create a new dictionary
d = dict()
d['xy'] = 123
d['zz'] = 234
# print the whole dictionary
print(d)
# print only the keys
print(d.keys())
# print only values
print(d.values())
# iterate over dictionary
for i in d:
    print("%s  %d" %(i ,d[i]))
# check if key exist
print("xy" in d)
# delete the key-value pair
del d['xy']

# check again
print("xy" in d)

#https://www.geeksforgeeks.org/python-set-4-dictionary-keywords-python/?ref=rp
