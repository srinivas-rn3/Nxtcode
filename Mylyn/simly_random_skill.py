# import math 
# print(math.isclose(1.233 ,1.466))
# print(math.isclose(1.5 ,1.5))
'''
math.isclose(a, b, rel_tol, abs_tol)
a	Required. The first value to check for closeness
b	Required. The second value to check for closeness
rel_tol = value	Optional. The relative tolerance. It is the maximum allowed difference between value a and b. Default value is 1e-09
abs_tol = value	Optional. The minimum absolute tolerance. It is used to compare values near 0. The value must be at least 0

'''
# print(math.isclose(1.23 ,8.450,abs_tol=0.4))
# print(math.isclose(8.005,8.450,abs_tol=0.5))
# print(math.isclose(8.005,8.450,rel_tol =0.5))
# #https://www.w3schools.com/python/ref_math_isclose.asp

from io import StringIO
# string1 = "This is intial string."
# file = StringIO(string1)
# print(file.read())
# file.write("Welocme to blachole.")
# file.seek(0)
# print("The String after writng is:",file.read())

# StringIO.getvalue(): This function returns the entire content of the file.

# s = "Hello and welcome to dreamworks"
# f = StringIO(s)
# print(f.getvalue())

# s = "Hola to Black hole.Once you come you never leave.Its Infinite Jail"

# f = StringIO(s)
# print("Is the file stream  interactive", f.isatty())
# print("Is the file stream readable",f.readable())
# print("Is the file stream writable",f.writable())
# print("Is the file stream seekable", f.seekable())
# print("Is the file stream closed?",f.closed)

'''
StringIO.seek(): The seek() function is used set the cursor position on the file. 
If we perform any read and write operation on a file the cursor 
is set on the last index so to move the cursor at starting index of the file seek() is used.

'''
# s = "Hola to Black hole.Once you come you never leave.Its Infinite Jail!!!!"
# f = StringIO(s)
# print("reading file")
# print(f.read())
# print(f.read())
# f.seek(0)
# print(f.read())

'''
4.StringIO.truncate(): This function is used to resize the size of the file stream.
This method drops the file after the provided index and saves it. 
'''
s = "Hola to Black hole.Once you come you never leave.Its Infinite Jail!!!!"
# f = StringIO(s)
# print(f.read())
# f.seek(0)
# print(f.truncate(17))
# print(f.read())

'''
StringIO.tell(): This method is used to tell the current stream or cursor position of the file.

'''
# f = StringIO(s)
# print(f.read())
# print(f.tell())
# f.seek(20)
# print(f.tell())

'''StringIO.close(): This method is used to close the file. After this function called on a file, 
 we cannot perform any operation on the file. If any operation is performed, it will raise a ValueError.'''

# f = StringIO(s)
# print(f.read())
# print("Is file is closed:",f.closed)
# f.close()
# print("Is file is closed:",f.closed)
# #https://www.geeksforgeeks.org/stringio-module-in-python/

# try:
#     #file1 = open(r"C:\Users\srini\OneDrive\Documents\test11.txt")
#     file1 = open(r"C:\Users\srini\OneDrive\Documents\test11.txt","r")
#     #both above stamtents are same 
#     read_content = file1.read()
#     print(read_content)
# finally:
#     file1.close()

# with open(r"c:\Users\srini\OneDrive\Documents\test11.txt") as file1:
#     read_content = file1.read()
#     print(read_content)
#Writing to Files in Python
# with open (r"C:\Users\srini\OneDrive\Documents\test11.txt",'a') as file1:
#     #write to file
#     file1.write("Because no light escapes a black hole, it is invisible – or \
#                 'black' – although they can be detected by their effect on the material around them.")
import os .path
# path =r"C:\Users\srini\OneDrive\Documents\test11.txt"
# check_file = os.path.isfile(path)
# print(check_file)

# path = r"C:\Users\srini\OneDrive\Documents1"
# cehck_file = os.path.exists(path)
# print(cehck_file)
# from pathlib import Path

# path = r"C:\Users\srini\OneDrive\Documents\test11.txt"
# p= Path(path)
# print(p.is_file())
# #https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/


#Python String strip() Method

txt = "     Banana    "
x = txt.strip()
print("All of all fruits",x,"is my favoite")
#The strip() method removes any leading (spaces at the beginning)
# and trailing (spaces at the end) characters (space is the default leading character to remove)
txt1 = ",,,,,rrttgg.....banana....rrr"
x = txt1.strip(",.grt")
print(x)