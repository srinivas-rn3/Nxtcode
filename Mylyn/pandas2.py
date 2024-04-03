import pandas as pd
#pd_public = pd.read_csv('C:\\Users\\rnsri\\Stackoverflow\\survey_results_public.csv')
pd_schemas = pd.read_csv('C:\\Users\\rnsri\\Stackoverflow\\survey_results_schema.csv',index_col='qid')
pd_public = pd.read_csv('C:\\Users\\rnsri\\Stackoverflow\\survey_results_public.csv',index_col='ResponseId')
#df1 = pd.DataFrame(pd_public)
#df2 = pd.DataFrame(pd_schemas)
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
#print(df1.loc[21:31,'Gender':'MentalHealth'])
#https://www.youtube.com/watch?v=W9XjRYFkkyw&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=3
'''
people = {
    "first" : ["Srini","Marnie","Kim"],
    "last": ["RN","Sapparnno","Randy"],
    "email": ["srini.rn@xxx.xxx","marnie.sapparnno@xxx.xxx","kim.randy@xxx.xxx"]
}
'''
#df = pd.DataFrame(people)
#print(df)
#print(df['email'])
#set index  and make change thsi email as index to data we have to use inplace = True
#print(df.set_index('email',inplace=True))
#print(df.index)#to see index
#print(df)
#to find the vlaeu from index
#print(df.loc['kim.randy@xxx.xxx'])
#now we dont have normal index we cahged to email
#print(df.loc[0])
#but iloc works Purely integer-location based indexing for selection by position.it operataes on integers
#print(df.iloc[0])
#to reset indexes back to original
#print(df.reset_index(inplace=True))
#print(df)
pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',10)
#print(df1.head())
#print(df1.columns)
#print(pd_public.loc[100])
#print(pd_schemas.head(5))
#print(pd_schemas.loc['QID308'])
#sort
pd_schemas.sort_index(inplace=True)
print(pd_schemas.head(5))
#https://www.youtube.com/watch?v=Lw2rlcxScZY&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=4