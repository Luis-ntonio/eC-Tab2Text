import json
import re
from dictionaries.full_specs_keys import full_specs_keys
from dictionaries.keys import keys
from dictionaries.reviews import reviews

final_json = {}
with open('products/products_clean.json', 'r') as f:
    data = json.load(f)

products = data.keys()

def clean_reviews(tmp_reviews: dict):
    k = tmp_reviews.keys()
    for k_ in k:
        cont = tmp_reviews[k_]
        tmp_reviews[k_] = cont.split("\n")[0]
        if k_ in ["Design and Disp\ufefflay", "Display and Design"] and tmp_reviews[k_] != "":
            tmp_reviews["Design and Display"] = tmp_reviews[k_]

    return tmp_reviews

def format_reviews(reviews_: str, p_keys: dict, tmp_reviews: dict, key: str = None):
    updated = reviews_.replace(":", "").replace("&", "and")
    for p_k in p_keys:
        if f"\n{p_k}\n" in updated:
            tmp = updated.split(f"\n{p_k}\n")
            if len(tmp) == 2:
                if tmp[0] != "":
                    tmp_reviews = format_reviews(tmp[0], p_keys, tmp_reviews)
                if tmp[1] != "":
                    tmp_reviews = format_reviews(tmp[1], p_keys, tmp_reviews, p_k)
            else:
                if key:
                    tmp_reviews[key] = tmp[0]
                return  tmp_reviews           
    if key:
        tmp_reviews[key] = updated
    return tmp_reviews


def ver(sec, val, content, it = r"[\s]"):
    return re.search(sec+it, val) and (content[sec] == "" or (type(content[sec]) == list and len(content[sec]) == 0 or (len(content[sec]) == 1 and (content[sec][0] == "," or content[sec][0] == "/"))) or type(content[sec]) == dict)

def iterable_function(fullspecs, i, primary_keys, secondary_keys, terceary_keys, quarter, content, key):
    if type(content) == dict:
        if secondary_keys != None:
            if terceary_keys != None:
                quarter = content.keys()
            else:
                terceary_keys = content.keys()
        else: 
            secondary_keys = content.keys()
        for j in range(i, len(fullspecs)):
            val_ = fullspecs[j]
            for p_k in primary_keys:
                if re.search(p_k, fullspecs[j]) and j != i:
                    return content
            if terceary_keys == None and quarter == None:
                for sec in secondary_keys:
                    if ver(sec, val_, content):       
                        content_ = content[sec]
                        content[sec] = iterable_function(fullspecs, j, primary_keys, secondary_keys, terceary_keys, quarter, content_, sec)
                        break
            elif quarter == None:
                for s_k in secondary_keys:
                    if re.search(s_k, fullspecs[j]) and j != i:
                        return content
                for ter in terceary_keys:
                    if ver(ter, val_, content, it=""):
                        content_ = content[ter]
                        content[ter] = iterable_function(fullspecs, j, primary_keys, secondary_keys, terceary_keys, quarter, content_, ter)
                        break
            else:
                for t_k in terceary_keys:
                    if re.search(t_k, fullspecs[j]) and j != i:
                        return content
                for q in quarter:
                    if ver(q, val_, content, it=""):
                        content_ = content[q]
                        content[q] = iterable_function(fullspecs, j, primary_keys, secondary_keys, terceary_keys, quarter, content_, q)
                        break

    elif type(content) == list:
        line_ = fullspecs[i:]
        try: 
            for j, l in enumerate(line_):
                l = l.replace(":","")
                for p_k in primary_keys:
                    if re.search(p_k, l) and j != 0:
                        raise Exception
                if secondary_keys:
                    for p_k in secondary_keys:
                        if re.search(p_k+r"[\s]", l) and j != 0:
                            raise Exception
                if terceary_keys:
                    for p_k in terceary_keys:
                        if re.search(p_k, l) and j != 0:
                            raise Exception
                if quarter:
                    for p_k in quarter:
                        if re.search(p_k, l) and j != 0:
                            raise Exception

                if len(content) > 0 and (content[0] == "," or content[0] == "/"):
                    l = l.split(key + " ")[1:]
                    for x, l_ in enumerate(l):
                        if l_ == "":
                            l[x] = key
                    l = " ".join(l)
                    linea = l.split(content[0] + " ")
                    content.pop()
                    for l_ in linea:
                        content.append(l_)
                else:
                    if j == 0:
                        linea = l.split(key)
                        if len(linea) > 1:
                            if linea[0] == "" and linea[1] == "":
                                continue
                            elif linea[0] == "":
                                linea = linea[1:]
                            for x, l_ in enumerate(linea):
                                if l_ == "":
                                    linea[x] = key
                            linea = " ".join(linea)
                            content.append(linea)
                    else:    
                        content.append(l)

        except Exception:
            return content
        
    else:
        val = fullspecs[i].replace(":"," ")
        content = val.split(key + " ")[1:]
        for x, c in enumerate(content):
            if c == "":
                content[x] = key
        content = " ".join(content)
    return content

for product in products:
    tmp_full = full_specs_keys().get_dict()
    tmp_key = keys().get_dict()
    tmp_reviews = reviews().get_dict()

    fullspecs = data[product]["full_specifications"]
    keys_ = data[product]["keys_specifications"]
    reviews_ = data[product]["reviews"][0]

    tmp_full["Model Name"] = keys_[0]
    #formatting fullspecifications
    primary_keys = tmp_full.keys()
    for i, line in enumerate(fullspecs):
        if i == 0 and "General" not in line:
            content = tmp_full["General"]
            tmp_full["General"] = iterable_function(fullspecs, i, primary_keys, None, None, None, content, "General")
        else:
            for primary_key in primary_keys:
                if re.search(primary_key, line):
                    content = tmp_full[primary_key]
                    tmp_full[primary_key] = iterable_function(fullspecs, i+1, primary_keys, None, None, None, content, primary_key)
                    break
    #formatting key specifications
    primary_keys = tmp_key.keys()
    for i, line in enumerate(keys_):
        if i == 0 and "Model" not in line:
            tmp_key["Model"] = keys_[0]
        if "Operating System" in line:
            tmp_key["Operating System"] = keys_[i + 1]
        else:
            for primary_key in primary_keys:
                if re.search(primary_key, line):
                    content = tmp_key[primary_key]
                    
                    tmp_key[primary_key] = iterable_function(keys_, i, primary_keys, None, None, None, content, primary_key)
                    break
    tmp_key = {k: v for k, v in tmp_key.items() if v}
    #formatting reviews
    p_keys = tmp_reviews.keys()
    tmp_reviews = format_reviews(reviews_, p_keys, tmp_reviews)
    tmp_reviews = clean_reviews(tmp_reviews)
    tmp_reviews = {k: v for k, v in tmp_reviews.items() if v}
    
    if tmp_reviews != {}:
        final_json[product] = {
            "keys_specifications": tmp_key,
            "full_specifications": tmp_full,
            "reviews": tmp_reviews
        }              
with open('products/products_formatted.json', 'w') as f:
    json.dump(final_json, f, indent=4)