from Task12.Models.BaseModel import *

class Project(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    status = CharField()
    deadline = DateField()
    priority = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([Project])