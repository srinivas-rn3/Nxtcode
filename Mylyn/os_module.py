'''
The os module in Python provides a way to interact with the operating system. 
It includes functionalities for file and directory manipulation, environment 
variables, and executing system commands. 
Here are some key features and examples of how to use the os module:
'''
import os 


#Listing Files in a Directory

current_dir = os.getcwd()  #os.getcwd(): Returns the current working directory.
files = os.listdir(current_dir) #os.listdir(path): Lists all files and directories in the specified path.
#print(f"Files in {current_dir} : {files}")
print(f"Files in {current_dir}")
for file in files:
    print(file)

#Checking File and Directory Existence
curr= r"C:\Users\srini\git\Nxtcode\IT AUTOMATION"

# Check if the path exists
if os.path.exists(curr): # os.path.exists(path): Checks if a specified path exists.


    print(f"Path: {curr} is exist")

# Check if it's a file
if os.path.isfile(curr): #os.path.isfile(path): Checks if a specified path is a file.
    print(f"Path : {curr} is file")
else:
    print(f"path :{curr} is not file!!")   

# Check if it's a directory
if os.path.isdir(curr): #os.path.isdir(path): Checks if a specified path is a directory.
    print(f"{curr}: is a directory.")

#Running System Commands
os.system("echo hello python!!!") #os.system(command): Runs a system command.


# Run a system command and capture the output
open =  os.popen('dir').read() #os.popen(command): Runs a system command and opens a pipe to read/write data.
print(open)
##################################################################
#example 01-07
import os
#Renaming Files in a Directory
directory_path = r"C:\Users\srini\OneDrive\Documents\DirPython"

# Check if the directory exists
if not os.path.exists(directory_path):
    print(f"Directory '{directory_path}' does not exist.")
    exit()

# Change the current working directory to the specified path
os.chdir(directory_path)

## List all files in the directory
files =  os.listdir()
print(files)

# Define the renaming pattern
pattern = "file_{}.txt"

# Iterate over the files and rename them
for index ,file  in enumerate(files):
    new_name = pattern.format(index +1)
    os.rename(file,new_name)
    
    print(f"Renamed: {file} -> {new_name}")

print("Renaming is completed")

#enumerate :enumerate() adds a counter to an iterable and returns it as an enumerate object. This 
fruits = ['apple','banana','cherry']
for index,fruit in enumerate(fruits):
    print(index+1,fruit)