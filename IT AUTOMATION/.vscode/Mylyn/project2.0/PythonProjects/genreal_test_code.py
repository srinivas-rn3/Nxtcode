add = lambda x,y:x+y 
print(add(10,100))

import requests 
response = requests.get("https://www.example222.com")
## Check if the status code indicates an error (4xx or 5xx)
response.raise_for_status()

'''
If the status code of the response is a client error (4xx) or a server error (5xx), 
the raise_for_status() method will raise an HTTPError exception, indicating that there was a
problem with the request. If the status code is not an error, the method does nothing and the program continues execution.

This method is particularly useful for handling errors in a concise and readable manner when 
making HTTP requests in Python, ensuring that errors are caught and handled appropriately in your code.
'''