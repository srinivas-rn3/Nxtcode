import requests 

# URL of the API endpoint
url = 'https://example.com/api'

# JSON payload to be sent in the request
payload = {'key':'value'}

# Make a POST request with JSON payload
response = requests.post(url,json=payload)

# Check the response status code
if response.status_code == 200:
    print("Request successsful!!!")
    print("Response :",response.json())
else:
    print("Request failed")
    print("Response status code :",response.status_code)


