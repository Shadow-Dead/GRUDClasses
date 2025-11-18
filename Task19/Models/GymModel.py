from Task19.Models.BaseModel import *

class GymModel(BaseModel):
    id = PrimaryKeyField()
    date = DateField()
    type = CharField()
    duration = IntegerField()
    calories = IntegerField()
    notes = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([GymModel])