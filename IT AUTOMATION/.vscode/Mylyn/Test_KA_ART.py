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
#ArticleBaseOnRequest_Path = PATH +r'/ArticleBaseOnRequest.xlsx'
#Person_Path = PATH +r'/Person.xlsx'
#PersonGroup_Path = PATH + r'/PersonGroup.xlsx'
#Article_Path = PATH +r'/Article.xlsx'
Request_Path = PATH +r'/Request.xlsx'
EXT = "*.zip"
all_zip_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]
for x in all_zip_files:
    os.remove(x)
##############################################Request_ File ##############################################
EXT5 = "Request_*.csv"
all_Request_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT5))]
df_from_Request_file = (pd.read_csv(f, sep=',') for f in all_Request_files)
df_Request_merged   = pd.concat(df_from_Request_file, ignore_index=True)
df_Request_merged.drop(df_Request_merged.columns[[0, 1]], axis = 1, inplace = True)
dict = {'Id':'Request ID','DisplayLabel':'Title','CurrentAssignment':'Current Assignment'}
df_Request_merged.rename(columns=dict,inplace=True)
df_Request_merged['Priority']=df_Request_merged['Priority'].replace('MediumPriority','Medium', regex=True)
df_Request_merged['Priority']=df_Request_merged['Priority'].replace('LowPriority','Low', regex=True)
df_Request_merged['Priority']=df_Request_merged['Priority'].replace('CriticalPriority','Critical', regex=True)
df_Request_merged['Priority']=df_Request_merged['Priority'].replace('HighPriority','High', regex=True)
df_Request_merged['ChatStatus']=df_Request_merged['ChatStatus'].replace('ChatStatusNone','None', regex=True)
df_Request_merged['ChatStatus']=df_Request_merged['ChatStatus'].replace('ChatStatusAbandoned','Abandoned', regex=True)
df_Request_merged['ChatStatus']=df_Request_merged['ChatStatus'].replace('ChatStatusPending','Pending', regex=True)
CreateTime=df_Request_merged['CreateTime']
CreateTime=pd.to_datetime(CreateTime, unit='ms')#.dt.strftime('%Y/%m/%d')
df_Request_merged['CreateTime'] = CreateTime
CloseTime=df_Request_merged['CloseTime']
CloseTime=pd.to_datetime(CloseTime, unit='ms')#.dt.strftime('%Y/%m/%d')
df_Request_merged['CloseTime'] = CloseTime
df=df_Request_merged.to_excel(Request_Path, index=False)
wb=load_workbook(Request_Path)
sheet=wb.active
for z in all_Request_files:
    os.remove(z)
print("Request file is done")