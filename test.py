from  cross_product import*
from model_db import*
from model_csv import csv_dict_writer


if __name__ == "__main__":
    a = {}
    products = Item_Character.select().where(Item_Character.character_ == "Серія")
    b = dict_structure(a, products)
    cross_product = "cpd.csv"
    data = b
    fieldnames = [main_id, name_character, cross_id1, cross_id2, cross_id3, cross_id4,\
                  cross_id5, cross_id6, cross_id7, cross_id8, cross_id9, cross_id10]
    csv_dict_writer("cpd.csv", fieldnames, b)