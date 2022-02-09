from encodings import utf_8
import json
from operator import index
import pandas as pd
json_file = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//Service_node.json'
with open(json_file ,'r') as f:
    data2 = json.loads(str(f.read()))
nesting_list =pd.json_normalize(data2, record_path=['relations'])
print (nesting_list)
nesting_list.to_csv('C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//test.csv',encoding = 'utf-8', index= False)