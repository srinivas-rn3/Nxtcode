import requests 
from bs4 import BeautifulSoup

#Define the URL
url = 'https://google.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content,'html.parser')
    
     # Find and print the page title
    title =  soup.title.string
    print(f"Page title: {title}")
    
    # Extract and print all links on the page
    links =  soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print(f"Failed to retrieve the webapge.Status code:{response.status_code}")