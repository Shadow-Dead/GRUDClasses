from Task9.Models.BaseModel import *

class GamesModel(BaseModel):
    id =PrimaryKeyField()
    title = CharField()
    genre = CharField()
    platform = CharField()
    completed = BooleanField(default=False)

if __name__ == "__main__":
    mysql_db.create_tables([GamesModel])