import os
import requests
from bs4 import BeautifulSoup

paths = ["./files/demos", "./files/scraped_essentials"]


for path in paths:
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"Folder {paths} already exists.")
        pass

url = "https://www.passiton.com/inspirational-quotes"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
