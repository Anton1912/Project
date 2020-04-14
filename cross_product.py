from model_db import*
from model_csv import csv_dict_writer

cross_product = "cpd.csv"

main_id = (Item_Character.select(Item_Character.product_, Item_Character.name_item).join(Product)
           .where(Item_Character.character_ == "Серія"))

for product in main_id:
    pass
