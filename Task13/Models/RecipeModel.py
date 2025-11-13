from Task13.Models.BaseModel import *

class Recipe(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    ingredients = CharField()
    cooking_time = TimeField()
    difficulty = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([Recipe])