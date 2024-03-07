'''
1. Parsing JSON:
You can parse JSON data into Python data structures (e.g., dictionaries,
lists) using the json.loads() function.

'''
import json

# JSON string
json_str = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string into a Python dictionary
data = json.loads(json_str)
print(data)

'''
2. Serializing Python Data to JSON:
You can convert Python data structures into JSON format using the json.dumps() function.
'''
# Convert Python dictionary to JSON string
# Python dictionary
data_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
json_for = json.dumps(data_dict)
print(json_for)

'''
3. Reading JSON from a File:
You can read JSON data from a file using the json.load() function.

'''
with open(r"C:\Users\srini\OneDrive\Documents\pythonFiles\json_text_py.json",'r') as f:
    
    #load JSON Data from file 
    data2 = json.load(f)
print(data2)

'''
4. Writing JSON to a File:
You can write JSON data to a file using the json.dump() function.
'''

data_json = {'name': 'John Wick', 'age': 302, 'city': 'Paris'}

with open(r"C:\Users\srini\OneDrive\Documents\pythonFiles\json_text_py.json",'w') as wf:
    
    #Write JSON Data file 
    json.dump(data_json,wf)