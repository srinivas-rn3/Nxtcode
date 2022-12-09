#https://www.youtube.com/watch?v=HQ6XO9eT-fc&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=6
#Python Pandas Tutorial (Part 6): Add/Remove Rows and Columns From DataFrames
people = {
    "first": ['Srini','Marine','Jane','Kim'],
    "last": ['RN','Chang','Doe','Doe'],
    "email": ['srinivas.rn@xxx.com','marnie.change@xxx.com','jane.doe@xxx.com','kim.doe@xxx.com']
}
import pandas as pd 

df1 = pd.DataFrame(people)
#print(df1)
df1['full_name'] = df1['first']+ ' '+df1['last']
#print(df1)
df1.drop(columns=['first','last'],inplace=True)
#print(df1)
# To create two more columns from 'single Columns'
#print(df1['full_name'].str.split(' ',expand=True))
df1[['fisr','last']] = df1['full_name'].str.split(' ',expand=True)
#print(df1)
#df1.append({'first':'Tony'},ignore_index=True)
#print(df1)
heros = {
    'first':['Tony','Steve'],
    'last':['Stark','Rogers'],
    'email':['ironman@avenger.com','cap@avenger.com']
}
df2 = pd.DataFrame(heros)
#print(df2)
#merge tow data frame
df1 = df1.append(df2,ignore_index=True)
print(df1)
df1 = df1.drop(index=4)#to drop Index
print(df1)
#another way ote remove row data
#df1 = df1.drop(index=df1[df1['last'] == 'Doe'].index)
print(df1)
#another way
filt = df1['last'] == 'Doe'
df1 = df1.drop(index=df1[filt].index)
print(df1)
#Python Pandas Tutorial Sorting Data
#https://www.youtube.com/watch?v=T11QYVfZoD0&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=7