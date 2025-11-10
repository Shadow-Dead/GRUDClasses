from Task5.Models.BaseModel import *

class Student(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    age = IntegerField()
    grade = CharField(max_length=1)

if __name__ == "__main__":
    mysql_db.create_tables([Student])