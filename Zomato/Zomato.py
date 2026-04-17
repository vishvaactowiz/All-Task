from lxml import html

with open('example.html', 'r',encoding='utf-8') as f:
    data = f.read()


tree = html.fromstring(data)
urls = tree.xpath('//a[starts-with(@href, "https")]//@href')

print("\n".join(urls))
print(len(urls))