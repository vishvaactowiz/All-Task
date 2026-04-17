import json

with open("bonker.json") as f:
    data = json.load(f)



result = []

for product in data["products"]:
    handle = product["handle"]
    vendor = product["vendor"]
    product_url = f"https://www.bonkerscorner.com/products/{handle}"

    variants = []
    sizes = []

    for v in product["variants"]:
        size = v["public_title"]
        sizes.append(size)

        variants.append({
            "variantName": size,
            "variantId": v["id"],
            "variantUrl": f"{product_url}?variant={v['id']}",
            "variantPrice": v["price"] / 100
        })

    result.append({
        "productName": handle.replace("-", " ").title(),
        "vendor": vendor,
        "productUrl": product_url,
        "productPrice": product["variants"][0]["price"] // 100,
        "variantCount": len(variants),
        "variantOptions": [
            {
                "optionName": "Size",
                "optionValues": sizes
            }
        ],
        "variants": variants
    })

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)