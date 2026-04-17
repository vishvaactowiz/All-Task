import json 
from lxml import html
import re
from urllib.parse import urljoin

base_url="https://igus.widen.net/"

with open('igus.html', 'r',encoding='utf-8') as f:
    data = f.read()

tree = html.fromstring(data)
data = tree.xpath('//script[@id = "__NEXT_DATA__"]/text()')[0]

script = json.loads(data)
atribute = []
# with open("igus.json",'w',encoding='utf-8') as f:
#     json.dump(script,f,indent=4
all_data = script.get("props").get("pageProps")
part_number = all_data.get('articleNumber')
material = all_data.get('articleData').get('material').get('name')
shape = all_data.get('_nextI18Next').get('userConfig').get('resources').get('en').get('bearing-hub/bearingHub').get('SHAPES').get('S').get('TITLE')
dimensions = all_data.get('articleData').get('dimensions')
manu_method = all_data.get('_nextI18Next').get('userConfig').get('resources').get('en').get('bearing-hub/bearingHub').get('PRODUCTION_METHODS').get('MOLD_INJECTION')
properties= all_data.get('akeneoProductData').get('usp')
pro = html.fromstring(properties)
p = pro.xpath("//li/text()")

for pro in p:
    # print(p)
    atribute.append(pro)

product_details = all_data.get('akeneoProductData').get('attributes').get('attr_description').get('value')
technical_data = all_data.get('technicalDataCategories')
technicalDataCategorieslist={}
for item in technical_data:
   atributeobject={}
   for attribute in item.get("attributes"):
       key=attribute.get("description").strip()
       value=attribute.get("value") 
       atributeobject[key] = value
    
   technicalDataCategorieslist[item.get("name")] = atributeobject



img = all_data.get('akeneoProductData').get('assets')
product_images=[]
for i in img:
    if i.get('key')=='attr_image_01' or i.get('key')=='drawing_01' :
        imgs=i.get('sources')
        for im in imgs:
            if im.get('contentType') == 'image':
                uri=urljoin(base_url, im.get('uri'))
                product_images.append(uri)
                
print(set(product_images))

output = {
    "part_number": part_number,
    "material": material,
    "shape": shape,
    "dimensions": dimensions,
    "manufacturing_method": manu_method,
    "properties": atribute,
    "product_details": product_details,
    "img": list(set(product_images)),
    "technical_data":technicalDataCategorieslist

}

with open("output.json",'w',encoding='utf-8') as f:
    json.dump(output,f,indent=4, ensure_ascii=False)