import requests 


# Define the URL and the book data
url = 'http://127.0.0.1:5000/books'

data = {
    
    "title": "The Night Circus",
    "author": "Erin Morgenstern"
}
headers={
    "Content-Type": "application/json"
}
# Send the POST request
response = requests.post(url,json=data,headers=headers)

#print the reponse
print(response.status_code)
print(response.json)