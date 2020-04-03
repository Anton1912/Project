from peewee import SqliteDatabase, Model, CharField, \
    ForeignKeyField, IntegerField, TextField, PrimaryKeyField

db = SqliteDatabase('data_product.db')

class BaseModel(Model):
    class Meta:
        database = db

class Group_Product(BaseModel):
    id_group = PrimaryKeyField()
    name_group = TextField()

class Product(BaseModel):
    id_product = PrimaryKeyField()
    name_product = CharField()
    status_product = IntegerField(null=True)
    group_ = ForeignKeyField(Group_Product, related_name="product", null=False)


class Characters(BaseModel):
    name_character = TextField(unique=True)

class Item_Character(BaseModel):
    name_item = CharField()
    character_ = ForeignKeyField(Characters, related_name="item_character")
    product_ = ForeignKeyField(Product, related_name="item_character")


if __name__ == "__main__":
    Group_Product.create_table()
    Product.create_table()
    Characters.create_table()
    Item_Character.create_table()
