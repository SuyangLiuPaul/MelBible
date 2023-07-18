import json
from opencc import OpenCC

# Read the json file
with open('chinese_union_simp.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Initialize the converter
cc = OpenCC('s2t')

def convert_to_traditional(val):
    if isinstance(val, dict):
        return {convert_to_traditional(k): convert_to_traditional(v) for k, v in val.items()}
    elif isinstance(val, list):
        return [convert_to_traditional(element) for element in val]
    elif isinstance(val, str):
        return cc.convert(val)
    else:
        return val

# Convert all simplified chinese to traditional chinese
traditional_data = convert_to_traditional(data)

# Write the result to a new json file
with open('chinese_union_trad.json', 'w', encoding='utf-8') as f:
    json.dump(traditional_data, f, ensure_ascii=False)

'chinese_union_trad.json'
