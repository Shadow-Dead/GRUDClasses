from Task6.Models.BaseModel import *

class Finance(BaseModel):
    id = PrimaryKeyField()
    amount = IntegerField()
    category = CharField()
    date = DateField()
    description = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([Finance])