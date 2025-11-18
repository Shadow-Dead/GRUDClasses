from Task18.Models.BaseModel import *

class EquipModel(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    type = CharField()
    serial = CharField()
    status = CharField()
    user = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([EquipModel])