from bs4 import BeautifulSoup
import requests

# Fetch the web page content
#file = r"c:/Users/srini/Documents/example.html"
url = "http://example.com"
response = requests.get(url)
web_content = response.text
#print(web_content)
#with open(file,'w',encoding='utf-8') as f:
#    f.write(web_content)
# Parse the web page content

soup = BeautifulSoup(web_content,'html.parser')

# Find and print the title of the page
title = soup.title.string
print("Page title:",title)

# Find and print all hyperlinks on the page
for link in soup.find_all('a'):
    print(link.get('href'))

# Find and print the text of a specific tag
para = soup.find('p').get_text()
print("First Paragraph:",para)