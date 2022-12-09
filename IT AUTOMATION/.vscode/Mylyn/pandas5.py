#https://www.youtube.com/watch?v=DCDe29sIKcE&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=5
#Python Pandas Tutorial (Part 5): Updating Rows and Columns - Modifying Data Within DataFrames

import pandas as pd
'''
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

#print(df)
#df.drop('Last_name',axis=1,inplace=True)
#df.drop('email',axis=1,inplace=True)
#print(df)
#another way ot cahnge the vlaue using'@
df.at[2,'Last_Name'] = 'Yungsumar'
df.at[2,'Email']='kim.yungsumar@xxx.com'
#print(df)
#start at video 11:00
#filt = (df['Email'] =='srinivas.rn@xxx.com')
#df.loc[filt,'Last_Name'] = 'RRR' #to update single row data 
#print(df)
#print(df['Email'].str.upper())
#To make changs multipl rows 
'''
#df['Email'] = df['Email'].str.upper()
#print(df)
#df['Email'] = df['Email'].str.lower()
#print(df)

'''
apply -> To work Data Frame, series.Call function on value
replace
map
applymap
'''
'''
#apply
#print(df['Email'].apply(len))
def upper_fucn_email(Email):
    return Email.upper()
print(df['Email'].apply(upper_fucn_email))#thsi will not update realt table to do so ... follow below
df['Email']= df['Email'].apply(upper_fucn_email)
#print(df)
#same as above with lambda
df['Email'] = df ['Email'].apply(lambda x :x.lower())
#print(df)
#start with 22:42
print(df.apply(len))
print(df['Email'].apply(len))
#print(len(df['Email']))
print(df.apply(pd.Series.min))
appl = df.apply(lambda x:x.min())
print(appl)
#applymap: Work with only dataframe.Apply map function  to each individual.
am = df.applymap(len)
print(am)
lowr = df.applymap(str.lower)
print(lowr)
#map : works with only series. Map is used for substituting each value in a series
#mpa1 = df['First_Name'].map({'marine':'lisa','kim':'Jung'})
mpa1 = df['First_Name'].replace({'marine':'lisa','kim':'Jung'})
print(mpa1)
'''

pd_schema = pd.read_csv(r'C:/Users/rnsri/Stackoverflow/survey_results_schema.csv')
pd_public = pd.read_csv(r'C:/Users/rnsri/Stackoverflow/survey_results_public.csv')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
df1 = pd.DataFrame(pd_public)
df2 = pd.DataFrame(pd_schema)
#print(df1.columns)
rename_one = df1.rename(columns={'ConvertedCompYearly':'SalaryUSD(Yearly)'},inplace=True)
#print(df1['SalaryUSD(Yearly)'])
#trans = df1['Trans'].map({'Yes':'True','No':'False'})
#to apply this change in Data
df1['Trans'] = df1['Trans'].map({'Yes':'True','No':'False'})
print(df1)
