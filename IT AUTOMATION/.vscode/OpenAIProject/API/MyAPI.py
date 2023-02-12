import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class APIS:
    
    URL = "https://api.open-notify.org/astros.json"

    def __init__(self):
        pass
    def Get_Status(self):
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        session.get(self.URL)
        self.response = requests.get(self.URL)
        print("Status Code is : ", self.response.status_code)
    def Json_Result(self):
        print("API Result:",self.reponse.json())

API = APIS()
API.Get_Status()
API.Json_Result()


