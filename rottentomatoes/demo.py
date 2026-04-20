import requests

all_urls = []
page = 1

while True:
    url = f"https://example.com/api/links?page={page}"
    res = requests.get(url)
    data = res.json()

    if not data:  # no more results
        break

    all_urls.extend(data)
    page += 1

print(len(all_urls))