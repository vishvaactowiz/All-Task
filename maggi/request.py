import requests as re

headers = {
    "content-type" : "text/html; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
url = "https://www.maggi.in/en/product/maggi-2-minute-special-masala-instant-noodles/"
data = re.get(url, headers=headers)

with open('maggi.html', 'w', encoding='utf-8') as f:
    f.write(data.text)
# print(data.text)