#use this script for monthly and demo
import os
from glob import glob
import pandas as pd
import os.path
import sys
from datetime import datetime,date, timedelta
import datetime
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook

#PATH = sys.argv[1]
PATH = r"C:\Users\rnsri\KA-July\TEST_KA_2911"
ArticleBaseOnRequest_Path = PATH +r'/ArticleBaseOnRequest.xlsx'
#Person_Path = PATH +r'/Person.xlsx'
#PersonGroup_Path = PATH + r'/PersonGroup.xlsx'
#Article_Path = PATH +r'/Article.xlsx'
#Request_Path = PATH +r'/Request.xlsx'
'''
EXT = "*.zip"
all_zip_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]
for x in all_zip_files:
    os.remove(x)
################################################ArticleBaseOnRequest_File################################################
EXT1 = "ArticleBaseOnRequest_*.csv"
all_ArticleBaseOnRequest_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT1))]
df_from_ArticleBaseOnRequest_file = (pd.read_csv(f, sep=',') for f in all_ArticleBaseOnRequest_files)
df_ArticleBaseOnRequest_merged   = pd.concat(df_from_ArticleBaseOnRequest_file, ignore_index=True)
df_ArticleBaseOnRequest_merged.drop(df_ArticleBaseOnRequest_merged.columns[[0, 1]], axis = 1, inplace = True)
df=df_ArticleBaseOnRequest_merged.to_excel(ArticleBaseOnRequest_Path, index=False)
df=df_ArticleBaseOnRequest_merged.to_excel(ArticleBaseOnRequest_Path, index=False)
wb=load_workbook(ArticleBaseOnRequest_Path)
sheet=wb.active
for y in all_ArticleBaseOnRequest_files:
    os.remove(y)
print("ArticleBaseOnRequest is done")
'''
#############################################Vlookup for Knowledge Article ID#################################################
df1 = pd.read_excel(ArticleBaseOnRequest_Path,engine='openpyxl')
dict = {'firstEntity_Request': 'Request ID','secondEntity_Article': 'Knowledge Article ID'}
df1.rename(columns=dict,inplace=True)
#df2=df1.append({'Request ID':'', 'Knowledge Article ID':'#N/A '}, ignore_index=True)
df2=df1.replace({'Request ID':'', 'Knowledge Article ID':'#N/A '})
con3 = pd.DataFrame(df2)
df2 = pd.concat([con3], ignore_index=True)
df = df1.to_excel(ArticleBaseOnRequest_Path,engine='openpyxl',index=False)
df1 = pd.read_excel(Request_Path,engine='openpyxl')
df2 = pd.read_excel(ArticleBaseOnRequest_Path,engine='openpyxl')
join = pd.merge(df1,df2[['Request ID', 'Knowledge Article ID']],on = 'Request ID' , how = 'left')
df = join.to_excel(Request_Path,index=False)
print("vlookup5 is done")