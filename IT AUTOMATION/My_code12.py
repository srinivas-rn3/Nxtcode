'''
OS Module in Python with Examples
The OS module in Python provides functions for interacting with the operating system. 
OS comes under Python’s standard utility modules. This module provides a portable way of 
using operating system-dependent functionality. 
The *os* and *os.path* modules include many functions to interact with the file system.
'''
# Python program to explain os.getcwd() method
# importing os module
import os

# Get the current working
# directory (CWD)
'''
cwd = os.getcwd()
# Print the current working
# directory (CWD)
print("Current working directory:", cwd)
'''
# os.listdir() method in Python is used to get the list of all files and directories in the specified directory. 
# If we don’t specify any directory, then the list of files and directories in the current working directory will be returned.
'''
path = "/"

dir_list = os.listdir(path)
print ("Files and directories in '",path,"' : ")
print(dir_list)
'''
'''
print(os.name)
'''
'''
Functional Programming in Python
Python too supports Functional Programming paradigms without the support of any special features or libraries.

Pure Functions
As Discussed above, pure functions have two properties.

It always produces the same output for the same arguments. For example, 3+7 will always be 10 no matter what.
It does not change or modifies the input variable.

'''
# Python program to demonstrate
# pure functions
# A pure function that does Not
# changes the input list and 
# returns the new List
def pur_fun(List):
    New_list = []
    for i in List:
        New_list.append(i*2)
    return New_list

original = [1,2,3,4,5]
original_list = pur_fun(original)
modifyied_list = pur_fun(original_list)

print("original list: ",original_list, end = "")
print("Modifying List :", modifyied_list ,end = "")