#Python Pandas Tutorial (Part 4): Filtering - Using Conditionals to Filter Rows and Columns
import pandas as pd
'''
people = {
    "first": ['Srini','Marine','Jane','Kim'],
    "last": ['RN','Chang','Doe','Doe'],
    "email": ['srinivas.rn@xxx.com','marnie.change@xxx.com','jane.doe@xxx.com','kim.doe@xxx.com']
}
df = pd.DataFrame(people)
#filt = (df['last']=='Doe')
#print(df[filt])
#or anther ways is 
#print(df[df['last']=='Doe'])# thsi difficult ot read
#or another way
#print(df.loc[filt])
#filter with &(and) |(or)
filt1 = (df['last'] =='Doe') & (df['first']=='Jane')
#print(df.loc[filt1,'email'])
#filter with or(|)
filt2 = (df['last'] == 'RN') | (df['first'] == 'John')
print(df.loc[filt2,'email'])
print(df.loc[~filt2,'email'])#neget opppsite of or {|}
'''
pd_schema = pd.read_csv(r'C:/Users/rnsri/Stackoverflow/survey_results_schema.csv')
pd_public = pd.read_csv(r'C:/Users/rnsri/Stackoverflow/survey_results_public.csv')

df1 = pd.DataFrame(pd_public)
df2 = pd.DataFrame(pd_schema)

#pd.set_option('display.max_columns',85)
#pd.set_option('display.max_rows',10)
#print(df1.head(10))
#print(df1.columns)
#high_salary = df1['ConvertedCompYearly'] >70000)
#gender_w =  (df1['Gender'] =='Woman') & (df1['ConvertedCompYearly']> 70000)
#print(df1.loc[gender_w,['Country','ConvertedCompYearly','Sexuality','Gender']])
#print(df1.loc[high_salary,['Country','Sexuality']])
#countries = ['India', 'United States of America','Israel']
#countries = ['Israel']
#filt3 = df1['Country'].isin(countries)
#print(df1.loc[high_salary,['Country','LanguageHaveWorkedWith','ConvertedCompYearly','Ethnicity']])
#print(df1.loc[filt3,['Country','LanguageHaveWorkedWith','ConvertedCompYearly']])
#lang = (df1['LanguageHaveWorkedWith'].str.contains('Python', na=False))
#print(df1.loc[lang,'LanguageHaveWorkedWith'])
#filter4 = (df1['Country'] == 'India') & (df1['Gender'] == 'Woman')
#print(df1.loc[filter4,['ConvertedCompYearly','Sexuality']])
countries = ['India']
filter5 = df1['Country'].isin(countries)
print(df1.loc[filter5,['ConvertedCompYearly','OpSysProfessional use',"Gender","Sexuality"]])
