#script to convert json to csv with only two columns 'end1Id & 'end3Id'
import json
import pandas as pd
#json load file location
json_file = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//Service_node.json'
#converted csv file location
output_csv = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//test3.csv'
with open(json_file ,'r') as f:
    data2 = json.loads(str(f.read()))
nesting_list = pd.json_normalize(data2, record_path=['relations'])
to_be_dropped = ['ucmdbId','globalId','type','properties','label','attributesQualifiers','displayLabel']
nesting_list.drop(columns = to_be_dropped, inplace = True)
#print (nesting_list)
#nesting_list.to_csv('C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//test2.csv',encoding = 'utf-8', index= False)
nesting_list.to_csv(output_csv,encoding = 'utf-8', index= False)