import pandas as pd
pd_public = pd.read_csv('C:\\Users\\rnsri\\Stackoverflow\\survey_results_public.csv')
pd_schemas = pd.read_csv('C:\\Users\\rnsri\\Stackoverflow\\survey_results_schema.csv')
df1 = pd.DataFrame(pd_public)
df2 = pd.DataFrame(pd_schemas)
#print(df1.shape)
#print(df2.shape) 
#print(df1.columns)
#print(df1['Sexuality'].value_counts())#segragte values in specific column
#print(df1.head())
#print(df1.loc[3])
#print(df1.loc[[20,11,12],['Sexuality','Gender']])
#same as above with using slice 
#print(df1.loc[11:20,['Sexuality','Gender']])
#anther way slicing with columns data
print(df1.loc[21:31,'Gender':'MentalHealth'])
#https://www.youtube.com/watch?v=W9XjRYFkkyw&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=3