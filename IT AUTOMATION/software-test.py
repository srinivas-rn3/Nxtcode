from ast import Continue
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
        print("global ID:", global_Id)
        ucmdbId = i["ucmdbId"]
        type2 = i["type"]
        end1Id = n["end1Id"]
        end2Id = n["end2Id"]
        print("End1ID:",end1Id)
        print("End2Id:", end2Id)
        if end1Id == ucmdbId and type2 == 'installed_software':
            print("end1id and UCMDB_ID are same!!!")
            break
        else:
            continue

dict1 = {"Global ID":[global_Id],"type":[type2],"End1ID":[end1Id],"Display label":[label1],"END2ID":[end2Id]}
df1 = pd.DataFrame(dict1)
df1.to_csv("C:\\Users\\rnsri\\Software-ucmdb\\Aug10\\TestOP\\json_output.csv",index=False)