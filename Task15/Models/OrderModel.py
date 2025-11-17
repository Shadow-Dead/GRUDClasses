from Task15.Models.BaseModel import *

class OrderModel(BaseModel):
    id = PrimaryKeyField()
    customer = CharField()
    product = CharField()
    amount = IntegerField()
    status = CharField()
    order_date = DateField()

if __name__ == "__main__":
    mysql_db.create_tables([OrderModel])