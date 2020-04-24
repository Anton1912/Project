from model_db import*
import csv

def dict_structure(data, request_data):
    def sort_value(item):
        return item[1]
    for id in request_data:
        id = {str(id.product_) : id.name_item}
        data.update(id)
    return dict(sorted(data.items(), key=sort_value))

def collections(data, request_data):
    for name in request_data:
        name = name.name_item
        data.append(name)
    return  data

if __name__ == "__main__":
    empty_dict_product = {}
    empty_list_collection = []
    products = Item_Character.select().where(Item_Character.character_ == "Серія")
    product_dict = dict_structure(empty_dict_product, products)
    collection_list = list(set(collections(empty_list_collection, products)))
    collection_list.sort()
    cross = []
    cross_product = []
    for keys, values in list(product_dict.items()):
        if collection_list[0] in product_dict[keys]:
            cross.append(keys)
        else:
            cross_product.append(list(cross))
            cross.clear()
            del collection_list[0]
            continue
with open("cross_product.csv", "w") as out_file:
    writer = csv.writer(out_file, delimiter=";")
    for row in cross_product:
        writer.writerow(row)




