from Task10.Models.BaseModel import *

class Ration(BaseModel):
    id = PrimaryKeyField()
    meal = CharField()
    food = CharField()
    calories = IntegerField()
    time = TimeField()

if __name__ == "__main__":
    mysql_db.create_tables([Ration])