import json
import sys
import pickle
from pprint import pprint
#import pandas as pd
 #json load file location
json_file = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//service_node_CI_Details.json'
#json_file = 'service_node_CI_Details.json'
#converted csv file location
#output_csv = 'C://Users//rnsri//OneDrive - Micro Focus//DXC Support Project//ETL//test333.csv'

with open (json_file) as f:
    document =  json.load(f)