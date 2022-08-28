'''
Description : Script fetch the json and extract the 'UCMDB ID' which matches to 'end1Id'.
              and compare type 'nt'
Input : JSON file present in ETL Machine
Output : '.csv' is created in  ETL Machine (Provided the file location)
Team : MFI.
Developer E-mail : srinivas.rn2@microfocus.com.
Version : 1.0.
Script Type : Python.
Compiler version :  Works with python 3.6 and above.
Modules Used : JSON,sys,time and pandas (Need to install all mentioned modules before executing).
File Permission : In Linux/Unix provide the file permission with '755'.

'''
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
csv_file_name = 'service_software_ETL_v2.0' + timert +'.csv'
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
#creating empty lists 
list1= []; list2 = []; list3 =[]; list4 =[]; list5 =[]; list6  =[];
list7 = []; list8 =[]; list9 =[]; list10 =[]; list11 =[];list12 =[];
#looping to fetch the  json data
for i in data["cis"]:
    type3 = i["type"]
    if type3 == "installed_software":
        properties = i["properties"]
    for n in data["relations"]:
        version1 = i["properties"]["version"]
        global_Id = i["globalId"]
        ucmdbId = i["ucmdbId"]
        type2 = i["type"]
        display_label = i["properties"]["display_label"]
        supported_operation_systems = i["properties"]["supported_operation_systems"]
        end2Id = n["end2Id"]
        end1Id = n["end1Id"]
        sd_type = i["properties"][sd_type]
        print("display label")
        print(display_label)
        print("supported_operation_systems")
        print(supported_operation_systems)
        print("version")
        print(version1)
        print("sd_type")
        print(sd_type)
'''
#dict1 = {"Global ID":[global_Id],"type":[type2],"End1ID":[end1Id],"Display label":[label1],"END2ID":[end2Id]}
#df1 = pd.DataFrame(dict1)
#df1.to_csv("C:\\Users\\rnsri\\Software-ucmdb\\Aug10\\TestOP\\json_output.csv",index=False)
        if end1Id == ucmdbId and type2 == 'nt':
            list1.append(end1Id)
            #list3.append(label1)
            list5.append(end2Id)
            list2.append(global_Id)
            #list6.append(display_label)
            #list7.append(sd_type)
            #list8.append(serial_number)
            #list9.append(last_used_date)
            #list10.append(discovered_vendor)
            list11.append(supported_operation_systems)
            #list12.append(last_discovered_time)
            #list3.append(ucmdbId)
        else:
            #print("UCMDB_ID are not matching!!! ")
            continue
#Constructing DataFrame from a dictionary.
try:
    df = pd.DataFrame({'End1ID':list1,'End2ID':list5,'Software Label':list3,'Global ID':list2,
                       'last_discovered_time':list12,'supported_operation_systems':list11,
                       'discovered_vendor':list10,'last_used_date':list9,})
    #print(df)
    #Write DataFrame to csv file.
    df.to_csv(output_csv,index=False)
    print("CSV Path Location is :",output_csv)
except pd.errors.ParserError as e :
    print(e)
    sys.exit(1)
f.close()
end = time.time()
print("The time of execution of above program is :", end-start)
'''