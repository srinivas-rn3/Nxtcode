import sys,os
import fileinput 

os.chdir(r"C://Users//srini//OneDrive//Documents//pythonFiles")

def pack_files(file_names):
    
    marker = ':::::::::TextPack==>'
    print(marker,end='')
    for file_name in file_names:
        with fileinput.input(file_name) as f:
            for lines in f:
                if fileinput.filelineno() == 1:
                    print(file_name,end=' ')
                    print(lines,end=' ')
                else:
                    print(lines.strip())
    print(marker,end='')

if __name__ == '__main__':
    files = ['file1.txt','file2.txt']
    pack_files(files)
#https://www.blackbox.ai/share/a114d07a-e219-45ae-87aa-6bb30c4deeb6
    