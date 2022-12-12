#https://www.youtube.com/watch?v=HQ6XO9eT-fc&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=6
#Python Pandas Tutorial (Part 6): Add/Remove Rows and Columns From DataFrames
'''
people = {
    "first": ['Srini','Marine','Jane','Kim','Adam'],
    "last": ['RN','Chang','Doe','Doe','Adrian'],
    "email": ['srinivas.rn@xxx.com','marnie.change@xxx.com','jane.doe@xxx.com','kim.doe@xxx.com','adam.adrian@xxx.com']
}
'''
import pandas as pd

'''
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
#merge two data frame
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
'''
#Python Pandas Tutorial Sorting Data
#https://www.youtube.com/watch?v=T11QYVfZoD0&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=7
#df = pd.DataFrame(people)
#print(df.sort_values(by='last',ascending=False))
#print(df.sort_values(by=['last','first'],ascending=False))
#asending in specfic cloumn
#df.sort_values(by=['last','first'],ascending=[False,True],inplace=True)
#print(df)
#df.sort_index()#To sort by index
#print(df)
#sort single series
#print(df['last'].sort_values())
#print(df)
#stackoverflow Data
pd_schema = pd.read_csv(r'C:/Users/rnsri/Stackoverflow/survey_results_schema.csv')
pd_public = pd.read_csv(r'C:/Users/rnsri/Stackoverflow/survey_results_public.csv')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
df_pub = pd.DataFrame(pd_public)
df_schema = pd.DataFrame(pd_schema)

#df_pub.sort_values(by=['Country','ConvertedCompYearly'],ascending=[True,False],inplace=True)
#print(df_pub[['Country','ConvertedCompYearly']].head(50))
#to sort biggest numbers in given columns
#print(df_pub['ConvertedCompYearly'].nlargest(50))
#For Entire DataFrame to apply nlargest
#print(df_pub.nlargest(10,'ConvertedCompYearly'))
#For smallest valeus 
print(df_pub.nsmallest(10,'ConvertedCompYearly'))