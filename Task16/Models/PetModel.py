from Task16.Models.BaseModel import *

class PetModel(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    type = CharField()
    age = IntegerField()
    owner = CharField()
    vaccinated = BooleanField(default=0)

if __name__ == "__main__":
    mysql_db.create_tables([PetModel])