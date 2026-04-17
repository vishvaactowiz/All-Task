import json
import jmespath

with open('data-2026216105652.json', 'r') as f:
    data = json.load(f)

All_data = jmespath.search('page_data.sections', data)
res_url = jmespath.search('page_info.canonicalUrl', data)
final_menu = {}

if All_data:
    rest_id = jmespath.search('SECTION_BASIC_INFO.res_id', All_data)
    name = jmespath.search('SECTION_BASIC_INFO.name', All_data)
    res_cont = jmespath.search('SECTION_RES_CONTACT.phoneDetails.phoneStr', All_data)

    address = {
        'full_addr': jmespath.search('SECTION_RES_CONTACT.address', All_data),
        'region': jmespath.search('SECTION_RES_CONTACT.country_name', All_data),
        'city': jmespath.search('SECTION_RES_CONTACT.city_name', All_data),
        'pincode': jmespath.search('SECTION_RES_CONTACT.zipcode', All_data),
    }

    cui = jmespath.search('SECTION_RES_HEADER_DETAILS.CUISINES', All_data)
    cuisines = [
        {
            'name': c.get('name'),
            'url': c.get('url')
        }
        for c in cui
    ]

    time = jmespath.search('SECTION_BASIC_INFO.timing.customised_timings.opening_hours', All_data)
    timings = []
    for t in time:
        timings.append({
            'timimgs': t.get('timing'),
            'days': t.get('days')
        })

menu = jmespath.search('page_data.order.menuList.menus', data)
menu_categories = []

for item in menu:
    categories = item.get('menu').get('categories')
    
    items = []
    
    for category in categories:
        for subitem in category.get('category').get('items'):
            nesteditem = subitem.get('item')
            
            temp = {
                "item_id": nesteditem.get('id'),
                "item_name": nesteditem.get('name'),
                "item_slugs": nesteditem.get('tag_slugs'),
                "item_url": '',
                "item_description": nesteditem.get('desc'),     
                "item_price": '',
                "is_veg": True if nesteditem.get('dietary_slugs')[0] == True else False
            }
            
            items.append(temp)
    
    category_data = {
        "category_name": item.get('menu').get('name'),
        "items": items
    }

    menu_categories.append(category_data)

output = {
    'rest_id': rest_id,
    'name': name,
    'res_url': res_url,
    'res_cont': res_cont,
    'address': address,
    'cuisines': cuisines,
    'timings': timings,
    'menu_categories': menu_categories
}

with open("J output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)