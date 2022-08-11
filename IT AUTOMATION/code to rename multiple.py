'''
# Python 3 code to rename multiple
# files in a directory or folder
#
# importing os module
import os
#
# Function to rename multiple files
def main():

	folder = r"C:\Users\rnsri\Test_folder_py"
	for count, filename in enumerate(os.listdir(folder)):
		dst = f"Request_{str(count)}.csv"
		src =f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
		dst =f"{folder}/{dst}"
		# rename() function will
		# rename all the files
		os.rename(src, dst)

# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()
'''
# Python program to rename all file
# names in your directory
import os

os.chdir(r"C:\Users\rnsri\Test_folder_py")
print(os.getcwd())

for count, f in enumerate(os.listdir()):
	f_name, f_ext = os.path.splitext(f)
	f_name = "Request" + str(count)

	new_name = f'{f_name}_{f_ext}'
	os.rename(f, new_name)