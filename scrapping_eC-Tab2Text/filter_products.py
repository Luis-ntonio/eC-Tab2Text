import json

with open('products/products.json', 'r') as f:
    data = json.load(f)

NEW_DICT = {}

for item in data:
    for key, val in item.items():
        k = list(val.keys())
        if "reviews" not in k:
            break
        for k_ in k:
            val[k_] = val[k_][0].split("\n")
        if list(item.keys())[0] not in NEW_DICT:
            NEW_DICT[list(item.keys())[0]] = {}
        NEW_DICT[list(item.keys())[0]] = val

with open('products/products_partial.json', 'w') as f:
    json.dump(NEW_DICT, f, indent=4)