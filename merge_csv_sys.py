import sys ,os
import glob
import pandas as pd
try:
    #files
    file_csv1 = sys.argv[1]
    file_csv2 =  sys.argv[2]
    final_csv = sys.argv[3]
    print("*** Merging multiple csv files into a single pandas dataframe ***")
    #merge file
    csv1 = pd.read_csv(file_csv1,index_col=None,header=0)
    csv2 = pd.read_csv(file_csv2,index_col=None,header=0)
    df = pd.concat([csv1,csv2],ignore_index = True)
    df.to_csv(final_csv, index = False)
    #remove files
    os.remove(file_csv1)
    os.remove(file_csv2)
except IndexError:
    print ("You did not specify a file!!")
    sys.exit(1)
except IOError as e:
    print(e)
    sys.exit(1)
except OSError as error:
    print(error)
    print("File path can not be removed")
    sys.exit(1)
