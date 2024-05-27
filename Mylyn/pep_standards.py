import os 
import sys 
import requests 

def cache_result(func):
      """Decorator to cache function results."""
      cache = {}
      
      def wrapper(*args):
          if args  not in cache:
              cache[args] = func(*args)
          return cache[args]
      return wrapper
  
class DataFacotr:
    """Class to fetch and cache data from an API."""
    
    API_URL = "https://api.example.com/data"
    
    def __init__(self,api_key):
        self.api = api_key 
    
    @cache_result
    def Fetch_data(self,endpoint):
          """Fetch data from the given endpoint."""
          url = f"{self.API_URL}/endpoint"
          response = requests.get(url,headers={"Authorization":f"Bearer: {self.api_key}"})
          if response.status_code == 200:
              return response.json()
          response.raise_for_status() 
          
def main():
      """Main function to demonstrate fetching data."""
      api_key = os.getenv("API_KEY")
      if not api_key:
          print("API Key is missing!!")
          sys.exit(1)
      fetcher = DataFacotr(api_key)
      try:
          data = fetcher.Fetch_data("resources")
          print(data)
      except requests.HTTPError as http_err:
          print(f"HTTP error occured: {http_err}")
      except Exception as err:
          print(f"Other error occured:{err}")

if __name__ == "__main__":
    main()
    