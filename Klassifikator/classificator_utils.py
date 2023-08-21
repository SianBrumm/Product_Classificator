import re

REG = re.compile(r'[a-z]-[A-Z]')

def edit_categories(categories):
    separators = ["&", ",", "/", " "]
    new_categories = []
    for cat in categories:
        if any(c in cat for c in separators):
            new_cat = re.split(r"&|,|\/|\s", cat)
            new_cat = [s.strip() for s in new_cat]
            new_categories.extend(new_cat)
        else:
            new_categories.append(cat)
    new_categories = flatten_list(new_categories)
    new_categories_copy = new_categories.copy()
    for cat_new in new_categories_copy:
        if "-" in cat_new:
            if not REG.search(cat_new):
                new_categories.remove(cat_new)
                continue
        if cat_new.islower():
            new_categories.remove(cat_new)
            continue
        if cat_new == "":
            new_categories.remove(cat_new)
    new_categories = flatten_list(new_categories)
    return new_categories

def edit_name(product_name):
    separators = [",", "/", "&", "(", ")", ":", "|", "."]
    for sep in separators:
        product_name = product_name.replace(sep, " ")
    product_name = product_name.split()
    product_name_copy = product_name.copy()
    for name in product_name_copy:
        if "-" in name:
            if REG.search(name):
                continue
            product_name.remove(name)
    return product_name

def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            for item in sublist:
                flat_list.append(item)
        else:
            flat_list.append(sublist)
    return flat_list

def categories_classificator(clas_obj, value, categories_edited):
    for cat in categories_edited:
        for word in value:
            if cat.lower() == word['keyword'].lower():
                clas_obj['segment_code'] = word['seg_code']
                clas_obj['segment_name'] = word['seg_name']
                return clas_obj
    return clas_obj

def name_classificator(clas_obj, value, name_edited):
    for name in name_edited:
        for word in value:
            if name.lower() == word['keyword'].lower():
                clas_obj['segment_code'] = word['seg_code']
                clas_obj['segment_name'] = word['seg_name']
                return clas_obj
    return clas_obj