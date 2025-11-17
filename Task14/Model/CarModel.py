from Task14.Model.BaseModel import *

class CarModel(BaseModel):
    id = PrimaryKeyField()
    brand = CharField()
    model = CharField()
    year = IntegerField()
    color = CharField()
    price = IntegerField()

if __name__ == "__main__":
    mysql_db.create_tables([CarModel])