import json
import sys
import pickle
import pandas as pd
 #json load file location
#json_file = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//Service_node.json'
json_file = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//service_node_CI_Details.json'
#converted csv file location
output_csv = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//test333.csv'
with open(json_file) as f:
    data = json.load(f)
    #print(data)

#create empty list
list1 = []
list2 = []
for i in data["relations"]:
    for n in data["cis"]:
        s = i['end1Id']
        #print(s) 
        t = i["end2Id"]
        #print(t)
        u = n["globalId"]
        print(u)
        if s == n["ucmdbId"]:
          print(n["ucmdbId"])
          list1.append(t)
          #list2.append(n["globalId"])
          list2.append(u)
        else:
          print("not matching")
print("ucmdb ID:" ,list1)
print("Global ID:",list2)

'''
df = pd.DataFrame({'Device_Global ID ':list1,'ServiceComp_Global ID':list2})

print(df)

#df1 = df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)

df.to_csv(output_csv,index=False)
'''