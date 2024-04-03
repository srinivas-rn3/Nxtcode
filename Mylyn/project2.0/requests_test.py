import requests
'''
r = rq.get("https://www.google.com")
print(r.status_code)
'''

'''
r = rq.get(url)
print(r.raise_for_status)
print(r.status_code)
'''
'''
url = "https://www.amazon.com/nothing_here"

try:
    r = requests.get(url,timeout=1)
    r.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP ERROR!!")
    print(errh.args[0])
    
#https://www.geeksforgeeks.org/exception-handling-of-python-requests-module/
'''
#url = "https://www.google.com"
#url1 ="https://www.amazon.com/nothing_here"
'''
try:
    r = requests.get(url,timeout=0.1)
    r.raise_for_status()
except requests.exceptions.RequestException as errx:
    print("Exception request")
'''
'''
try:
    r = requests.get(url1,timeout=1)
    r.raise_for_status()
except requests.exceptions.ReadTimeout as errR:
    print("TimeOut Error!!!")
except requests.exceptions.ConnectionError as errc:
    print("Failed to connect!!")
    print(errc.args[0])
except requests.exceptions.HTTPError as errh:
    print("HTTP Error")
    print(errh.args[0])
'''
'''
Handle Exceptions: It's a good practice to handle exceptions that may occur during the request, such as network issues or timeouts. 
You can use the try and except blocks to catch exceptions and handle them gracefully.
'''
'''
import requests

url = 'https://example.com'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses
    print("GET request was successful!")
    print("Response content:", response.text)
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Other Error: {err}")
'''
'''
Check for Specific Status Codes: Instead of just checking for a status code of 200, you might want to handle other specific status codes differently.
For example, you might want to treat a 404 (Not Found) differently from a 500 (Internal Server Error).
'''
'''
import requests 

url = "https://example.com"
response = requests.get(url)
if response.status_code == 200:
    print("GET Request was successful!!!")
    print("response Content:",response.text)
elif response.status_code == 404:
    print("The Requested resource was not found!!!")
else:
    print(f"GET request failed with status code {response.status_code}")
    print("Reponse content:",response.text)
'''
'''
#Exception Handling for Connection Error
url = "https://www.blahhh.com"
try:
    r = requests.get(url,timeout=1,verify=True)
    r.raise_for_status()
except requests.exceptions.ConnectionError as errr:
    print("Connection Error")
except requests.exceptions.HTTPError as errh:
    print("HTTP Connection Error!!!")
except requests.exceptions.ReadTimeout as errrt:
    print("Time out")
'''
def calulator_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negitive numbers")

    else:
        return number ** 0.5
try:
    result = calulator_square_root(-9)
    print("Square root:",result)
except ValueError as e:
    print("Error:",e)
