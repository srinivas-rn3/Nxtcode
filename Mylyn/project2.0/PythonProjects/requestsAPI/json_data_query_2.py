import json 
json_data = '''
{
    "students": [
        {
            "name": "Alice",
            "age": 20,
            "grade": "A"
        },
        {
            "name": "Bob",
            "age": 22,
            "grade": "B"
        },
        {
            "name": "Charlie",
            "age": 21,
            "grade": "C"
        }
    ]
}
'''
#load Json data 
data = json.loads(json_data)
print(data)

# Query and select specific values
selected_names = [student['name'] for student in data['students'] if student['age'] > 20]
print("names of student older than 20:" )
#print(list(selected_names))
#for names in selected_names:
#    print(names)
for index,names in enumerate(selected_names,1):
    print(f"{index} : {names}")
    
########################################### Eg.2 #######################################################
try:
    with open(r"C:\Users\srini\OneDrive\Documents\pythonFiles\book_json.json","r") as json_file:
        data2 = json.load(json_file)

    ## Query and select specific values
    selected_titles = [book['title'] for book in data2["library"]["books"] if book['genre'] == 'Fiction' and book['available']]

    print("Title of available fiction are: ")
    for title in selected_titles:
        print(title)
except FileNotFoundError:
    print("Error: File not found!!")

except json.JSONDecodeError as e:
    print("Error: Invalid JSON data format:",e)

except KeyError as e:
    print("Error: Missing key in jSON Data:",e)

except Exception as e:
    print("An Error occured:" ,e)
    