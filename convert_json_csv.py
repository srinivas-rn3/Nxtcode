import pandas as pd
import json
# Create json string
# with student details
json_string = '''
[
    { "id": "1", "name": "sravan","age":22 },
    { "id": "2", "name": "harsha","age":22 },
    { "id": "3", "name": "deepika","age":21 },
    { "id": "4", "name": "jyothika","age":23 }
]
'''
# Load json data and convert to Dataframe 
df = pd.json_normalize(json.loads(json_string)) 
# Display the Dataframe
print(df)