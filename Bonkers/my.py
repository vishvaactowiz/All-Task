import json
import jmespath

with open(r"bonker.json") as f:
    data = json.load(f)


result = jmespath.search("products[]", data)
print(result)

# with open('bonker.json','r',encoding='utf-8') as f:
#     data=json.load(f)

# all_data=data.get('products')

# for a in all_data:
#     vendor=a.get('vendor')
# print(vendor)

