import json
import csv ,pickle
json_file = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//service_node_CI_Details.json'

with open (json_file , 'r') as f:
    data = json.loads(f.read())
    print (data)