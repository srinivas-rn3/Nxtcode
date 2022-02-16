'''
Description : Script fetch the json and extract the 'GlobalId' which matches to 'end1Id' of 'ucmdbID'
              and fetch the 'GlobalId' matches with 'ucmdbID' of end2ID.
Input : Json file present in ETL Machine
Output : '.csv' is created in  ETL Machine (Provided the file location)
Team : MFI.
Developer E-mail : srinivas.rn2@microfocus.com.
Version : 1.0.
Script Type : Python.
Compiler version :  Works with python 3.6 and above.
Modules Used: json,sys,time and pandas (Need to install all mentioned modules before executing).
File Permission : In linux/unix provide the file permssion with '755'.

'''
import json
import sys
import pandas as pd
import time
#To get date & time
timert = time.strftime("%Y-%m-%d-%H-%M-%S")
csv_file_name = 'systemelementcontainsdevice-' + timert +'.csv'
#print(timert)
#json file Location
#json_file = 'C:\\Users\\rnsri\\OneDrive - Micro Focus\\DXC Support Project\\ETL\\today_date_service_json_data.json'
json_file = 'C:\\Users\\rnsri\\OneDrive - Micro Focus\\DXC Support Project\\ETL\\systemelementcontainsdevice.json'
#output/csv file location
output_csv = 'C:\\Users\\rnsri\\OneDrive - Micro Focus\\DXC Support Project\\ETL\\'+ csv_file_name
 
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
list1= []; list2 = []; list3 =[]
#looping to fetch the  json data
for i in data["relations"]:
    for n in data["cis"]:
        end1Id = i["end1Id"]
        #print("End1Id:", end1Id)
        end2Id = i["end2Id"]
        #print("End2Id:", end2Id)
        globalId = n["globalId"]
        #print("GloabId:",globalID)
        ucmdbId = n["ucmdbId"]
        if end1Id == ucmdbId:
            #print("ucmdbId:", ucmdbId)
            #list1.append(end2Id)
            list2.append(globalId)
            #list3.append(ucmdbId)
        elif end2Id == ucmdbId:
            list3.append(globalId)
        else:
            print("UCMDB_ID are not matching!!! ")
#print(list1)
#print(list2)
#print(list3)

#Constructing DataFrame from a dictionary.
try:
    df  = pd.DataFrame({'End2Id_GlobalId':list3,'End1_GlobalId':list2})
    #print(df)
    #Write DataFrame to csv file.
    df.to_csv(output_csv,index=False)
except pd.errors.ParserError as e :
    print(e)
    sys.exit(1)
f.close()
