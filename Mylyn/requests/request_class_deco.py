#This is smaple code only..not gone work!!

import requests 
class AuthenticationError(Exception):
    pass

def is_authenticated(username,password):
    valid_cred ={
        "user1":"Password1",
        "user2":"Password2",
        "user3":"Password3"
    }
    if username in valid_cred and valid_cred[username] == 'password':
        return True 
    else:
        return False

#Decorator
def authenticated(func):
    def wrapper(*args,**kwargs):
        if not is_authenticated():
            raise AuthenticationError("User is not defined!")
        return func(*args,**kwargs)
    return wrapper

#Apli client class
class ApiClient:
    def __init__(self,base_url):
        self.base_url = base_url
    
    @authenticated
    def get_data(self,endpoint):
        response = requests.get(self.base_url + endpoint)
        return response.json()
    
    @authenticated
    def post_data(self,endpoint,data):
        response = requests.post(self.base_url + endpoint,json=data)
        return response.json()
    
# Instantiate API client
api_client = ApiClient("https://api.example.com")


# Try accessing data without authentication (will raise AuthenticationError)
try:
    data = api_client.get_data("/user")

except AuthenticationError as e:
    print("Authentication error:",e)

# Simulating authentication by ensuring is_authenticated returns True
data = api_client.get_data("/Users")
print("Response:",data)

# Simulating authentication by ensuring is_authenticated returns True
json = {'user':'xxxxxx',
        'pass':'secrets'}
data = api_client.post_data("/create_user",json) 
print("Response:",data)
