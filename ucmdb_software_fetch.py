#import Json module and parse
import json ,sys, csv
import pandas as pd
from pandas import json_normalize
from datetime import datetime,timezone

# datetime object containing current date and time
st_time1 = datetime.now()
st_time = st_time1.strftime("%d%m%Y%H%M%S")
#csv file Location and Name
csv_loc = r"C:\Users\rnsri\Software-ucmdb\ucmdb_software_fetch"+"_"+st_time+'.''csv'
#json File
json_file = sys.argv[1]

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
        ucmdbId = i["ucmdbId"]
        display_label = i["properties"]["display_label"]
        #print(display_label)
        #print("End1Id:", end1Id)
        type1 = i["type"]
        print(type1)
        #print("End2Id:", end2Id)
        end2Id = n["end2Id"]
        end1Id = n["end1Id"]
        #print("GloabId:",globalID)
        ucmdbId = n["ucmdbId"]
        if ucmdbId == end2Id :
            #print("ucmdbId:", ucmdbId)
            #list1.append(end2Id)
                print("matches!!!!")
                list1.append(type1)
                list2.append(ucmdbId)
                list3.append(end2Id)
                list4.append(display_label)
                list5.append(end1Id)
                #list3.append(ucmdbId)
        else:
            continue
#print(list1)
#print(list2)
print(list3)

#Constructing DataFrame from a dictionary.
try:
    df  = pd.DataFrame({'end1':list5,'search_in_type':list1,'ucmdbid':list2,'display_label':list4,'end2Id':list3})
    #print(df)
    #Write DataFrame to csv file.
    df.to_csv(csv_loc,index=False)
except pd.errors.ParserError as e :
    print(e)
    sys.exit(1)
f.close()