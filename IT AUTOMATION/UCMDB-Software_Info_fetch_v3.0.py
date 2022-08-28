import atexit
import json
import sys
import pandas as pd
import time
from datetime import timedelta, datetime
#To get date & time
timert = time.strftime("%Y-%m-%d-%H-%M-%S")
#To get arguments and check the arguments
if len(sys.argv) >= 2:
    print("No. of arguments is:",str(sys.argv))
    #Json file path as input
    json_file = sys.argv[1]
else :
     print("No arguments are found, hence exiting the code!!!")
     sys.exit(2)
start = time.time()
#Final CSV File Name creation
csv_file_name = 'service_software_ETL_v2.0_' + timert +'.csv'
#json_file = 'C:\\Users\\rnsri\\OneDrive - Micro Focus\\DXC Support Project\\ETL\\service_comp_system_element.json'
#output/csv file location
output_csv = 'C:\\Users\\rnsri\\Software-ucmdb\\\Aug26\\'+ csv_file_name
#Exception Handling for file open and Json load
try:
    #reading json file and loading json data
    with open (json_file, 'rb') as f:
        data = json.loads(f.read()) 
        #print(data)
except FileNotFoundError:
        print("Sorry, the file "+ json_file + " does not exist.")
        sys.exit(1)
except json.decoder.JSONDecodeError:
        print("String could not be converted to JSON")
        sys.exit(1)
#looping to fetch the  json data
#for i in data["cis"]:

#json_data = pd.json_normalize(data,record_path=['cis'])
#json_data1 = pd.json_normalize(data,record_path=['relations'])

'''
df_reindex = df3.reindex(columns=['properties.discovered_vendor','ucmdbId','globalId',
                          'properties.supported_operation_systems',
                          'properties.display_label','properties.last_used_date',
                          'properties.version','properties.last_discovered_time',
                          'properties.discovered_vendor',
                          'properties.sd_type','properties.serial_number','end1Id','end2Id'])

df4 = df_merge.rename({'properties.discovered_vendor':'discovered_vendor',
                 'ucmdbId':'UcmdbId','globalId':'GlobalID',
                 'properties.supported_operation_systems':'OS',
                 'properties.display_label':'Display Label',
                 'properties.last_used_date':'Last Used Date',
                 'properties.version':'Version',
                 'properties.last_discovered_time':'Last Discovered Time',
                 'properties.discovered_vendor':'Discovered Vendor',
                 'properties.sd_type':'SD Type',
                 'properties.serial_number':'Serial Number',
                 'end1Id':'End1Id',
                 'end2Id':'End2Id'
                 })
'''
df = pd.json_normalize(data, record_path=['cis'])
df.to_csv(output_csv,index=False)
print("CSV Path Location is :",output_csv)