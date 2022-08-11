import random, os,sys
def random_rename():
    #path = r"C:\Users\rnsri\Test_folder_py"
    path = sys.argv[1]
    file_list = os.listdir(path)
    for file_name in file_list: 
        old_name = os.path.join(path, file_name)
        new_name = os.path.join(path, 'Request'+'_'+str(random.randint(0,10)) +'.csv')
        os.rename(old_name, new_name)
random_rename()