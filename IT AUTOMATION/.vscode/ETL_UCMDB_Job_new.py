'''
Description : Script fetch the json and extract the 'GlobalId' which matches to 'end1Id' of 'ucmdbID'
              and fetch the 'GlobalId' matches with 'ucmdbID' of end2ID.
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
import json
import sys
import pandas as pd
import time
import os
#To get date & time
#timert = time.strftime("%Y%m%d%H%M%S")
#To get arguments and check the arguments
if len(sys.argv) >= 4:
    print("No. of arguments is:",str(sys.argv))
    #Json file path as input
    json_file = sys.argv[1]
    csv_file_name1 = sys.argv[2]
    csv_path = sys.argv[3]
else :
     print("No arguments are found, hence exiting the code!!!")
     sys.exit(2)
#creation of the driectory for csv
#dir = '/opt/nfs/UCMDB-SMAX-ETL/etl-output-csv/'
#filename = timert
#mode = 0o755
#path = os.path.join(dir, filename)
#os.mkdir(path, mode)
#Final CSV File Name creation
csv_file_name = csv_file_name1 +'.csv'
#json_file = 'C:\\Users\\rnsri\\OneDrive - Micro Focus\\DXC Support Project\\ETL\\service_comp_system_element.json'
#output/csv file location
#output_csv = '/opt/nfs/UCMDB-SMAX-ETL/etl-output-csv/' + csv_file_name
output_csv = csv_path +'/'  + csv_file_name
print ("csv file location :",output_csv)
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
            #print("UCMDB_ID are not matching!!!")
            #added to by pass print statment 21/03
            pass
#print(list1)
#print(list2)
#print(list3)

# selection of the headers for the csv


service = csv_file_name1
if service == "servicecomponentcontainsdevice":
    first_index = "device_globalid"
    second_index = "servicecomponent_globalid"
    
elif service == "systemelementcontainsdevice_1":
    first_index = "device_globalid"
    second_index = "systemelement_globalid"

elif service == "systemelementcontainsdevice_2":
    first_index = "device_globalid"
    second_index = "systemelement_globalid"
    
elif service == "servicecomponentcontainssystemelement":
    first_index = "systemelement_globalid"
    second_index = "servicecomponent_globalid"
    
elif service == "actualservicecontainsservicecomponent":
    first_index = "servicecomponent_globalid"
    second_index = "actualservice_globalid"
    
else:
    first_index = "device_globalid"
    second_index = "servicecomponent_globalid"
    
print("service Name is :", service)
print("First Index:" ,first_index, end = " " )
print("Second Index is :",second_index , end= " ")

#Constructing DataFrame from a dictionary.
try:
    #df  = pd.DataFrame({'device_globalid':list3,'servicecomponent_globalid':list2})
    df  = pd.DataFrame({first_index :list3, second_index:list2})
    #print(df)
    #Write DataFrame to csv file.
    df.to_csv(output_csv,index=False)
except pd.errors.ParserError as e :
    print(e)
    sys.exit(1)
f.close()
