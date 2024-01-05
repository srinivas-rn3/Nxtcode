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
url = "https://www.amazon.com/nothing_here"

try:
    r = requests.get(url,timeout=1)
    r.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP ERROR!!")
    print(errh.args[0])
    
#https://www.geeksforgeeks.org/exception-handling-of-python-requests-module/




