from Task17.Models.BaseModel import *

class MusicModel(BaseModel):
    id = PrimaryKeyField()
    title = CharField()
    artist = CharField()
    album = CharField()
    year = IntegerField()
    genre = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([MusicModel])