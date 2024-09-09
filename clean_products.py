import json

with open('products/products_partial.json', 'r') as f:
    data = json.load(f)

with open('products/products_reviews.json', 'r') as f:
    reviews = json.load(f)

urls = list(data.keys())

for key in data.keys():
    for k, v in data[key].items():
        if k == "keys_specifications":
            data[key][k] = [v[0]]
            flg = False
            for t in v[1:len(v)-1]:
                if flg:
                    data[key][k].append(t)
                if "Key Specs & Features" in t:
                    flg = True
        if k == "full_specifications":
            data[key][k] = v[4:len(v)-1]

        if k == "reviews":
            for i in range(len(reviews)):
                if key in reviews[i]:
                    data[key][k] = reviews[i][key]["reviews"]
                    break

with open('products/products_clean.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('urls/reviews_urls.json', 'w') as f:
    json.dump(urls, f, indent=4)