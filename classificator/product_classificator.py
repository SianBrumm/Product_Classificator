import json
import os
from classificator.classificator_utils import edit_categories, edit_name, flatten_list, categories_classificator, name_classificator
import importlib.resources

SEGMENTCODES = {'clothing':67000000, 'kitchenware': 73000000, 'food': 50000000, 'hygiene': 53000000, 'office_supplies': 62000000}
KEYWORDS_NOK = ["Tiernahrung", "Spielwaren", "Tierbedarf"]

def product_classificator(product_name, product_categories):

    data_path = importlib.resources.path('classificator', 'data')
    json_path = os.path.join(data_path, "keywords.json")
    with open(json_path, encoding='utf-8') as json_file:
        key_list = json.load(json_file)

    classificator = {"clothing": [],
                    "hygiene": [],
                    "kitchenware": [],
                    "office_supplies": [],
                    "food": []}

    for key_obj in key_list:
        if not key_obj['critical']:
            seg_code = key_obj['path'][0]['segment_code']
            seg_name = key_obj['path'][0]['segment_name']
            for key, value in SEGMENTCODES.items():
                if value == seg_code:
                    classificator[key].append({'keyword': key_obj['keyword'], 'seg_code':seg_code, 'seg_name': seg_name})
                    break

    clas_obj = {'segment_code': None, 'segment_name': None,
                'family_code': None, 'family_name': None,
                'class_code': None, 'class_name': None,
                'brick_code': None, 'brick_name': None}

    categories_edited = edit_categories(product_categories)
    for nok in KEYWORDS_NOK:
        if nok in categories_edited:
            return clas_obj

    for key, value in classificator.items():
        if clas_obj["segment_code"] is None:
            clas_obj = categories_classificator(clas_obj, value, categories_edited)
        else:
            break
    
    name_edited = edit_name(product_name)
    if clas_obj['segment_code'] is None:
        for key, value in classificator.items():
            if clas_obj["segment_code"] is None:
                clas_obj = name_classificator(clas_obj, value, name_edited)
            else:
                break

    return clas_obj
 
