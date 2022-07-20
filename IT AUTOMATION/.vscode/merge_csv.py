import sys ,os
import glob
import pandas as pd
#files
file_csv1 = r"C:\Users\rnsri\Downloads\systemelementcontainsdevice1.csv"
file_csv2 = r"C:\Users\rnsri\Downloads\systemelementcontainsdevice2.csv"
final_csv = r"C:\Users\rnsri\Downloads\systemelementcontainsdevice_new.csv"
#csv = os.path.join(file_csv1,file_csv2)
#csv = glob.glob(csv)
print("*** Merging multiple csv files into a single pandas dataframe ***")
#merge file
csv1 = pd.read_csv(file_csv1,index_col=None,header=0)
csv2 = pd.read_csv(file_csv2,index_col=None,header=0)
df = pd.concat([csv1,csv2],ignore_index = True)
df.to_csv(final_csv, index = False)