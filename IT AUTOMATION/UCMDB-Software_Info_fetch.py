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
#Final CSV File Name creation
csv_file_name = 'sercice_software_ETL' + timert +'.csv'
#json_file = 'C:\\Users\\rnsri\\OneDrive - Micro Focus\\DXC Support Project\\ETL\\service_comp_system_element.json'
#output/csv file location
output_csv = 'C:\\Users\\rnsri\\Software-ucmdb\\Aug10\\'+ csv_file_name
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
list1= []; list2 = []; list3 =[]; list4 =[]; list5 =[];
#looping to fetch the  json data
for i in data["cis"]:
    for n in data["relations"]:
        label1 = i["properties"]["display_label"]
        global_Id = i["globalId"]
        ucmdbId = i["ucmdbId"]
        type2 = i["type"]
        end2Id = n["end2Id"]
        end1Id = n["end1Id"]
#dict1 = {"Global ID":[global_Id],"type":[type2],"End1ID":[end1Id],"Display label":[label1],"END2ID":[end2Id]}
#df1 = pd.DataFrame(dict1)
#df1.to_csv("C:\\Users\\rnsri\\Software-ucmdb\\Aug10\\TestOP\\json_output.csv",index=False)
        if end1Id == ucmdbId and type2 == 'nt':
            list1.append(end1Id)
            list3.append(label1)
            list5.append(end2Id)
            list2.append(global_Id)
            #list3.append(ucmdbId)
        else:
            #print("UCMDB_ID are not matching!!! ")
            continue
#Constructing DataFrame from a dictionary.
try:
    df = pd.DataFrame({'End1ID':list1,'End2ID':list5,'Software Label':list3,'Global ID':list2})
    #print(df)
    #Write DataFrame to csv file.
    df.to_csv(output_csv,index=False)
    print("CSV Path Location is :",output_csv)
except pd.errors.ParserError as e :
    print(e)
    sys.exit(1)
f.close()