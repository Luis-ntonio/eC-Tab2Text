import json
import pandas as pd
import datasets
from itertools import permutations 

with open('./products/products_formatted.json', encoding='utf-8') as f:
    data = json.load(f)

dataset = []

for key in data:
  prop_ = [key for key in data[key]["reviews"]]
  for i in range(1, len(prop_)):
    props_ = permutations(prop_, i)
    for props in props_:
        reviews = {}
        tmp = {}
        tmp_keys = []
        for prop in props:
            tmp[prop] = {"type": "string"}
            reviews[prop] = data[key]["reviews"][prop]
            tmp_keys.append(prop)
        Text = f"""Given following json that contains specifications of a product, generate a review of the key characteristics with json format. Follow the values on {{Keys}} to write the Output:
### Product: {data[key]["full_specifications"]}
### Keys: {tmp_keys}
### Output: {reviews}"""
        props = tmp
        prompt = f"""{Text}"""
        dataset.append({"Text": prompt})

with open('prompts/prompts.json', 'w') as f:
    json.dump(dataset, f, indent=4)

dataset = datasets.Dataset.from_list(dataset)
dataset = dataset.train_test_split(test_size=0.2)
print(dataset)

dataset.push_to_hub("kokujin/prompts_1")
        
"""        
        Text = {
            "Input": {
            "Product": data[key]["full_specifications"],
            "Instruction": "{Product}. Given following json that contains specifications of a mobile product, generate a review of the key characteristics with json format. Use the keys inside 'Review' format in {output control} to generate a review based on the values of the {Product}. Here is an example: {Example}"
            },
            "output control": {
            'Review': {
                'type': 'List["string"]',
                'properties': props
                }
            },
            "Example": reviews
            }
"""