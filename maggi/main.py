from lxml import html
import json

with open('maggi.html', 'r', encoding='utf-8') as f:
    data = f.read()

tree = html.fromstring(data)

rows = tree.xpath("//tbody/tr")

final_data = {}
def to_float(value):
    value = value.replace("%", "").strip()   # remove %
    
    if value == "-":
        return None
    
    try:
        return float(value)
    except:
        return None
for row in rows:

    cols = row.xpath("./td/text()")   

    clean_cols = []
    for c in cols:
        clean_cols.append(c.strip())

    if clean_cols:   

        name = clean_cols[0].lstrip("-").strip()

        final_data[name] = {
            "per 100g":to_float(clean_cols[1]),
            "per serve": to_float(clean_cols[2]),
            "%GDA per serve": clean_cols[3],
            "%RDA per serve": clean_cols[4]
        }

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=4)




