from Task2.Models.BaseModel import *

class PhoneBook(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    phone = CharField(max_length=10)
    email = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([PhoneBook])