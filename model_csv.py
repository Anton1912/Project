import csv
from peewee import IntegrityError
from model_db import*

def csv_reader_group(file):
    with open(file, newline='') as f_obj:
        reader = csv.reader(f_obj, delimiter=";")
        for row in reader:
            try:
                Group_Product.create(id_group=row[4], name_group=row[5])
            except IntegrityError:
                pass

def csv_reader_product(file):
    with open(file, newline='') as f_obj:
        reader = csv.reader(f_obj, delimiter=";")
        for row in reader:
            try:
                Product.create(id_product=row[0], name_product=row[1], status_product=row[6], group_=row[4])
            except IntegrityError:
                pass

def csv_reader_characters(file):
    with open(file, newline='') as f_obj:
        reader = csv.reader(f_obj, delimiter=";")
        for row in reader:
            try:
                Characters.create(name_character=row[2])
            except IntegrityError:
                pass

def csv_reader_item_character(file):
    with open(file, newline='') as f_obj:
        reader = csv.reader(f_obj, delimiter=";")
        for row in reader:
            try:
                Item_Character.create(name_item=row[3], character_=row[2], product_=row[0])
            except IntegrityError:
                pass

def csv_dict_writer(file, data):
    with open(file, "w", newline="") as out_file:
        writer = csv.DictWriter(out_file, delimiter=";")
        for row in data:
            writer.writerows(row)


