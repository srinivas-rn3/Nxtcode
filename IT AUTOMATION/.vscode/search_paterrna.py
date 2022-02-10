import json
import sys
import pickle
 #json load file location
json_file = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//Service_node.json'
#converted csv file location
output_csv = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//test3.csv'
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
        if s == n["ucmdbId"]:
          print(n["ucmdbId"])
          list1.append(t)
          list2.append(n["globalId"])
        else:
          print("not matching")
print(list1)
print(list2)
