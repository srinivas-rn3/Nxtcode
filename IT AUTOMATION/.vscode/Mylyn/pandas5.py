#https://www.youtube.com/watch?v=DCDe29sIKcE&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=5
#Python Pandas Tutorial (Part 5): Updating Rows and Columns - Modifying Data Within DataFrames

import pandas as pd

people = {
    "first": ['Srini','Marine','Jane','Kim'],
    "last": ['RN','Chang','Doe','Doe'],
    "email": ['srinivas.rn@xxx.com','marnie.change@xxx.com','jane.doe@xxx.com','kim.doe@xxx.com']
}
df = pd.DataFrame(people)
df.columns  = ['First_Name','Last_Name','Email']
df.columns = [x.lower() for x in df.columns]
print(df.columns,end='\n')
#print(df)
df.columns = df.columns.str.replace('_','-')
#print('\n')
#print(df)
df.rename(columns={'first-name':'First_Name','last-name':'Last_Name','email':'Email'},inplace=True)
print('\n')
print(df)
df.loc[2] = ['Kim','V','kim.v@xxx.com'] # repalce entire row data in columns 2
print(df)

df.loc[2,['Last_Name','Email']] = ['Yang','kim.yang@xxx.com']# to change the columns values
print(df)
#change single vlaue
df.loc[2,'Last_Name'] = "Yungsu"
df.loc[2,'Email'] = 'kim.yangsu@xxx.com'

print(df)
#df.drop('Last_name',axis=1,inplace=True)
#df.drop('email',axis=1,inplace=True)
#print(df)
#another way ot cahnge the vlaue using'@
df.at[2,'Last_Name'] = 'Yungsumar'
df.at[2,'Email']='kim.yungsumar@xxx.com'
print(df)
#start at video 11:00