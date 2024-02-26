import os
files = r"C:\Users\srini\OneDrive\Documents\pythonFiles\file2.txt.txt"

if os.path.exists(files):
    with open(files,'r') as file:
        print(file.read())
else:
    print("File not found!! ")