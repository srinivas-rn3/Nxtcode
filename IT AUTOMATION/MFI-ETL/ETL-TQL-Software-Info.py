import atexit
import json
import sys
import pandas as pd
import time
from datetime import timedelta, datetime
#To get date & time
def ucmdb_software_info(tql_json,tql_name):
    timert = time.strftime("%Y-%m-%d-%H-%M-%S")
    #To get arguments and check the arguments
    json_file = tql_json
    start = time.time()
    #Final CSV File Name creation
    csv_file_name = tql_name+'-'+ timert +'.csv'
    #json_file = 'C:\\Users\\rnsri\\OneDrive - Micro Focus\\DXC Support Project\\ETL\\service_comp_system_element.json'
    #output/csv file location
    output_csv = 'C:\\Users\\rnsri\\Software-ucmdb\\SEP1\\'+ csv_file_name
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
    #Normalize the data
    df = pd.json_normalize(data, record_path=['cis'])
    df1 = pd.DataFrame(df,columns=['ucmdbId','globalId','type','label',
                                   'properties.display_label','properties.last_used_date',
                                   'properties.last_discovered_time','properties.discovered_vendor','properties.supported_operation_systems',
                                   'properties.version'])
    df1.to_csv(output_csv,index=False)
    print("CSV Path Location is :",output_csv)
    end = time.time()
    print("The time of execution of above program is :", end-start)
#calling function
ucmdb_software_info("C://Users//rnsri//Software-ucmdb//SEP1//InstalledSoftware_adobe.json","InstalledSoftware_adobe")