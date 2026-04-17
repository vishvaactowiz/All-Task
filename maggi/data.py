import urllib.request
import json
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = urllib.request.urlopen(url)

html = response.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

books = soup.find_all("h3")

data = []
    
for book in books:
    title = book.text.strip()
    data.append({"title": title})

# write to JSON file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("data.json created successfully")