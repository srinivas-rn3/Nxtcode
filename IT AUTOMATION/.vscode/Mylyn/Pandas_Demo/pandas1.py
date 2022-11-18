#https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
#stackOverFlow
import pandas as pd
pd_public = pd.read_csv('C:\\Users\\rnsri\\Stackoverflow\\survey_results_public.csv')
pd_schemas = pd.read_csv('C:\\Users\\rnsri\\Stackoverflow\\survey_results_schema.csv')
#print(df)
#print(df.shape)
#print(df.info())
#pd.set_option('display.max_columns',79)
#print(df)
#print(pd_schemas)
#print(df.head(10))
#print(df.tail(10))
#https://www.youtube.com/watch?v=zmdjNSmRXF4&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=2
#pd.set_option('display.max_columns',85)
#pd.set_option('display.max_rows',85)
#print(df.head())
people ={
    "first" : ['Srinu','Marnie','Goku'],
    "last" : ['shet','Sararnno','Takashi'],
    "email": ['srini@xxxx.com','marine@xxxx.com','goku@xxxx.com']
}
#print(people['email'])
df = pd.DataFrame(people)
#access columns
#print(df['email'])
#print(type(df['email']))
#or another way to access column
#print(df.email)
#print(df[['first','last']])
#print(df.columns)
#to acess row use 'DataFrame.iloc' or 'DataFrame.loc'
#print(df.iloc[2])
#to pass multiple rows(pass as list[])
#print(df.iloc[[0,1]])
#to get rows along with columns 
# print(df.iloc[[0,1],2])# 2 is columns in our case 'email
#loc search for lable of rows nothing but index
#print(df.loc[0])
#to get frist row and secod row using loc
#print(df.loc[[0,1]])
#to get frist row and secod row  along with column using loc
#print(df.loc[[0,1],'email'])
#print(df.loc[[0,1],['email','last']])#multiple columns

