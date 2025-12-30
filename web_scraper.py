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
#print(soup.prettify())
with open("./files/demos/demo1.txt", "w", encoding='utf-8') as f:
    f.write(soup.prettify())

"""quotes = []
quote_boxes = soup.find_all('div', class_="text-center mb-8")
for box in quote_boxes:
    quote_text = box.img['alt'].split(" #") #type: ignore
    quote = {
        'theme': box.h5.text.strip(),   #type: ignore
        'image_url': box.img['src'],    #type: ignore
        'lines': quote_text[0],
        'author': quote_text[1] if len(quote_text) > 1 else 'Unknown'
    }

    quotes.append(quote)"""


