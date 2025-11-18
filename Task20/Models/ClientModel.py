from Task20.Models.BaseModel import *

class ClientModel(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    contact_person = CharField()
    phone = CharField()
    email = CharField()
    status = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([ClientModel])