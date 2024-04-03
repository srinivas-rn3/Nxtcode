import json
import sys
import pandas as pd
#json file Location
json_file = 'C:\\Users\\rnsri\\OneDrive - Micro Focus\\DXC Support Project\\ETL\\today_date_service_json_data.json'
output_csv = 'C:\\Users\\rnsri\\OneDrive - Micro Focus\\DXC Support Project\\ETL\\test-ETL.csv'
with open (json_file, 'r') as f:
    data = json.loads(f.read())
    #print(data)
list1= []; list2 = []; list3 =[]
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
            list1.append(end2Id)
            list2.append(globalId)
            list3.append(ucmdbId)
        else:
            print("end1Id & ucmdbId are not matching!!! ")
print(list1)
print(list2)

df  = pd.DataFrame({'end2Id':list1,'Global ID':list2, 'ucmdbID':list3})
print(df)
df.to_csv(output_csv,index=False)