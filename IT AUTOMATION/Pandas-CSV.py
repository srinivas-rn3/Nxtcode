import sys
import pandas as pd
import numpy as np
CSV_FILE = r"C:\Users\rnsri\KA_API\Request_0\Request_0.csv"

#df = pd.read_csv(CSV_FILE, sep= ',', usecols=['Priority'])
df = pd.read_csv(CSV_FILE, sep= ',')
df1 = pd.DataFrame(df)
df1= df.fillna('NONE',inplace=True)

#df1.replace(' ',np.nan,regex=True)
#df1 = df['Priority'].replace('MediumPriority','Medium',regex=True)
df2  = df.replace({'Priority':{'MediumPriority':'Medium','LowPriority':'Low','HighPriority':'High','CriticalPriority':'Critical'}})
#print(df1)
#df3 = pd.DataFrame(df2, columns=['Id','AssignedToGroup','AssignedToPerson','ServiceDeskGroup','Priority','CreateTime'])
df3 = df2.rename(columns={'Id':'Request ID', 'AssignedToGroup':'Assigned Group', 'AssignedToPerson':'Assigned Person'})
df4 = pd.DataFrame(df3,columns=['Request ID','Assigned Group','Assigned Person','Priority','ServiceDeskGroup','CreateTime'])
#df3.to_csv(r'C:\Users\rnsri\KA_API\Request_0\Request_New1.csv')
df4.to_excel(r'C:\Users\rnsri\KA_API\Request_0\Request_New1.xlsx')
