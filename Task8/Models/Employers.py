from Task8.Models.BaseModel import *

class Employers(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    position = CharField()
    salary = IntegerField()
    department = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([Employers])