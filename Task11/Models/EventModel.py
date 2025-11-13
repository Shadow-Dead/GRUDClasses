from Task11.Models.BaseModel import *

class Event(BaseModel):
    id = PrimaryKeyField()
    title = CharField()
    date = DateField()
    time = TimeField()
    description = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([Event])