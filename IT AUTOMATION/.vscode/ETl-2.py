import json
import os 
import csv ,pickle
json_file = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//Service_node.json'
with open(json_file ,'r') as f:
    data2 = json.loads(str(f.read()))
# create an empty list   
data_list = []
# append the items to the list in the same order.
data_list.append(data2['end1Id'])
'''
with open ('C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//tests32.txt', 'wb') as f2:
            pickle.dump(s,f2)
        with open ('C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//testt32.txt', 'wb') as f1:
            pickle.dump(t,f1)
'''